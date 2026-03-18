"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class StringProperty(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/StringProperty"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "external_definition_of_name",
            IRI,
            "externalDefinitionOfName",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) to an external definition of the property name.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the string property.",
            instructions="Enter a descriptive name for this property.",
        ),
        Property(
            "value",
            str,
            "value",
            formatting="text/plain",
            required=True,
            description="Entry for a property.",
            instructions="Enter the text value that is described by this string property.",
        ),
    ]

    def __init__(self, external_definition_of_name=None, name=None, value=None):
        return super().__init__(
            external_definition_of_name=external_definition_of_name,
            name=name,
            value=value,
        )
