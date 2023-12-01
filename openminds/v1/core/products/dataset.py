"""
Structured information on data originating from human/animal studies or simulations (concept level).
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Dataset(LinkedMetadata):
    """
    Structured information on data originating from human/animal studies or simulations (concept level).
    """

    type_ = "https://openminds.ebrains.eu/core/Dataset"
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
            instructions="Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references).",
        ),
        Property(
            "digital_identifier",
            "openminds.v1.core.DigitalIdentifier",
            "digitalIdentifier",
            required=True,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (title) for this research product.",
        ),
        Property(
            "has_versions",
            "openminds.v1.core.DatasetVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to variants of an original.",
            instructions="Add one or several versions of this dataset.",
        ),
        Property(
            "homepage",
            str,
            "homepage",
            formatting="text/plain",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this research product (max. 30 characters; no space).",
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
        short_name=None,
    ):
        return super().__init__(
            id=id,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            short_name=short_name,
        )
