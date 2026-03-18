"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class RightCylinder(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RightCylinder"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "base_distance",
            "openminds.latest.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the two base planes of this right cylinder.",
        ),
        Property(
            "base_shape",
            ["openminds.latest.sands.Circle", "openminds.latest.sands.Ellipse"],
            "baseShape",
            required=True,
            description="no description available",
            instructions="Enter the two-dimensional elliptic base shape of the two planes of this right cylinder.",
        ),
    ]

    def __init__(self, base_distance=None, base_shape=None):
        return super().__init__(
            base_distance=base_distance,
            base_shape=base_shape,
        )
