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

    type_ = "https://openminds.ebrains.eu/core/Comment"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "about",
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
            "openminds.v3_0.core.Person",
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
