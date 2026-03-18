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
    schema_version = "v5.0"

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
                "openminds.v5.computation.ValidationTest",
                "openminds.v5.computation.ValidationTestVersion",
                "openminds.v5.computation.WorkflowRecipe",
                "openminds.v5.computation.WorkflowRecipeVersion",
                "openminds.v5.core.Dataset",
                "openminds.v5.core.DatasetVersion",
                "openminds.v5.core.Interface",
                "openminds.v5.core.InterfaceVersion",
                "openminds.v5.core.MetaDataModel",
                "openminds.v5.core.MetaDataModelVersion",
                "openminds.v5.core.Model",
                "openminds.v5.core.ModelVersion",
                "openminds.v5.core.Software",
                "openminds.v5.core.SoftwareVersion",
                "openminds.v5.publications.LivePaper",
                "openminds.v5.publications.LivePaperVersion",
                "openminds.v5.sands.AnatomicalAtlas",
                "openminds.v5.sands.AnatomicalAtlasVersion",
                "openminds.v5.sands.CommonCoordinateFramework",
                "openminds.v5.sands.CommonCoordinateFrameworkVersion",
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
