"""
<description not available>
"""

# this file was auto-generated!

from numbers import Real

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class GeoCoordinates(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/GeoCoordinates"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "elevation",
            Real,
            "elevation",
            description="no description available",
            instructions="Enter the elevation of the location in metres, following the definitions of the WGS84 system.",
        ),
        Property(
            "latitude",
            Real,
            "latitude",
            required=True,
            description="no description available",
            instructions="Enter the latitude of the location in decimal degrees, following the definitions of the WGS84 system.",
        ),
        Property(
            "longitude",
            Real,
            "longitude",
            required=True,
            description="no description available",
            instructions="Enter the longitude of the location in decimal degrees, following the definitions of the WGS84 system.",
        ),
    ]

    def __init__(self, elevation=None, latitude=None, longitude=None):
        return super().__init__(
            elevation=elevation,
            latitude=latitude,
            longitude=longitude,
        )
