"""
Representations of metadata fields/properties

# Copyright (c) 2023 openMetadataInitiative
"""

from .registry import lookup
from .base import Node


class Property:
    """Representation of an openMINDS property (a metadata field)."""

    def __init__(self, name, types, path, required=False, multiple=False,
                 reverse=None, formatting=None, description="", instructions="",
                 unique_items=None, min_items=None, max_items=None):
        self.name = name
        if isinstance(types, (type, str)):
            self._types = (types,)
        else:
            self._types = tuple(types)
        self._resolved_types = False
        self.path = path
        self.required = required
        self.multiple = multiple
        self.reverse = reverse
        self.formatting = formatting
        self.description = description
        self.instructions = instructions
        self.unique_items = unique_items
        self.min_items = min_items
        self.max_items = max_items
        self._resolved_types = False

    def __repr__(self):
        return "Property(name='{}', types={}, path='{}', required={}, multiple={})".format(
            self.name, self._types, self.path, self.required, self.multiple)

    @property
    def types(self):
        if not self._resolved_types:
            self._types = tuple([lookup(obj) if isinstance(obj, str) else obj for obj in self._types])
            self._resolved_types = True
        return self._types

    def deserialize(self, data):
        """
        Deserialize a JSON-LD data structure into Python objects.

        Args:
            data: the JSON-LD data
        """
        # todo: check data type
        if self.types == (str,):
            if self.formatting != "text/plain":
                breakpoint()
            return data
        elif float in self.types:
            return data
        elif int in self.types:
            return data
        elif all(issubclass(t, Node) for t in self.types):
            # use data["@type"] to figure out class to use
            if "@type" in data:
                for cls in self.types:
                    if cls.type_ == data["@type"]:
                        return cls.from_jsonld(data)
            else:
                raise Exception("missing @type")
        else:
            raise NotImplementedError()