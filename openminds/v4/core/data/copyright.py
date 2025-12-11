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
    schema_version = "v4.0"

    properties = [
        Property(
            "holders",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
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
            instructions="Enter the year during which the copyright was first asserted and, optionally, later years during which updated versions were published.",
        ),
    ]

    def __init__(self, holders=None, years=None):
        return super().__init__(
            holders=holders,
            years=years,
        )
