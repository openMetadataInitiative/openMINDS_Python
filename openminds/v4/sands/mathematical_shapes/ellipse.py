"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Ellipse(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Ellipse"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "semi_major_axis",
            "openminds.v4.core.QuantitativeValue",
            "semiMajorAxis",
            required=True,
            description="no description available",
            instructions="Enter the length of the semi-minor axis of this ellipse.",
        ),
        Property(
            "semi_minor_axis",
            "openminds.v4.core.QuantitativeValue",
            "semiMinorAxis",
            required=True,
            description="no description available",
            instructions="Enter the length of the semi-major axis of this ellipse.",
        ),
    ]

    def __init__(self, id=None, semi_major_axis=None, semi_minor_axis=None):
        return super().__init__(
            id=id,
            semi_major_axis=semi_major_axis,
            semi_minor_axis=semi_minor_axis,
        )
