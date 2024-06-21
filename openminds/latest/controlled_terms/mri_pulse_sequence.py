"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MRIPulseSequence(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/MRIPulseSequence"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the m r i pulse sequence.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the m r i pulse sequence.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


MRIPulseSequence.echo_planar_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/echoPlanarPulseSequence",
    definition="In magnetic resonance imaging, an 'echo-planar pulse sequence' is a contrasting technique where each radio frequency field (RF) excitation is followed by a train of gradient echoes with different spatial encoding allowing for very rapid scanning. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Physics_of_magnetic_resonance_imaging#Echo-planar_imaging)]",
    name="echo planar pulse sequence",
    synonyms=["echo-planar imaging"],
)
MRIPulseSequence.fast_low_angle_shot_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/fastLowAngleShotPulseSequence",
    definition="A gradient echo pulse sequence that combines a low-flip angle radio-frequency excitation of the nuclear magnetic resonance signal (recorded as a spatially encoded gradient echo) with a short repetition time. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Fast_low_angle_shot_magnetic_resonance_imaging)]",
    name="fast low angle shot pulse sequence",
    synonyms=["FLASH", "FLASH pulse sequence"],
)
MRIPulseSequence.fluid_attenuated_inversion_recovery_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/fluidAttenuatedInversionRecoveryPulseSequence",
    definition="A special inversion recovery pulse sequence where the inversion time is adjusted such that at equilibrium there is no net transverse magnetization of fluid in order to null the signal from fluid in the resulting image.",
    name="fluid attenuated inversion recovery pulse sequence",
    synonyms=["FLAIR", "FLAIR pulse sequence"],
)
MRIPulseSequence.gradient_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/gradientEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'gradient-echo pulse sequence' is a contrast generation technique that rapidly induces bulk changes in the spin magnetization of a sample by applying a series of carefully constructed pulses so that the change in the gradient of the magnetic field is maximized, trading contrast for speed (cf. [Hargreaves (2012)](https://doi.org/10.1002/jmri.23742)).",
    name="gradient-echo pulse sequence",
    synonyms=["GRE pulse sequence"],
)
MRIPulseSequence.magnetization_transfer_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/magnetizationTransferPulseSequence",
    definition="A combination of two radiofrequency pulses, the first off-resonance, the second in resonance with the Larmor frequency of free-water protons.",
    name="magnetization transfer pulse sequence",
    synonyms=["MT pulse sequence"],
)
MRIPulseSequence.spin_echo_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/spinEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'spin echo pulse sequence' is a contrast generation technique that induces bulk changes in the spin magnetization of a sample by applying sequential pulses of resonant electromagnetic waves at different angles (cf. [Fonseca (2013)](https://doi.org/10.5772/53693)).",
    name="spin echo pulse sequence",
    synonyms=["SE pulse sequence"],
)
MRIPulseSequence.t1_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/T1PulseSequence",
    definition="In magnetic resonance imaging, a 'T1 pulse sequence' is a contrasting technique that allows the magnetization of the specimen or object to recover (spin-lattice relaxation) before measuring the magnetic resonance signal by changing the repetition time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/MRI_sequence)]",
    name="T1 pulse sequence",
    synonyms=[
        "T1 weighted imaging",
        "T1 weighted magnetic resonance imaging",
        "T1 weighted MRI",
        "T1w imaging",
        "T1w magnetic resonance imaging",
        "T1w MRI",
    ],
)
MRIPulseSequence.t2_pulse_sequence = MRIPulseSequence(
    id="https://openminds.ebrains.eu/instances/MRIPulseSequence/T2PulseSequence",
    definition="In magnetic resonance imaging, a 'T2 pulse sequence' is a contrasting technique that allows the magnetization of the specimen or object to decay (spin-spin relaxation) before measuring the magnetic resonance signal by changing the echo time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/MRI_sequence)]",
    name="T2 pulse sequence",
    synonyms=[
        "T2 weighted imaging",
        "T2 weighted magnetic resonance imaging",
        "T2 weighted MRI",
        "T2w imaging",
        "T2w magnetic resonance imaging",
        "T2w MRI",
    ],
)
