"""
Structured information about a relationship between two entities, such as a person and their employer.
"""

# this file was auto-generated!

from datetime import date

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Affiliation(EmbeddedMetadata):
    """
    Structured information about a relationship between two entities, such as a person and their employer.
    """

    type_ = "https://openminds.ebrains.eu/core/Affiliation"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "end_date",
            date,
            "endDate",
            description="Date in the Gregorian calendar at which something terminates in time.",
            instructions="Enter the end date of this affiliation, formatted as 'YYYY-MM-DD'. Leave blank if this affiliation is still current.",
        ),
        Property(
            "member_of",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization"],
            "memberOf",
            required=True,
            description="no description available",
            instructions="Add the organization or consortium another party was or still is a member of.",
        ),
        Property(
            "start_date",
            date,
            "startDate",
            description="Date in the Gregorian calendar at which something begins in time",
            instructions="Enter the start date of this affiliation, formatted as 'YYYY-MM-DD'.",
        ),
    ]

    def __init__(self, end_date=None, member_of=None, start_date=None):
        return super().__init__(
            end_date=end_date,
            member_of=member_of,
            start_date=start_date,
        )
