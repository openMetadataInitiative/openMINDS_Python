"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class SpecimenAge(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SpecimenAge"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "age",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "age",
            required=True,
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Enter the age value.",
        ),
        Property(
            "reference",
            "openminds.latest.controlled_terms.AgeReference",
            "reference",
            required=True,
            description="no description available",
            instructions="Enter the age reference for the specified age value.",
        ),
    ]

    def __init__(self, age=None, reference=None):
        return super().__init__(
            age=age,
            reference=reference,
        )
