"""
Structured information on a research project.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Project(LinkedMetadata):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.ebrains.eu/core/Project"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
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
            instructions="Enter a descriptive full name (title) for this project.",
        ),
        Property(
            "has_research_products",
            [
                "openminds.v1.core.Dataset",
                "openminds.v1.core.DatasetVersion",
                "openminds.v1.core.MetaDataModel",
                "openminds.v1.core.MetaDataModelVersion",
                "openminds.v1.core.Model",
                "openminds.v1.core.ModelVersion",
                "openminds.v1.core.Software",
                "openminds.v1.core.SoftwareVersion",
            ],
            "hasResearchProducts",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="Reference to subsidiary research products.",
            instructions="Add all research products or research product versions that are part of this project.",
        ),
        Property(
            "homepage",
            str,
            "homepage",
            formatting="text/plain",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this model version.",
        ),
        Property(
            "project_leaders",
            ["openminds.v1.core.Organization", "openminds.v1.core.Person"],
            "projectLeader",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add one or several project leader (person or organization).",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this project.",
        ),
    ]

    def __init__(
        self,
        id=None,
        description=None,
        full_name=None,
        has_research_products=None,
        homepage=None,
        project_leaders=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            description=description,
            full_name=full_name,
            has_research_products=has_research_products,
            homepage=homepage,
            project_leaders=project_leaders,
            short_name=short_name,
        )
