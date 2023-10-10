"""
A persistent identifier for a researcher provided by Open Researcher and Contributor ID, Inc.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ORCID(LinkedMetadata):
    """
    A persistent identifier for a researcher provided by Open Researcher and Contributor ID, Inc.
    """

    type_ = "https://openminds.ebrains.eu/core/ORCID"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone.",
            instructions="Enter the resolvable identifier (IRI) of the Open Researcher and Contributor ID, Inc.",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
