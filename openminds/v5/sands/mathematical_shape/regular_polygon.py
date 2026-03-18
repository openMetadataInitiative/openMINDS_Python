"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class RegularPolygon(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RegularPolygon"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "circumradius",
            "openminds.v5.core.QuantitativeValue",
            "circumradius",
            required=True,
            description="no description available",
            instructions="Enter the common distance from the center to a vertex of this regular polygon.",
        ),
        Property(
            "number_of_sides",
            int,
            "numberOfSides",
            required=True,
            description="no description available",
            instructions="Enter the number of sides of this regular polygon.",
        ),
    ]

    def __init__(self, circumradius=None, number_of_sides=None):
        return super().__init__(
            circumradius=circumradius,
            number_of_sides=number_of_sides,
        )
