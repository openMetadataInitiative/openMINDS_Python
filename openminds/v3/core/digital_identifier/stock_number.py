"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class StockNumber(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/StockNumber"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify something or someone.",
            instructions="Enter the stock number of an item provided by a store or company.",
        ),
        Property(
            "vendor",
            "openminds.v3.core.Organization",
            "vendor",
            required=True,
            description="no description available",
            instructions="Add the vendor that has the item with this identifier in stock.",
        ),
    ]

    def __init__(self, identifier=None, vendor=None):
        return super().__init__(
            identifier=identifier,
            vendor=vendor,
        )
