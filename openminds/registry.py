"""
Classes and functions for looking up schema classes
based on names and type identifiers.

"""

from __future__ import annotations
from collections import defaultdict
from typing import TYPE_CHECKING, Union, List, Optional

if TYPE_CHECKING:
    from .base import ContainsMetadata

registry: dict = {"names": {}, "types": defaultdict(dict)}


def register_class(target_class: ContainsMetadata):
    """Add a class to the registry"""
    if "openminds" in target_class.__module__:
        parts = target_class.__module__.split(".")
        assert parts[0] == "openminds"
        version = parts[1]
        name = ".".join(parts[0:3] + [target_class.__name__])  # e.g. openminds.latest.core.Dataset

        if hasattr(target_class, "type_"):
            registry["names"][name] = target_class
            type_ = target_class.type_
            registry["types"][version][type_] = target_class


def lookup(class_name: str) -> ContainsMetadata:
    """Return the class whose name is given."""
    return registry["names"][class_name]


def lookup_type(class_type: str, version: str = "latest") -> ContainsMetadata:
    """Return the class whose global type identifier (a URI) is given."""
    if isinstance(class_type, str):
        if class_type in registry["types"][version]:
            return registry["types"][version][class_type]
        else:
            raise ValueError(f"Type '{class_type}' was not found in the registry for version {version}.")
    else:
        raise TypeError("class type must be a string")


docstring_template = """
{base}

Args
----
{args}

"""


class Registry(type):
    """Metaclass for registering Knowledge Graph classes."""

    properties = []

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        cls._base_docstring = class_dict.get("__doc__", "").strip()
        register_class(cls)
        return cls

    def _get_doc(cls) -> str:
        """Dynamically generate docstrings"""
        field_docs = []
        if hasattr(cls, "properties"):

            def gen_path(type_):
                if type_.__module__ == "builtins":
                    return type_.__name__
                else:
                    return "~{}.{}".format(type_.__module__, type_.__name__)

            for property in cls.properties:
                doc = "{} : {}\n    {}".format(
                    property.name, ", ".join(gen_path(t) for t in property.types), property.description
                )
                # todo: add property.instructions if present
                field_docs.append(doc)
        return docstring_template.format(base=cls._base_docstring, args="\n".join(field_docs))

    __doc__ = property(_get_doc)
