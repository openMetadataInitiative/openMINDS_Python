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
    schema_version = "v3.0"

    properties = [
        Property(
            "max_value",
            float,
            "maxValue",
            required=True,
            description="Greatest quantity attained or allowed.",
            instructions="Enter the maximum value.",
        ),
        Property(
            "max_value_unit",
            "openminds.v3.controlled_terms.UnitOfMeasurement",
            "maxValueUnit",
            description="no description available",
            instructions="Add the unit of measurement for the maximum value.",
        ),
        Property(
            "min_value",
            float,
            "minValue",
            required=True,
            description="Smallest quantity attained or allowed.",
            instructions="Enter the minimum value.",
        ),
        Property(
            "min_value_unit",
            "openminds.v3.controlled_terms.UnitOfMeasurement",
            "minValueUnit",
            description="no description available",
            instructions="Add the unit of measurement for the minimum value.",
        ),
    ]

    def __init__(self, max_value=None, max_value_unit=None, min_value=None, min_value_unit=None):
        return super().__init__(
            max_value=max_value,
            max_value_unit=max_value_unit,
            min_value=min_value,
            min_value_unit=min_value_unit,
        )
