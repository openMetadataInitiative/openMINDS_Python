"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Ellipsoid(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Ellipsoid"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "intermediate_diameter",
            "openminds.v5.core.QuantitativeValue",
            "intermediateDiameter",
            required=True,
            description="no description available",
            instructions="Enter the intermediate diameter of this ellipsoid.",
        ),
        Property(
            "major_diameter",
            "openminds.v5.core.QuantitativeValue",
            "majorDiameter",
            required=True,
            description="no description available",
            instructions="Enter the major diameter of this ellipsoid.",
        ),
        Property(
            "minor_diameter",
            "openminds.v5.core.QuantitativeValue",
            "minorDiameter",
            required=True,
            description="no description available",
            instructions="Enter the minor diameter of this ellipsoid.",
        ),
    ]

    def __init__(self, intermediate_diameter=None, major_diameter=None, minor_diameter=None):
        return super().__init__(
            intermediate_diameter=intermediate_diameter,
            major_diameter=major_diameter,
            minor_diameter=minor_diameter,
        )
