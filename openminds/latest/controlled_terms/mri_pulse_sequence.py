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

    type_ = "https://openminds.om-i.org/types/MRIPulseSequence"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
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
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


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
