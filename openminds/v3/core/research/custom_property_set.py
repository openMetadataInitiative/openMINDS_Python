"""
Structured information about properties of an entity that are not represented in an openMINDS schema.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CustomPropertySet(EmbeddedMetadata):
    """
    Structured information about properties of an entity that are not represented in an openMINDS schema.
    """

    type_ = "https://openminds.ebrains.eu/core/CustomPropertySet"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "context",
            str,
            "context",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the common context for this custom property set.",
        ),
        Property(
            "data_location",
            ["openminds.v3.core.Configuration", "openminds.v3.core.File", "openminds.v3.core.PropertyValueList"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the data that define the custom property set for the given context (e.g., stored as file or other entities such as property-value lists).",
        ),
        Property(
            "relevant_for",
            [
                "openminds.v3.controlled_terms.AnalysisTechnique",
                "openminds.v3.controlled_terms.StimulationApproach",
                "openminds.v3.controlled_terms.StimulationTechnique",
                "openminds.v3.controlled_terms.Technique",
            ],
            "relevantFor",
            required=True,
            description="Reference to what or whom something or someone bears significance.",
            instructions="Add the technique for which this custom property set is relevant.",
        ),
    ]

    def __init__(self, context=None, data_location=None, relevant_for=None):
        return super().__init__(
            context=context,
            data_location=data_location,
            relevant_for=relevant_for,
        )
