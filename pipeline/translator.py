from datetime import date, time, datetime
import json
from numbers import Real
import os.path
import re
from typing import List, Optional, Dict
from jinja2 import Environment, select_autoescape, FileSystemLoader


number_names = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def generate_python_name(json_name, allow_multiple=False):
    python_name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", json_name.strip())
    python_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", python_name).lower()
    replacements = [
        ("-", "_"),
        (".", "_"),
        ("'", "_prime_"),
        ("+", "plus"),
        ("#", "sharp"),
        (",", "comma"),
        ("(", ""),
        (")", ""),
    ]
    for before, after in replacements:
        python_name = python_name.replace(before, after)
    if python_name[0] in number_names:  # Python variables can't start with a number
        python_name = number_names[python_name[0]] + python_name[1:]
    if not python_name.isidentifier():
        raise NameError(f"Cannot generate a valid Python name from '{json_name}'")
    return python_name


def customize_description(property, obj_title):
    """Replace generic text with a type-specific name."""
    if obj_title.upper() == obj_title:  # for acronyms, e.g. DOI
        obj_title_readable = obj_title
    elif "UBERON" in obj_title:
        obj_title_readable = obj_title
    else:
        obj_title_readable = re.sub("([A-Z])", " \g<0>", obj_title).strip().lower()
    doc = property.get("description", "no description available")
    doc = doc.replace("someone or something", f"the {obj_title_readable}")
    doc = doc.replace("something or somebody", f"the {obj_title_readable}")
    doc = doc.replace("something or someone", f"the {obj_title_readable}")
    doc = doc.replace("a being or thing", f"the {obj_title_readable}")
    return doc


class PythonBuilder(object):
    """docstring"""

    def __init__(
        self,
        schema_file_path: str,
        root_path: str,
        instances: Optional[dict] = None,
        additional_methods: Optional[dict] = None,
    ):
        self.env = Environment(
            loader=FileSystemLoader(os.path.dirname(os.path.realpath(__file__))), autoescape=select_autoescape()
        )
        _relative_path_without_extension = (
            schema_file_path[len(root_path) + 1 :].replace(".schema.omi.json", "").split("/")
        )
        self.version = _relative_path_without_extension[0]
        self.template_name = "src/module_template.py.txt"
        if self.version in ["v3.0", "v2.0", "v1.0"]:
            self.context_vocab = "https://openminds.ebrains.eu/vocab/"
        else:
            self.context_vocab = "https://openminds.om-i.org/props/"

        self.relative_path_without_extension = [
            generate_python_name(part) for part in _relative_path_without_extension[1:]
        ]
        with open(schema_file_path, "r") as schema_f:
            self._schema_payload = json.load(schema_f)
        self.instances = instances or {}
        self.additional_methods = additional_methods

    @property
    def _version_module(self):
        # we keep only the major version.
        # this code assumes that minor versions are processed from oldest to newest
        # so that the Python package will always contain the latest minor version
        return self.version.split(".")[0]

    def _target_file_without_extension(self) -> str:
        return os.path.join(self._version_module, "/".join(self.relative_path_without_extension))

    def translate(self, embedded=None, class_to_module_map=None):
        def get_type(property):
            type_map = {
                "string": "str",
                "integer": "int",
                "number": "Real",
                "date": "date",
                "date-time": "datetime",
                "time": "time",
                "iri": "IRI",
                "email": "str",  # todo: add an Email class for validation?
                "ECMA262": "str",  #       ...
                "boolean": "bool",
            }
            if "_linkedTypes" in property:
                types = []
                for item in property["_linkedTypes"]:
                    openminds_module_from_type, class_name = item.split("/")[-2:]
                    if isinstance(class_to_module_map, dict) and (class_name in class_to_module_map):
                        openminds_module = generate_python_name(class_to_module_map[class_name])
                    else:
                        openminds_module = generate_python_name(openminds_module_from_type)
                    types.append(f"openminds.{self._version_module}.{openminds_module}.{class_name}")
                if len(types) == 1:
                    types = f'"{types[0]}"'
                return types
            elif "_embeddedTypes" in property:
                types = []
                for item in property["_embeddedTypes"]:
                    openminds_module_from_type, class_name = item.split("/")[-2:]
                    if isinstance(class_to_module_map, dict) and (class_name in class_to_module_map):
                        openminds_module = generate_python_name(class_to_module_map[class_name])
                    else:
                        openminds_module = generate_python_name(openminds_module_from_type)
                    types.append(f"openminds.{self._version_module}.{openminds_module}.{class_name}")
                if len(types) == 1:
                    types = f'"{types[0]}"'
                return types
            elif "type" in property:
                if isinstance(property["type"], list):
                    return [type_map[item] for item in property["type"]]
                else:
                    if property["type"] == "array":
                        return type_map[property["items"]["type"]]
                    elif "_formats" in property:
                        assert isinstance(property["_formats"], list)
                        if len(property["_formats"]) > 1:
                            types = f"[{', '.join([type_map[p] for p in property['_formats']])}]"
                            return types
                        return type_map[property["_formats"][0]]
                    else:
                        return type_map[property["type"]]

            else:
                raise NotImplementedError

        class_name = self._schema_payload["name"]
        openminds_type = self._schema_payload["_type"]
        if openminds_type in embedded:
            base_class = "EmbeddedMetadata"
        else:
            base_class = "LinkedMetadata"

        def filter_value(value):
            if isinstance(value, str):
                return value.replace('"', "'").replace("\n", " ")
            return value

        def filter_instance(instance):
            filtered_instance = {
                k: filter_value(v) for k, v in instance.items() if k[0] != "@" and k[:4] != "http" and v is not None
            }
            filtered_instance["id"] = instance["@id"]
            return filtered_instance

        instances = {
            generate_python_name(instance["@id"].split("/")[-1]): filter_instance(instance)
            for instance in self.instances.get(openminds_type, [])
        }
        instances = {name: instances[name] for name in sorted(instances)}  # sort by key

        properties = []
        for iri, property in self._schema_payload["properties"].items():
            allow_multiple = property.get("type", "") == "array"
            if allow_multiple:
                if "namePlural" in property:
                    property_name = property["namePlural"]
                else:
                    print(f"Missing plural name for '{property['name']}'")
                    property_name = property["name"] + "s"
            else:
                property_name = property["name"]
            pythonic_name = generate_python_name(property_name)
            properties.append(
                {
                    "name": pythonic_name,
                    "type": get_type(property),  # compress using JSON-LD context
                    "iri": property["name"],  # assumes IRI uses standard @vocab
                    "allow_multiple": allow_multiple,
                    "required": iri in self._schema_payload.get("required", []),
                    "description": customize_description(property, class_name),
                    "instructions": property.get("_instruction", "no instructions available"),
                    "formatting": property.get("formatting", None),
                    "multiline": property.get("multiline", None),
                    "unique_items": property.get("uniqueItems", False),
                    "min_items": property.get("minItems", None),
                    "max_items": property.get("maxItems", None),
                }
            )
            # unused in property:  "nameForReverseLink"
            for instance in instances.values():
                if property["name"] in instance:
                    instance[pythonic_name] = instance.pop(property["name"])
        self.context = {
            "docstring": self._schema_payload.get("description", "<description not available>"),
            "base_class": base_class,
            "preamble": "",  # default value, may be updated below
            "class_name": class_name,
            "openminds_type": openminds_type,
            "schema_version": self.version,
            "context_vocab": self.context_vocab,
            "properties": properties,
            "additional_methods": "",
            "instances": instances,
        }

        if len(instances) > 0:
            self.context["additional_methods"] = self.additional_methods["by_name"]

        import_map = {
            "date": "from datetime import date",
            "datetime": "from datetime import datetime",
            "time": "from datetime import time",
            "IRI": "from openminds.base import IRI",
            "[datetime, time]": "from datetime import datetime, time",
            "Real": "from numbers import Real",
        }
        extra_imports = set()
        if len(instances) > 0:
            extra_imports.add(import_map["IRI"])
        for property in self.context["properties"]:
            if isinstance(property["type"], list):
                for t in property["type"]:
                    imp = import_map.get(t, None)
                    if imp:
                        extra_imports.add(imp)
            else:
                imp = import_map.get(property["type"], None)
                if imp:
                    extra_imports.add(imp)
            if extra_imports:
                self.context["preamble"] = "\n".join(sorted(extra_imports))

    def build(self, embedded=None, class_to_module_map=None):
        target_file_path = os.path.join("target", "openminds", f"{self._target_file_without_extension()}.py")
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        self.translate(embedded=embedded, class_to_module_map=class_to_module_map)

        with open(target_file_path, "w") as target_file:
            contents = self.env.get_template(self.template_name).render(self.context)
            target_file.write(contents)

        return (self._target_file_without_extension().replace("/", "."), self.context["class_name"])

    def get_edges(self):
        embedded = set()
        linked = set()
        for property in self._schema_payload["properties"].values():
            embedded.update(property.get("_embeddedTypes", []))
            linked.update(property.get("_linkedTypes", []))
        return embedded, linked

    def update_class_to_module_map(self, class_to_module_map):
        """
        Updates a dictionary with the class name and its corresponding module based on the schemas.

        This method extracts the class name and module from the `_schema_payload` attribute
        and updates the provided dictionary (`class_to_module_map`) with a mapping of
        the class name to its module. If the `_module` key exists in `_schema_payload`
        (which was introduced in version 4 of openMINDS), its value is used as the module.
        Otherwise, the module is derived from the second-to-last component of the `_type`
        field in `_schema_payload`.

        Args:
            class_to_module_map (dict): A dictionary where keys are class names and values
                                      are their corresponding modules.

        Returns:
            dict: The updated dictionary with the class name and module mapping.
        """
        schema_type = self._schema_payload["_type"]
        class_name = schema_type.split("/")[-1]
        if "_module" in self._schema_payload:
            module = self._schema_payload["_module"]
        else:
            module = schema_type.split("/")[-2]

        class_to_module_map[class_name] = module

        return class_to_module_map
