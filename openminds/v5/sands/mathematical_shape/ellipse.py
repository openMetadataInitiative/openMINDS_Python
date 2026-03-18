"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Ellipse(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Ellipse"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "diameters",
            "openminds.v5.core.QuantitativeValue",
            "diameters",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the lengths of the major and minor diameters of this ellipse.",
        ),
    ]

    def __init__(self, diameters=None):
        return super().__init__(
            diameters=diameters,
        )
