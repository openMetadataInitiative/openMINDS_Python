"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class TermSuggestion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/TermSuggestion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "add_existing_terminology",
            "openminds.v2.controlled_terms.Terminology",
            "addExistingTerminology",
            description="Reference to an existing terminology (distinct class to group related terms).",
            instructions="Add an existing terminology in which the suggested term should be integrated in.",
        ),
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
        Property(
            "suggest_new_terminology",
            str,
            "suggestNewTerminology",
            formatting="text/plain",
            description="Proposal of a new distinct class to group related terms.",
            instructions="Propose a name for a new terminology in which the suggested term should be integrated in.",
        ),
    ]

    def __init__(
        self,
        id=None,
        add_existing_terminology=None,
        definition=None,
        description=None,
        name=None,
        ontology_identifier=None,
        suggest_new_terminology=None,
    ):
        return super().__init__(
            id=id,
            add_existing_terminology=add_existing_terminology,
            definition=definition,
            description=description,
            name=name,
            ontology_identifier=ontology_identifier,
            suggest_new_terminology=suggest_new_terminology,
        )
