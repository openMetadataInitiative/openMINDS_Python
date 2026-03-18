"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Parallelogram(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Parallelogram"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "base_distance",
            "openminds.v5.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the parallel lines of the base of this parallelogram.",
        ),
        Property(
            "base_length",
            "openminds.v5.core.QuantitativeValue",
            "baseLength",
            required=True,
            description="no description available",
            instructions="Enter the uniform length of the bottom and top sides (the base) of this parallelogram.",
        ),
        Property(
            "interior_angle",
            "openminds.v5.core.QuantitativeValue",
            "interiorAngle",
            required=True,
            description="no description available",
            instructions="Enter an interior angle between the base and an adjacent side of this parallelogram.",
        ),
    ]

    def __init__(self, base_distance=None, base_length=None, interior_angle=None):
        return super().__init__(
            base_distance=base_distance,
            base_length=base_length,
            interior_angle=interior_angle,
        )
