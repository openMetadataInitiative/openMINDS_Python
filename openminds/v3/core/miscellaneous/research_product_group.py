"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ResearchProductGroup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ResearchProductGroup"
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
            instructions="Enter the common context for this research product group.",
        ),
        Property(
            "has_parts",
            [
                "openminds.v3.computation.ValidationTest",
                "openminds.v3.computation.ValidationTestVersion",
                "openminds.v3.computation.WorkflowRecipe",
                "openminds.v3.computation.WorkflowRecipeVersion",
                "openminds.v3.core.Dataset",
                "openminds.v3.core.DatasetVersion",
                "openminds.v3.core.MetaDataModel",
                "openminds.v3.core.MetaDataModelVersion",
                "openminds.v3.core.Model",
                "openminds.v3.core.ModelVersion",
                "openminds.v3.core.Software",
                "openminds.v3.core.SoftwareVersion",
                "openminds.v3.core.WebService",
                "openminds.v3.core.WebServiceVersion",
                "openminds.v3.publications.LivePaper",
                "openminds.v3.publications.LivePaperVersion",
                "openminds.v3.sands.BrainAtlas",
                "openminds.v3.sands.BrainAtlasVersion",
                "openminds.v3.sands.CommonCoordinateSpace",
                "openminds.v3.sands.CommonCoordinateSpaceVersion",
            ],
            "hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all research products (research product versions) that should be grouped under the given 'context'.",
        ),
    ]

    def __init__(self, id=None, context=None, has_parts=None):
        return super().__init__(
            id=id,
            context=context,
            has_parts=has_parts,
        )
