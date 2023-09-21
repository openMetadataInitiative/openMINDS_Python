"""
Structured information on a software tool (concept level).
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Software(LinkedMetadata):
    """
    Structured information on a software tool (concept level).
    """

    type_ = ["https://openminds.ebrains.eu/core/Software"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "custodian",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "developer",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add all parties that developed this software.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.RRID", "openminds.latest.core.SWHID"],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_version",
            "openminds.latest.core.SoftwareVersion",
            "vocab:hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this software tool.",
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(
        self,
        id=None,
        custodian=None,
        description=None,
        developer=None,
        digital_identifier=None,
        full_name=None,
        has_version=None,
        homepage=None,
        how_to_cite=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            custodian=custodian,
            description=description,
            developer=developer,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_version=has_version,
            homepage=homepage,
            how_to_cite=how_to_cite,
            short_name=short_name,
        )
