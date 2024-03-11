"""
Structured information on the life cycle (semantic term) of a specific age group.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class AgeCategory(LinkedMetadata):
    """
    Structured information on the life cycle (semantic term) of a specific age group.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/AgeCategory"
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


AgeCategory.adolescent = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/adolescent",
    definition="'Adolescent' categorizes a transitional life cycle stage of growth and development between childhood and adulthood, often described as 'puberty'.",
    name="adolescent",
    synonyms=["puberty"],
)
AgeCategory.adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/adult",
    definition="'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0729043",
    name="adult",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000113",
    synonyms=["adult stage", "post-juvenile adult", "post-juvenile adult stage"],
)
AgeCategory.embryo = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/embryo",
    definition="'Embryo' categorizes the life cycle stage of an animal or human that starts with fertilitzation and ends with the fully formed embryo.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0735599",
    name="embryo",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000068",
    synonyms=["embryo stage", "embryonic stage"],
)
AgeCategory.infant = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/infant",
    definition="'Infant' categorizes the life cycle stage of mammals (animal or human) that follows the neonate stage and ends at weaning.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0735063",
    name="infant",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0034920",
    synonyms=["infant stage"],
)
AgeCategory.juvenile = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/juvenile",
    definition="'Juvenile' categorizes the life cycle stage of an animal or human that starts with the independence of the nest and/or caregivers and ends with sexual maturity.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0730395",
    name="juvenile",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0034919",
    synonyms=["juvenile stage"],
)
AgeCategory.late_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/lateAdult",
    definition="'Late adult' categorizes the life cycle stage of an animal or human that follows the prime adult stage.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0725713",
    name="late adult",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0007222",
    synonyms=["elderly", "elderly stage", "geriatric", "geriatric stage", "late adult stage"],
)
AgeCategory.neonate = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/neonate",
    definition="'Neonate' categorizes the life cycle stage of an animal or human that immediately follows birth.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0732178",
    name="neonate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0007221",
    synonyms=["neonatal stage", "neonate stage"],
)
AgeCategory.perinatal = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/perinatal",
    definition="'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0724163",
    name="perinatal",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0012101",
    synonyms=["perinatal stage"],
)
AgeCategory.prime_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/primeAdult",
    definition="'Prime adult' categorizes the life cycle stage of an animal or human that starts at the onset of sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0733125",
    name="prime adult",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0018241",
    synonyms=["adulthood stage", "prime adult stage"],
)
AgeCategory.young_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/youngAdult",
    definition="'Young adult' categorizes the early adult stage of an animal or human when sexual maturity has been reached, but not the cessation of growth.",
    name="young adult",
    synonyms=["early adult", "early adult stage", "young adult stage"],
)
