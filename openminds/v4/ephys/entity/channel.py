"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Channel(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Channel"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies the channel within a particular product.",
            instructions="Enter the identifier (or label) of this channel that is used within the corresponding data files to identify this channel.",
        ),
        Property(
            "unit",
            "openminds.v4.controlled_terms.UnitOfMeasurement",
            "unit",
            required=True,
            description="Determinate quantity adopted as a standard of measurement.",
            instructions="Add the unit of measurement for this channel.",
        ),
    ]

    def __init__(self, internal_identifier=None, unit=None):
        return super().__init__(
            internal_identifier=internal_identifier,
            unit=unit,
        )
