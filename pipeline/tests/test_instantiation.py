"""
Tests for openMINDS Python module
"""

import random
import string
from datetime import date, time, datetime
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

P_PROPERTY_PRESENT = 0.8
MAX_DEPTH = 10


def property_present(p):
    # randomly leave some properties empty
    if random.random() < p:
        return True
    else:
        return False


def classes_in_module(module):
    contents = [getattr(module, name) for name in dir(module)]
    return [
        item
        for item in contents
        if isinstance(item, type) and issubclass(item, Node)
    ]


def build_fake_node(cls, depth=0):
    data = {}
    for property in cls.properties:
        if property.types:
            if property.types == (str,):
                # todo: check for property.formatting
                value = "".join(random.choices(string.printable, k=random.randint(0, 40)))
                data[property.name] = value
            elif float in property.types:
                value = 100 * random.random()
                data[property.name] = value
            elif int in property.types:
                value = random.randint(0, 100)
                data[property.name] = value
            elif issubclass(property.types[0], Node):
                if depth < MAX_DEPTH and property_present(P_PROPERTY_PRESENT):
                    child_cls = random.choice(property.types)
                    if child_cls != cls:  # reduce risk of recursion
                        value = build_fake_node(child_cls, depth=depth + 1)
                        data[property.name] = value
            elif property.types == (IRI,):
                value = "https://example.com/" + "".join(random.choices(string.ascii_letters, k=random.randint(0, 40)))
            elif datetime in property.types:
                value = datetime.now()
            elif date in property.types:
                value = date.today()
            else:
                raise TypeError(f"unexpected type(s): {property.types}")
    return cls(**data)


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
