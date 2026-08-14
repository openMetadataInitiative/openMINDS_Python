"""
Tests for openMINDS Python module
"""

from importlib import import_module
import sys

import pytest

from openminds.base import Node, IRI, Link, LinkedNodeEmbedding
from utils import build_fake_node

module_names = (
    "chemicals",
    "computation",
    "controlled_terms",
    "core",
    "ephys",
    "publications",
    "sands",
    "specimen_prep",
    "stimulation",
)
versions = ("v3", "v4", "latest")  # "v1" and "v2" currently produce errors

all_modules = []
for version in versions:
    for module_name in module_names:
        path = f"openminds.{version}.{module_name}"
        try:
            module = import_module(path)
        except ModuleNotFoundError:
            continue
        else:
            sys.modules[path] = module
            all_modules.append(module)


def classes_in_module(module):
    contents = [getattr(module, name) for name in dir(module)]
    return [
        item for item in contents if isinstance(item, type) and issubclass(item, Node)
    ]


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
        "file:///path/to/my/file.txt",
    ]
    for value in valid_iris:
        iri = IRI(value)
        assert iri.value == value
        failures = iri._validate()
        if value.startswith("http"):
            assert not failures
        else:
            assert failures["value"][0] == "IRI points to a local file path"
    invalid_iris = [
        ("/path/to/my/file.txt", "Invalid IRI"),
        ("https://example.com/path with spaces/to/my/file.txt", "Invalid IRI - replace spaces with '%20'"),
        ("https://data-proxy.ebrains.eu/api/v1/buckets/report%.pdf", "Invalid IRI")  # lone '%' not allowed
    ]
    for value, expected_message in invalid_iris:
        iri = IRI(value)
        assert iri.value == value
        failures = iri._validate()
        assert len(failures["value"]) == 1
        assert failures["value"][0] == expected_message


def test_link():
    from openminds.v4.controlled_terms import Species
    from openminds.v4.core import DatasetVersion

    maybe_mouse = Link("https://openminds.om-i.org/instances/species/musMusculus")

    definitely_mouse = Link(
        "https://openminds.om-i.org/instances/species/musMusculus",
        allowed_types=[Species],
    )

    my_dsv1 = DatasetVersion(study_targets=[maybe_mouse])
    failures1 = my_dsv1.validate(ignore=["required"])
    assert len(failures1["type"]) == 1
    assert "study_targets" in failures1["type"][0]

    my_dsv2 = DatasetVersion(study_targets=[definitely_mouse])
    failures2 = my_dsv2.validate(ignore=["required"])
    assert len(failures2) == 0

    expected = {
        "@context": {
            "@vocab": "https://openminds.om-i.org/props/",
        },
        "@type": "https://openminds.om-i.org/types/DatasetVersion",
        "studyTarget": [
            {
                "@id": "https://openminds.om-i.org/instances/species/musMusculus",
            },
        ],
    }
    assert my_dsv1.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.NEVER
    ) == my_dsv2.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.NEVER
    ) == expected


def test_linked_node_embedding():
    from openminds.v4.core import Organization, Person
    from openminds.v4.core.actors.affiliation import Affiliation

    uni = Organization(full_name="University of Somewhere", id="_:001")
    person_with_id = Person(
        given_name="Ada",
        family_name="Lovelace",
        id="_:002",
        affiliations=[Affiliation(member_of=uni)],
    )
    person_without_id = Person(
        given_name="Ada",
        family_name="Lovelace",
        affiliations=[Affiliation(member_of=uni)],
    )

    # ALWAYS: linked nodes are embedded inline
    result = person_with_id.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.ALWAYS,
    )
    affiliation = result["affiliation"][0]
    assert affiliation["memberOf"]["@type"] == "https://openminds.om-i.org/types/Organization"
    assert affiliation["memberOf"]["fullName"] == "University of Somewhere"

    # NEVER: linked nodes with id are replaced by {"@id": ...}
    result = person_with_id.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.NEVER,
    )
    affiliation = result["affiliation"][0]
    assert affiliation["memberOf"] == {"@id": "_:001"}

    # NEVER: raises ValueError when a linked node has no id
    uni_no_id = Organization(full_name="University of Nowhere")
    person_with_unidentified_org = Person(
        given_name="Ada",
        family_name="Lovelace",
        id="_:003",
        affiliations=[Affiliation(member_of=uni_no_id)],
    )
    with pytest.raises(ValueError, match="requires @id to be defined"):
        person_with_unidentified_org.to_jsonld(
            include_empty_properties=False,
            embed_linked_nodes=LinkedNodeEmbedding.NEVER,
        )

    # IF_NECESSARY: linked nodes with id are replaced by {"@id": ...}
    result = person_with_id.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.IF_NECESSARY,
    )
    affiliation = result["affiliation"][0]
    assert affiliation["memberOf"] == {"@id": "_:001"}

    # IF_NECESSARY: linked nodes without id are embedded inline
    result = person_with_unidentified_org.to_jsonld(
        include_empty_properties=False,
        embed_linked_nodes=LinkedNodeEmbedding.IF_NECESSARY,
    )
    affiliation = result["affiliation"][0]
    assert affiliation["memberOf"]["@type"] == "https://openminds.om-i.org/types/Organization"
    assert affiliation["memberOf"]["fullName"] == "University of Nowhere"
