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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "configuration",
            str,
            "vocab:configuration",
            formatting="text/plain",
            multiline=True,
            required=True,
            description="no description available",
            instructions="Enter the configuration in a simple text based format (e.g., JSON or YAML).",
        ),
        Property(
            "format",
            "openminds.v3_0.core.ContentType",
            "vocab:format",
            required=True,
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this configuration.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
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