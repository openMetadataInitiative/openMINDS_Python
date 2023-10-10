"""
An International Standard Serial Number of the ISSN International Centre.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ISSN(LinkedMetadata):
    """
    An International Standard Serial Number of the ISSN International Centre.
    """

    type_ = "https://openminds.ebrains.eu/core/ISSN"
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
            instructions="Enter the serial number for serial publications 'International Standard Serial Number' (ISSN) following the defined pattern (e.g., 1234-5678 or 1234-567X).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
