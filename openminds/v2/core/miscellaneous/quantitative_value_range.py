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
    schema_version = "v2.0"

    properties = [
        Property(
            "max_value",
            float,
            "maxValue",
            required=True,
            description="Greatest quantity attained or allowed.",
            instructions="Add the maximum value measured for this range.",
        ),
        Property(
            "min_value",
            float,
            "minValue",
            required=True,
            description="Smallest quantity attained or allowed.",
            instructions="Add the minimum value measured for this range.",
        ),
        Property(
            "unit",
            "openminds.v2.controlled_terms.UnitOfMeasurement",
            "unit",
            description="Determinate quantity adopted as a standard of measurement.",
            instructions="Add the unit of measurement of this quantitative value range.",
        ),
    ]

    def __init__(self, max_value=None, min_value=None, unit=None):
        return super().__init__(
            max_value=max_value,
            min_value=min_value,
            unit=unit,
        )
