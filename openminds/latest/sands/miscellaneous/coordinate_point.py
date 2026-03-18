"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CoordinatePoint(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CoordinatePoint"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "coordinate_framework",
            [
                "openminds.latest.sands.CommonCoordinateFrameworkVersion",
                "openminds.latest.sands.CustomCoordinateFramework",
            ],
            "coordinateFramework",
            required=True,
            description="no description available",
            instructions="Add the coordinate framework in which this coordinate point exists in.",
        ),
        Property(
            "coordinates",
            "openminds.latest.core.QuantitativeValue",
            "coordinates",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=3,
            required=True,
            description="Pair or triplet of numbers defining a location in a given coordinate space.",
            instructions="Enter the coordinates of this point within the stated coordinate space for two-dimensonal spaces as [x, y] or for three-dimensional space as [x, y, z].",
        ),
    ]

    def __init__(self, coordinate_framework=None, coordinates=None):
        return super().__init__(
            coordinate_framework=coordinate_framework,
            coordinates=coordinates,
        )
