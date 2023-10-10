"""
Structured information on a coordinate point.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class CoordinatePoint(LinkedMetadata):
    """
    Structured information on a coordinate point.
    """

    type_ = "https://openminds.ebrains.eu/sands/CoordinatePoint"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "coordinate_space",
            "openminds.v1.sands.CoordinateSpace",
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this coordinate point exists in.",
        ),
        Property(
            "coordinates",
            "openminds.v1.core.QuantitativeValue",
            "coordinates",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=3,
            required=True,
            description="Pair or triplet of numbers defining a location in a given coordinate space.",
            instructions="Add two or three coordinates (2D: [x, y] or 3D: [x, y, z]) that define the exact location of this point in the stated space.",
        ),
    ]

    def __init__(self, id=None, coordinate_space=None, coordinates=None):
        return super().__init__(
            id=id,
            coordinate_space=coordinate_space,
            coordinates=coordinates,
        )
