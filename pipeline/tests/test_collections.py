"""
Tests of the Collection class.
"""

import os.path
import shutil

from openminds.collection import Collection
import openminds.latest.controlled_terms
import openminds.latest.core as omcore
import openminds.latest.publications
import openminds.latest.computation
import openminds.latest.sands


from utils import build_fake_node


test_output_dir = "test_tmp"


def test_save_collection_single_file():
    shutil.rmtree(test_output_dir, ignore_errors=True)
    person = build_fake_node(omcore.Person)
    collection = Collection(person)
    test_file_path = os.path.join(test_output_dir, "test_collection.jsonld")
    collection.save(test_file_path, individual_files=False, include_empty_properties=False)


def test_round_trip_single_file():
    shutil.rmtree(test_output_dir, ignore_errors=True)
    person = build_fake_node(omcore.Person)
    collection = Collection(person)
    test_file_path = os.path.join(test_output_dir, "test_collection.jsonld")
    collection.save(test_file_path, individual_files=False, include_empty_properties=False)

    new_collection = Collection()
    new_collection.load(test_file_path)

    assert len(collection) == len(new_collection)

    for node in new_collection:
        if node.id == person.id:
            new_person = person
            break

    p = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    np = new_person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    assert p == np


def test_save_collection_multi_file():
    shutil.rmtree(test_output_dir, ignore_errors=True)
    person = build_fake_node(omcore.Person)
    collection = Collection(person)
    collection.save(test_output_dir, individual_files=True, include_empty_properties=False)


def test_round_trip_multi_file():
    shutil.rmtree(test_output_dir, ignore_errors=True)
    person = build_fake_node(omcore.Person)
    collection = Collection(person)
    collection.save(test_output_dir, individual_files=True, include_empty_properties=False)
    new_collection = Collection()
    new_collection.load(test_output_dir)

    assert len(collection) == len(new_collection)

    for node in new_collection:
        if node.id == person.id:
            new_person = person
            break

    p = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    np = new_person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    assert p == np


def test_collection_sort_by_id():
    person = omcore.Person(given_name="A", family_name="Professor", id="_:004")
    uni1 = omcore.Organization(full_name="University of This Place", id="_:002")
    uni2 = omcore.Organization(full_name="University of That Place", id="_:001")
    person.affiliations = [
        omcore.Affiliation(member_of = uni1),
        omcore.Affiliation(member_of = uni2),
    ]

    c = Collection(person,uni1,uni2)
    output_paths = c.save("test_collection_sort_by_id.jsonld", individual_files=False, include_empty_properties=False)
    
    assert output_paths == ["test_collection_sort_by_id.jsonld"]

    with open(output_paths[0]) as fp:
        saved_data = json.load(fp)
    os.remove("test_collection_sort_by_id.jsonld")

    expected_saved_data={
        "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
        "@graph": [
            {
                "@id": "_:001",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "fullName": "University of That Place"
            },
            {
                "@id": "_:002",
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "fullName": "University of This Place"
            },
            {
                "@id": "_:004",
                "@type": "https://openminds.ebrains.eu/core/Person",
                "affiliation": [
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "memberOf": {
                            "@id": "_:002"
                        }
                    },
                    {
                        "@type": "https://openminds.ebrains.eu/core/Affiliation",
                        "memberOf": {
                            "@id": "_:001"
                        }
                    }
                ],
                "familyName": "Professor",
                "givenName": "A"
            }
        ]
    }

    assert saved_data == expected_saved_data
