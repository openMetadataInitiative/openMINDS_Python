"""
Structured information about a property of some entity or process whose value is a number.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class NumericalProperty(EmbeddedMetadata):
    """
    Structured information about a property of some entity or process whose value is a number.
    """

    type_ = "https://openminds.ebrains.eu/core/NumericalProperty"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this numerical property.",
        ),
        Property(
            "values",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "value",
            multiple=True,
            unique_items=False,
            min_items=1,
            required=True,
            description="Entry for a property.",
            instructions="Enter all quantitative values that are described by this numerical property.",
        ),
    ]

    def __init__(self, name=None, values=None):
        return super().__init__(
            name=name,
            values=values,
        )
