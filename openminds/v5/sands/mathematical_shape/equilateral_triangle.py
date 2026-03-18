"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class EquilateralTriangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/EquilateralTriangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "side_length",
            "openminds.v5.core.QuantitativeValue",
            "sideLength",
            required=True,
            description="no description available",
            instructions="Enter the common length of the sides of this equilateral triangle.",
        ),
    ]

    def __init__(self, side_length=None):
        return super().__init__(
            side_length=side_length,
        )
