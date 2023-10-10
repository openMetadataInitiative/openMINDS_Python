"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class StringParameter(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/StringParameter"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this parameter.",
        ),
        Property(
            "value",
            str,
            "value",
            formatting="text/plain",
            required=True,
            description="Entry for a property.",
            instructions="Enter a text value for this parameter.",
        ),
    ]

    def __init__(self, name=None, value=None):
        return super().__init__(
            name=name,
            value=value,
        )
