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

    type_ = "https://openminds.ebrains.eu/core/RRID"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify something or someone.",
            instructions="Enter the resource identifier provided by the Resource Identification Initiative ('Research Resource IDentifier'; RRID) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://scicrunch.org/resolver/' + RRID).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
