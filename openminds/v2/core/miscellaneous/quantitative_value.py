"""
Structured information on a quantitative value.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class QuantitativeValue(EmbeddedMetadata):
    """
    Structured information on a quantitative value.
    """

    type_ = "https://openminds.ebrains.eu/core/QuantitativeValue"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "type_of_uncertainty",
            "openminds.v2.controlled_terms.TypeOfUncertainty",
            "typeOfUncertainty",
            description="Distinct technique used to quantify the uncertainty of a measurement.",
            instructions="Add the type of uncertainty used for this quantitative value.",
        ),
        Property(
            "uncertainties",
            float,
            "uncertainty",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            description="Quantitative value range defining the uncertainty of a measurement.",
            instructions="Enter the measurement uncertainty of this quantitative value.",
        ),
        Property(
            "unit",
            "openminds.v2.controlled_terms.UnitOfMeasurement",
            "unit",
            description="Determinate quantity adopted as a standard of measurement.",
            instructions="Add the unit of measurement of this quantitative value.",
        ),
        Property(
            "value",
            float,
            "value",
            required=True,
            description="Entry for a property.",
            instructions="Enter the measurement value of this quantitative value.",
        ),
    ]

    def __init__(self, type_of_uncertainty=None, uncertainties=None, unit=None, value=None):
        return super().__init__(
            type_of_uncertainty=type_of_uncertainty,
            uncertainties=uncertainties,
            unit=unit,
            value=value,
        )
