"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class StringProperty(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/StringProperty"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the string property.",
            instructions="Enter a descriptive name for this property.",
        ),
        Property(
            "value",
            str,
            "value",
            formatting="text/plain",
            required=True,
            description="Entry for a property.",
            instructions="Enter the text value that is described by this string property.",
        ),
    ]

    def __init__(self, name=None, value=None):
        return super().__init__(
            name=name,
            value=value,
        )
