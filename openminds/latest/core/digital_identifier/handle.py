"""
A persistent identifier for an information resource provided by the Handle System of the Corporation for National Research Initiatives.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class HANDLE(LinkedMetadata):
    """
    A persistent identifier for an information resource provided by the Handle System of the Corporation for National Research Initiatives.
    """

    type_ = "https://openminds.ebrains.eu/core/HANDLE"
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
            instructions="Enter the identifier for a superset of DOIs provided by the Corporation for National Research Initiatives (HANDLE) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'http://hdl.handle.net/' + HANDLE).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
