"""
Base classes for openMINDS

# Copyright (c) 2023 openMetadataInitiative
"""

from __future__ import annotations

from datetime import date, datetime
from collections import defaultdict
import json
from typing import Union
from .registry import Registry


class Node(metaclass=Registry):
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
        docstring goes here
        """

        def value_to_jsonld(value):
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
                    item = {"@id": value.id, "@type": value.type_}
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

        data = {"@type": self.type_}
        if with_context:
            data["@context"] = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
        if hasattr(self, "id") and self.id:
            data["@id"] = self.id
        for property in self.__class__.properties:
            value = getattr(self, property.name)
            if value or include_empty_properties:
                if property.multiple:
                    if not isinstance(value, (tuple, list)):
                        value = [value]
                    data[property.path] = [value_to_jsonld(item) for item in value]
                else:
                    data[property.path] = value_to_jsonld(value)
        return {key: data[key] for key in sorted(data)}

    @classmethod
    def from_jsonld(cls, data):
        """
        docstring goes here
        """
        data_copy = data.copy()
        context = data_copy.pop("@context", None)
        type_ = data_copy.pop("@type")
        if type_ and type_ != cls.type_:
            raise TypeError(f"Mismatched types. Data has '{type_}' but trying to create '{cls.type_}'")
        deserialized_data = {}
        if issubclass(cls, LinkedMetadata):
            deserialized_data["id"] = data_copy.pop("@id", None)
        for property in cls.properties:
            if property.path in data_copy:  # todo: use context to resolve uris
                value = data_copy.pop(property.path)
                if value:
                    deserialized_data[property.name] = property.deserialize(value)
                else:
                    deserialized_data[property.name] = value
        if len(data_copy) > 0:
            raise NameError(f"Unexpected arguments for {cls}: {tuple(data_copy.keys())}")
        return cls(**deserialized_data)

    def validate(self):
        """
        Check whether all constraints are satisfied.

        Returns a dict containing information about any validation failures.
        """
        failures = defaultdict(list)
        for property in self.properties:
            value = getattr(self, property.name, None)
            for key, values in property.validate(value).items():
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


class LinkedMetadata(Node):
    """
    docstring goes here
    """

    def __init__(self, id=None, **properties):
        self.id = id  # todo: check this is a URI
        for name, value in properties.items():
            setattr(self, name, value)

    def save(self, file_path, indent=2):
        """
        docstring goes here
        """
        with open(file_path, "w") as output_file:
            json.dump(self.to_jsonld(), output_file, indent=indent)

    @classmethod
    def load(cls, file_path):
        """
        docstring goes here
        """
        with open(file_path, "r") as input_file:
            data = json.load(input_file)
        return cls.from_jsonld(data)


class EmbeddedMetadata(Node):
    """
    docstring goes here
    """

    def __init__(self, **properties):
        for name, value in properties.items():
            setattr(self, name, value)


class IRI:
    def __init__(self, value: Union[str, IRI]):
        if isinstance(value, IRI):
            iri = value.value
        else:
            iri = value
        if not iri.startswith("http"):
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
