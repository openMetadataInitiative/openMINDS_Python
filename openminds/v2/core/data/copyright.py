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

    type_ = "https://openminds.ebrains.eu/core/Copyright"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "holders",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "holder",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person in possession of something.",
            instructions="Add one or several persons or organisations that hold the copyright.",
        ),
        Property(
            "year",
            str,
            "year",
            formatting="text/plain",
            required=True,
            description="Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December.",
            instructions="Enter the year during which the copyright was first asserted.",
        ),
    ]

    def __init__(self, holders=None, year=None):
        return super().__init__(
            holders=holders,
            year=year,
        )
