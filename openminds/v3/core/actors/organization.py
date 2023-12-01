"""
Structured information on an organization.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Organization(LinkedMetadata):
    """
    Structured information on an organization.
    """

    type_ = "https://openminds.ebrains.eu/core/Organization"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "affiliations",
            "openminds.v3.core.Affiliation",
            "affiliation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Declaration of a person being closely associated to an organization.",
            instructions="Enter all current and, if necessary, past affiliations of this organization.",
        ),
        Property(
            "digital_identifiers",
            ["openminds.v3.core.GRIDID", "openminds.v3.core.RORID", "openminds.v3.core.RRID"],
            "digitalIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add all globally unique and persistent digital identifier of this organization.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter the full name of this organization.",
        ),
        Property(
            "has_parents",
            "openminds.v3.core.Organization",
            "hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a parent object or legal person.",
            instructions="Add all parent organizations of this organization.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this organization.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this organization that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(
        self,
        id=None,
        affiliations=None,
        digital_identifiers=None,
        full_name=None,
        has_parents=None,
        homepage=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            affiliations=affiliations,
            digital_identifiers=digital_identifiers,
            full_name=full_name,
            has_parents=has_parents,
            homepage=homepage,
            short_name=short_name,
        )
