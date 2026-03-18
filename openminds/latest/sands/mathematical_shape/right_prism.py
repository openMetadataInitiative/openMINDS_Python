"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class RightPrism(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RightPrism"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "base_distance",
            "openminds.latest.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the two base planes of this right prism.",
        ),
        Property(
            "base_shape",
            [
                "openminds.latest.sands.EquilateralTriangle",
                "openminds.latest.sands.IsoscelesTriangle",
                "openminds.latest.sands.Kite",
                "openminds.latest.sands.Parallelogram",
                "openminds.latest.sands.Rectangle",
                "openminds.latest.sands.RegularPolygon",
                "openminds.latest.sands.Rhombus",
                "openminds.latest.sands.RightTriangle",
                "openminds.latest.sands.Square",
                "openminds.latest.sands.Trapezoid",
                "openminds.latest.sands.Triangle",
            ],
            "baseShape",
            required=True,
            description="no description available",
            instructions="Enter the two-dimensional base shape of the two planes of this right prism.",
        ),
    ]

    def __init__(self, base_distance=None, base_shape=None):
        return super().__init__(
            base_distance=base_distance,
            base_shape=base_shape,
        )
