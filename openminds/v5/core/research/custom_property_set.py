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

    type_ = "https://openminds.om-i.org/types/CustomPropertySet"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

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
            ["openminds.v5.core.Configuration", "openminds.v5.core.File", "openminds.v5.core.PropertyValueList"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the data that define the custom property set for the given context (e.g., stored as file or other entities such as property-value lists).",
        ),
        Property(
            "relevant_for",
            [
                "openminds.v5.controlled_terms.AnalysisTechnique",
                "openminds.v5.controlled_terms.MRIFatSuppressionTechnique",
                "openminds.v5.controlled_terms.MRIParallelAcquisitionTechnique",
                "openminds.v5.controlled_terms.MRIPulseSequence",
                "openminds.v5.controlled_terms.MRISpoilingTechnique",
                "openminds.v5.controlled_terms.MRIWeighting",
                "openminds.v5.controlled_terms.SpatialEncoding",
                "openminds.v5.controlled_terms.StimulationApproach",
                "openminds.v5.controlled_terms.StimulationTechnique",
                "openminds.v5.controlled_terms.Technique",
            ],
            "relevantFor",
            required=True,
            description="Reference to what or whom the custom property set bears significance.",
            instructions="Add the technique for which this custom property set is relevant.",
        ),
    ]

    def __init__(self, context=None, data_location=None, relevant_for=None):
        return super().__init__(
            context=context,
            data_location=data_location,
            relevant_for=relevant_for,
        )
