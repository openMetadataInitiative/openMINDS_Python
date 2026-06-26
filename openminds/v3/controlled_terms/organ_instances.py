# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.organ import Organ


Organ.brain = Organ(
    id="https://openminds.ebrains.eu/instances/organ/brain",
    definition="'Brain' is part of the central nervous system.",
    description="The brain is the center of the nervous system in all vertebrate, and most invertebrate, animals. Some primitive animals such as jellyfish and starfish have a decentralized nervous system without a brain, while sponges lack any nervous system at all. In vertebrates, the brain is located in the head, protected by the skull and close to the primary sensory apparatus of vision, hearing, balance, taste, and smell[WP].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101431"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0000955#brain-1"),
    name="brain",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000955"),
)

Organ.heart = Organ(
    id="https://openminds.ebrains.eu/instances/organ/heart",
    definition="'Heart' is part of the cardiovascular system",
    description="A myogenic muscular circulatory organ found in the vertebrate cardiovascular system composed of chambers of cardiac muscle. It is the primary circulatory organ.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0732254"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0000948#heart"),
    name="heart",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000948"),
    synonyms=["chambered heart", "vertebrate heart"],
)

Organ.liver = Organ(
    id="https://openminds.ebrains.eu/instances/organ/liver",
    definition="'Liver' is an organ that is part of the digestive system of vertebrate animals.",
    description="An exocrine gland which secretes bile and functions in metabolism of protein and carbohydrate and fat, synthesizes substances involved in the clotting of the blood, synthesizes vitamin A, detoxifies poisonous substances, stores glycogen, and breaks down worn-out erythrocytes[GO].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0725629"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0002107#liver"),
    name="liver",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002107"),
)

Organ.muscle = Organ(
    id="https://openminds.ebrains.eu/instances/organ/muscle",
    definition="'Muscle' is part of the musculoskeletal system.",
    description="Organ consisting of a tissue made up of various elongated cells that are specialized to contract and thus to produce movement and mechanical work.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107218"),
    name="muscle",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001630"),
)

Organ.skin = Organ(
    id="https://openminds.ebrains.eu/instances/organ/skin",
    definition="'Skin' is the organ covering the body that consists of the dermis and epidermis.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0727256"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0002097#skin-of-body"),
    name="skin",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002097"),
    synonyms=["entire skin", "skin organ"],
)
