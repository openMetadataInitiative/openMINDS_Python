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
    schema_version = "v2.0"

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
            "digital_identifier",
            "openminds.v2.core.DOI",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this brain atlas.",
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
            "openminds.v2.sands.BrainAtlasVersion",
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
            "openminds.v2.core.URL",
            "homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this brain atlas.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this brain atlas. Leave blank if citation text can be extracted from the assigned digital identifier.",
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

    def __init__(
        self,
        id=None,
        description=None,
        digital_identifier=None,
        full_name=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            short_name=short_name,
        )
