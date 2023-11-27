"""
Representations of metadata fields/properties

# Copyright (c) 2023 openMetadataInitiative
"""

from datetime import datetime, date
from collections import defaultdict
from .registry import lookup
from .base import Node, IRI, Link


class Property:
    """Representation of an openMINDS property (a metadata field)."""

    def __init__(
        self,
        name,
        types,
        path,
        required=False,
        multiple=False,
        reverse=None,
        formatting=None,
        multiline=False,
        description="",
        instructions="",
        unique_items=None,
        min_items=None,
        max_items=None,
    ):
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
        self.multiline = multiline
        self.description = description
        self.instructions = instructions
        self.unique_items = unique_items
        self.min_items = min_items
        self.max_items = max_items
        self._resolved_types = False

    def __repr__(self):
        return "Property(name='{}', types={}, path='{}', required={}, multiple={})".format(
            self.name, self._types, self.path, self.required, self.multiple
        )

    @property
    def types(self):
        if not self._resolved_types:
            self._types = tuple([lookup(obj) if isinstance(obj, str) else obj for obj in self._types])
            self._resolved_types = True
        return self._types

    def validate(self, value):
        """
        Check whether `value` satisfies all constraints.

        Returns a dict containing information about any validation failures.
        """
        failures = defaultdict(list)
        if value is None:
            if self.required:
                failures["required"].append(f"{self.name} is required, but was not provided")
        else:
            if self.multiple:
                if not isinstance(value, (list, tuple)):
                    value = [value]
                for item in value:
                    if not isinstance(item, self.types):
                        failures["type"].append(
                            f"{self.name}: Expected {', '.join(t.__name__ for t in self.types)}, "
                            f"value contains {type(item)}"
                        )
                    elif isinstance(item, Node):
                        failures.update(item.validate())
                if self.min_items:
                    if len(value) < self.min_items:
                        failures["multiplicity"].append(
                            f"{self.name}: minimum {self.min_items} items required, "
                            f"value only contains {len(value)}"
                        )
                if self.max_items:
                    if len(value) > self.max_items:
                        failures["multiplicity"].append(
                            f"{self.name}: maximum {self.max_items} items allowed, " f"value contains {len(value)}"
                        )
                if self.unique_items:
                    try:
                        unique_items = set(value)
                    except TypeError:  # unhashable, i.e. can't anyway check if items are unique
                        pass
                    else:
                        if len(unique_items) < len(value):
                            failures["multiplicity"].append(f"{self.name}: items in array should be unique")
            elif isinstance(value, (list, tuple)):
                failures["multiplicity"].append(
                    f"{self.name} does not accept multiple values, but contains {len(value)}"
                )
            elif not isinstance(value, self.types):
                failures["type"].append(
                    f"{self.name}: Expected {', '.join(t.__name__ for t in self.types)}, " f"value is {type(value)}"
                )
            elif isinstance(value, Node):
                failures.update(value.validate())
        # todo: check formatting, multiline
        return failures

    def deserialize(self, data):
        """
        Deserialize a JSON-LD data structure into Python objects.

        Args:
            data: the JSON-LD data
        """

        # todo: check data type
        def deserialize_item(item):
            if self.types == (str,):
                if self.formatting != "text/plain":
                    pass  # todo
                return item
            elif self.types == (IRI,):
                assert isinstance(item, str)
                return IRI(item)
            elif float in self.types:
                return item
            elif int in self.types:
                return item
            elif datetime in self.types:
                return datetime.fromisoformat(item)
            elif date in self.types:
                return date.fromisoformat(item)
            elif all(issubclass(t, Node) for t in self.types):
                # use data["@type"] to figure out class to use
                if "@type" in item:
                    for cls in self.types:
                        if cls.type_ == item["@type"]:
                            return cls.from_jsonld(item)
                else:
                    return Link(item["@id"])
            else:
                raise NotImplementedError()

        if self.multiple and isinstance(data, (tuple, list)):
            return [deserialize_item(item) for item in data]
        else:
            return deserialize_item(data)
