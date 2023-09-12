"""
Base classes for openMINDS

# Copyright (c) 2023 openMetadataInitiative
"""

from __future__ import annotations

import json
from typing import Union
from .registry import Registry


class Node(metaclass=Registry):

    def __init__(self, id=None, **properties):
        self.id = id  # todo: check this is a URI
        for name, value in properties.items():
            setattr(self, name, value)

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

    def to_jsonld(self, include_empty_properties=True, with_context=True):
        """
        docstring goes here
        """
        data = {
            "@type": self.type_
        }
        if with_context:
            data["@context"] = {
                "vocab": "https://openminds.ebrains.eu/vocab/"
            }
        if self.id:
            data["@id"] = id
        for property in self.__class__.properties:
            value = getattr(self, property.name)
            if value or include_empty_properties:
                if hasattr(value, "to_jsonld"):
                    data[property.path] = value.to_jsonld(with_context=False)
                else:
                    data[property.path] = value
        return data

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
        docstring goes here
        """
        raise NotImplementedError


class LinkedMetadata(Node):
    """
    docstring goes here
    """

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
    pass


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
