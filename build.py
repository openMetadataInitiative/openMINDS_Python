from collections import defaultdict
import json
import os.path
import shutil
import subprocess
import sys

from jinja2 import Environment, select_autoescape, FileSystemLoader

from pipeline.translator import PythonBuilder
from pipeline.utils import clone_sources, SchemaLoader

print("***************************************")
print(f"Triggering the generation of Python package for openMINDS")
print("***************************************")

# Step 1 - clone central repository in main branch to get the latest sources
clone_sources()
schema_loader = SchemaLoader()
if os.path.exists("target"):
    shutil.rmtree("target")

python_modules = defaultdict(list)
for schema_version in schema_loader.get_schema_versions():

    # Step 2 - find all involved schemas for the current version
    schemas_file_paths = schema_loader.find_schemas(schema_version)

    # Step 3a - figure out which schemas are embedded and which are linked
    embedded = set()
    linked = set()
    for schema_file_path in schemas_file_paths:
        emb, lnk = PythonBuilder(schema_file_path, schema_loader.schemas_sources).get_edges()
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

    # Step 3b - translate and build each openMINDS schema as JSON-Schema
    for schema_file_path in schemas_file_paths:
        module_path, class_name = PythonBuilder(
            schema_file_path, schema_loader.schemas_sources
        ).build(embedded=embedded)

        parts = module_path.split(".")
        parent_path = ".".join(parts[:-1])
        python_modules[parent_path].append((parts[-1], class_name))

# Step 4 - create additional files, e.g. __init__.py
for path, classes in python_modules.items():
    dir_path = ["target", "openminds"] + path.split(".")
    init_file_path = os.path.join(*(dir_path + ["__init__.py"]))
    with open(init_file_path, "w") as fp:
        for class_module, class_name in classes:
            fp.write(f"from .{class_module} import {class_name}\n")
    while len(dir_path) > 2:
        child_dir = dir_path[-1]
        dir_path = dir_path[:-1]
        init_file_path = os.path.join(*(dir_path + ["__init__.py"]))
        with open(init_file_path, "a") as fp:
            if len(dir_path) > 3:
                class_names = ", ".join(class_name for _, class_name in classes)
                fp.write(f"from .{child_dir} import ({class_names})\n")

env = Environment(
    loader=FileSystemLoader(os.path.dirname(os.path.realpath(__file__))),
    autoescape=select_autoescape()
)
context = {
    "version": "0.1.0",
}
with open("target/pyproject.toml", "w") as fp:
    contents = env.get_template("pipeline/src/pyproject_template.toml.txt").render(context)
    fp.write(contents)

shutil.copy("pipeline/src/base.py", "target/openminds/base.py")
shutil.copy("pipeline/src/properties.py", "target/openminds/properties.py")
shutil.copy("pipeline/src/registry.py", "target/openminds/registry.py")
shutil.copy("pipeline/src/collection.py", "target/openminds/collection.py")
shutil.copy("pipeline/src/README.md", "target/README.md")
shutil.copy("./LICENSE", "target/LICENSE")

# Step 5 - run formatter
subprocess.call([sys.executable, "-m", "black", "--quiet", "target"])
