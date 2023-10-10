"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Periodical(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/Periodical"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official (or most commonly used) abbreviation of the periodical (e.g., J. Physiol).",
        ),
        Property(
            "digital_identifier",
            "openminds.v3.core.ISSN",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this periodical.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name (or title) of this periodical (e.g., Journal of Physiology).",
        ),
    ]

    def __init__(self, id=None, abbreviation=None, digital_identifier=None, name=None):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            digital_identifier=digital_identifier,
            name=name,
        )
