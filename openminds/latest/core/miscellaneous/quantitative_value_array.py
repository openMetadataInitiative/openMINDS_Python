"""
A representation of an array of quantitative values, optionally with uncertainties.
"""

# this file was auto-generated!

from numbers import Real

from openminds.base import LinkedMetadata
from openminds.properties import Property


class QuantitativeValueArray(LinkedMetadata):
    """
    A representation of an array of quantitative values, optionally with uncertainties.
    """

    type_ = "https://openminds.ebrains.eu/core/QuantitativeValueArray"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "negative_uncertainties",
            Real,
            "negativeUncertainties",
            multiple=True,
            unique_items=False,
            min_items=2,
            description="no description available",
            instructions="Enter the negative uncertainties for all values. Note that the length of the arrays have to match.",
        ),
        Property(
            "positive_uncertainties",
            Real,
            "positiveUncertainties",
            multiple=True,
            unique_items=False,
            min_items=2,
            description="no description available",
            instructions="Enter the positive uncertainties for all values. Note that the length of the arrays have to match.",
        ),
        Property(
            "type_of_uncertainty",
            "openminds.latest.controlled_terms.TypeOfUncertainty",
            "typeOfUncertainty",
            description="Distinct technique used to quantify the uncertainty of a measurement.",
            instructions="Add the type of estimation for the uncertainties.",
        ),
        Property(
            "unit",
            "openminds.latest.controlled_terms.UnitOfMeasurement",
            "unit",
            description="Determinate quantity adopted as a standard of measurement.",
            instructions="Add the unit of measurement of the values and their uncertainties.",
        ),
        Property(
            "values",
            Real,
            "values",
            multiple=True,
            unique_items=False,
            min_items=2,
            required=True,
            description="no description available",
            instructions="Enter all measured values.",
        ),
    ]

    def __init__(
        self,
        id=None,
        negative_uncertainties=None,
        positive_uncertainties=None,
        type_of_uncertainty=None,
        unit=None,
        values=None,
    ):
        return super().__init__(
            id=id,
            negative_uncertainties=negative_uncertainties,
            positive_uncertainties=positive_uncertainties,
            type_of_uncertainty=type_of_uncertainty,
            unit=unit,
            values=values,
        )
