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
    schema_version = "v2.0"

    properties = [
        Property(
            "authors",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add one or several authors (person or organization) that contributed to the production and publication of this dataset.",
        ),
        Property(
            "custodians",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add one or several custodians (person or organization) that are responsible for this research product. Note that this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references). Note that this description should be fitting for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            "openminds.v2.core.DOI",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (title) for this research product.  Note that this full name should be fitting for all attached research product versions.",
        ),
        Property(
            "has_versions",
            "openminds.v2.core.DatasetVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add one or several versions of this dataset.",
        ),
        Property(
            "homepage",
            "openminds.v2.core.URL",
            "homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
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
        authors=None,
        custodians=None,
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
            authors=authors,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            short_name=short_name,
        )
