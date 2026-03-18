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
    schema_version = "latest"

    properties = [
        Property(
            "apex_angle",
            "openminds.latest.core.QuantitativeValue",
            "apexAngle",
            required=True,
            description="no description available",
            instructions="Enter the angle at the apex of this triangle.",
        ),
        Property(
            "leg_lengthss",
            "openminds.latest.core.QuantitativeValue",
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

    def __init__(self, apex_angle=None, leg_lengthss=None):
        return super().__init__(
            apex_angle=apex_angle,
            leg_lengthss=leg_lengthss,
        )
