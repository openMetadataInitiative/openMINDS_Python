"""
Structured information on the copyright.
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Copyright(EmbeddedMetadata):
    """
    Structured information on the copyright.
    """

    type_ = "https://openminds.om-i.org/types/Copyright"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "custom_usage_clause",
            str,
            "customUsageClause",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a statement describing the usage rights, such as 'All rights reserved.'.",
        ),
        Property(
            "holders",
            ["openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "holder",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person in possession of something.",
            instructions="Add all parties that hold this copyright.",
        ),
        Property(
            "years",
            str,
            "year",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            required=True,
            description="Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December.",
            instructions="Enter the year when the copyright was first asserted, and optionally any subsequent years when the copyright holder and/or the rights-reservation clause was updated.",
        ),
    ]

    def __init__(self, custom_usage_clause=None, holders=None, years=None):
        return super().__init__(
            custom_usage_clause=custom_usage_clause,
            holders=holders,
            years=years,
        )
