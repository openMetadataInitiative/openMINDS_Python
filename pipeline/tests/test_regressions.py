from openminds import IRI
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
        node1.to_jsonld(include_empty_properties=False)
        == node2.to_jsonld(include_empty_properties=False)
        == expected
    )
