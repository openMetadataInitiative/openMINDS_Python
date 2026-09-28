# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.mri_pulse_sequence import MRIPulseSequence


MRIPulseSequence.echo_planar_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/echoPlanarPulseSequence",
    definition="A magnetic resonance image pulse sequence that is composed of multiple echoes at different phase steps (often collected blocks of 64 or 128 phase steps), which are acquired using rephasing gradients where rephasing is achieved by rapidly reversing the readout or frequency-encoding gradient.",
    name="echo planar pulse sequence",
    synonyms=["echo-planar imaging"],
)

MRIPulseSequence.fast_low_angle_shot_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/fastLowAngleShotPulseSequence",
    definition="A gradient echo pulse sequence that combines a low-flip angle radio-frequency excitation of the nuclear magnetic resonance signal (recorded as a spatially encoded gradient echo) with a short repetition time. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Fast_low_angle_shot_magnetic_resonance_imaging)]",
    name="fast low angle shot pulse sequence",
    synonyms=["FLASH", "FLASH pulse sequence"],
)

MRIPulseSequence.fast_spin_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/fastSpinEchoPulseSequence",
    definition="A magnetic resonance image pulse sequence that collects multiple echos instead of a single echo during a spin echo pulse sequence, multiple echos are recorded for each 90-degree pulse by using multiple 180-degree inversion pulses with slightly different phase encoding gradients.",
    name="fast spin echo pulse sequence",
    synonyms=[
        "turbo spin echo",
        "TSE",
        "FSE",
        "fast spin-echo imaging",
        "FSE pulse sequence",
        "FSE imaging",
        "TSE pulse sequence",
        "TSE imaging",
        "turbo spin-echo imaging",
    ],
)

MRIPulseSequence.fluid_attenuated_inversion_recovery_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/fluidAttenuatedInversionRecoveryPulseSequence",
    definition="A special inversion recovery pulse sequence where the inversion time is adjusted such that at equilibrium there is no net transverse magnetization of fluid in order to null the signal from fluid in the resulting image.",
    name="fluid attenuated inversion recovery pulse sequence",
    synonyms=["FLAIR", "FLAIR pulse sequence"],
)

MRIPulseSequence.gradient_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/gradientEchoPulseSequence",
    definition="A magnetic resonance imaging pulse sequence composed of one or more radio frequency pulses that are usually less than 90 degrees interleaved with the application of a spatial magnetic field gradient.",
    name="gradient-echo pulse sequence",
    synonyms=["GRE pulse sequence"],
)

MRIPulseSequence.inversion_recovery_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/inversionRecoveryPulseSequence",
    definition="A magnetic resonance imaging pulse sequence composed of a 180-degree radiofrequency pulse, followed by a spin echo pulse sequence.",
    name="inversion recovery pulse sequence",
)

MRIPulseSequence.magnetization_transfer_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/magnetizationTransferPulseSequence",
    definition="A combination of two radiofrequency pulses, the first off-resonance, the second in resonance with the Larmor frequency of free-water protons.",
    name="magnetization transfer pulse sequence",
    synonyms=["MT pulse sequence"],
)

MRIPulseSequence.multi_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/multi-echoPulseSequence",
    definition="A magnetic resonance imaging pulse sequence composed of multiple gradient reversals following a single radiofrequency pulse.",
    name="multi-echo pulse sequence",
)

MRIPulseSequence.saturation_recovery_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/saturationRecoveryPulseSequence",
    definition="A magnetic resonance imaging pulse sequence composed of multiple slice selective 90-degree radiofrequency pulses at regular intervals delayed to allow the recovery of all the longitudinal magnetization before another pulse is applied.",
    name="saturation recovery pulse sequence",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0110354"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0110354"),
    synonyms=["SR pulse sequence"],
)

MRIPulseSequence.spin_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/spinEchoPulseSequence",
    definition="A magnetic resonance imaging pulse sequence composed of a slice selective 90-degree pulse followed by one or more (for fast spin echo sequences) 180-degree refocusing pulses.",
    name="spin echo pulse sequence",
    synonyms=["SE pulse sequence"],
)

MRIPulseSequence.t2_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/T2PulseSequence",
    definition="A magnetic resonance imaging pulse sequence that is optimized to measure the spin-spin relaxation time (T2).",
    name="T2 pulse sequence",
)

MRIPulseSequence.t2_star_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/T2-starPulseSequence",
    definition="A magnetic resonance imaging pulse sequence that is optimized to measure the effective spin-spin relaxation time (T2-star).",
    name="T2-star pulse sequence",
    synonyms=["T2* pulse sequence"],
)
