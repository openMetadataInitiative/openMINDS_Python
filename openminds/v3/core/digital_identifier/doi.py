"""
Structured information about a digital object identifier, as standardized by the International Organization for Standardization.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class DOI(LinkedMetadata):
    """
    Structured information about a digital object identifier, as standardized by the International Organization for Standardization.
    """

    type_ = "https://openminds.ebrains.eu/core/DOI"
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
            instructions="Enter the unique and persistent object identifier provided by the International Digital Object Identifier Foundation ('Digital Object Identifier'; DOI) as an internationalized resource identifier (IRI) following the defined pattern (i.e., 'https://doi.org/' + DOI).",
        ),
    ]

    def __init__(self, id=None, identifier=None):
        return super().__init__(
            id=id,
            identifier=identifier,
        )
