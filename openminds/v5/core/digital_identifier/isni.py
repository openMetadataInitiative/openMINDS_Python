"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ISNI(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ISNI"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the ISNI.",
            instructions="Enter the identifier for legal entities provided by the International Standard Name Identifier Assignment Agency ('International Standard Name Identifier'; ISNI) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://isni.org/' + ISNI).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
