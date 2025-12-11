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

    type_ = "https://openminds.om-i.org/types/ResearchProductGroup"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
                "openminds.v4.computation.ValidationTest",
                "openminds.v4.computation.ValidationTestVersion",
                "openminds.v4.computation.WorkflowRecipe",
                "openminds.v4.computation.WorkflowRecipeVersion",
                "openminds.v4.core.Dataset",
                "openminds.v4.core.DatasetVersion",
                "openminds.v4.core.MetaDataModel",
                "openminds.v4.core.MetaDataModelVersion",
                "openminds.v4.core.Model",
                "openminds.v4.core.ModelVersion",
                "openminds.v4.core.Software",
                "openminds.v4.core.SoftwareVersion",
                "openminds.v4.core.WebService",
                "openminds.v4.core.WebServiceVersion",
                "openminds.v4.publications.LivePaper",
                "openminds.v4.publications.LivePaperVersion",
                "openminds.v4.sands.BrainAtlas",
                "openminds.v4.sands.BrainAtlasVersion",
                "openminds.v4.sands.CommonCoordinateSpace",
                "openminds.v4.sands.CommonCoordinateSpaceVersion",
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
