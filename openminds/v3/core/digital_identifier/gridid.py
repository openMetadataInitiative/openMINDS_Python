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
    schema_version = "v3.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify something or someone.",
            instructions="Enter the identifier for research organizations provided by the International Digital Object Identifier Foundation ('Global Research Identifier Database IDentifier'; GRIDID) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://grid.ac/institutes/' + GRIDID).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
