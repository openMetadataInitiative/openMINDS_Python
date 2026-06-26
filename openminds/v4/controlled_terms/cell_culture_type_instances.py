# this file was auto-generated!


from openminds.base import IRI

from openminds.v4.controlled_terms.cell_culture_type import CellCultureType


CellCultureType.primary = CellCultureType(
    id="https://openminds.om-i.org/instances/cellCultureType/primary",
    definition="A cell culture comprised of primary cultured cells and the media in which they are being actively propagated or quiescently stored.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0490188"),
    name="primary cell culture",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0452904"),
)

CellCultureType.secondary = CellCultureType(
    id="https://openminds.om-i.org/instances/cellCultureType/secondary",
    definition="A cultured cell population that is derived through one or more passages in culture.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0782434"),
    name="secondary cell culture",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_0001905"),
)
