"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class NumericalParameter(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/core/NumericalParameter"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this numerical parameter.",
        ),
        Property(
            "value",
            ["openminds.v2_0.core.QuantitativeValue", "openminds.v2_0.core.QuantitativeValueRange"],
            "vocab:value",
            multiple=True,
            unique_items=False,
            min_items=1,
            required=True,
            description="Entry for a property.",
            instructions="Add at least one quantitative value for this parameter.",
        ),
    ]

    def __init__(self, name=None, value=None):
        return super().__init__(
            name=name,
            value=value,
        )