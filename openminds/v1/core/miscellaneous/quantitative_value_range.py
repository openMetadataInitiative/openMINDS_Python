"""
A representation of a range of quantitative values.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class QuantitativeValueRange(EmbeddedMetadata):
    """
    A representation of a range of quantitative values.
    """

    type_ = "https://openminds.ebrains.eu/core/QuantitativeValueRange"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "max_value",
            "openminds.v1.core.QuantitativeValue",
            "maxValue",
            required=True,
            description="Greatest quantity attained or allowed.",
            instructions="Add the maximum quantitative value of this range.",
        ),
        Property(
            "min_value",
            "openminds.v1.core.QuantitativeValue",
            "minValue",
            required=True,
            description="Smallest quantity attained or allowed.",
            instructions="Add the minimum quantitative value of this range.",
        ),
    ]

    def __init__(self, max_value=None, min_value=None):
        return super().__init__(
            max_value=max_value,
            min_value=min_value,
        )
