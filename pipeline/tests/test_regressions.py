from datetime import date
import json
import os
from openminds import Collection, IRI
from openminds.latest import core as omcore
from utils import build_fake_node


def test_issue_0002():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/2
    # @type should not be given as a list but as a string

    node = build_fake_node(omcore.Person)
    data = node.to_jsonld()
    assert data["@type"] == "https://openminds.ebrains.eu/core/Person"


def test_issue_0003():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/3
    # validate() does not complain about direct entries that should be lists

    # we address this by always wrapping a single item in a list in such cases

    some_file = omcore.File(
        iri=IRI("http://example.com/some_file.txt"),
        name="some_file.txt",
    )

    node1 = omcore.FileArchive(
        iri=IRI("http://example.com/archive.zip"),
        format=omcore.ContentType(name="application/zip"),
        source_data=[some_file],  # multiple=True, min_items=1
    )
    node2 = omcore.FileArchive(
        iri=IRI("http://example.com/archive.zip"),
        format=omcore.ContentType(name="application/zip"),
        source_data=some_file,  # multiple=True, min_items=1
    )
    # on export, a single item should be wrapped in a list, where the property expects an array
    expected = {
        "@context": {"vocab": "https://openminds.ebrains.eu/vocab/"},
        "@type": "https://openminds.ebrains.eu/core/FileArchive",
        "vocab:IRI": "http://example.com/archive.zip",
        "vocab:format": {
            "@type": "https://openminds.ebrains.eu/core/ContentType",
            "vocab:name": "application/zip",
        },
        "vocab:sourceData": [
            {
                "@type": "https://openminds.ebrains.eu/core/File",
                "vocab:IRI": "http://example.com/some_file.txt",
                "vocab:name": "some_file.txt",
            }
        ],
    }
    assert (
        node1.to_jsonld(include_empty_properties=False) == node2.to_jsonld(include_empty_properties=False) == expected
    )


def test_issue0005():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/5
    # validate() does not complain about list/tuple entries that should be a direct single entry
    uni1 = omcore.Organization(full_name="University of This Place")
    person = omcore.Person(
        given_name="A",
        family_name="Professor",
        affiliation=[omcore.Affiliation(member_of=uni1, end_date=(2023, 9, 30))],
    )
    failures = person.validate()
    assert len(failures) == 1

    person.affiliation[0].end_date = date(2023, 9, 30)
    failures = person.validate()
    assert len(failures) == 0


def test_issue0007():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/7
    # Instances of embedded types with value type "array" are not correctly resolved for saving and causing an error.

    person = omcore.Person(given_name="A", family_name="Professor", id="_:001")
    uni1 = omcore.Organization(full_name="University of This Place", id="_:002")
    uni2 = omcore.Organization(full_name="University of That Place", id="_:003")
    person.affiliation = [
        omcore.Affiliation(member_of=uni1),
        omcore.Affiliation(member_of=uni2),
    ]

    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"vocab": "https://openminds.ebrains.eu/vocab/"},
        "@id": "_:001",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "vocab:familyName": "Professor",
        "vocab:givenName": "A",
        "vocab:affiliation": [
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "vocab:memberOf": {
                    "@id": "_:002",
                    "@type": "https://openminds.ebrains.eu/core/Organization",
                },
            },
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "vocab:memberOf": {
                    "@id": "_:003",
                    "@type": "https://openminds.ebrains.eu/core/Organization",
                },
            },
        ],
    }
    assert actual == expected

    c = Collection(person, uni1, uni2)
    output_paths = c.save("issue0007.jsonld", individual_files=False, include_empty_properties=False)
    assert output_paths == ["issue0007.jsonld"]

    with open(output_paths[0]) as fp:
        saved_data = json.load(fp)
    os.remove("issue0007.jsonld")
    expected_saved_data = {
        "@context": {"vocab": "https://openminds.ebrains.eu/vocab/"},
        "@graph": [
            {
                "@id": "_:001",
                "@type": "https://openminds.ebrains.eu/core/Person",
                "vocab:affiliation": [
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "vocab:memberOf": {
                            "@id": "_:002",
                            "@type": "https://openminds.ebrains.eu/core/Organization",
                        },
                    },
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "vocab:memberOf": {
                            "@id": "_:003",
                            "@type": "https://openminds.ebrains.eu/core/Organization",
                        },
                    },
                ],
                "vocab:familyName": "Professor",
                "vocab:givenName": "A",
            },
            {
                "@id": "_:002",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "vocab:fullName": "University of This Place",
            },
            {
                "@id": "_:003",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "vocab:fullName": "University of That Place",
            },
        ],
    }
    assert saved_data == expected_saved_data


def test_issue0008():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/8
    # The instance of linked types in instances of embedded types are integrated as embedded not linked
    # (example: person -> affiliation (embedded) -> organization (linked))

    uni1 = omcore.Organization(full_name="University of This Place", id="_:001")
    person = omcore.Person(
        id="_:002",
        given_name="A",
        family_name="Professor",
        affiliation=[omcore.Affiliation(member_of=uni1, end_date=date(2023, 9, 30))],
    )
    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"vocab": "https://openminds.ebrains.eu/vocab/"},
        "@id": "_:002",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "vocab:affiliation": [
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "vocab:endDate": "2023-09-30",
                "vocab:memberOf": {
                    "@id": "_:001",
                    "@type": "https://openminds.ebrains.eu/core/Organization",
                },
            }
        ],
        "vocab:familyName": "Professor",
        "vocab:givenName": "A",
    }
    assert actual == expected
