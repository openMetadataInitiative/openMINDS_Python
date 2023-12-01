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
    schema_version = "latest"

    properties = [
        Property(
            "grouping_types",
            "openminds.latest.controlled_terms.FileBundleGrouping",
            "groupingType",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all grouping types that are defined by this file path pattern.",
        ),
        Property(
            "regex",
            str,
            "regex",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the regular expression that defines this file path pattern. Note that it must have the same number of groups as stated under 'groupingType'.",
        ),
    ]

    def __init__(self, grouping_types=None, regex=None):
        return super().__init__(
            grouping_types=grouping_types,
            regex=regex,
        )
