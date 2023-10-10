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
    schema_version = "v2.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone.",
            instructions="Enter the International Standard Book Number of the International ISBN Agency.",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
