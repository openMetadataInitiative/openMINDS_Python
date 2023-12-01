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

    type_ = "https://openminds.ebrains.eu/core/Project"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "coordinators",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization", "openminds.v3.core.Person"],
            "coordinator",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Legal person who organizes the collaborative work of people or groups.",
            instructions="Add all parties that coordinate this project.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this project.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this project.",
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
            min_items=2,
            required=True,
            description="no description available",
            instructions="Add all research product (versions) that are part of this project.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this project.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(
        self,
        id=None,
        coordinators=None,
        description=None,
        full_name=None,
        has_parts=None,
        homepage=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            coordinators=coordinators,
            description=description,
            full_name=full_name,
            has_parts=has_parts,
            homepage=homepage,
            short_name=short_name,
        )
