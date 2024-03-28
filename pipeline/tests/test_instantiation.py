"""
Tests for openMINDS Python module
"""

import pytest

from openminds.base import Node, IRI
from openminds.latest import (
    chemicals,
    computation,
    controlled_terms,
    core,
    ephys,
    publications,
    sands,
    specimen_prep,
    stimulation,
)
from utils import build_fake_node

all_modules = (
    chemicals,
    computation,
    controlled_terms,
    core,
    ephys,
    publications,
    sands,
    specimen_prep,
    stimulation,
)


def classes_in_module(module):
    contents = [getattr(module, name) for name in dir(module)]
    return [item for item in contents if isinstance(item, type) and issubclass(item, Node)]


def test_instantiation_random_data():
    for module in all_modules:
        classes = classes_in_module(module)
        assert len(classes) > 0

        for cls in classes:
            node = build_fake_node(cls)


def test_json_roundtrip():
    for module in all_modules:
        for cls in classes_in_module(module):
            node = build_fake_node(cls)
            data = node.to_jsonld(include_empty_properties=False)
            recreated_node = cls.from_jsonld(data)
            assert recreated_node.to_jsonld(include_empty_properties=False) == data


def test_IRI():
    valid_iris = [
        "https://example.com/path/to/my/file.txt",
        "file:///path/to/my/file.txt"
    ]
    for value in valid_iris:
        iri = IRI(value)
        assert iri.value == value
        failures = iri.validate()
        if value.startswith("http"):
            assert not failures
        else:
            assert failures["value"][0] == "IRI points to a local file path"
    invalid_iris = [
        "/path/to/my/file.txt"
    ]
    for value in invalid_iris:
        with pytest.raises(ValueError) as exc_info:
            iri = IRI(value)
        assert exc_info.value.args[0] == "Invalid IRI"
