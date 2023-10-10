"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContentTypePattern(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ContentTypePattern"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "content_type",
            "openminds.v3.core.ContentType",
            "contentType",
            required=True,
            description="no description available",
            instructions="Add the content type that can be defined by the regular expression of this content type pattern (e.g., for file extensions).",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this content type pattern that may help you to find this instance more easily.",
        ),
        Property(
            "regex",
            str,
            "regex",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the regular expression for common elements within the file names (including their file path and/or extension) of the files formatted using the stated 'contentType'.",
        ),
    ]

    def __init__(self, id=None, content_type=None, lookup_label=None, regex=None):
        return super().__init__(
            id=id,
            content_type=content_type,
            lookup_label=lookup_label,
            regex=regex,
        )
