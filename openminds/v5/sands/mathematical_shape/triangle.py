"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Triangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Triangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "apex_angle",
            "openminds.v5.core.QuantitativeValue",
            "apexAngle",
            required=True,
            description="no description available",
            instructions="Enter the angle at the apex of this triangle.",
        ),
        Property(
            "leg_lengths",
            "openminds.v5.core.QuantitativeValue",
            "legLengths",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the lengths of the two sides meeting at the apex of this triangle.",
        ),
    ]

    def __init__(self, apex_angle=None, leg_lengths=None):
        return super().__init__(
            apex_angle=apex_angle,
            leg_lengths=leg_lengths,
        )
