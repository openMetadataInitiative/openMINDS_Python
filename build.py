import argparse
from collections import defaultdict
import json
import os.path
import shutil
import subprocess
import sys
from urllib.request import urlopen, HTTPError

from jinja2 import Environment, select_autoescape, FileSystemLoader

from pipeline.translator import PythonBuilder
from pipeline.utils import clone_sources, SchemaLoader, InstanceLoader


include_instances = True  # to speed up the build during development, set this to False

parser = argparse.ArgumentParser(prog=sys.argv[0], description="Generate Python package for openMINDS")
parser.add_argument('--branch', help="The branch to build from ('main' or 'development')", default="main")
args = parser.parse_args()

print("*******************************************************************************")
print(f"Triggering the generation of Python package for openMINDS, from the {args.branch} branch")
print("*******************************************************************************")

# Step 0 - read code for additional methods
additional_methods = {}
with open("pipeline/src/additional_methods/by_name.py.txt") as fp:
    code = fp.read()
additional_methods["by_name"] = code

# Step 1 - clone central repository in main or development branch to get the latest sources
clone_sources(args.branch)
schema_loader = SchemaLoader()
instance_loader = InstanceLoader()
if os.path.exists("target"):
    shutil.rmtree("target")

# Step 2 - load instances
instances = {}
if include_instances:
    for version in instance_loader.get_instance_versions():
        instances[version] = defaultdict(list)
        for instance_path in instance_loader.find_instances(version):
            with open(instance_path) as fp:
                instance_data = json.load(fp)
            instances[version][instance_data["@type"]].append(instance_data)

python_modules = defaultdict(list)

for schema_version in schema_loader.get_schema_versions():

    # Step 3 - find all involved schemas for the current version
    schemas_file_paths = schema_loader.find_schemas(schema_version)

    # Step 4a - figure out which schemas are embedded and which are linked
    embedded = set()
    linked = set()
    class_to_module_map = {}
    for schema_file_path in schemas_file_paths:
        emb, lnk = PythonBuilder(schema_file_path, schema_loader.schemas_sources).get_edges()
        class_to_module_map=PythonBuilder(schema_file_path, schema_loader.schemas_sources).update_class_to_module_map(class_to_module_map)
        embedded.update(emb)
        linked.update(lnk)
    conflicts = linked.intersection(embedded)
    if conflicts:
        print(f"Found schema(s) in version {schema_version} "
              f"that are both linked and embedded: {conflicts}")
        # conflicts should not happen in new versions.
        # There is one conflict in v1.0, QuantitativeValue,
        # which we treat as embedded
        for schema_identifier in conflicts:
            linked.remove(schema_identifier)

    # Step 4b - translate and build each openMINDS schema as a Python class
    for schema_file_path in schemas_file_paths:
        module_path, class_name = PythonBuilder(
            schema_file_path,
            schema_loader.schemas_sources,
            instances=instances.get(schema_version, None),
            additional_methods=additional_methods,
        ).build(embedded=embedded,class_to_module_map=class_to_module_map)

        parts = module_path.split(".")
        parent_path = ".".join(parts[:-1])
        python_modules[parent_path].append((parts[-1], class_name))

# Step 5 - create additional files, e.g. __init__.py
openminds_modules = defaultdict(set)
for path in sorted(python_modules):
    classes = python_modules[path]
    dir_path = ["target", "openminds"] + path.split(".")
    openminds_modules[dir_path[2]].add(dir_path[3])
    init_file_path = os.path.join(*(dir_path + ["__init__.py"]))
    with open(init_file_path, "w") as fp:
        for class_module, class_name in sorted(classes):
            fp.write(f"from .{class_module} import {class_name}\n")
    while len(dir_path) > 3:
        child_dir = dir_path[-1]
        dir_path = dir_path[:-1]
        init_file_path = os.path.join(*(dir_path + ["__init__.py"]))
        with open(init_file_path, "a") as fp:
            if len(dir_path) > 3:
                class_names = ", ".join(sorted(class_name for _, class_name in classes))
                fp.write(f"from .{child_dir} import ({class_names})\n")

for version, module_list in openminds_modules.items():
    init_file_path = os.path.join("target", "openminds", version, "__init__.py")
    with open(init_file_path, "w") as fp:
        fp.write(f"from . import ({', '.join(sorted(module_list))})\n")

env = Environment(
    loader=FileSystemLoader(os.path.dirname(os.path.realpath(__file__))),
    autoescape=select_autoescape()
)
context = {
    "version": "0.3.0",
}
if args.branch == "development":
    context["version"] += ".dev"

with open("target/pyproject.toml", "w") as fp:
    contents = env.get_template("pipeline/src/pyproject_template.toml.txt").render(context)
    fp.write(contents)
with open("target/openminds/__init__.py", "w") as fp:
    contents = env.get_template("pipeline/src/init_template.py.txt").render(context)
    fp.write(contents)

shutil.copy("pipeline/src/base.py", "target/openminds/base.py")
shutil.copy("pipeline/src/properties.py", "target/openminds/properties.py")
shutil.copy("pipeline/src/registry.py", "target/openminds/registry.py")
shutil.copy("pipeline/src/collection.py", "target/openminds/collection.py")
shutil.copy("pipeline/src/README.md", "target/README.md")
shutil.copy("./LICENSE", "target/LICENSE")

# If we have a PyPI release for the current version, complete the codemeta.json template
try:
    with urlopen(f"https://pypi.org/pypi/openminds/{context['version']}/json") as handle:
        pypi_metadata = json.loads(handle.read())
except HTTPError:
    pypi_metadata = None

if pypi_metadata:
    with open("pipeline/src/codemeta.json") as fp:
        codemeta = json.load(fp)
        codemeta["version"] = context["version"]
        for item in pypi_metadata["urls"]:
            if item["packagetype"] == "sdist":
                codemeta["downloadUrl"] = item["url"]
                codemeta["dateModified"] = item["upload_time"].split("T")[0]
                break
    with open("target/codemeta.json", "w") as fp:
        json.dump(codemeta, fp, indent=2)

# Step 6 - run formatter
subprocess.call([sys.executable, "-m", "black", "--quiet", "target"])
