# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.measured_quantity import MeasuredQuantity


MeasuredQuantity.chloride_reversal_potential = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/chlorideReversalPotential",
    definition="The reversal potential for chloride ions.",
    name="chloride reversal potential",
)

MeasuredQuantity.compensation_current = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/compensationCurrent",
    definition="Current injected into a cell to maintain the membrane potential at a target value.",
    name="compensation current",
)

MeasuredQuantity.holding_potential = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/holdingPotential",
    definition="Measured membrane potential during a voltage-clamp protocol.",
    name="holding potential",
    synonyms=["measured holding potential"],
)

MeasuredQuantity.input_resistance = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/inputResistance",
    definition="Total resistance observed by the amplifier during an electrophysiological recording.",
    name="input resistance",
    synonyms=["access resistance"],
)

MeasuredQuantity.liquid_junction_potential = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/liquidJunctionPotential",
    definition="A potential difference that develops when two solutions of electrolytes of different concentrations are in contact with each other.",
    name="liquid junction potential",
)

MeasuredQuantity.membrane_potential = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/membranePotential",
    definition="A quality inhering in a cell's plasma membrane by virtue of the electric potential difference across it.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106774"),
    name="membrane potential",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0106774"),
)

MeasuredQuantity.seal_resistance = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/sealResistance",
    definition="Resistance of the seal between the pipette tip and cell membrane in patch-clamp recording.",
    name="seal resistance",
)

MeasuredQuantity.series_resistance = MeasuredQuantity(
    id="https://openminds.ebrains.eu/instances/measuredQuantity/seriesResistance",
    definition="Resistance of the electrode during an electrophysiological recording.",
    name="series resistance",
    synonyms=["access resistance", "electrode resistance"],
)
