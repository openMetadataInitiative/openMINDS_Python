"""
<description not available>
"""

# this file was auto-generated!

from numbers import Real

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Frustum(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Frustum"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "base_distance",
            "openminds.v5.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the centered major and minor base planes of this frustum.",
        ),
        Property(
            "major_base_shape",
            [
                "openminds.v5.sands.Circle",
                "openminds.v5.sands.CircularSector",
                "openminds.v5.sands.Ellipse",
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
            "majorBaseShape",
            required=True,
            description="no description available",
            instructions="Enter the major two-dimensional base shape of this frustum.",
        ),
        Property(
            "minor_base_scale",
            Real,
            "minorBaseScale",
            required=True,
            description="no description available",
            instructions="Enter the ratio of the smaller to the larger base size of this frustum.",
        ),
    ]

    def __init__(self, base_distance=None, major_base_shape=None, minor_base_scale=None):
        return super().__init__(
            base_distance=base_distance,
            major_base_shape=major_base_shape,
            minor_base_scale=minor_base_scale,
        )
