# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.tissue_sample_type import TissueSampleType


TissueSampleType.biopsy_sample = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/biopsySample",
    definition="Typically very small sample of tissue that was excised from a living or deceased multicellular organism body.",
    name="biopsy sample",
    other_ontology_identifiers=["http://uri.interlex.org/ilx_0782394"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_0002650"),
)

TissueSampleType.fluid_specimen = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/fluidSpecimen",
    definition="A fluid sample either taken directly from a living or deceased multicellular organism body (i.e. body fluids) or produced in a laboratory.",
    name="fluid specimen",
)

TissueSampleType.hemisphere = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/hemisphere",
    definition="One of the symmetric halves excised from a bilateral organ tissue sample (e.g., a brain) from a living or deceased multicellular organism body.",
    name="hemisphere",
)

TissueSampleType.heterogeneous_cell_population = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/heterogeneousCellPopulation",
    definition="A sample of multiple cells/a population of cells that are of two or more different cell types.",
    name="heterogeneous cell population",
)

TissueSampleType.homogeneous_cell_population = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/homogeneousCellPopulation",
    definition="A sample of multiple cells/a population of cells that are of the same cell type.",
    name="homogeneous cell population",
)

TissueSampleType.nerve = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/nerve",
    definition="A nerve sample (i.e. a whole nerve or a part of a nerve) from a living or deceased multicellular organism body.",
    name="nerve",
)

TissueSampleType.single_cell = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/singleCell",
    definition="A single cell sample from a living or deceased multicellular organism body.",
    name="single cell",
)

TissueSampleType.tissue_block = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/tissueBlock",
    definition="A cube-like sample of tissue that was excised from a larger tissue sample (e.g., a whole organ) from a living or deceased multicellular organism body.",
    name="tissue block",
)

TissueSampleType.tissue_slice = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/tissueSlice",
    definition="A thin and often flat sample of tissue that was excised from a larger tissue sample (e.g., a tissue block or a whole organ) from a living or deceased multicellular organism body.",
    name="tissue slice",
)

TissueSampleType.whole_organ = TissueSampleType(
    id="https://openminds.om-i.org/instances/tissueSampleType/wholeOrgan",
    definition="A whole organ sample from a living or deceased multicellular organism body.",
    name="whole organ",
)
