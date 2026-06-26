# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.preparation_type import PreparationType


PreparationType.ex_vivo = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/exVivo",
    definition="Something happening or existing outside a living body.",
    name="ex vivo",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739736"),
    synonyms=["ex vivo technique"],
)

PreparationType.in_silico = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inSilico",
    definition="Conducted or produced by means of computer modelling or simulation.",
    name="in silico",
    other_ontology_identifiers=["http://uri.interlex.org/ilx_0494742"],
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0572590"),
)

PreparationType.in_situ = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inSitu",
    definition="Something happening or being examined in the original place instead of being moved to another place",
    name="in situ",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/ilx_0739593"),
    synonyms=["in situ technique"],
)

PreparationType.in_utero = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inUtero",
    definition="Something happening in, within, or while inside the uterus.",
    name="in utero",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/ilx_0739675"),
    synonyms=["in utero technique"],
)

PreparationType.in_vitro = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inVitro",
    definition="Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).",
    name="in vitro",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739568"),
    synonyms=["in vitro technique"],
)

PreparationType.in_vivo = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inVivo",
    definition="Something happening or existing inside a living body.",
    name="in vivo",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739622"),
    synonyms=["in vivo technique"],
)
