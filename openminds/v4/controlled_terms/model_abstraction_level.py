"""
Structured information on abstraction level of the computational model.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ModelAbstractionLevel(LinkedMetadata):
    """
    Structured information on abstraction level of the computational model.
    """

    type_ = "https://openminds.om-i.org/types/ModelAbstractionLevel"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
            description="Longer statement or account giving the characteristics of the model abstraction level.",
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
            description="Word or phrase that constitutes the distinctive designation of the model abstraction level.",
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


ModelAbstractionLevel.algorithm = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/algorithm",
    definition="Modelling of a neural structure or process as an algorithm",
    name="algorithm",
)
ModelAbstractionLevel.cognitive_modelling = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/cognitiveModelling",
    definition="Modelling of cognitive processes",
    name="cognitive modelling",
)
ModelAbstractionLevel.population_modelling = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/populationModelling",
    definition="Modelling of neural circuits at the population level",
    name="population modelling",
)
ModelAbstractionLevel.population_modelling_neural_field = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/populationModelling-neuralField",
    definition="Modelling neural populations using the approximation of a neural field",
    name="population modelling: neural field",
)
ModelAbstractionLevel.population_modelling_neural_mass = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/populationModelling-neuralMass",
    definition="Modelling neural populations using the approximation of neural masses",
    name="population modelling: neural mass",
)
ModelAbstractionLevel.protein_structure = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/proteinStructure",
    definition="Modelling of protein structure",
    name="protein structure",
)
ModelAbstractionLevel.rate_neurons = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/rateNeurons",
    definition="Modelling neural networks in which individual neurons are represented by their firing rate",
    name="rate neurons",
)
ModelAbstractionLevel.spiking_neurons = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/spikingNeurons",
    definition="Modelling neural networks in which the action potentials of individual neurons are represented",
    name="spiking neurons",
)
ModelAbstractionLevel.spiking_neurons_biophysical = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/spikingNeurons-biophysical",
    definition="Modelling neural networks in which individual neurons are represented by models with detailed morphology and biophysical models of ion channels",
    name="spiking neurons: biophysical",
)
ModelAbstractionLevel.spiking_neurons_point_neuron = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/spikingNeurons-pointNeuron",
    definition="Modelling neural networks in which individual neurons are represented by point neuron models",
    name="spiking neurons: point neuron",
)
ModelAbstractionLevel.statistical_model = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/statisticalModel",
    definition="Statistical modelling of neural data generation",
    name="statistical model",
)
ModelAbstractionLevel.systems_biology = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/systemsBiology",
    definition="Modelling of neural systems below the level of individual neurons",
    name="systems biology",
)
ModelAbstractionLevel.systems_biology_continuous = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/systemsBiology-continuous",
    definition="Systems biology modelling using concentrations",
    name="systems biology: continuous",
)
ModelAbstractionLevel.systems_biology_discrete = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/systemsBiology-discrete",
    definition="Systems biology modelling using representations of individual particles",
    name="systems biology: discrete",
)
ModelAbstractionLevel.systems_biology_flux_balance = ModelAbstractionLevel(
    id="https://openminds.om-i.org/instances/modelAbstractionLevel/systemsBiology-fluxBalance",
    definition="Systems biology modelling using flux balance analysis",
    name="systems biology: flux balance",
)
