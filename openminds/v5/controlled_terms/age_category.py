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

    type_ = "https://openminds.om-i.org/types/AgeCategory"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

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
            description="Longer statement or account giving the characteristics of the age category.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the age category.",
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


AgeCategory.adolescent = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/adolescent",
    definition="'Adolescent' categorizes a transitional life cycle stage of growth and development between childhood and adulthood, often described as 'puberty'.",
    name="adolescent",
    synonyms=["puberty"],
)
AgeCategory.adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/adult",
    definition="'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity.",
    name="adult",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0729043"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000113"),
    synonyms=["adult stage", "post-juvenile adult", "post-juvenile adult stage"],
)
AgeCategory.embryo = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/embryo",
    definition="'Embryo' categorizes the life cycle stage of an animal or human that starts with fertilitzation and ends with the fully formed embryo.",
    name="embryo",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0735599"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000068"),
    synonyms=["embryo stage", "embryonic stage"],
)
AgeCategory.infant = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/infant",
    definition="'Infant' categorizes the life cycle stage of mammals (animal or human) that follows the neonate stage and ends at weaning.",
    name="infant",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0735063"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034920"),
    synonyms=["infant stage"],
)
AgeCategory.juvenile = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/juvenile",
    definition="'Juvenile' categorizes the life cycle stage of an animal or human that starts with the independence of the nest and/or caregivers and ends with sexual maturity.",
    name="juvenile",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0730395"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034919"),
    synonyms=["juvenile stage"],
)
AgeCategory.late_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/lateAdult",
    definition="'Late adult' categorizes the life cycle stage of an animal or human that follows the prime adult stage.",
    name="late adult",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0725713"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007222"),
    synonyms=["elderly", "elderly stage", "geriatric", "geriatric stage", "late adult stage"],
)
AgeCategory.neonate = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/neonate",
    definition="'Neonate' categorizes the life cycle stage of an animal or human that immediately follows birth.",
    name="neonate",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0732178"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007221"),
    synonyms=["neonatal stage", "neonate stage"],
)
AgeCategory.perinatal = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/perinatal",
    definition="'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.",
    name="perinatal",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0724163"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0012101"),
    synonyms=["perinatal stage"],
)
AgeCategory.prime_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/primeAdult",
    definition="'Prime adult' categorizes the life cycle stage of an animal or human that starts at the onset of sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.",
    name="prime adult",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0733125"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0018241"),
    synonyms=["adulthood stage", "prime adult stage"],
)
AgeCategory.young_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/youngAdult",
    definition="'Young adult' categorizes the early adult stage of an animal or human when sexual maturity has been reached, but not the cessation of growth.",
    name="young adult",
    synonyms=["early adult", "early adult stage", "young adult stage"],
)
