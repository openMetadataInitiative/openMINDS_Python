"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class StimulationTechnique(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/StimulationTechnique"
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
            description="Longer statement or account giving the characteristics of someone or something.",
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
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
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


StimulationTechnique.abstract_image_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/abstractImageVisualStimulation",
    definition="In an 'abstract image visual stimulation' a subject is visually stimulated with a static image that does not show a natural scene but reduced information or forms (e.g., colored symbols or outlines of faces).",
    name="abstract image visual stimulation",
)
StimulationTechnique.checkerboard_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/checkerboardVisualStimulation",
    definition="Stimulation technique that uses a checkerboard as visual stimulus.",
    name="checkerboard visual stimulation",
    synonyms=[
        "checker board stimulation",
        "checker board visual stimulation",
        "checker-board stimulation",
        "checker-board visual stimulation",
    ],
)
StimulationTechnique.current_step_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/currentStepStimulation",
    definition="Current step stimulation is a technique in which an amount of current is applied in predefined steps, whilst measuring changes in neural/muscular activity.",
    name="current step stimulation",
)
StimulationTechnique.drifting_grating_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/driftingGratingVisualStimulation",
    name="drifting grating visual stimulation",
)
StimulationTechnique.electrical_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/electricalStimulation",
    definition="A technique used to elicit a reaction by an electrical stimulus.",
    interlex_identifier="http://uri.interlex.org/ilx_0739699",
    name="electrical stimulation",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/188",
)
StimulationTechnique.figure_ground_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/figure-groundVisualStimulation",
    name="figure-ground visual stimulation",
)
StimulationTechnique.gestalt_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/GestaltVisualStimulation",
    name="Gestalt visual stimulation",
)
StimulationTechnique.microstimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/microstimulation",
    name="microstimulation",
)
StimulationTechnique.natural_image_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/naturalImageVisualStimulation",
    definition="In a 'natural image visual stimulation' a subject is visually stimulated with a static image that shows a natural scene (e.g., landscape or a person).",
    name="natural image visual stimulation",
)
StimulationTechnique.natural_sound_auditory_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/naturalSoundAuditoryStimulation",
    name="natural sound auditory stimulation",
)
StimulationTechnique.optogenetic_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/optogeneticStimulation",
    definition="Using light of a particular wavelength, 'optogenetic stimulation' increases or inhibits the activity of neuron populations that express (typically due to genetic manipulation) light-sensitive ion channels, pumps or enzymes.",
    name="optogenetic stimulation",
)
StimulationTechnique.photon_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/photonStimulation",
    name="photon stimulation",
)
StimulationTechnique.random_dot_motion_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/randomDotMotionStimulation",
    definition="In a 'random dot motion stimulation' a subject is visually stimulated with a video where simulated randomly distributed dot(s) are re-positioned at a new random location with each video frame [[Newsome & Paré, 1988](https://doi.org/10.1523/jneurosci.08-06-02201.1988).",
    name="random dot motion stimulation",
    synonyms=["random dot visual stimulation", "random dot visual stimulation technique"],
)
StimulationTechnique.single_pulse_electrical_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/singlePulseElectricalStimulation",
    definition="A 'single pulse electrical stimulation' is a cortical stimulation technique typically used in the field of epilepsy surgery.",
    name="single pulse electrical stimulation",
    synonyms=["SPES"],
)
StimulationTechnique.static_grating_visual_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/staticGratingVisualStimulation",
    name="static grating visual stimulation",
)
StimulationTechnique.subliminal_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/technique/subliminalStimulation",
    definition="'Subliminal stimulation' is a technique providing any sensory stimuli below an individual's threshold for conscious perception (adapted from [wikipedia](https://en.wikipedia.org/wiki/Subliminal_stimuli))",
    name="subliminal stimulation",
)
StimulationTechnique.subliminal_visual_simulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/technique/subliminalVisualSimulation",
    definition="'Subliminal visual simulation' is a technique providing visual stimuli below an indivdual's threshold for conscious perception [adapted from [wikipedia](https://en.wikipedia.org/wiki/Subliminal_stimuli)]",
    name="subliminal visual simulation",
)
StimulationTechnique.transcranial_magnetic_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/transcranialMagneticStimulation",
    name="transcranial magnetic stimulation",
)
StimulationTechnique.whisker_stimulation = StimulationTechnique(
    id="https://openminds.ebrains.eu/instances/stimulationTechnique/whiskerStimulation",
    definition="'Whisker stimulation' comprises all stimulation techniques in which a single whisker or a group of whiskers is deflected in repeatable manner.",
    name="whisker stimulation",
)
