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
    schema_version = "v4.0"

    properties = [
        Property(
            "about",
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
            "openminds.v4.core.Person",
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
