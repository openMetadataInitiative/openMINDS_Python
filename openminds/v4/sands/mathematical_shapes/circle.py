"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Circle(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Circle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "radius",
            "openminds.v4.core.QuantitativeValue",
            "radius",
            required=True,
            description="no description available",
            instructions="Enter the radius of this circle.",
        ),
    ]

    def __init__(self, id=None, radius=None):
        return super().__init__(
            id=id,
            radius=radius,
        )
