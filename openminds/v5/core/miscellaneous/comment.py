"""
Structured information about a short text expressing an opinion on, or giving information about some entity.
"""

# this file was auto-generated!

from datetime import datetime

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Comment(LinkedMetadata):
    """
    Structured information about a short text expressing an opinion on, or giving information about some entity.
    """

    type_ = "https://openminds.om-i.org/types/Comment"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "about",
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
            "about",
            required=True,
            description="no description available",
            instructions="Add the research product (version) that this comment is about.",
        ),
        Property(
            "comment",
            str,
            "comment",
            formatting="text/plain",
            multiline=True,
            required=True,
            description="no description available",
            instructions="Enter the comment about the research product (version) stated under 'about'.",
        ),
        Property(
            "commenter",
            "openminds.v5.core.Person",
            "commenter",
            required=True,
            description="no description available",
            instructions="Add the person that created this comment.",
        ),
        Property(
            "timestamp",
            datetime,
            "timestamp",
            required=True,
            description="no description available",
            instructions="Enter the date and time on which this comment was made, formatted as '2023-02-07T16:00:00+00:00'.",
        ),
    ]

    def __init__(self, id=None, about=None, comment=None, commenter=None, timestamp=None):
        return super().__init__(
            id=id,
            about=about,
            comment=comment,
            commenter=commenter,
            timestamp=timestamp,
        )
