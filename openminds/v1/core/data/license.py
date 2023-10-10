"""
Structured information on a used license.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class License(LinkedMetadata):
    """
    Structured information on a used license.
    """

    type_ = "https://openminds.ebrains.eu/core/License"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "deed",
            str,
            "deed",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the deed of this license.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter the full name of this license.",
        ),
        Property(
            "legal_code",
            str,
            "legalCode",
            formatting="text/plain",
            required=True,
            description="Type of legislation that claims to cover the law system (complete or parts) as it existed at the time the code was enacted.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the legal code of this license.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter the short name of this license.",
        ),
    ]

    def __init__(self, id=None, deed=None, full_name=None, legal_code=None, short_name=None):
        return super().__init__(
            id=id,
            deed=deed,
            full_name=full_name,
            legal_code=legal_code,
            short_name=short_name,
        )
