"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Rhombus(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Rhombus"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "diagonal_lengths",
            "openminds.v5.core.QuantitativeValue",
            "diagonalLengths",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the lengths of the two perpendicular diagonals of this rhombus.",
        ),
    ]

    def __init__(self, diagonal_lengths=None):
        return super().__init__(
            diagonal_lengths=diagonal_lengths,
        )
