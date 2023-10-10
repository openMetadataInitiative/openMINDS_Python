"""
A GRID (Global Research Identifier Database) identifier.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class GRIDID(LinkedMetadata):
    """
    A GRID (Global Research Identifier Database) identifier.
    """

    type_ = "https://openminds.ebrains.eu/core/GRIDID"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone.",
            instructions="Enter the resolvable identifier (IRI) of the Global Research Identifier Database.",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
