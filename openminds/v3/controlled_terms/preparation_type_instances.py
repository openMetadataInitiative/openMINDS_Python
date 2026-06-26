# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.preparation_type import PreparationType


PreparationType.ex_vivo = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/exVivo",
    definition="Something happening or existing outside a living body.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739736"),
    name="ex vivo",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88"),
    synonyms=["ex vivo technique"],
)

PreparationType.in_silico = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inSilico",
    definition="Conducted or produced by means of computer modelling or simulation.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0494742"),
    name="in silico",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0572590"),
)

PreparationType.in_situ = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inSitu",
    definition="Something happening or being examined in the original place instead of being moved to another place",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739593"),
    name="in situ",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu"),
    synonyms=["in situ technique"],
)

PreparationType.in_utero = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inUtero",
    definition="Something happening in, within, or while inside the uterus.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739675"),
    name="in utero",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90"),
    synonyms=["in utero technique"],
)

PreparationType.in_vitro = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inVitro",
    definition="Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739568"),
    name="in vitro",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro"),
    synonyms=["in vitro technique"],
)

PreparationType.in_vivo = PreparationType(
    id="https://openminds.ebrains.eu/instances/preparationType/inVivo",
    definition="Something happening or existing inside a living body.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739622"),
    name="in vivo",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89"),
    synonyms=["in vivo technique"],
)
