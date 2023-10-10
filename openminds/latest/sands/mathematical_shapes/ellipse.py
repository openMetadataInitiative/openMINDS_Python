"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Ellipse(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Ellipse"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "semi_major_axis",
            "openminds.latest.core.QuantitativeValue",
            "semiMajorAxis",
            required=True,
            description="no description available",
            instructions="Enter the length of the semi-minor axis of this ellipse.",
        ),
        Property(
            "semi_minor_axis",
            "openminds.latest.core.QuantitativeValue",
            "semiMinorAxis",
            required=True,
            description="no description available",
            instructions="Enter the length of the semi-major axis of this ellipse.",
        ),
    ]

    def __init__(self, semi_major_axis=None, semi_minor_axis=None):
        return super().__init__(
            semi_major_axis=semi_major_axis,
            semi_minor_axis=semi_minor_axis,
        )
