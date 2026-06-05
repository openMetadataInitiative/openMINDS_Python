import glob
import os
import shutil
from typing import List

from git import Repo, GitCommandError

from pipeline.translator import generate_python_name


class PythonRef:
    """A bare Python identifier/expression rendered without quotes in generated code."""

    def __init__(self, ref):
        self.ref = ref

    def __repr__(self):
        return self.ref

    def __str__(self):
        return self.ref


def build_instance_id_to_ref(instances_by_type):
    """Build a map from instance @id → (class_name, python_attr_name) for all instances."""
    id_to_ref = {}
    for type_iri, type_instances in instances_by_type.items():
        ref_class = type_iri.split("/")[-1]
        for inst in type_instances:
            ref_name = generate_python_name(inst["@id"].split("/")[-1])
            id_to_ref[inst["@id"]] = (ref_class, ref_name)
    return id_to_ref


def build_instance_ref_graph(instances_by_type, id_to_ref):
    """Build a directed graph: class_name → set of class_names it references via instances."""
    graph = {}

    def collect(val, source_class):
        if isinstance(val, dict) and set(val.keys()) == {"@id"}:
            entry = id_to_ref.get(val["@id"])
            if entry and entry[0] != source_class:
                graph.setdefault(source_class, set()).add(entry[0])
        elif isinstance(val, list):
            for item in val:
                collect(item, source_class)

    for type_iri, insts in instances_by_type.items():
        source_class = type_iri.split("/")[-1]
        for inst in insts:
            for val in inst.values():
                collect(val, source_class)
    return graph


def _resolve_value(value, id_to_ref, referenced_classes):
    """Convert {'@id': '...'} instance refs to PythonRef. Collect referenced class names."""
    if isinstance(value, dict) and set(value.keys()) == {"@id"}:
        entry = id_to_ref.get(value["@id"])
        if entry:
            ref_class, ref_name = entry
            referenced_classes.add(ref_class)
            return PythonRef(f"{ref_class}.{ref_name}")
    elif isinstance(value, list):
        return [_resolve_value(item, id_to_ref, referenced_classes) for item in value]
    return value


def _has_cyclic_ref(value, deferred_classes):
    """True if value contains a PythonRef whose class is in deferred_classes."""
    if isinstance(value, PythonRef):
        return value.ref.split(".")[0] in deferred_classes
    if isinstance(value, list):
        return any(_has_cyclic_ref(item, deferred_classes) for item in value)
    return False


def _instance_needs_iri(props):
    """
    True if any property of props will be rendered as IRI(...) by the instances template,
    i.e. is a string starting with 'http' in a property other than 'id'.
    """
    return any(
        isinstance(value, str) and value.startswith("http") for key, value in props.items() if key != "id"
    )


def _collect_python_ref_classes(value, classes):
    """Collect the class name of every PythonRef found within value (recursing into lists)."""
    if isinstance(value, PythonRef):
        classes.add(value.ref.split(".")[0])
    elif isinstance(value, list):
        for item in value:
            _collect_python_ref_classes(item, classes)


def _sort_classes_by_creation_order(dependency_graph, classes):
    """
    Sort classes so dependencies come before the classes that depend on them.

    Returns (order, cyclic_edges) where:
      order         — class names in creation order (dependencies first)
      cyclic_edges  — set of (referencing_class, referenced_class) pairs that form cycles;
                      referencing_class's refs to referenced_class must be deferred to phase 2
    """
    UNVISITED, VISITING, DONE = 0, 1, 2
    visit_state = {cls: UNVISITED for cls in classes}
    order = []
    cyclic_edges = set()

    def visit(cls_name):
        visit_state[cls_name] = VISITING
        for neighbor in sorted(dependency_graph.get(cls_name, set())):
            if neighbor not in classes:
                continue
            if visit_state[neighbor] == VISITING:
                cyclic_edges.add((cls_name, neighbor))
            elif visit_state[neighbor] == UNVISITED:
                visit(neighbor)
        visit_state[cls_name] = DONE
        order.append(cls_name)

    for cls in sorted(classes):
        if visit_state[cls] == UNVISITED:
            visit(cls)

    return order, cyclic_edges


def generate_class_instances_file(version_module, dir_path, cls_name, full_module_path,
                                   instances_raw, deferred_classes, id_to_ref,
                                   class_full_modules, env):
    """
    Write target/openminds/{version_module}/{dir_path}/{module_name}_instances.py
    containing only cls_name's own instances.

    Properties whose value references another class in deferred_classes are routed
    to cross_class_patches (returned) rather than rendered here, so that this file
    never needs to import a class it is cyclically coupled with.
    """
    module_name = full_module_path.split(".")[-1]
    referenced_classes = set()
    phase1_instances = []
    phase2_patches = []
    cross_class_patches = []

    for inst_name, inst_data in instances_raw.items():
        phase1_props = {}
        for prop_name, value in inst_data.items():
            local_refs = set()
            filtered = _resolve_value(value, id_to_ref, local_refs)
            if _has_cyclic_ref(filtered, deferred_classes):
                if local_refs - {cls_name}:
                    cross_class_patches.append((cls_name, inst_name, prop_name, filtered))
                else:
                    phase2_patches.append((cls_name, inst_name, prop_name, filtered))
                    referenced_classes |= local_refs
            else:
                phase1_props[prop_name] = filtered
                referenced_classes |= local_refs
        phase1_instances.append((cls_name, inst_name, phase1_props))

    imports = {f"from openminds.{version_module}.{full_module_path} import {cls_name}"}
    if any(_instance_needs_iri(props) for _cls_name, _inst_name, props in phase1_instances):
        imports.add("from openminds.base import IRI")
    for ref_class in referenced_classes:
        if ref_class in class_full_modules:
            full_path = class_full_modules[ref_class]
            imports.add(f"from openminds.{version_module}.{full_path} import {ref_class}")

    context = {
        "imports": sorted(imports),
        "phase1_instances": phase1_instances,
        "phase2_patches": phase2_patches,
    }

    output_path = os.path.join(
        "target", "openminds", version_module, dir_path, f"{module_name}_instances.py"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as fp:
        contents = env.get_template("pipeline/src/instances_template.py.txt").render(context)
        fp.write(contents)

    return cross_class_patches


def generate_instance_patches_file(version_module, dir_path, cross_class_patches, class_full_modules, env):
    """Write target/openminds/{version_module}/{dir_path}/_instance_patches.py."""
    imports = set()
    for cls_name, _inst_name, _prop_name, value in cross_class_patches:
        referenced_classes = {cls_name}
        _collect_python_ref_classes(value, referenced_classes)
        for ref_class in referenced_classes:
            if ref_class in class_full_modules:
                full_path = class_full_modules[ref_class]
                imports.add(f"from openminds.{version_module}.{full_path} import {ref_class}")

    context = {
        "imports": sorted(imports),
        "patches": cross_class_patches,
    }

    output_path = os.path.join("target", "openminds", version_module, dir_path, "_instance_patches.py")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as fp:
        contents = env.get_template("pipeline/src/instance_patches_template.py.txt").render(context)
        fp.write(contents)


def generate_directory_instance_files(version_module, dir_path, dir_class_data,
                                       all_instances_for_version, id_to_ref,
                                       class_full_modules, env):
    """
    Write one {module_name}_instances.py per class with instances in this directory,
    plus a shared _instance_patches.py for any cross-class cyclic references.

    Returns True if a _instance_patches.py file was written (so the caller can wire
    up its import trigger in __init__.py), False otherwise.
    """
    classes = {item[0] for item in dir_class_data}

    # Build a dependency_graph restricted to intra-directory edges (for cycle detection)
    dir_instances_by_type = {}
    for cls_name, _full_mod, _raw in dir_class_data:
        for type_iri, type_insts in all_instances_for_version.items():
            if type_iri.split("/")[-1] == cls_name:
                dir_instances_by_type[type_iri] = type_insts
                break

    full_dependency_graph = build_instance_ref_graph(dir_instances_by_type, id_to_ref)
    local_dependency_graph = {
        class_name: {dependency for dependency in dependencies if dependency in classes}
        for class_name, dependencies in full_dependency_graph.items()
        if class_name in classes
    }

    _order, cyclic_edges = _sort_classes_by_creation_order(local_dependency_graph, classes)

    all_cross_class_patches = []
    for cls_name, full_module_path, instances_raw in dir_class_data:
        # Defer cross-class cyclic refs AND same-class refs (forward-reference risk)
        deferred_classes = {
            referenced_class for (referencing_class, referenced_class) in cyclic_edges
            if referencing_class == cls_name
        } | {cls_name}

        cross_class_patches = generate_class_instances_file(
            version_module, dir_path, cls_name, full_module_path, instances_raw,
            deferred_classes, id_to_ref, class_full_modules, env
        )
        all_cross_class_patches.extend(cross_class_patches)

    if all_cross_class_patches:
        generate_instance_patches_file(version_module, dir_path, all_cross_class_patches, class_full_modules, env)
        return True
    return False


def clone_sources(branch="main"):
    if os.path.exists("_sources"):
        shutil.rmtree("_sources")
    Repo.clone_from(
        "https://github.com/openMetadataInitiative/openMINDS.git",
        to_path="_sources/schemas",
        depth=1,
        branch=branch,
        single_branch=True,
    )
    Repo.clone_from(
        "https://github.com/openMetadataInitiative/openMINDS_instances.git",
        to_path="_sources/instances",
        depth=1,
        single_branch=True,
    )


class SchemaLoader:
    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.schemas_sources = os.path.join(self._root_directory, "_sources/schemas", "schemas")

    def get_schema_versions(self) -> List[str]:
        return os.listdir(self.schemas_sources)

    def find_schemas(self, version: str) -> List[str]:
        return glob.glob(
            os.path.join(self.schemas_sources, version, f"**/*.schema.omi.json"),
            recursive=True,
        )


class InstanceLoader:
    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.instances_sources = os.path.join(self._root_directory, "_sources/instances", "instances")

    def get_instance_versions(self) -> List[str]:
        return os.listdir(self.instances_sources)

    def find_instances(self, version: str) -> List[str]:
        return glob.glob(
            os.path.join(self.instances_sources, version, f"**/*.jsonld"),
            recursive=True,
        )
