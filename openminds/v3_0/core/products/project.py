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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "coordinator",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:coordinator",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Legal person who organizes the collaborative work of people or groups.",
            instructions="Add all parties that coordinate this project.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this project.",
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this project.",
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
            min_items=2,
            required=True,
            description="no description available",
            instructions="Add all research product (versions) that are part of this project.",
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this project.",
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(
        self,
        id=None,
        coordinator=None,
        description=None,
        full_name=None,
        has_part=None,
        homepage=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            coordinator=coordinator,
            description=description,
            full_name=full_name,
            has_part=has_part,
            homepage=homepage,
            short_name=short_name,
        )
