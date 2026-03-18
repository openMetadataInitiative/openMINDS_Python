"""
Structured information on a person.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Person(LinkedMetadata):
    """
    Structured information on a person.
    """

    type_ = "https://openminds.om-i.org/types/Person"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "alternate_names",
            str,
            "alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any other known full name of this person.",
        ),
        Property(
            "associated_accounts",
            "openminds.v5.core.AccountInformation",
            "associatedAccount",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the information about web service accounts held by this person.",
        ),
        Property(
            "contact_information",
            "openminds.v5.core.ContactInformation",
            "contactInformation",
            description="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).",
            instructions="Add the contact information of this person.",
        ),
        Property(
            "digital_identifiers",
            ["openminds.v5.core.GenericIdentifier", "openminds.v5.core.ORCID"],
            "digitalIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add all globally unique and persistent digital identifier of this person.",
        ),
        Property(
            "family_name",
            str,
            "familyName",
            formatting="text/plain",
            description="Name borne in common by members of a family.",
            instructions="Enter the family name, surname, or equivalent of this person.",
        ),
        Property(
            "given_name",
            str,
            "givenName",
            formatting="text/plain",
            description="Name given to a person, including all potential middle names, but excluding the family name.",
            instructions="Enter the given name(s) of this person, or a name chosen in place of the given name. At least one of the names should be spelled out in full; initials may be used for the others.",
        ),
        Property(
            "preferred_name",
            str,
            "preferredName",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the person’s preferred way to write their name in a professional context. It is recommended to place given before family name separated by space.",
        ),
    ]

    def __init__(
        self,
        id=None,
        alternate_names=None,
        associated_accounts=None,
        contact_information=None,
        digital_identifiers=None,
        family_name=None,
        given_name=None,
        preferred_name=None,
    ):
        return super().__init__(
            id=id,
            alternate_names=alternate_names,
            associated_accounts=associated_accounts,
            contact_information=contact_information,
            digital_identifiers=digital_identifiers,
            family_name=family_name,
            given_name=given_name,
            preferred_name=preferred_name,
        )
