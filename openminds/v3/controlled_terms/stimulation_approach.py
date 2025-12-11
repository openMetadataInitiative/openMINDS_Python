"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class StimulationApproach(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/StimulationApproach"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

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
            description="Longer statement or account giving the characteristics of the stimulation approach.",
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
            description="Word or phrase that constitutes the distinctive designation of the stimulation approach.",
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


StimulationApproach.auditory_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/auditoryStimulation",
    definition="A stimulation of the auditory (hearing) system.",
    description="The sensory modality that pertains to the sense of hearing. It usually arises from an audible stimulation of the auditory (hearing) system, such as from a sound.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0101001"),
    name="auditory stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00125"),
    synonyms=["auditory modality", "auditory stimulus"],
)
StimulationApproach.gustatory_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/gustatoryStimulation",
    definition="A stimulation of the gustatory (taste and flavor perception) system.",
    description="The sensory modality that pertains to the sense of taste or flavor. It usually but not always arises through stimulation of the gustatory system (e.g., tastebuds, nasal receptors).",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0104834"),
    name="gustatory stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00123"),
    synonyms=["gustatory modality", "gustatory stimulus"],
)
StimulationApproach.interoceptive_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/interoceptiveStimulation",
    definition="A stimulation that arises from inside an organism.",
    description="The sensory modality that pertains to the sense of interoception, or internal sensations.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0105596"),
    name="interoceptive stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00128"),
    synonyms=["interoceptive modality", "interoceptive stimulus"],
)
StimulationApproach.olfactory_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/olfactoryStimulation",
    definition="A stimulation of the olfactory (smelling) system.",
    description="The sensory modality that pertains to the sense of smelling. It usually but not always arises from the stimulation of the olfactory system by chemicals.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107962"),
    name="olfactory stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00130"),
    synonyms=["olfactory modality", "olfactory stimulus"],
)
StimulationApproach.tactile_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/tactileStimulation",
    definition="A stimulation of the tactile (touch) system.",
    description="The sensory modality that pertains to the sense of touch or contact via the skin. It usually but not always arises from a tactile stimulation via contact of the skin to other external objects.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0111485"),
    name="tactile stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00131"),
    synonyms=["tactile modality", "tactile stimulus"],
)
StimulationApproach.visual_stimulation = StimulationApproach(
    id="https://openminds.ebrains.eu/instances/stimulationApproach/visualStimulation",
    definition="A stimulation of the visual (sight) system.",
    description="The sensory modality that pertains to the sense of sight. It usually but not always arises from the stimulation of the visual system with a light source of sufficient brightness to be visible.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0112525"),
    name="visual stimulation",
    preferred_ontology_identifier=IRI("http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00132"),
    synonyms=["visual modality", "visual stimulus"],
)
