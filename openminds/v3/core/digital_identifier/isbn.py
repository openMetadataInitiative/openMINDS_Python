"""
An International Standard Book Number of the International ISBN Agency.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ISBN(LinkedMetadata):
    """
    An International Standard Book Number of the International ISBN Agency.
    """

    type_ = "https://openminds.ebrains.eu/core/ISBN"
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
            instructions="Enter the numeric commercial book identifier 'International Standard Book Number' (ISBN) following the defined pattern (e.g., 123-4-567-89012-3 (13-digit ISBN) or 4-567-89012-3 (10-digit ISBN)).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
