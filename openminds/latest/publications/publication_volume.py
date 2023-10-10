"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class PublicationVolume(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/PublicationVolume"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "is_part_of",
            "openminds.latest.publications.Periodical",
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the periodical this publication volume is part of.",
        ),
        Property(
            "volume_number",
            str,
            "volumeNumber",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the volume number of this publication volume.",
        ),
    ]

    def __init__(self, id=None, is_part_of=None, volume_number=None):
        return super().__init__(
            id=id,
            is_part_of=is_part_of,
            volume_number=volume_number,
        )
