"""
Structured information on a used license.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class License(LinkedMetadata):
    """
    Structured information on a used license.
    """

    type_ = "https://openminds.ebrains.eu/core/License"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
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
            IRI,
            "legalCode",
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
        Property(
            "webpages",
            str,
            "webpage",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Hypertext document (block of information) found on the World Wide Web.",
            instructions="Enter one or several webpages related to this license (e.g. homepage).",
        ),
    ]

    def __init__(self, id=None, full_name=None, legal_code=None, short_name=None, webpages=None):
        return super().__init__(
            id=id,
            full_name=full_name,
            legal_code=legal_code,
            short_name=short_name,
            webpages=webpages,
        )
