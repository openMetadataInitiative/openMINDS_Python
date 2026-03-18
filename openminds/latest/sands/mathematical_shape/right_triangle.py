"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class RightTriangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RightTriangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "perpendicular_leg_lengthss",
            "openminds.latest.core.QuantitativeValue",
            "perpendicularLegLengths",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the lengths of the two perpendicular legs of this right triangle.",
        ),
    ]

    def __init__(self, perpendicular_leg_lengthss=None):
        return super().__init__(
            perpendicular_leg_lengthss=perpendicular_leg_lengthss,
        )
