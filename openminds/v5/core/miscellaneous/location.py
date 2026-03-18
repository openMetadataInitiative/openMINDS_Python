"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Location(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Location"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "address",
            str,
            "address",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the address of the location, in the format [Street address], City, [Region/State], [Postal code]. The minimum requested information is City.",
        ),
        Property(
            "country",
            "openminds.v5.controlled_terms.SovereignState",
            "country",
            required=True,
            description="no description available",
            instructions="Enter the country in which the location is found.",
        ),
        Property(
            "geo_coordinates",
            "openminds.v5.core.GeoCoordinates",
            "geoCoordinates",
            description="no description available",
            instructions="Enter the geographic coordinates of the location.",
        ),
    ]

    def __init__(self, address=None, country=None, geo_coordinates=None):
        return super().__init__(
            address=address,
            country=country,
            geo_coordinates=geo_coordinates,
        )
