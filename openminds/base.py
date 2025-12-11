"""
This module contains base classes that define interfaces
and contain code common to sub-classes, to avoid code duplication.

# Copyright (c) 2025 openMetadataInitiative
"""

from __future__ import annotations

from datetime import date, datetime
from collections import defaultdict
import json
from typing import Union

import rfc3987

from .registry import Registry


def value_to_jsonld(value, include_empty_properties=True, embed_linked_nodes=True):
    if isinstance(value, LinkedMetadata):
        if embed_linked_nodes:
            item = value.to_jsonld(
                with_context=False,
                include_empty_properties=include_empty_properties,
                embed_linked_nodes=embed_linked_nodes,
            )
        else:
            if hasattr(value, "id") and value.id is None:
                raise ValueError("Exporting as a stand-alone JSON-LD document requires @id to be defined.")
            item = {"@id": value.id}
    elif isinstance(value, EmbeddedMetadata):
        item = value.to_jsonld(
            with_context=False,
            include_empty_properties=include_empty_properties,
            embed_linked_nodes=embed_linked_nodes,
        )
    elif hasattr(value, "to_jsonld"):  # e.g. IRI
        item = value.to_jsonld()
    elif isinstance(value, (date, datetime)):
        item = value.isoformat()
    else:
        item = value
    return item


class Node(metaclass=Registry):
    """
    Base class for a metadata node
    """

    @property
    def uuid(self):
        if self.id is not None:
            return self.id.split("/")[-1]
        else:
            return None

    def has_property(self, name):
        for property in self.properties:
            if property.name == name:
                return True
        return False

    def to_jsonld(self, include_empty_properties=True, embed_linked_nodes=True, with_context=True):
        """
        Return a represention of this metadata node as a dictionary that can be directly serialized to JSON-LD.
        """

        data = {"@type": self.type_}
        if with_context:
            if self.type_.startswith("https://openminds.ebrains.eu/"):
                data["@context"] = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
            else:
                data["@context"] = {"@vocab": "https://openminds.om-i.org/props/"}
        if hasattr(self, "id") and self.id:
            data["@id"] = self.id
        for property in self.__class__.properties:
            value = getattr(self, property.name)
            if value or include_empty_properties:
                if property.multiple:
                    if value is None:
                        data[property.path] = value
                    else:
                        if not isinstance(value, (tuple, list)):
                            value = [value]
                        data[property.path] = [
                            value_to_jsonld(
                                item,
                                include_empty_properties=include_empty_properties,
                                embed_linked_nodes=embed_linked_nodes,
                            )
                            for item in value
                        ]
                elif isinstance(value, (tuple, list)):
                    # if property.multiple is False, then this means the node does not validate,
                    # but we should try to serialize it anyway
                    data[property.path] = [
                        value_to_jsonld(
                            item,
                            include_empty_properties=include_empty_properties,
                            embed_linked_nodes=embed_linked_nodes,
                        )
                        for item in value
                    ]
                else:
                    data[property.path] = value_to_jsonld(
                        value,
                        include_empty_properties=include_empty_properties,
                        embed_linked_nodes=embed_linked_nodes,
                    )
        return {key: data[key] for key in sorted(data)}

    @classmethod
    def from_jsonld(cls, data, ignore_unexpected_keys=False):
        """
        Create a Python object representing a metadata node from a JSON-LD-compatible dictionary.

        By default, a NameError will be raised if the data contain keys that are not
        recognised by this metadata node.
        If `ignore_unexpected_keys` is set to True, no error is raised.
        """
        data_copy = data.copy()
        context = data_copy.pop("@context", None)
        type_ = data_copy.pop("@type")
        if isinstance(type_, list) and len(type_) == 1:
            type_ = type_[0]
        if type_ and type_ != cls.type_:
            raise TypeError(f"Mismatched types. Data has '{type_}' but trying to create '{cls.type_}'")
        deserialized_data = {}
        if issubclass(cls, LinkedMetadata):
            deserialized_data["id"] = data_copy.pop("@id", None)
        for property in cls.properties:
            found = False
            if property.path in data_copy:
                value = data_copy.pop(property.path)
                found = True
            else:
                # todo: implement or import a function that does a full JSON-LD expansion
                #       not just this special case
                expanded_path = f"{cls.context['@vocab']}{property.path}"
                if expanded_path in data_copy:
                    value = data_copy.pop(expanded_path)
                    found = True
            if found:
                if value:
                    deserialized_data[property.name] = property.deserialize(value)
                else:
                    deserialized_data[property.name] = value
        if len(data_copy) > 0 and not ignore_unexpected_keys:
            raise NameError(f"Unexpected arguments for {cls}: {tuple(data_copy.keys())}")
        return cls(**deserialized_data)

    def validate(self, ignore=None):
        """
        Check whether all constraints are satisfied.

        Arguments:
            ignore: an optional list of check types that should be ignored
                    ("required", "type", "multiplicity")

        Returns a dict containing information about any validation failures.
        """
        return dict(self._validate(ignore=ignore))

    def _validate(self, ignore=None, seen=None):
        # this is implemented as an internal method so that the
        # "seen" set, needed to avoid possible infinite recursion,
        # can be hidden from the public interface.
        if seen is None:
            seen = set()
        failures = defaultdict(list)
        for property in self.properties:
            value = getattr(self, property.name, None)
            if (id(self), property.name) not in seen:
                seen.add((id(self), property.name))
                for key, values in property.validate(value, ignore=ignore, seen=seen).items():
                    failures[key] += values
        return failures

    @property
    def is_valid(self):
        failures = self.validate()
        return len(failures) == 0

    @property
    def links(self):
        """
        Return a list of attributes that reference other metadata nodes
        """
        _links = []
        for property in self.__class__.properties:
            value = getattr(self, property.name)
            if property.multiple:
                if not isinstance(value, (tuple, list)):
                    value = [value]
                for item in value:
                    if isinstance(item, LinkedMetadata):
                        _links.append(item)
                    if hasattr(item, "links"):
                        _links.extend(item.links)
            elif isinstance(value, LinkedMetadata):
                _links.append(value)
            if hasattr(value, "links"):
                _links.extend(value.links)
        return _links

    def _resolve_links(self, node_lookup):
        """Replace `Link` attributes with typed Nodes where possible"""
        for property in self.__class__.properties:
            value = getattr(self, property.name)
            if isinstance(value, Link):
                resolved_value = node_lookup.get(value.identifier, value)
                setattr(self, property.name, resolved_value)
            elif hasattr(value, "_resolve_links"):
                value._resolve_links(node_lookup)
            elif isinstance(value, (tuple, list)):
                resolved_values = []
                for item in value:
                    if isinstance(item, Link):
                        resolved_values.append(node_lookup[item.identifier])
                    else:
                        resolved_values.append(item)
                        if hasattr(item, "_resolve_links"):
                            item._resolve_links(node_lookup)
                setattr(self, property.name, resolved_values)


class LinkedMetadata(Node):
    """
    A Python representation of a metadata node that should have a unique identifier.
    """

    _instance_lookup = None

    def __init__(self, id=None, **properties):
        self.id = id  # todo: check this is a URI
        for name, value in properties.items():
            setattr(self, name, value)

    def save(self, file_path, indent=2):
        """
        Save this object to a file in JSON-LD format.

        It is recommended to use the extension ".jsonld".
        """
        with open(file_path, "w") as output_file:
            json.dump(self.to_jsonld(), output_file, indent=indent)

    @classmethod
    def load(cls, file_path, ignore_unexpected_keys=False):
        """
        Create a Python object representing a metadata node from a JSON-LD file.

        By default, a NameError will be raised if the data contain keys that are not
        recognised by this metadata node.
        If `ignore_unexpected_keys` is set to True, no error is raised.
        """
        with open(file_path, "r") as input_file:
            data = json.load(input_file)
        return cls.from_jsonld(data, ignore_unexpected_keys=ignore_unexpected_keys)


class EmbeddedMetadata(Node):
    """
    A Python representation of a metadata node that should only be embedded within another node,
    and should not have a unique identifier.
    """

    def __init__(self, **properties):
        for name, value in properties.items():
            setattr(self, name, value)


class Link:
    """Representation of a metadata node for which only the identifier is currently known."""

    def __init__(self, identifier, allowed_types=None):
        self.identifier = identifier
        self.allowed_types = allowed_types

    def to_jsonld(self):
        return {"@id": self.identifier}


class IRI:
    """
    Representation of an International Resource Identifier
    """

    def __init__(self, value: Union[str, IRI]):
        if isinstance(value, IRI):
            iri = value.value
        else:
            iri = value
        if not rfc3987.match(iri, rule="IRI"):
            raise ValueError("Invalid IRI")
        self.value: str = iri

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value

    def __repr__(self):
        return f"IRI({self.value})"

    def __str__(self):
        return self.value

    def to_jsonld(self):
        return self.value

    def _validate(self, ignore=None, seen=None):
        if ignore is None:
            ignore = []
        failures = defaultdict(list)
        if self.value.startswith("file") and "value" not in ignore:
            failures["value"].append("IRI points to a local file path")
        return failures
