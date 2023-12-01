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
    schema_version = "v2.0"

    properties = [
        Property(
            "coordinators",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "coordinator",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Legal person who organizes the collaborative work of people or groups.",
            instructions="Add one or several project coordinators (person or organization).",
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
            instructions="Enter a descriptive full name (title) for this project.",
        ),
        Property(
            "has_research_products",
            [
                "openminds.v2.core.Dataset",
                "openminds.v2.core.DatasetVersion",
                "openminds.v2.core.MetaDataModel",
                "openminds.v2.core.MetaDataModelVersion",
                "openminds.v2.core.Model",
                "openminds.v2.core.ModelVersion",
                "openminds.v2.core.Software",
                "openminds.v2.core.SoftwareVersion",
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
            "openminds.v2.core.URL",
            "homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this project.",
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
        coordinators=None,
        description=None,
        full_name=None,
        has_research_products=None,
        homepage=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            coordinators=coordinators,
            description=description,
            full_name=full_name,
            has_research_products=has_research_products,
            homepage=homepage,
            short_name=short_name,
        )
