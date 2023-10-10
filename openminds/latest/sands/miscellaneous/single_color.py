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

    type_ = "https://openminds.ebrains.eu/sands/SingleColor"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

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
