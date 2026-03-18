"""
Structured information on a research project.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Project(LinkedMetadata):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.om-i.org/types/Project"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "contributions",
            "openminds.latest.core.Contribution",
            "contribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all individual, organisational, or consortial contributions to this project.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the project.",
            instructions="Enter a description of this project.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the project.",
            instructions="Enter a descriptive full name (or title) for this project.",
        ),
        Property(
            "has_parts",
            [
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipe",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.Dataset",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.Interface",
                "openminds.latest.core.InterfaceVersion",
                "openminds.latest.core.MetaDataModel",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.Software",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.publications.LivePaper",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.AnatomicalAtlas",
                "openminds.latest.sands.AnatomicalAtlasVersion",
                "openminds.latest.sands.CommonCoordinateFramework",
                "openminds.latest.sands.CommonCoordinateFrameworkVersion",
            ],
            "hasPart",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="no description available",
            instructions="Add all research product (versions) that are part of this project.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the project.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this project.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the project.",
            instructions="Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "type",
            "openminds.latest.controlled_terms.ProjectType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this project (e.g., research project, grant project).",
        ),
    ]

    def __init__(
        self,
        id=None,
        contributions=None,
        description=None,
        full_name=None,
        has_parts=None,
        homepage=None,
        short_name=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            contributions=contributions,
            description=description,
            full_name=full_name,
            has_parts=has_parts,
            homepage=homepage,
            short_name=short_name,
            type=type,
        )
