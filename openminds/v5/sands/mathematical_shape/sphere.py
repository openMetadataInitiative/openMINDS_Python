"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Sphere(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Sphere"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "radius",
            "openminds.v5.core.QuantitativeValue",
            "radius",
            required=True,
            description="no description available",
            instructions="Enter the radius of this sphere.",
        ),
    ]

    def __init__(self, radius=None):
        return super().__init__(
            radius=radius,
        )
