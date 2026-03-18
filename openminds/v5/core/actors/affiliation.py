"""
Structured information about a relationship between two entities, such as a person and their employer.
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Affiliation(EmbeddedMetadata):
    """
    Structured information about a relationship between two entities, such as a person and their employer.
    """

    type_ = "https://openminds.om-i.org/types/Affiliation"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "organizations",
            "openminds.v5.core.Organization",
            "organization",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legally accountable, administrative and functional structure.",
            instructions="Add all organizations (in display order) with which the specified individual is affiliated.",
        ),
        Property(
            "person",
            "openminds.v5.core.Person",
            "person",
            required=True,
            description="no description available",
            instructions="Add the individual to whom this affiliation belongs.",
        ),
    ]

    def __init__(self, organizations=None, person=None):
        return super().__init__(
            organizations=organizations,
            person=person,
        )
