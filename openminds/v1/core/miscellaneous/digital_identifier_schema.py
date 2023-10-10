"""
Structured information on a digital identifier schema.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class DigitalIdentifierSchema(LinkedMetadata):
    """
    Structured information on a digital identifier schema.
    """

    type_ = "https://openminds.ebrains.eu/core/DigitalIdentifierSchema"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "iri",
            str,
            "IRI",
            formatting="text/plain",
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) of this digital identifier schema.",
        ),
        Property(
            "identifier_pattern",
            str,
            "identifierPattern",
            formatting="text/plain",
            description="Format of a term or code used to identify something or someone.",
            instructions="Enter the required pattern for the identifiers of this digital identifier schema.",
        ),
        Property(
            "type",
            str,
            "type",
            formatting="text/plain",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Enter the type of this digital identifier schema.",
        ),
    ]

    def __init__(self, id=None, iri=None, identifier_pattern=None, type=None):
        return super().__init__(
            id=id,
            iri=iri,
            identifier_pattern=identifier_pattern,
            type=type,
        )
