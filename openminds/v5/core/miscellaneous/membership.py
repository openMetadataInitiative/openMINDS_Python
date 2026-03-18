"""
<description not available>
"""

# this file was auto-generated!

from datetime import date

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Membership(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Membership"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "end_date",
            date,
            "endDate",
            description="Date in the Gregorian calendar at which something terminates in time.",
            instructions="Enter the end date of this membership, formatted as 'YYYY-MM-DD'.",
        ),
        Property(
            "member",
            ["openminds.v5.core.Consortium", "openminds.v5.core.Organization", "openminds.v5.core.Person"],
            "member",
            required=True,
            description="no description available",
            instructions="Add the actor associated with this membership.",
        ),
        Property(
            "start_date",
            date,
            "startDate",
            description="Date in the Gregorian calendar at which something begins in time",
            instructions="Enter the start date of this membership, formatted as 'YYYY-MM-DD'.",
        ),
    ]

    def __init__(self, end_date=None, member=None, start_date=None):
        return super().__init__(
            end_date=end_date,
            member=member,
            start_date=start_date,
        )
