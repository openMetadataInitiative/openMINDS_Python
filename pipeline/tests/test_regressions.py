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
        "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
        "@type": "https://openminds.ebrains.eu/core/FileArchive",
        "IRI": "http://example.com/archive.zip",
        "format": {
            "@type": "https://openminds.ebrains.eu/core/ContentType",
            "name": "application/zip",
        },
        "sourceData": [
            {
                "@type": "https://openminds.ebrains.eu/core/File",
                "IRI": "http://example.com/some_file.txt",
                "name": "some_file.txt",
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
        affiliations=[omcore.Affiliation(member_of=uni1, end_date=(2023, 9, 30))],
    )
    failures = person.validate()
    assert len(failures) == 1

    person.affiliations[0].end_date = date(2023, 9, 30)
    failures = person.validate()
    assert len(failures) == 0


def test_issue0007():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/7
    # Instances of embedded types with value type "array" are not correctly resolved for saving and causing an error.

    person = omcore.Person(given_name="A", family_name="Professor", id="_:001")
    uni1 = omcore.Organization(full_name="University of This Place", id="_:002")
    uni2 = omcore.Organization(full_name="University of That Place", id="_:003")
    person.affiliations = [
        omcore.Affiliation(member_of=uni1),
        omcore.Affiliation(member_of=uni2),
    ]

    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
        "@id": "_:001",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "familyName": "Professor",
        "givenName": "A",
        "affiliation": [
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "memberOf": {
                    "@id": "_:002"
                },
            },
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "memberOf": {
                    "@id": "_:003"
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
        "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
        "@graph": [
            {
                "@id": "_:001",
                "@type": "https://openminds.ebrains.eu/core/Person",
                "affiliation": [
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "memberOf": {
                            "@id": "_:002"
                        },
                    },
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "memberOf": {
                            "@id": "_:003"
                        },
                    },
                ],
                "familyName": "Professor",
                "givenName": "A",
            },
            {
                "@id": "_:002",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "fullName": "University of This Place",
            },
            {
                "@id": "_:003",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "fullName": "University of That Place",
            },
        ],
    }
    assert saved_data == expected_saved_data


def test_issue0008():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/8
    # The instance of linked types in instances of embedded types are integrated as embedded not linked
    # (example: person -> affiliations (embedded) -> organization (linked))

    uni1 = omcore.Organization(full_name="University of This Place", id="_:001")
    person = omcore.Person(
        id="_:002",
        given_name="A",
        family_name="Professor",
        affiliations=[omcore.Affiliation(member_of=uni1, end_date=date(2023, 9, 30))],
    )
    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
        "@id": "_:002",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "affiliation": [
            {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "endDate": "2023-09-30",
                "memberOf": {
                    "@id": "_:001"
                },
            }
        ],
        "familyName": "Professor",
        "givenName": "A",
    }
    assert actual == expected


def test_issue0026():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/26
    # When reading a JSON-LD file, the attributes of LinkedMetadata nodes
    # inside EmbeddedMetadata nodes are not set properly

    uni1 = omcore.Organization(full_name="University of This Place", id="_:uthisp")
    person = omcore.Person(
        given_name="A",
        family_name="Professor",
        affiliations = [omcore.Affiliation(member_of=uni1)],
        id="_:ap"
    )

    c = Collection(person)

    # uni1 was not added explicitly, but should nevertheless be included in the JSON-LD export

    output_paths = c.save("issue0026.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths)
    os.remove("issue0026.jsonld")

    person_again = [item for item in new_collection if isinstance(item, omcore.Person)][0]
    assert len(person_again.affiliations) == 1
    assert person_again.affiliations[0].member_of.full_name == "University of This Place"


def test_issue0023():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/23
    # If a user adds an instance/node to a collection, and then later adds linked types to the instance,
    # currently that is not added to the collection

    uni1 = omcore.Organization(full_name="University of This Place", id="_:uthisp")
    person = omcore.Person(
        given_name="A",
        family_name="Professor",
        affiliations = [omcore.Affiliation(member_of=uni1)],
        id="_:ap"
    )
    dv = omcore.DatasetVersion(
        full_name="The name of the dataset version",
        custodians=[person],
        id="_:dv"
    )

    c = Collection(dv)

    # even though we add uni2 and the repository after creating the collection,
    # they should be included when we save the collection.
    uni2 = omcore.Organization(full_name="University of That Place", id="_:uthatp")
    person.affiliations.append(omcore.Affiliation(member_of=uni2))
    dv.repository = omcore.FileRepository(iri="http://example.com", id="_:fr")

    output_paths = c.save("issue0023.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths)
    os.remove("issue0023.jsonld")

    dv_again = [item for item in new_collection if isinstance(item, omcore.DatasetVersion)][0]
    assert isinstance(dv_again.repository, omcore.FileRepository)
    assert dv_again.repository.iri.value == "http://example.com"
    assert len(dv_again.custodians[0].affiliations) == 2
    assert dv_again.custodians[0].affiliations[0].member_of.full_name == "University of This Place"
    assert dv_again.custodians[0].affiliations[1].member_of.full_name == "University of That Place"
