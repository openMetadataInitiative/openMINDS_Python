"""
Structured information about the properties or parameters of an entity or process.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Configuration(LinkedMetadata):
    """
    Structured information about the properties or parameters of an entity or process.
    """

    type_ = "https://openminds.ebrains.eu/core/Configuration"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "configuration",
            str,
            "configuration",
            formatting="text/plain",
            multiline=True,
            required=True,
            description="no description available",
            instructions="Enter the configuration in a simple text based format (e.g., JSON or YAML).",
        ),
        Property(
            "format",
            "openminds.v3.core.ContentType",
            "format",
            required=True,
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this configuration.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this configuration that may help you to find this instance more easily.",
        ),
    ]

    def __init__(self, id=None, configuration=None, format=None, lookup_label=None):
        return super().__init__(
            id=id,
            configuration=configuration,
            format=format,
            lookup_label=lookup_label,
        )
