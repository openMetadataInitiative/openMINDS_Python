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
    schema_version = "v2.0"

    properties = [
        Property(
            "end_date",
            date,
            "endDate",
            description="Date in the Gregorian calendar at which something terminates in time.",
            instructions="Enter the end date of this affiliation. Leave blank if the affiliation is still current.",
        ),
        Property(
            "organization",
            "openminds.v2.core.Organization",
            "organization",
            required=True,
            description="Legally accountable, administrative and functional structure.",
            instructions="Add organization to which a person is or was affiliated.",
        ),
        Property(
            "start_date",
            date,
            "startDate",
            description="Date in the Gregorian calendar at which something begins in time",
            instructions="Enter the start date of this affiliation.",
        ),
    ]

    def __init__(self, end_date=None, organization=None, start_date=None):
        return super().__init__(
            end_date=end_date,
            organization=organization,
            start_date=start_date,
        )
