"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PreparationType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/PreparationType"
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


PreparationType.ex_vivo = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/exVivo",
    definition="Something happening or existing outside a living body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739736",
    name="ex vivo",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88",
    synonyms=["ex vivo technique"],
)
PreparationType.in_silico = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inSilico",
    definition="Conducted or produced by means of computer modelling or simulation.",
    interlex_identifier="http://uri.interlex.org/ilx_0494742",
    name="in silico",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0572590",
)
PreparationType.in_situ = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inSitu",
    definition="Something happening or being examined in the original place instead of being moved to another place",
    interlex_identifier="http://uri.interlex.org/ilx_0739593",
    name="in situ",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu",
    synonyms=["in situ technique"],
)
PreparationType.in_utero = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inUtero",
    definition="Something happening in, within, or while inside the uterus.",
    interlex_identifier="http://uri.interlex.org/ilx_0739675",
    name="in utero",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90",
    synonyms=["in utero technique"],
)
PreparationType.in_vitro = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inVitro",
    definition="Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739568",
    name="in vitro",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro",
    synonyms=["in vitro technique"],
)
PreparationType.in_vivo = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inVivo",
    definition="Something happening or existing inside a living body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739622",
    name="in vivo",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89",
    synonyms=["in vivo technique"],
)
