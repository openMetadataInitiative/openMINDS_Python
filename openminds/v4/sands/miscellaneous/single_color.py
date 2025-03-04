"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class SingleColor(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SingleColor"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "value",
            str,
            "value",
            formatting="text/plain",
            required=True,
            description="Entry for a property.",
            instructions="Enter the Hex color code following the define pattern (e.g., #000000 or #C0C0C0).",
        ),
    ]

    def __init__(self, id=None, value=None):
        return super().__init__(
            id=id,
            value=value,
        )
