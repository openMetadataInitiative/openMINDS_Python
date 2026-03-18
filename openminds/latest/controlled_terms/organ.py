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

    type_ = "https://openminds.om-i.org/types/Organ"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
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
            description="Longer statement or account giving the characteristics of the organ.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the organ.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "other_cross_references",
            str,
            "otherCrossReference",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.",
        ),
        Property(
            "other_ontology_identifiers",
            str,
            "otherOntologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.",
        ),
        Property(
            "preferred_cross_reference",
            IRI,
            "preferredCrossReference",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).",
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
        name=None,
        other_cross_references=None,
        other_ontology_identifiers=None,
        preferred_cross_reference=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            name=name,
            other_cross_references=other_cross_references,
            other_ontology_identifiers=other_ontology_identifiers,
            preferred_cross_reference=preferred_cross_reference,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


Organ.brain = Organ(
    id="https://openminds.om-i.org/instances/organ/brain",
    definition="'Brain' is part of the central nervous system.",
    description="The brain is the center of the nervous system in all vertebrate, and most invertebrate, animals. Some primitive animals such as jellyfish and starfish have a decentralized nervous system without a brain, while sponges lack any nervous system at all. In vertebrates, the brain is located in the head, protected by the skull and close to the primary sensory apparatus of vision, hearing, balance, taste, and smell[WP].",
    name="brain",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0101431"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000955#brain-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000955"),
)
Organ.heart = Organ(
    id="https://openminds.om-i.org/instances/organ/heart",
    definition="'Heart' is part of the cardiovascular system",
    description="A myogenic muscular circulatory organ found in the vertebrate cardiovascular system composed of chambers of cardiac muscle. It is the primary circulatory organ.",
    name="heart",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0732254"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000948#heart"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000948"),
    synonyms=["chambered heart", "vertebrate heart"],
)
Organ.liver = Organ(
    id="https://openminds.om-i.org/instances/organ/liver",
    definition="'Liver' is an organ that is part of the digestive system of vertebrate animals.",
    description="An exocrine gland which secretes bile and functions in metabolism of protein and carbohydrate and fat, synthesizes substances involved in the clotting of the blood, synthesizes vitamin A, detoxifies poisonous substances, stores glycogen, and breaks down worn-out erythrocytes[GO].",
    name="liver",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0725629"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002107#liver"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002107"),
)
Organ.muscle = Organ(
    id="https://openminds.om-i.org/instances/organ/muscle",
    definition="'Muscle' is part of the musculoskeletal system.",
    description="Organ consisting of a tissue made up of various elongated cells that are specialized to contract and thus to produce movement and mechanical work.",
    name="muscle",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0107218"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001630"),
)
Organ.skin = Organ(
    id="https://openminds.om-i.org/instances/organ/skin",
    definition="'Skin' is the organ covering the body that consists of the dermis and epidermis.",
    name="skin",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0727256"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002097#skin-of-body"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002097"),
    synonyms=["entire skin", "skin organ"],
)
