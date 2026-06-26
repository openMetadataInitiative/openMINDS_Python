# this file was auto-generated!


from openminds.latest.controlled_terms.mri_pulse_sequence import MRIPulseSequence


MRIPulseSequence.echo_planar_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/echoPlanarPulseSequence",
    definition="In magnetic resonance imaging, an 'echo-planar pulse sequence' is a contrasting technique where each radio frequency field (RF) excitation is followed by a train of gradient echoes with different spatial encoding allowing for very rapid scanning. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Physics_of_magnetic_resonance_imaging#Echo-planar_imaging)]",
    name="echo planar pulse sequence",
    synonyms=["echo-planar imaging"],
)

MRIPulseSequence.fast_low_angle_shot_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/fastLowAngleShotPulseSequence",
    definition="A gradient echo pulse sequence that combines a low-flip angle radio-frequency excitation of the nuclear magnetic resonance signal (recorded as a spatially encoded gradient echo) with a short repetition time. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Fast_low_angle_shot_magnetic_resonance_imaging)]",
    name="fast low angle shot pulse sequence",
    synonyms=["FLASH", "FLASH pulse sequence"],
)

MRIPulseSequence.fluid_attenuated_inversion_recovery_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/fluidAttenuatedInversionRecoveryPulseSequence",
    definition="A special inversion recovery pulse sequence where the inversion time is adjusted such that at equilibrium there is no net transverse magnetization of fluid in order to null the signal from fluid in the resulting image.",
    name="fluid attenuated inversion recovery pulse sequence",
    synonyms=["FLAIR", "FLAIR pulse sequence"],
)

MRIPulseSequence.gradient_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/gradientEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'gradient-echo pulse sequence' is a contrast generation technique that rapidly induces bulk changes in the spin magnetization of a sample by applying a series of carefully constructed pulses so that the change in the gradient of the magnetic field is maximized, trading contrast for speed (cf. [Hargreaves (2012)](https://doi.org/10.1002/jmri.23742)).",
    name="gradient-echo pulse sequence",
    synonyms=["GRE pulse sequence"],
)

MRIPulseSequence.magnetization_transfer_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/magnetizationTransferPulseSequence",
    definition="A combination of two radiofrequency pulses, the first off-resonance, the second in resonance with the Larmor frequency of free-water protons.",
    name="magnetization transfer pulse sequence",
    synonyms=["MT pulse sequence"],
)

MRIPulseSequence.spin_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.om-i.org/instances/MRIPulseSequence/spinEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'spin echo pulse sequence' is a contrast generation technique that induces bulk changes in the spin magnetization of a sample by applying sequential pulses of resonant electromagnetic waves at different angles (cf. [Fonseca (2013)](https://doi.org/10.5772/53693)).",
    name="spin echo pulse sequence",
    synonyms=["SE pulse sequence"],
)
