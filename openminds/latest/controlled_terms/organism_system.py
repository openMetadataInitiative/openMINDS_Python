"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class OrganismSystem(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/OrganismSystem"
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


OrganismSystem.cardiovascular_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/cardiovascularSystem",
    definition="'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101670",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0004535#cardiovascular-system",
    name="cardiovascular system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0004535",
)
OrganismSystem.central_nervous_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/centralNervousSystem",
    definition="The 'central nervous system' is the main processing center in most organisms. Its function is to take in sensory information, process information, and send out motor signals.",
    description="In vertebrates, the central nervous system (CNS) consists of the brain and the spinal cord. In invertebrates, it includes the central ganglia and the nerve cord.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101901",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0001017#central-nervous-system-1",
    name="central nervous system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0001017",
    synonyms=["systema nervosum centrale", "CNS"],
)
OrganismSystem.cholinergic_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/cholinergicSystem",
    definition="The cholinergic system is composed of any molecule, protein, cell, tissue or organ that is related to acetylcholine.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0102133",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0025595#cholinergic-system-1",
    name="cholinergic system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0002204http://purl.obolibrary.org/obo/UBERON_0025595",
    synonyms=["acetylcholine system", "ach system", "ACh system"],
)
OrganismSystem.digestive_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/digestiveSystem",
    definition="The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0729362",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0001007#digestive-system",
    name="digestive system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0001007",
)
OrganismSystem.gabaergic_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/gabaergicSystem",
    definition="The gabaergic system is composed of any molecule, protein, cell, tissue or organ that is related to GABA.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104506",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXANAT:1005024#gabaergic-system",
    name="gabaergic system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0025591",
    synonyms=["GABAergic system"],
)
OrganismSystem.glutamatergic_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/glutamatergicSystem",
    definition="The glutamatergic system is composed of any molecule, protein, cell, tissue or organ that is related to glutamate (when in the role of a neurotransmitter).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104682",
    name="glutamatergic system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0025592",
)
OrganismSystem.musculoskeletal_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/musculoskeletalSystem",
    definition="The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.",
    description="The musculoskeletal system (sometimes also called locomotor system) is subdivided into two broader systems, the skeletal system and the muscular system. The skeletal system includes bones and joints. The muscular system includes all muscles in the body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0728294",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0002204#musculoskeletal-system",
    name="musculoskeletal system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0002204",
    synonyms=["musculo-skeletal system"],
)
OrganismSystem.noradrenergic_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/noradrenergicSystem",
    definition="The noradrenergic system is composed of any molecule, protein, cell, tissue or organ that is related to norepinephrine (also known as noradrenaline).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107679",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXANAT:1005027#noradrenergic-system",
    name="noradrenergic system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0027225",
)
OrganismSystem.serotonergic_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/serotonergicSystem",
    definition="The serotonergic system is composed of any molecule, protein, cell, tissue or organ that is related to serotonin.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0110555",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0025593#serotonergic-system-1",
    name="serotonergic system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0025593",
    synonyms=["serotonin system", "5HT system", "5-HT system", "5-ht system", "5ht system"],
)
OrganismSystem.vascular_system = OrganismSystem(
    id="https://openminds.ebrains.eu/instances/organismSystem/vascularSystem",
    definition="The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0726589",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0007798#vascular-system",
    name="vascular system",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0007798",
)
