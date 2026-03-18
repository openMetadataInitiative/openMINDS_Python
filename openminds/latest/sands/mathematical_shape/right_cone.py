"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class RightCone(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RightCone"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "apex_base_distance",
            "openminds.latest.core.QuantitativeValue",
            "apexBaseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance from the center of the base plane to the apex of this right cone.",
        ),
        Property(
            "base_shape",
            ["openminds.latest.sands.Circle", "openminds.latest.sands.Ellipse"],
            "baseShape",
            required=True,
            description="no description available",
            instructions="Enter the two-dimensional elliptic base shape of this right cone.",
        ),
    ]

    def __init__(self, apex_base_distance=None, base_shape=None):
        return super().__init__(
            apex_base_distance=apex_base_distance,
            base_shape=base_shape,
        )
