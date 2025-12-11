"""
Representations of metadata fields/properties

# Copyright (c) 2025 openMetadataInitiative
"""

from datetime import datetime, date
from collections import defaultdict
from numbers import Real
from typing import Optional, Union, Iterable

from .registry import lookup
from .base import Node, IRI, Link


def _could_be_instance(value, types):
    """
    True if a Link's allowed types are consistent with the given types
    """
    return isinstance(value, Link) and value.allowed_types and set(value.allowed_types).issubset(types)


class Property:
    """
    Representation of an openMINDS property (a metadata field).

    Args:
        name (str): The name of the field.
        types (str, date, datetime, int, KGObject, EmbeddedMetadata): The types of values that the field can take.
        path (URI): The globally unique identifier of this field.
        required (bool, optional): Whether the field is required or not. Defaults to False.
        multiple (bool, optional): Whether the field can have multiple values or not. Defaults to False.
        reverse (str, optional): The name of the reverse field, if any.
        formatting (str, optional): todo
        multiline (bool, optional): todo - defaults to False
        description (str, optional): todo
        instructions (str, optional): todo
        unique_items (str, optional): todo
        min_items (int, optional): todo
        max_items (int, optional): todo


    The class also contains machinery for serialization into JSON-LD of values stored in fields in
    KGObjects and EmbeddedMetadata instances, and for de-serialization from JSON-LD into Python objects.
    """

    def __init__(
        self,
        name: str,
        types: Union[
            str,
            type,
            Node,
            Iterable[Union[str, type, Node]],
        ],
        path: str,
        required: bool = False,
        multiple: bool = False,
        reverse: Optional[str] = None,
        formatting: Optional[str] = None,
        multiline: bool = False,
        description: str = "",
        instructions: str = "",
        unique_items: bool = False,
        min_items: Optional[int] = None,
        max_items: Optional[int] = None,
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

    @property
    def is_link(self) -> bool:
        return issubclass(self.types[0], Node)

    def validate(self, value, ignore=None, seen=None):
        """
        Check whether `value` satisfies all constraints.

        Arguments:
            value: the value to be checked
            ignore: an optional list of check types that should be ignored
                    ("required", "type", "multiplicity")
            seen: for internal use: contains a set with Python object ids that have
                  already been encountered in the validation tree.

        Returns a dict containing information about any validation failures.
        """
        if ignore is None:
            ignore = []
        if not isinstance(ignore, (list, tuple)):
            raise TypeError("`ignore` must be a list or tuple")
        failures = defaultdict(list)
        if value is None:
            if self.required and "required" not in ignore:
                failures["required"].append(f"{self.name} is required, but was not provided")
        else:
            if self.multiple:
                if not isinstance(value, (list, tuple)):
                    value = [value]
                for item in value:
                    if not (isinstance(item, self.types) or _could_be_instance(item, self.types)):
                        if "type" not in ignore:
                            if isinstance(item, Link):
                                item_type = f"value contains a link to {item.allowed_types}"
                            else:
                                item_type = f"value contains {type(item).__name__}"
                            failures["type"].append(
                                f"{self.name}: Expected {', '.join(t.__name__ for t in self.types)}, " + item_type
                            )
                    elif isinstance(item, (Node, IRI)):
                        failures.update(item._validate(ignore=ignore, seen=seen))
                if self.min_items:
                    if len(value) < self.min_items and "multiplicity" not in ignore:
                        failures["multiplicity"].append(
                            f"{self.name}: minimum {self.min_items} items required, value only contains {len(value)}"
                        )
                if self.max_items:
                    if len(value) > self.max_items and "multiplicity" not in ignore:
                        failures["multiplicity"].append(
                            f"{self.name}: maximum {self.max_items} items allowed, value contains {len(value)}"
                        )
                if self.unique_items:
                    try:
                        unique_items = set(value)
                    except TypeError:  # unhashable, i.e. can't anyway check if items are unique
                        pass
                    else:
                        if len(unique_items) < len(value) and "multiplicity" not in ignore:
                            failures["multiplicity"].append(f"{self.name}: items in array should be unique")
            elif isinstance(value, (list, tuple)):
                if "multiplicity" not in ignore:
                    failures["multiplicity"].append(
                        f"{self.name} does not accept multiple values, but contains {len(value)}"
                    )
            elif not (isinstance(value, self.types) or _could_be_instance(value, self.types)):
                if "type" not in ignore:
                    if isinstance(value, Link):
                        value_type = f"value contains a link to {value.allowed_types}"
                    else:
                        value_type = f"value contains {type(value).__name__}"
                    failures["type"].append(
                        f"{self.name}: Expected {', '.join(t.__name__ for t in self.types)}, " + value_type
                    )
            elif isinstance(value, (Node, IRI)):
                failures.update(value._validate(ignore=ignore, seen=seen))
        # todo: check formatting, multiline
        return failures

    def deserialize(self, data):
        """
        Deserialize a JSON-LD data structure into Python objects.

        Args:
            data: the JSON-LD data
        """
        # todo: check data type
        link_keys = set(("@id", "@type"))

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
            elif Real in self.types:
                return item
            elif int in self.types:
                return item
            elif datetime in self.types:
                return datetime.fromisoformat(item)
            elif date in self.types:
                try:
                    return date.fromisoformat(item)
                except ValueError as err:
                    # if a datetime string has been provided
                    # take the date part.
                    try:
                        return datetime.fromisoformat(item).date()
                    except ValueError:
                        raise err
            elif all(issubclass(t, Node) for t in self.types):
                # use data["@type"] to figure out class to use
                if "@type" in item:
                    if isinstance(item["@type"], list) and len(item["@type"]) == 1:
                        item_type = item["@type"][0]
                    else:
                        item_type = item["@type"]
                    for cls in self.types:
                        if cls.type_ == item_type:
                            if set(item.keys()) == link_keys:
                                # if we only have @id and @type, it's a Link
                                return Link(item["@id"], allowed_types=[cls])
                            else:
                                # otherwise it's a Node
                                return cls.from_jsonld(item)
                    raise TypeError(
                        f"Mismatched types. Data has '{item_type}' "
                        f"but property only allows one of {[cls.type_ for cls in self.types]}"
                    )
                else:
                    return Link(item["@id"], allowed_types=self.types)
            else:
                raise NotImplementedError()

        if isinstance(data, (tuple, list)):
            return [deserialize_item(item) for item in data]
        else:
            return deserialize_item(data)
