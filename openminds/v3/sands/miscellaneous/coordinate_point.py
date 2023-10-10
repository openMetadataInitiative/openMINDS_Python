"""
Structured information on a coordinate point.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CoordinatePoint(EmbeddedMetadata):
    """
    Structured information on a coordinate point.
    """

    type_ = "https://openminds.ebrains.eu/sands/CoordinatePoint"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "coordinate_space",
            ["openminds.v3.sands.CommonCoordinateSpaceVersion", "openminds.v3.sands.CustomCoordinateSpace"],
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this coordinate point exists in.",
        ),
        Property(
            "coordinates",
            "openminds.v3.core.QuantitativeValue",
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

    def __init__(self, coordinate_space=None, coordinates=None):
        return super().__init__(
            coordinate_space=coordinate_space,
            coordinates=coordinates,
        )
