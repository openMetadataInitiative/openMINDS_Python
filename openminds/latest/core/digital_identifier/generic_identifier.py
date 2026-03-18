"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class GenericIdentifier(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/GenericIdentifier"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "emitter",
            "openminds.latest.core.Organization",
            "emitter",
            required=True,
            description="no description available",
            instructions="Add the organization that governs and/or emits the identifier.",
        ),
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the generic identifier.",
            instructions="Enter a persistent, unique identifier emitted by an organization.",
        ),
        Property(
            "type",
            str,
            "type",
            formatting="text/plain",
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Enter the type of identifier, e.g. 'PubMed ID'.",
        ),
    ]

    def __init__(self, id=None, emitter=None, identifier=None, type=None):
        return super().__init__(
            id=id,
            emitter=emitter,
            identifier=identifier,
            type=type,
        )
