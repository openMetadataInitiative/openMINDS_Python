
from openminds.latest import core as omcore
from utils import build_fake_node


def test_issue_0002():
    # https://github.com/openMetadataInitiative/openMINDS_Python/issues/2
    # @type should not be given as a list but as a string

    node = build_fake_node(omcore.Person)
    data = node.to_jsonld()
    assert data["@type"] == "https://openminds.ebrains.eu/core/Person"
