"""
Structured information on an organization.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Organization(LinkedMetadata):
    """
    Structured information on an organization.
    """

    type_ = "https://openminds.ebrains.eu/core/Organization"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "digital_identifiers",
            "openminds.v1.core.DigitalIdentifier",
            "digitalIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add one or several globally unique and persistent digital identifier for this organization.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter the full name of the organization.",
        ),
        Property(
            "has_parent",
            "openminds.v1.core.Organization",
            "hasParent",
            description="Reference to a parent object or legal person.",
            instructions="Add a parent organization to this organization.",
        ),
        Property(
            "homepage",
            str,
            "homepage",
            formatting="text/plain",
            description="Main website of something or someone.",
            instructions="Enter a internationalized resource identifier (IRI) to the homepage of this organization.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter the short name of this organization.",
        ),
    ]

    def __init__(
        self, id=None, digital_identifiers=None, full_name=None, has_parent=None, homepage=None, short_name=None
    ):
        return super().__init__(
            id=id,
            digital_identifiers=digital_identifiers,
            full_name=full_name,
            has_parent=has_parent,
            homepage=homepage,
            short_name=short_name,
        )
