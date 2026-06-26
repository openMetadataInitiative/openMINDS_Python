# this file was auto-generated!


from openminds.base import IRI

from openminds.v4.controlled_terms.age_category import AgeCategory


AgeCategory.adolescent = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/adolescent",
    definition="'Adolescent' categorizes a transitional life cycle stage of growth and development between childhood and adulthood, often described as 'puberty'.",
    name="adolescent",
    synonyms=["puberty"],
)

AgeCategory.adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/adult",
    definition="'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0729043"),
    name="adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000113"),
    synonyms=["adult stage", "post-juvenile adult", "post-juvenile adult stage"],
)

AgeCategory.embryo = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/embryo",
    definition="'Embryo' categorizes the life cycle stage of an animal or human that starts with fertilitzation and ends with the fully formed embryo.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0735599"),
    name="embryo",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000068"),
    synonyms=["embryo stage", "embryonic stage"],
)

AgeCategory.infant = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/infant",
    definition="'Infant' categorizes the life cycle stage of mammals (animal or human) that follows the neonate stage and ends at weaning.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0735063"),
    name="infant",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034920"),
    synonyms=["infant stage"],
)

AgeCategory.juvenile = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/juvenile",
    definition="'Juvenile' categorizes the life cycle stage of an animal or human that starts with the independence of the nest and/or caregivers and ends with sexual maturity.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0730395"),
    name="juvenile",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034919"),
    synonyms=["juvenile stage"],
)

AgeCategory.late_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/lateAdult",
    definition="'Late adult' categorizes the life cycle stage of an animal or human that follows the prime adult stage.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0725713"),
    name="late adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007222"),
    synonyms=["elderly", "elderly stage", "geriatric", "geriatric stage", "late adult stage"],
)

AgeCategory.neonate = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/neonate",
    definition="'Neonate' categorizes the life cycle stage of an animal or human that immediately follows birth.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0732178"),
    name="neonate",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007221"),
    synonyms=["neonatal stage", "neonate stage"],
)

AgeCategory.perinatal = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/perinatal",
    definition="'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0724163"),
    name="perinatal",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0012101"),
    synonyms=["perinatal stage"],
)

AgeCategory.prime_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/primeAdult",
    definition="'Prime adult' categorizes the life cycle stage of an animal or human that starts at the onset of sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0733125"),
    name="prime adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0018241"),
    synonyms=["adulthood stage", "prime adult stage"],
)

AgeCategory.young_adult = AgeCategory(
    id="https://openminds.om-i.org/instances/ageCategory/youngAdult",
    definition="'Young adult' categorizes the early adult stage of an animal or human when sexual maturity has been reached, but not the cessation of growth.",
    name="young adult",
    synonyms=["early adult", "early adult stage", "young adult stage"],
)
