"""
An identifiable list of property-value pairs.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class PropertyValueList(LinkedMetadata):
    """
    An identifiable list of property-value pairs.
    """

    type_ = "https://openminds.ebrains.eu/core/PropertyValueList"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this property-value list that may help you to find this instance more easily.",
        ),
        Property(
            "property_value_pairs",
            ["openminds.latest.core.NumericalProperty", "openminds.latest.core.StringProperty"],
            "propertyValuePair",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Enter all numerical and string property-value pairs that belong to this property-value list.",
        ),
    ]

    def __init__(self, id=None, lookup_label=None, property_value_pairs=None):
        return super().__init__(
            id=id,
            lookup_label=lookup_label,
            property_value_pairs=property_value_pairs,
        )
