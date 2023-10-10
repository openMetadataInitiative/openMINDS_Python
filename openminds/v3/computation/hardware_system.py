"""
Structured information about computing hardware.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class HardwareSystem(LinkedMetadata):
    """
    Structured information about computing hardware.
    """

    type_ = "https://openminds.ebrains.eu/computation/HardwareSystem"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this hardware system.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this hardware system.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this hardware system.",
        ),
    ]

    def __init__(self, id=None, description=None, name=None, version_identifier=None):
        return super().__init__(
            id=id,
            description=description,
            name=name,
            version_identifier=version_identifier,
        )
