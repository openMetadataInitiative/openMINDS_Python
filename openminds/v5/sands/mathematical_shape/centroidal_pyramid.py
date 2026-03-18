"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CentroidalPyramid(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CentroidalPyramid"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "apex_base_distance",
            "openminds.v5.core.QuantitativeValue",
            "apexBaseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance from the centroid of the base plane to the apex of this centroidal pyramid.",
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
            instructions="Enter the two-dimensional base shape of this centroidal pyramid.",
        ),
    ]

    def __init__(self, apex_base_distance=None, base_shape=None):
        return super().__init__(
            apex_base_distance=apex_base_distance,
            base_shape=base_shape,
        )
