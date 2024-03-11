"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class OrganismSubstance(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/OrganismSubstance"
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


OrganismSubstance.arterial_blood = OrganismSubstance(
    id="https://openminds.ebrains.eu/instances/organismSubstance/arterialBlood",
    definition="'Arterial blood' is the oxygenated portion of blood which occupies the pulmonary vein, the left chambers of the heart, and the arteries of the circulatory system.",
    description="Blood that flows through an artery.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0725460",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0013755#arterial-blood",
    name="arterial blood",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0013755",
    synonyms=["arterial blood", "blood in artery", "portion of arterial blood"],
)
OrganismSubstance.blood = OrganismSubstance(
    id="https://openminds.ebrains.eu/instances/organismSubstance/blood",
    definition="''Blood' is a body fluid in the circulatory system of vertebrates that transports substances to and from cells (e.g. nutrients, oxygen or metabolic waste products). [[adapted from Wikipedia](https://en.wikipedia.org/wiki/Blood)]",
    description="A bodily fluid that is composed of blood plasma and erythrocytes (blood cells).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101354",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0000178#blood",
    name="blood",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000178",
    synonyms=["portion of blood", "vertebrate blood"],
)
OrganismSubstance.venous_blood = OrganismSubstance(
    id="https://openminds.ebrains.eu/instances/organismSubstance/venousBlood",
    definition="'Venous blood' is deoxygenated blood which travels from the peripheral vessels, through the venous system into the right atrium of the heart.",
    description="Blood that flows through a vein.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0734397",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0013756#venous-blood",
    name="venous blood",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0013756",
    synonyms=["blood in vein", "portion of venous blood", "venous blood"],
)
