"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Rectangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Rectangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "major_side_length",
            "openminds.latest.core.QuantitativeValue",
            "majorSideLength",
            required=True,
            description="no description available",
            instructions="Enter the common length of the major sides of this rectangle.",
        ),
        Property(
            "minor_side_length",
            "openminds.latest.core.QuantitativeValue",
            "minorSideLength",
            required=True,
            description="no description available",
            instructions="Enter the common length of the minor sides of this rectangle.",
        ),
    ]

    def __init__(self, major_side_length=None, minor_side_length=None):
        return super().__init__(
            major_side_length=major_side_length,
            minor_side_length=minor_side_length,
        )
