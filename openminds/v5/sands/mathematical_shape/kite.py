"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Kite(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Kite"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "leg_lengthss",
            "openminds.v5.core.QuantitativeValue",
            "legLengths",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the two common leg lengths (for the shorter and longer leg pairs) of this kite.",
        ),
        Property(
            "symmetry_diagonal_length",
            "openminds.v5.core.QuantitativeValue",
            "symmetryDiagonalLength",
            required=True,
            description="no description available",
            instructions="Enter the length of the symmetry diagonal of this kite.",
        ),
    ]

    def __init__(self, leg_lengthss=None, symmetry_diagonal_length=None):
        return super().__init__(
            leg_lengthss=leg_lengthss,
            symmetry_diagonal_length=symmetry_diagonal_length,
        )
