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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "context",
            str,
            "vocab:context",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the common context for this research product group.",
        ),
        Property(
            "has_part",
            [
                "openminds.v3_0.computation.ValidationTest",
                "openminds.v3_0.computation.ValidationTestVersion",
                "openminds.v3_0.computation.WorkflowRecipe",
                "openminds.v3_0.computation.WorkflowRecipeVersion",
                "openminds.v3_0.core.Dataset",
                "openminds.v3_0.core.DatasetVersion",
                "openminds.v3_0.core.MetaDataModel",
                "openminds.v3_0.core.MetaDataModelVersion",
                "openminds.v3_0.core.Model",
                "openminds.v3_0.core.ModelVersion",
                "openminds.v3_0.core.Software",
                "openminds.v3_0.core.SoftwareVersion",
                "openminds.v3_0.core.WebService",
                "openminds.v3_0.core.WebServiceVersion",
                "openminds.v3_0.publications.LivePaper",
                "openminds.v3_0.publications.LivePaperVersion",
                "openminds.v3_0.sands.BrainAtlas",
                "openminds.v3_0.sands.BrainAtlasVersion",
                "openminds.v3_0.sands.CommonCoordinateSpace",
                "openminds.v3_0.sands.CommonCoordinateSpaceVersion",
            ],
            "vocab:hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all research products (research product versions) that should be grouped under the given 'context'.",
        ),
    ]

    def __init__(self, id=None, context=None, has_part=None):
        return super().__init__(
            id=id,
            context=context,
            has_part=has_part,
        )
