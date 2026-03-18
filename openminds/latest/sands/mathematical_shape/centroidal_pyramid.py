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
    schema_version = "latest"

    properties = [
        Property(
            "apex_base_distance",
            "openminds.latest.core.QuantitativeValue",
            "apexBaseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance from the centroid of the base plane to the apex of this centroidal pyramid.",
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
            instructions="Enter the two-dimensional base shape of this centroidal pyramid.",
        ),
    ]

    def __init__(self, apex_base_distance=None, base_shape=None):
        return super().__init__(
            apex_base_distance=apex_base_distance,
            base_shape=base_shape,
        )
