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
    schema_version = "v2.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone.",
            instructions="Enter the resolvable identifier (IRI) of the Research Organization Registry.",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
