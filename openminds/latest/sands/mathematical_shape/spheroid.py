"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Spheroid(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Spheroid"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "equatorial_diameter",
            "openminds.latest.core.QuantitativeValue",
            "equatorialDiameter",
            required=True,
            description="no description available",
            instructions="Enter the equatorial diameters of this spheroid.",
        ),
        Property(
            "polar_diameter",
            "openminds.latest.core.QuantitativeValue",
            "polarDiameter",
            required=True,
            description="no description available",
            instructions="Enter the polar diameter of this spheroid.",
        ),
    ]

    def __init__(self, equatorial_diameter=None, polar_diameter=None):
        return super().__init__(
            equatorial_diameter=equatorial_diameter,
            polar_diameter=polar_diameter,
        )
