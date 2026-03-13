from datetime import date
import json
import os

import pytest

from openminds import Collection, IRI
import openminds.latest
import openminds.v4
import openminds.v5
from utils import build_fake_node


@pytest.mark.parametrize("om", [openminds.latest, openminds.v4])
def test_issue_0002(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/2
    # @type should not be given as a list but as a string

    node = build_fake_node(om.core.Person)
    data = node.to_jsonld()
    assert data["@type"] == "https://openminds.om-i.org/types/Person"


@pytest.mark.parametrize("om", [openminds.latest, openminds.v4])
def test_issue_0003(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/3
    # validate() does not complain about direct entries that should be lists

    # we address this by always wrapping a single item in a list in such cases

    some_file = om.core.File(
        iri=IRI("http://example.com/some_file.txt"),
        name="some_file.txt",
    )

    node1 = om.core.FileArchive(
        iri=IRI("http://example.com/archive.zip"),
        format=om.core.ContentType(name="application/zip"),
        source_data=[some_file],  # multiple=True, min_items=1
    )
    node2 = om.core.FileArchive(
        iri=IRI("http://example.com/archive.zip"),
        format=om.core.ContentType(name="application/zip"),
        source_data=some_file,  # multiple=True, min_items=1
    )
    # on export, a single item should be wrapped in a list, where the property expects an array
    expected = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@type": "https://openminds.om-i.org/types/FileArchive",
        "IRI": "http://example.com/archive.zip",
        "format": {
            "@type": "https://openminds.om-i.org/types/ContentType",
            "name": "application/zip",
        },
        "sourceData": [
            {
                "@type": "https://openminds.om-i.org/types/File",
                "IRI": "http://example.com/some_file.txt",
                "name": "some_file.txt",
            }
        ],
    }

    assert (
        node1.to_jsonld(include_empty_properties=False) == node2.to_jsonld(include_empty_properties=False) == expected
    )


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0005a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/5
    # validate() does not complain about list/tuple entries that should be a direct single entry
    uni1 = om.core.Organization(full_name="University of This Place")
    person = om.core.Person(
        given_name="A",
        family_name="Professor",
        affiliations=[om.core.Affiliation(member_of=uni1, end_date=(2023, 9, 30))],
    )
    failures = person.validate()
    assert len(failures) == 1

    person.affiliations[0].end_date = date(2023, 9, 30)
    failures = person.validate()
    assert len(failures) == 0

@pytest.mark.parametrize("om", [openminds.v5, openminds.latest])
def test_issue0005b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/5
    # validate() does not complain about list/tuple entries that should be a direct single entry
    person = om.core.Person(
        preferred_name="A",
        family_name="Professor"
    )
    uni1 = om.core.Organization(name="University of This Place", country_of_formation=om.controlled_terms.sovereign_state.SovereignState.by_name("Germany"), type=om.controlled_terms.organization_type.OrganizationType.by_name('organizational unit'), memberships=[om.core.Membership(member=person, end_date=(2023, 9, 30))])
    failures = uni1.validate()
    assert len(failures) == 1

    uni1.memberships[0].end_date = date(2023, 9, 30)
    print(uni1.type)
    failures = uni1.validate()
    assert len(failures) == 0


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0007a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/7
    # Instances of embedded types with value type "array" are not correctly resolved for saving and causing an error.

    person = om.core.Person(given_name="A", family_name="Professor", id="_:001")
    uni1 = om.core.Organization(full_name="University of This Place", id="_:002")
    uni2 = om.core.Organization(full_name="University of That Place", id="_:003")
    person.affiliations = [
        om.core.Affiliation(member_of=uni1),
        om.core.Affiliation(member_of=uni2),
    ]

    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "_:001",
        "@type": "https://openminds.om-i.org/types/Person",
        "familyName": "Professor",
        "givenName": "A",
        "affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "memberOf": {"@id": "_:002"},
            },
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "memberOf": {"@id": "_:003"},
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
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@graph": [
            {
                "@id": "_:001",
                "@type": "https://openminds.om-i.org/types/Person",
                "affiliation": [
                    {
                        "@type": "https://openminds.om-i.org/types/Affiliation",
                        "memberOf": {"@id": "_:002"},
                    },
                    {
                        "@type": "https://openminds.om-i.org/types/Affiliation",
                        "memberOf": {"@id": "_:003"},
                    },
                ],
                "familyName": "Professor",
                "givenName": "A",
            },
            {
                "@id": "_:002",
                "@type": "https://openminds.om-i.org/types/Organization",
                "fullName": "University of This Place",
            },
            {
                "@id": "_:003",
                "@type": "https://openminds.om-i.org/types/Organization",
                "fullName": "University of That Place",
            },
        ],
    }
    assert saved_data == expected_saved_data


@pytest.mark.parametrize("om", [openminds.v5, openminds.latest])
def test_issue0007b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/7
    # Instances of embedded types with value type "array" are not correctly resolved for saving and causing an error.

    person = om.core.Person(preferred_name="A", family_name="Professor", id="_:001")
    uni1 = om.core.Organization(name="University of This Place", id="_:002")
    uni2 = om.core.Organization(name="University of That Place", id="_:003")
    person2 = om.core.Person(preferred_name="B", family_name="Professor", id="_:004")
    uni1.memberships = [
        om.core.Membership(member=person),
    ]
    uni2.memberships = [
        om.core.Membership(member=person),
        om.core.Membership(member=person2)
    ]

    actual = uni1.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "_:002",
        "@type": "https://openminds.om-i.org/types/Organization",
        "membership": [
            {
                "@type": "https://openminds.om-i.org/types/Membership",
                "member": {"@id": "_:001"}
            }
        ],
        "name": "University of This Place"
    }
    assert actual == expected

    c = Collection(person, uni1, uni2)
    output_paths = c.save("issue0007.jsonld", individual_files=False, include_empty_properties=False)
    assert output_paths == ["issue0007.jsonld"]

    with open(output_paths[0]) as fp:
        saved_data = json.load(fp)
    os.remove("issue0007.jsonld")
    expected_saved_data = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@graph": [
            {
                "@id": "_:001",
                "@type": "https://openminds.om-i.org/types/Person",
                "familyName": "Professor",
                "preferredName": "A",
            },
            {
                "@id": "_:002",
                "@type": "https://openminds.om-i.org/types/Organization",
                "membership": [
                    {
                        "@type": "https://openminds.om-i.org/types/Membership",
                        "member": {"@id": "_:001"},
                    }
                ],
                "name": "University of This Place",
            },
            {
                "@id": "_:003",
                "@type": "https://openminds.om-i.org/types/Organization",
                "membership": [
                    {
                        "@type": "https://openminds.om-i.org/types/Membership",
                        "member": {"@id": "_:001"},
                    },
                    {
                        "@type": "https://openminds.om-i.org/types/Membership",
                        "member": {"@id": "_:004"},
                    },
                ],
                "name": "University of That Place",
            },
            {
                "@id": "_:004",
                "@type": "https://openminds.om-i.org/types/Person",
                "familyName": "Professor",
                "preferredName": "B",
            }
        ],
    }
    assert saved_data == expected_saved_data


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0008a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/8
    # The instance of linked types in instances of embedded types are integrated as embedded not linked
    # (example: person -> affiliations (embedded) -> organization (linked))

    uni1 = om.core.Organization(full_name="University of This Place", id="_:001")
    person = om.core.Person(
        id="_:002",
        given_name="A",
        family_name="Professor",
        affiliations=[om.core.Affiliation(member_of=uni1, end_date=date(2023, 9, 30))],
    )
    actual = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "_:002",
        "@type": "https://openminds.om-i.org/types/Person",
        "affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "endDate": "2023-09-30",
                "memberOf": {"@id": "_:001"},
            }
        ],
        "familyName": "Professor",
        "givenName": "A",
    }
    assert actual == expected


@pytest.mark.parametrize("om", [openminds.v5, openminds.latest])
def test_issue0008b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/8
    # The instance of linked types in instances of embedded types are integrated as embedded not linked
    # (example: organization -> memberships (embedded) -> person (linked))

    person = om.core.Person(
        id="_:002",
        preferred_name="A",
        family_name="Professor"
    )

    uni1 = om.core.Organization(
        name="University of This Place",
        id="_:001",
        memberships=om.core.Membership(member=person, end_date=date(2023, 9, 30))
    )
    actual = uni1.to_jsonld(include_empty_properties=False, embed_linked_nodes=False, with_context=True)
    expected = {
        '@context': {'@vocab': 'https://openminds.om-i.org/props/'},
        '@id': '_:001',
        '@type': 'https://openminds.om-i.org/types/Organization',
        'membership': [
            {
                '@type': 'https://openminds.om-i.org/types/Membership',
                'endDate': '2023-09-30',
                'member': {'@id': '_:002'}
            }
        ],
        'name': 'University of This Place'
    }
    assert actual == expected


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0026a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/26
    # When reading a JSON-LD file, the attributes of LinkedMetadata nodes
    # inside EmbeddedMetadata nodes are not set properly

    uni1 = om.core.Organization(full_name="University of This Place", id="_:uthisp")
    person = om.core.Person(
        given_name="A", family_name="Professor", affiliations=[om.core.Affiliation(member_of=uni1)], id="_:ap"
    )

    c = Collection(person)

    # uni1 was not added explicitly, but should nevertheless be included in the JSON-LD export

    output_paths = c.save("issue0026.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths, version=om.__name__.split(".")[1])
    os.remove("issue0026.jsonld")

    person_again = [item for item in new_collection if isinstance(item, om.core.Person)][0]
    assert len(person_again.affiliations) == 1
    assert person_again.affiliations[0].member_of.full_name == "University of This Place"


@pytest.mark.parametrize("om", [openminds.v5, openminds.latest])
def test_issue0026b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/26
    # When reading a JSON-LD file, the attributes of LinkedMetadata nodes
    # inside EmbeddedMetadata nodes are not set properly

    person = om.core.Person(
        preferred_name="A", family_name="Professor", id="_:ap"
    )
    uni1 = om.core.Organization(name="University of This Place",
                                id="_:uthisp",
                                memberships=[om.core.Membership(member=person)])
    c = Collection(uni1)

    # person was not added explicitly, but should nevertheless be included in the JSON-LD export

    output_paths = c.save("issue0026.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths, version=om.__name__.split(".")[1])
    os.remove("issue0026.jsonld")

    uni_again = [item for item in new_collection if isinstance(item, om.core.Organization)][0]
    assert len(uni_again.memberships) == 1
    assert uni_again.memberships[0].member.family_name == "Professor"


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0023a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/23
    # If a user adds an instance/node to a collection, and then later adds linked types to the instance,
    # currently that is not added to the collection

    uni1 = om.core.Organization(full_name="University of This Place", id="_:uthisp")
    person = om.core.Person(
        given_name="A", family_name="Professor", affiliations=[om.core.Affiliation(member_of=uni1)], id="_:ap"
    )
    dv = om.core.DatasetVersion(full_name="The name of the dataset version", custodians=[person], id="_:dv")

    c = Collection(dv)

    # even though we add uni2 and the repository after creating the collection,
    # they should be included when we save the collection.
    uni2 = om.core.Organization(full_name="University of That Place", id="_:uthatp")
    person.affiliations.append(om.core.Affiliation(member_of=uni2))
    dv.repository = om.core.FileRepository(iri="http://example.com", id="_:fr")

    output_paths = c.save("issue0023.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths, version=om.__name__.split(".")[1])
    os.remove("issue0023.jsonld")

    dv_again = [item for item in new_collection if isinstance(item, om.core.DatasetVersion)][0]
    assert isinstance(dv_again.repository, om.core.FileRepository)
    assert dv_again.repository.iri.value == "http://example.com"
    assert len(dv_again.custodians[0].affiliations) == 2
    assert dv_again.custodians[0].affiliations[0].member_of.full_name == "University of This Place"
    assert dv_again.custodians[0].affiliations[1].member_of.full_name == "University of That Place"


@pytest.mark.parametrize("om", [openminds.v5])
def test_issue0023b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/23
    # If a user adds an instance/node to a collection, and then later adds linked types to the instance,
    # currently that is not added to the collection

    person = om.core.Person(
        preferred_name="A", family_name="Professor", id="_:ap"
    )
    uni1 = om.core.Organization(name="University of This Place",
                                id="_:uthisp",
                                memberships=[om.core.Membership(member=person)])
    dv = om.core.DatasetVersion(full_name="The name of the dataset version",
                                contributions=[om.core.Contribution(contributors=[uni1],
                                                                    type=om.controlled_terms.contribution_type.ContributionType.by_name('custodianship'))],
                                id="_:dv")

    c = Collection(dv)

    # even though we add uni2 and the repository after creating the collection,
    # they should be included when we save the collection.
    person2 = om.core.Person(
        preferred_name="B", family_name="Professor", id="_:bp"
    )
    uni1.memberships.append(om.core.Membership(member=person2))
    #dv.contributions.append(om.core.Contribution(contributors=[uni2],
    #type=om.controlled_terms.contribution_type.ContributionType.by_name('ownership')))
    dv.repository = om.core.FileRepository(iri="http://example.com", id="_:fr")

    output_paths = c.save("issue0023.jsonld", individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(*output_paths, version=om.__name__.split(".")[1])
    os.remove("issue0023.jsonld")

    dv_again = [item for item in new_collection if isinstance(item, om.core.DatasetVersion)][0]
    assert isinstance(dv_again.repository, om.core.FileRepository)
    assert dv_again.repository.iri.value == "http://example.com"
    assert len(dv_again.contributions[0].contributors[0].memberships) == 2
    assert (dv_again.contributions[0].contributors[0].name == "University of This Place")
    assert dv_again.contributions[0].contributors[0].memberships[0].member.preferred_name == "A"
    assert dv_again.contributions[0].contributors[0].memberships[1].member.preferred_name == "B"


@pytest.mark.parametrize("om", [openminds.latest, openminds.v4])
def test_issue0056(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/56
    # Since we are permissive on object creation, serialization to JSON-LD should work
    # even if the object gives validation failures.
    # However, under some circumstances, to_jsonld() produces a data structure
    # that cannot be saved as a JSON string.
    dataset = om.core.Dataset(
        digital_identifier=[
            om.core.DOI(identifier="abc"),
            om.core.DOI(identifier="def")
        ]
    )
    failures = dataset.validate(ignore=["required"])
    assert len(failures) == 1
    assert failures["multiplicity"] == ['digital_identifier does not accept multiple values, but contains 2']
    data = dataset.to_jsonld()
    json.dumps(data)  # this should not raise an Exception


@pytest.mark.parametrize("om", [openminds.v4])
def test_issue0073a(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/73
    # Infinite recursion in validate()
    ds1 = om.core.DatasetVersion(
        short_name="ds1",
        is_alternative_version_of=None
    )
    ds2 = om.core.DatasetVersion(
        short_name="ds2",
        is_alternative_version_of=ds1
    )
    ds1.is_alternative_version_of = ds2

    failures = ds1.validate()


@pytest.mark.parametrize("om", [openminds.latest])
def test_issue0073b(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/73
    # Infinite recursion in validate()
    ds1 = om.core.DatasetVersion(
        short_name="ds1",
        is_variant_of=None
    )
    ds2 = om.core.DatasetVersion(
        short_name="ds2",
        is_variant_of=ds1
    )
    ds1.is_variant_of = ds2

    failures = ds1.validate()


@pytest.mark.parametrize("om", [openminds.latest])
def test_issue0069(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/69
    # The License class has a classmethod "by_name()" which assumes License is a controlled term
    # (i.e., it has properties "name" and "synonyms").
    # However License does not have these properties, it has "short_name" and "full_name".

    # Test with default arguments (single result, exact match)
    result = om.core.License.by_name("CC-BY-4.0")
    assert result.short_name == "CC-BY-4.0"

    result = om.sands.ParcellationEntity.by_name("NODa,b")
    assert result.abbreviation == "NODa,b"

    result = om.sands.CommonCoordinateFramework.by_name("MEBRAINS population-based monkey brain template")
    assert result.full_name == "MEBRAINS population-based monkey brain template"

    assert om.controlled_terms.BiologicalOrder.by_name("rodents") == om.controlled_terms.BiologicalOrder.by_name("Rodentia") != None

    # Test with "all=True"
    results = om.sands.AnatomicalAtlasVersion.by_name("Julich-Brain Atlas", all=True)
    assert len(results) == 30
    assert all(r.short_name == "Julich-Brain Atlas" for r in results)
    assert len(set(r.id for r in results)) == len(results)

    # Test with "match='contains'"
    results = om.core.License.by_name("Creative Commons", all=True, match="contains")
    assert len(results) == 7
    assert all("CC" in r.short_name for r in results)


@pytest.mark.parametrize("om", [openminds.latest])
def test_pr0083(om):
    # https://github.com/openMetadataInitiative/openMINDS_Python/pull/83
    # by_name() should return None consistently
    # when no matches are found, regardless of the 'all' parameter

    # all=False (default) should return None when no match is found
    result = om.controlled_terms.BiologicalOrder.by_name("nonexistent_order_xyz")
    assert result is None

    # all=True should also return None when no match is found
    results = om.controlled_terms.BiologicalOrder.by_name("nonexistent_order_xyz", all=True)
    assert results is None


@pytest.mark.parametrize("om", [openminds.latest, openminds.v4])
def test_issue0084(om):
    # Properties whose value evaluates to False (e.g., zero)
    # are not serialized if using include_empty_properties=False
    obj = om.publications.LivePaperSection(name="test", order=0)
    data = obj.to_jsonld(include_empty_properties=False)
    assert data == {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@type": "https://openminds.om-i.org/types/LivePaperSection",
        "name": "test",
        "order": 0,
    }
