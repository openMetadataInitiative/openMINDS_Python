"""
Tests of the Collection class.
"""

import os.path
import shutil
import json

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
    new_collection.load(test_file_path, version='latest')
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
    new_collection.load(test_output_dir, version='latest')

    assert len(collection) == len(new_collection)

    for node in new_collection:
        if node.id == person.id:
            new_person = person
            break

    p = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    np = new_person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    assert p == np


def test_round_trip_multi_file_group_by_schema():
    shutil.rmtree(test_output_dir, ignore_errors=True)
    person = build_fake_node(omcore.Person)
    collection = Collection(person)
    collection.save(test_output_dir, individual_files=True, include_empty_properties=False, group_by_schema=True)
    new_collection = Collection()
    new_collection.load(test_output_dir, version='latest')

    assert len(collection) == len(new_collection)

    for node in new_collection:
        if node.id == person.id:
            new_person = person
            break

    p = person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    np = new_person.to_jsonld(include_empty_properties=False, embed_linked_nodes=True)
    assert p == np


def test_collection_sort_by_id():
    person = omcore.Person(preferred_name="A", family_name="Professor", id="_:004")
    uni1 = omcore.Organization(name="University of This Place", id="_:002")
    uni2 = omcore.Organization(name="University of That Place", id="_:001")
    uni1.membershipss = [
        omcore.Membership(member=person),
    ]
    uni2.membershipss = [
        omcore.Membership(member=person),
    ]

    c = Collection(person, uni1, uni2)
    output_paths = c.save("test_collection_sort_by_id.jsonld", individual_files=False, include_empty_properties=False)

    assert output_paths == ["test_collection_sort_by_id.jsonld"]

    with open(output_paths[0]) as fp:
        saved_data = json.load(fp)
    os.remove("test_collection_sort_by_id.jsonld")

    expected_saved_data = {
       "@context":{
          "@vocab":"https://openminds.om-i.org/props/"
       },
       "@graph":[
          {
             "@id":"_:001",
             "@type":"https://openminds.om-i.org/types/Organization",
             "memberships":[
                {
                   "@type":"https://openminds.om-i.org/types/Membership",
                   "member":{
                      "@id":"_:004"
                   }
                }
             ],
             "name":"University of That Place"
          },
          {
             "@id":"_:002",
             "@type":"https://openminds.om-i.org/types/Organization",
             "memberships":[
                {
                   "@type":"https://openminds.om-i.org/types/Membership",
                   "member":{
                      "@id":"_:004"
                   }
                }
             ],
             "name":"University of This Place"
          },
          {
             "@id":"_:004",
             "@type":"https://openminds.om-i.org/types/Person",
             "familyName":"Professor",
             "preferredName":"A"
          }
       ]
    }

    assert saved_data == expected_saved_data
