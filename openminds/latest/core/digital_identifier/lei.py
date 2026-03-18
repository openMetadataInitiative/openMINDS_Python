"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class LEI(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/LEI"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the LEI.",
            instructions="Enter the identifier for legal entities provided by a local operating unit delegated by the Global Legal Entity Identifier Foundation ('Legal Entity Identifier'; LEI) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://lei.global/LEI/' + LEI).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
