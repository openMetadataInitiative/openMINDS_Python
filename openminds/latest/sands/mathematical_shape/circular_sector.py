"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CircularSector(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CircularSector"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "central_angle",
            "openminds.latest.core.QuantitativeValue",
            "centralAngle",
            required=True,
            description="no description available",
            instructions="Enter the central angle of this circular sector.",
        ),
        Property(
            "radius",
            "openminds.latest.core.QuantitativeValue",
            "radius",
            required=True,
            description="no description available",
            instructions="Enter the radius of this circular sector.",
        ),
    ]

    def __init__(self, central_angle=None, radius=None):
        return super().__init__(
            central_angle=central_angle,
            radius=radius,
        )
