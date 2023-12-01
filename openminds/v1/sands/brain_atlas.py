"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class BrainAtlas(LinkedMetadata):
    """
    Structured information on a brain atlas (concept level).
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlas"
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
            instructions="Enter a short description for this brain atlas.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this brain atlas.",
        ),
        Property(
            "has_versions",
            "openminds.v1.sands.BrainAtlasVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add one or several brain atlas versions that belong to this brain atlas.",
        ),
        Property(
            "homepage",
            str,
            "homepage",
            formatting="text/plain",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this brain atlas.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this brain atlas.",
        ),
    ]

    def __init__(self, id=None, description=None, full_name=None, has_versions=None, homepage=None, short_name=None):
        return super().__init__(
            id=id,
            description=description,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            short_name=short_name,
        )
