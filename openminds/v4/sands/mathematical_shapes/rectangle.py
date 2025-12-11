"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Rectangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Rectangle"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "length",
            "openminds.v4.core.QuantitativeValue",
            "length",
            required=True,
            description="no description available",
            instructions="Enter the length of this rectangle.",
        ),
        Property(
            "width",
            "openminds.v4.core.QuantitativeValue",
            "width",
            required=True,
            description="no description available",
            instructions="Enter the width of this rectangle.",
        ),
    ]

    def __init__(self, length=None, width=None):
        return super().__init__(
            length=length,
            width=width,
        )
