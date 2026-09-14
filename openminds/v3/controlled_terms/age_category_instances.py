# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.age_category import AgeCategory


AgeCategory.adolescent = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/adolescent",
    definition="Life cycle stage of a subject loosely defined by the transitional growth and development between childhood and adulthood, often described as 'puberty'.",
    name="adolescent",
    synonyms=["puberty"],
)

AgeCategory.adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/adult",
    definition="Life cycle stage of a subject that starts with sexual maturity and ends with death.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0729043"),
    name="adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000113"),
    synonyms=["adult stage", "post-juvenile adult", "post-juvenile adult stage"],
)

AgeCategory.embryo = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/embryo",
    definition="Life cycle stage of a subject that starts with fertilization and ends with the fully formed embryo.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0735599"),
    name="embryo",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000068"),
    synonyms=["embryo stage", "embryonic stage"],
)

AgeCategory.infant = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/infant",
    definition="Life cycle stage of a mammalian subject that follows the neonate stage and ends at weaning.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0735063"),
    name="infant",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034920"),
    synonyms=["infant stage"],
)

AgeCategory.juvenile = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/juvenile",
    definition="Life cycle stage of a subject that starts with the independence of the nest and/or caregiver and ends with sexual maturity.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0730395"),
    name="juvenile",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0034919"),
    synonyms=["juvenile stage"],
)

AgeCategory.late_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/lateAdult",
    definition="Life cycle stage of a subject that follows the prime adult stage and ends with death.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0725713"),
    name="late adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007222"),
    synonyms=["elderly", "elderly stage", "geriatric", "geriatric stage", "late adult stage"],
)

AgeCategory.neonate = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/neonate",
    definition="Life cycle stage of a subject that immediately follows birth.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0732178"),
    name="neonate",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007221"),
    synonyms=["neonatal stage", "neonate stage"],
)

AgeCategory.perinatal = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/perinatal",
    definition="'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0724163"),
    name="perinatal",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0012101"),
    synonyms=["perinatal stage"],
)

AgeCategory.prime_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/primeAdult",
    definition="Life cycle stage of a subject that starts with sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0733125"),
    name="prime adult",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0018241"),
    synonyms=["adulthood stage", "prime adult stage"],
)

AgeCategory.young_adult = AgeCategory(
    id="https://openminds.ebrains.eu/instances/ageCategory/youngAdult",
    definition="Life cycle stage of a subject that starts with sexual maturity and ends with the cessation of growth (if reached after sexual maturity).",
    name="young adult",
    synonyms=["early adult", "early adult stage", "young adult stage"],
)
