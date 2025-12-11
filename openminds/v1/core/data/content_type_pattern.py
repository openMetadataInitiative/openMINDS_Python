"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class ContentTypePattern(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ContentTypePattern"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "content_type",
            "openminds.v1.core.ContentType",
            "contentType",
            required=True,
            description="no description available",
            instructions="Enter the content type that can be defined by the given regular expression for file names/extensions.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this content type pattern.",
        ),
        Property(
            "regex",
            str,
            "regex",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter a regular expression for the file names/extensions that defines the give content type.",
        ),
    ]

    def __init__(self, content_type=None, lookup_label=None, regex=None):
        return super().__init__(
            content_type=content_type,
            lookup_label=lookup_label,
            regex=regex,
        )
