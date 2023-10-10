"""
Structured information on a digital identifier.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class DigitalIdentifier(LinkedMetadata):
    """
    Structured information on a digital identifier.
    """

    type_ = "https://openminds.ebrains.eu/core/DigitalIdentifier"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for the resource this digital identifier stands for.",
        ),
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify something or someone.",
            instructions="Enter the digital identifier of a resource.",
        ),
        Property(
            "identifier_schema",
            "openminds.v1.core.DigitalIdentifierSchema",
            "identifierSchema",
            required=True,
            description="Standard for creating a particular identifier for something or someone.",
            instructions="Add the used schema of this digital identifier.",
        ),
    ]

    def __init__(self, id=None, how_to_cite=None, identifier=None, identifier_schema=None):
        return super().__init__(
            id=id,
            how_to_cite=how_to_cite,
            identifier=identifier,
            identifier_schema=identifier_schema,
        )
