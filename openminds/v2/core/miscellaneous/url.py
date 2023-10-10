"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class URL(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/URL"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "url",
            IRI,
            "URL",
            description="no description available",
            instructions="Enter a uniform resource locator (URL).",
        ),
    ]

    def __init__(self, id=None, url=None):
        return super().__init__(
            id=id,
            url=url,
        )
