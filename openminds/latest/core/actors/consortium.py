"""
Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Consortium(LinkedMetadata):
    """
    Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
    """

    type_ = "https://openminds.ebrains.eu/core/Consortium"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "contact_information",
            "openminds.latest.core.ContactInformation",
            "contactInformation",
            description="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).",
            instructions="Add the contact information of this consortium.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter the full name of this consortium.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this consortium.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this consortium that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(self, id=None, contact_information=None, full_name=None, homepage=None, short_name=None):
        return super().__init__(
            id=id,
            contact_information=contact_information,
            full_name=full_name,
            homepage=homepage,
            short_name=short_name,
        )
