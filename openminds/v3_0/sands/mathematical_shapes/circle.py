"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Circle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Circle"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "radius",
            "openminds.v3_0.core.QuantitativeValue",
            "vocab:radius",
            required=True,
            description="no description available",
            instructions="Enter the radius of this circle.",
        ),
    ]

    def __init__(self, radius=None):
        return super().__init__(
            radius=radius,
        )