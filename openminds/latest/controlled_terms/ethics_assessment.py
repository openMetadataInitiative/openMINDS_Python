"""
Structured information on the ethics assessment of a dataset.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class EthicsAssessment(LinkedMetadata):
    """
    Structured information on the ethics assessment of a dataset.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/EthicsAssessment"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

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
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
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
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


EthicsAssessment.eu_compliant = EthicsAssessment(
    id="https://openminds.ebrains.eu/instances/ethicsAssessment/EUCompliant",
    definition="Data are ethically approved in compliance with EU law. No additional ethics assessment was made by the data sharing initiative.",
    description="Data are ethically approved in compliance with EU law. No additional ethics assessment was made by the data sharing initiative. This is typically true for all, human post-mortem data, human cross-subject statistics, non-primate vertebrate animals as well as cephalopods.",
    name="EU compliant",
)
EthicsAssessment.eu_compliantplus = EthicsAssessment(
    id="https://openminds.ebrains.eu/instances/ethicsAssessment/EUCompliant+",
    definition="Data are ethically approved in compliance with EU law and an additional assessment was made by the data sharing initiative.",
    description="Data are ethically approved in compliance with EU law and an additional assessment was made by the data sharing initiative. This is typically true for all living human single-subject data as well as all non-human primate data.",
    name="EU compliant +",
)
EthicsAssessment.not_required = EthicsAssessment(
    id="https://openminds.ebrains.eu/instances/ethicsAssessment/notRequired",
    definition="An ethics assessment is 'not required' when no ethics approval was needed to conduct the study.",
    description="An ethics assessment is 'not required' when no ethics approval was needed to conduct the study. This is typically true for all simulated and invertebrate data (except cephalopods).",
    name="not required",
)
