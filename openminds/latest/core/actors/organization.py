"""
An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Organization(LinkedMetadata):
    """
    An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)
    """

    type_ = "https://openminds.om-i.org/types/Organization"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "acronym",
            str,
            "acronym",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the acronym of this organization.",
        ),
        Property(
            "alternate_names",
            str,
            "alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any other known name or acronym of this organization.",
        ),
        Property(
            "country_of_formation",
            "openminds.latest.controlled_terms.SovereignState",
            "countryOfFormation",
            required=True,
            description="no description available",
            instructions="Add the country where the organization was formed.",
        ),
        Property(
            "digital_identifiers",
            [
                "openminds.latest.core.GenericIdentifier",
                "openminds.latest.core.ISNI",
                "openminds.latest.core.LEI",
                "openminds.latest.core.RORID",
                "openminds.latest.core.RRID",
            ],
            "digitalIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add all globally unique and persistent digital identifier of this organization.",
        ),
        Property(
            "has_parents",
            "openminds.latest.core.Organization",
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
            description="Main website of the organization.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this organization.",
        ),
        Property(
            "jurisdiction",
            [
                "openminds.latest.controlled_terms.SovereignState",
                "openminds.latest.controlled_terms.SupranationalBody",
            ],
            "jurisdiction",
            description="no description available",
            instructions="Add the jurisdiction under which the organization operates.",
        ),
        Property(
            "location",
            "openminds.latest.core.Location",
            "location",
            description="no description available",
            instructions="Add the headquarters location of this organization.",
        ),
        Property(
            "memberships",
            "openminds.latest.core.Membership",
            "membership",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all membership records (one per member) for this organization. Who is considered a qualified member is typically defined in the organization’s membership agreements.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the organization.",
            instructions="Enter the organization’s preferred name for use in international contexts.",
        ),
        Property(
            "type",
            "openminds.latest.controlled_terms.OrganizationType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this organization (legal entity or organizational unit).",
        ),
    ]

    def __init__(
        self,
        id=None,
        acronym=None,
        alternate_names=None,
        country_of_formation=None,
        digital_identifiers=None,
        has_parents=None,
        homepage=None,
        jurisdiction=None,
        location=None,
        memberships=None,
        name=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            acronym=acronym,
            alternate_names=alternate_names,
            country_of_formation=country_of_formation,
            digital_identifiers=digital_identifiers,
            has_parents=has_parents,
            homepage=homepage,
            jurisdiction=jurisdiction,
            location=location,
            memberships=memberships,
            name=name,
            type=type,
        )
