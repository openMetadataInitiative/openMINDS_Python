"""
Classes and functions for looking up schema classes
based on names and type identifiers.

"""

from __future__ import annotations
from collections import defaultdict
from typing import TYPE_CHECKING, Union, List, Dict
from warnings import warn

if TYPE_CHECKING:
    from .base import Node
    from .properties import Property


registry: dict = {"names": {}, "types": defaultdict(dict)}


def register_class(target_class: Registry):
    """Add a class to the registry"""
    if hasattr(target_class, "schema_version"):
        assert "openminds" in target_class.__module__
        parts = target_class.__module__.split(".")
        version = target_class.schema_version.split(".")[0]  # e.g. 'v3' or 'latest'
        name = ".".join(parts[0:3] + [target_class.__name__])  # e.g. openminds.latest.core.Dataset
        # taking the first 3 parts is artbitrary, should add an attribute to each class
        # with its preferred import name
        # e.g. for `openminds.latest.core.research.protocol_execution.ProtocolExecution`
        #      the preferred import name is `openminds.latest.core.ProtocolExecution`
        #      because the intermediate directory structure is an implementation detail

        registry["names"][name] = target_class

        if isinstance(target_class.type_, str):
            type_ = target_class.type_
            registry["types"][version][type_] = target_class
        else:
            for type_ in target_class.type_:
                registry["types"][version][type_] = target_class


def lookup(class_name: str) -> Node:
    """Return the class whose name is given."""
    return registry["names"][class_name]


def lookup_type(class_type: str, version: str = "latest") -> Node:
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

    properties: List[Property] = []
    type_: Union[str, List[str]]
    context: Dict[str, str]
    _base_docstring: str

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

    __doc__ = property(_get_doc)  # type: ignore[assignment]

    @property
    def property_names(cls) -> List[str]:
        return [p.name for p in cls.properties]

    @property
    def required_property_names(cls) -> List[str]:
        return [p.name for p in cls.properties if p.required]
