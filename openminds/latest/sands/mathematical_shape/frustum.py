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
    schema_version = "latest"

    properties = [
        Property(
            "base_distance",
            "openminds.latest.core.QuantitativeValue",
            "baseDistance",
            required=True,
            description="no description available",
            instructions="Enter the perpendicular distance between the centered major and minor base planes of this frustum.",
        ),
        Property(
            "major_base_shape",
            [
                "openminds.latest.sands.Circle",
                "openminds.latest.sands.CircularSector",
                "openminds.latest.sands.Ellipse",
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
