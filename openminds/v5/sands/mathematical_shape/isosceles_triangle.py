"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class IsoscelesTriangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/IsoscelesTriangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "apex_angle",
            "openminds.v5.core.QuantitativeValue",
            "apexAngle",
            required=True,
            description="no description available",
            instructions="Enter the angle at the apex between the two equal sides of this isosceles triangle.",
        ),
        Property(
            "leg_length",
            "openminds.v5.core.QuantitativeValue",
            "legLength",
            required=True,
            description="no description available",
            instructions="Enter the common length of the two equal sides meeting at the apex of this isosceles triangle.",
        ),
    ]

    def __init__(self, apex_angle=None, leg_length=None):
        return super().__init__(
            apex_angle=apex_angle,
            leg_length=leg_length,
        )
