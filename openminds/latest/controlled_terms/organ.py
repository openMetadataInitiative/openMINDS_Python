"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Organ(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Organ"
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


Organ.brain = Organ(
    id="https://openminds.ebrains.eu/instances/organ/brain",
    definition="'Brain' is part of the central nervous system.",
    description="The brain is the center of the nervous system in all vertebrate, and most invertebrate, animals. Some primitive animals such as jellyfish and starfish have a decentralized nervous system without a brain, while sponges lack any nervous system at all. In vertebrates, the brain is located in the head, protected by the skull and close to the primary sensory apparatus of vision, hearing, balance, taste, and smell[WP].",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101431",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0000955#brain-1",
    name="brain",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000955",
)
Organ.heart = Organ(
    id="https://openminds.ebrains.eu/instances/organ/heart",
    definition="'Heart' is part of the cardiovascular system",
    description="A myogenic muscular circulatory organ found in the vertebrate cardiovascular system composed of chambers of cardiac muscle. It is the primary circulatory organ.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0732254",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0000948#heart",
    name="heart",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000948",
    synonyms=["chambered heart", "vertebrate heart"],
)
Organ.liver = Organ(
    id="https://openminds.ebrains.eu/instances/organ/liver",
    definition="'Liver' is an organ that is part of the digestive system of vertebrate animals.",
    description="An exocrine gland which secretes bile and functions in metabolism of protein and carbohydrate and fat, synthesizes substances involved in the clotting of the blood, synthesizes vitamin A, detoxifies poisonous substances, stores glycogen, and breaks down worn-out erythrocytes[GO].",
    interlex_identifier="http://uri.interlex.org/base/ilx_0725629",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0002107#liver",
    name="liver",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0002107",
)
Organ.muscle = Organ(
    id="https://openminds.ebrains.eu/instances/organ/muscle",
    definition="'Muscle' is part of the musculoskeletal system.",
    description="Organ consisting of a tissue made up of various elongated cells that are specialized to contract and thus to produce movement and mechanical work.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107218",
    name="muscle",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0001630",
)
Organ.skin = Organ(
    id="https://openminds.ebrains.eu/instances/organ/skin",
    definition="'Skin' is the organ covering the body that consists of the dermis and epidermis.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0727256",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0002097#skin-of-body",
    name="skin",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0002097",
    synonyms=["entire skin", "skin organ"],
)
