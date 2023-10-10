"""
A persistent identifier for a research organization, provided by the Research Organization Registry.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class RORID(LinkedMetadata):
    """
    A persistent identifier for a research organization, provided by the Research Organization Registry.
    """

    type_ = "https://openminds.ebrains.eu/core/RORID"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify something or someone.",
            instructions="Enter the identifier for research organizations provided by the Corporation for National Research Initiatives ('Research Organization Registry IDentifier'; RORID) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://ror.org/' + RORID).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
