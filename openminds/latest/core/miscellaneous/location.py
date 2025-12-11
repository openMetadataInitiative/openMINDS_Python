"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Location(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Location"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

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
            "openminds.latest.controlled_terms.SovereignState",
            "country",
            required=True,
            description="no description available",
            instructions="Enter the country in which the location is found.",
        ),
        Property(
            "geo_coordinates",
            "openminds.latest.core.GeoCoordinates",
            "geoCoordinates",
            description="no description available",
            instructions="Enter the geographic coordinates of the location.",
        ),
    ]

    def __init__(self, id=None, address=None, country=None, geo_coordinates=None):
        return super().__init__(
            id=id,
            address=address,
            country=country,
            geo_coordinates=geo_coordinates,
        )
