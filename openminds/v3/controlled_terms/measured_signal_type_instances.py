# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.measured_signal_type import MeasuredSignalType


MeasuredSignalType.alpha_activity = MeasuredSignalType(
    id="https://openminds.ebrains.eu/instances/measuredSignalType/alphaActivity",
    definition="A neural oscillation in the low frequency range (typically between 8-12 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Alpha_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0100494"),
    name="alpha activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0100494"),
    synonyms=["alpha-wave", "alpha wave", "alpha", "alpha oscillation", "alpha rhythm"],
)

MeasuredSignalType.beta_activity = MeasuredSignalType(
    id="https://openminds.ebrains.eu/instances/measuredSignalType/betaActivity",
    definition="A neural oscillation in the mid frequency range (typically between 12-30 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Beta_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101243"),
    name="beta activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0101243"),
    synonyms=["beta-wave", "beta wave", "beta", "beta oscillation", "beta rhythm"],
)

MeasuredSignalType.gamma_activity = MeasuredSignalType(
    id="https://openminds.ebrains.eu/instances/measuredSignalType/gammaActivity",
    definition="A neural oscillation in the high frequency range (typically between 30-150 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Gamma_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0104539"),
    name="gamma activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0104539"),
    synonyms=["gamma-wave", "gamma wave", "gamma", "gamma oscillation", "gamma rhythm"],
)
