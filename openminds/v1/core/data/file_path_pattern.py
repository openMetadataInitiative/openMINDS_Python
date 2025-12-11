"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class FilePathPattern(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/FilePathPattern"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "grouping_type",
            "openminds.v1.controlled_terms.FileBundleGrouping",
            "groupingType",
            required=True,
            description="no description available",
            instructions="Add the type of grouping that is defined by the given file path pattern.",
        ),
        Property(
            "regex",
            str,
            "regex",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the regular expression that defines this file path pattern.",
        ),
    ]

    def __init__(self, grouping_type=None, regex=None):
        return super().__init__(
            grouping_type=grouping_type,
            regex=regex,
        )
