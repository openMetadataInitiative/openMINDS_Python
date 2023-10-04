"""
Tests for openMINDS Python module
"""

from openminds.base import Node
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
