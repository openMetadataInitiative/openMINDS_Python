"""
Structured information on the scope of the computational model.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ModelScope(LinkedMetadata):
    """
    Structured information on the scope of the computational model.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/ModelScope"
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


ModelScope.network = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/network",
    definition="A model of a neuronal network",
    name="network",
)
ModelScope.network_brain_region = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/network-brainRegion",
    definition="A model of one or more brain regions",
    name="network: brain region",
)
ModelScope.network_microcircuit = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/network-microcircuit",
    definition="A model of a neuronal microcircuit",
    name="network: microcircuit",
)
ModelScope.network_whole_brain = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/network-wholeBrain",
    definition="A model of an entire brain",
    name="network: whole brain",
)
ModelScope.single_cell = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/singleCell",
    definition="A model of a single cell",
    name="single cell",
)
ModelScope.subcellular = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/subcellular",
    definition="A model of an entity or process contained within a cell",
    name="subcellular",
)
ModelScope.subcellular_ion_channel = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/subcellular-ionChannel",
    definition="A model of an ion channel",
    name="subcellular: ion channel",
)
ModelScope.subcellular_molecular = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/subcellular-molecular",
    definition="A model of the structure or behaviour of molecules",
    name="subcellular: molecular",
)
ModelScope.subcellular_signalling = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/subcellular-signalling",
    definition="A model of sub-cellular signalling pathways",
    name="subcellular: signalling",
)
ModelScope.subcellular_spine = ModelScope(
    id="https://openminds.ebrains.eu/instances/modelScope/subcellular-spine",
    definition="A model of a dendritic spine, or of a dendritic region containing several spines",
    name="subcellular: spine",
)
