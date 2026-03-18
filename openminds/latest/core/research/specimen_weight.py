"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class SpecimenWeight(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SpecimenWeight"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "type",
            "openminds.latest.controlled_terms.WeightType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Enter the weight type for the specified weight value.",
        ),
        Property(
            "weight",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "weight",
            required=True,
            description="Amount that a thing or being weighs.",
            instructions="Enter the weight value.",
        ),
    ]

    def __init__(self, type=None, weight=None):
        return super().__init__(
            type=type,
            weight=weight,
        )
