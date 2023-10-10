from datetime import date, time, datetime
import json
import os.path
import re
from typing import List, Optional, Dict
from jinja2 import Environment, select_autoescape, FileSystemLoader


def generate_python_name(json_name, allow_multiple=False):
    python_name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", json_name)
    python_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", python_name).lower()
    python_name = python_name.replace("-", "_")
    # if (
    #     allow_multiple
    #     and python_name[-1] != "s"
    #     and python_name[-3:] not in ("_of", "_by", "_in", "_to")
    #     and not python_name.endswith("data")
    # ):
    #     if python_name in custom_multiple:
    #         python_name = custom_multiple[python_name]
    #     elif python_name.endswith("y"):
    #         python_name = python_name[:-1] + "ies"
    #     else:
    #         python_name += "s"
    # elif python_name in custom_singular:
    #     python_name = custom_singular[python_name]
    # if isinstance(python_name, list):
    #     python_name.sort()
    return python_name


class PythonBuilder(object):
    """docstring"""

    def __init__(self, schema_file_path: str, root_path: str):
        self.template_name = "src/module_template.py.txt"
        self.env = Environment(
            loader=FileSystemLoader(os.path.dirname(os.path.realpath(__file__))), autoescape=select_autoescape()
        )
        _relative_path_without_extension = (
            schema_file_path[len(root_path) + 1 :].replace(".schema.omi.json", "").split("/")
        )
        self.version = _relative_path_without_extension[0]
        self.relative_path_without_extension = [
            generate_python_name(part) for part in _relative_path_without_extension[1:]
        ]
        with open(schema_file_path, "r") as schema_f:
            self._schema_payload = json.load(schema_f)

    def _target_file_without_extension(self) -> str:
        return os.path.join(self.version.replace(".", "_"), "/".join(self.relative_path_without_extension))

    def translate(self, embedded=None):
        def get_type(property):
            type_map = {
                "string": "str",
                "integer": "int",
                "number": "float",
                "date": "date",
                "date-time": "datetime",
                "time": "time",
                "iri": "IRI",
                "email": "str",  # todo: add an Email class for validation?
                "ECMA262": "str",  #       ...
            }
            version_module = self.version.replace(".", "_")
            if "_linkedTypes" in property:
                types = []
                for item in property["_linkedTypes"]:
                    openminds_module, class_name = item.split("/")[-2:]
                    openminds_module = generate_python_name(openminds_module)
                    types.append(f"openminds.{version_module}.{openminds_module}.{class_name}")
                if len(types) == 1:
                    types = f'"{types[0]}"'
                return types
            elif "_embeddedTypes" in property:
                types = []
                for item in property["_embeddedTypes"]:
                    openminds_module, class_name = item.split("/")[-2:]
                    openminds_module = generate_python_name(openminds_module)
                    types.append(f"openminds.{version_module}.{openminds_module}.{class_name}")
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

        if self._schema_payload["_type"] in embedded:
            base_class = "EmbeddedMetadata"
        else:
            base_class = "LinkedMetadata"
        self.context = {
            "docstring": self._schema_payload.get("description", "<description not available>"),
            "base_class": base_class,
            "preamble": "",  # todo: e.g. extra imports
            "class_name": self._schema_payload["name"],
            "openminds_type": self._schema_payload["_type"],
            "properties": [  # call this "properties"
                {
                    "name": generate_python_name(property["name"]),
                    "type": get_type(property),  # compress using JSON-LD context
                    "iri": property['name'],  # assumes IRI uses standard @vocab
                    "allow_multiple": property.get("type", "") == "array",
                    "required": iri in self._schema_payload.get("required", []),
                    "description": property.get("description", "no description available"),
                    "instructions": property.get("_instruction", "no instructions available"),
                    "formatting": property.get("formatting", None),
                    "multiline": property.get("multiline", None),
                    "unique_items": property.get("uniqueItems", False),
                    "min_items": property.get("minItems", None),
                    "max_items": property.get("maxItems", None),
                }
                for iri, property in self._schema_payload["properties"].items()
            ],  # todo
            # unused in property:  "nameForReverseLink"
            "additional_methods": "",
        }
        import_map = {
            "date": "from datetime import date",
            "datetime": "from datetime import datetime",
            "time": "from datetime import time",
            "IRI": "from openminds.base import IRI",
            "[datetime, time]": "from datetime import datetime, time",
        }
        extra_imports = set()
        for property in self.context["properties"]:
            if isinstance(property["type"], list):
                for t in property["type"]:
                    imp = import_map.get(t, None)
                    if imp:
                        extra_imports.add(imp)
                        breakpoint()
            else:
                imp = import_map.get(property["type"], None)
                if imp:
                    extra_imports.add(imp)
            if extra_imports:
                self.context["preamble"] = "\n".join(extra_imports)

    def build(self, embedded=None):
        target_file_path = os.path.join("target", "openminds", f"{self._target_file_without_extension()}.py")
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        self.translate(embedded=embedded)

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
