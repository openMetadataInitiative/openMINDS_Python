"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Strain(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Strain"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "identifiers",
            str,
            "identifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone.",
            instructions="Enter other database identifiers for the given strain that are supported by the members of the Alliance of Genome Resources (https://www.alliancegenome.org/).",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the related ontological term.",
        ),
    ]

    def __init__(
        self, id=None, definition=None, description=None, identifiers=None, name=None, ontology_identifier=None
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            identifiers=identifiers,
            name=name,
            ontology_identifier=ontology_identifier,
        )
