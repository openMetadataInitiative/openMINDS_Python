"""
A persistent identifier for a research resource provided by the Resource Identification Initiative.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class RRID(LinkedMetadata):
    """
    A persistent identifier for a research resource provided by the Resource Identification Initiative.
    """

    type_ = "https://openminds.om-i.org/types/RRID"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the RRID.",
            instructions="Enter the resource identifier provided by the Resource Identification Initiative ('Research Resource IDentifier'; RRID) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://scicrunch.org/resolver/' + RRID).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
