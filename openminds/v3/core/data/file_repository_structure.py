"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileRepositoryStructure(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/FileRepositoryStructure"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "file_path_patterns",
            "openminds.v3.core.FilePathPattern",
            "filePathPattern",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all file path patterns that define this file repository structure.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this file repository structure that may help you to find this instance more easily.",
        ),
    ]

    def __init__(self, id=None, file_path_patterns=None, lookup_label=None):
        return super().__init__(
            id=id,
            file_path_patterns=file_path_patterns,
            lookup_label=lookup_label,
        )
