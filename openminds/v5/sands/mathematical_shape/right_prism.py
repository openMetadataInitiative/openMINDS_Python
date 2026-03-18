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
    schema_version = "v5.0"

    properties = [
        Property(
            "base_distance",
            "openminds.v5.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the two base planes of this right prism.",
        ),
        Property(
            "base_shape",
            [
                "openminds.v5.sands.EquilateralTriangle",
                "openminds.v5.sands.IsoscelesTriangle",
                "openminds.v5.sands.Kite",
                "openminds.v5.sands.Parallelogram",
                "openminds.v5.sands.Rectangle",
                "openminds.v5.sands.RegularPolygon",
                "openminds.v5.sands.Rhombus",
                "openminds.v5.sands.RightTriangle",
                "openminds.v5.sands.Square",
                "openminds.v5.sands.Trapezoid",
                "openminds.v5.sands.Triangle",
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
