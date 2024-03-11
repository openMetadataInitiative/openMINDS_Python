"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleAttribute(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/TissueSampleAttribute"
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


TissueSampleAttribute.fixated = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/fixated",
    definition="A specimen that was treated with a fixative (e.g., paraformaldehyde) to preserve its existing form and structure.",
    name="fixated",
)
TissueSampleAttribute.free_floating = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/freeFloating",
    definition="A specimen that has been suspended in solution for further handling or experimental steps (e.g., immunohistochemical staining), or temporary storage before further use.",
    name="free floating",
)
TissueSampleAttribute.labeled = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/labeled",
    definition="A specimen that has been modified using chemical or biochemical substances for selective tagging of e.g., molecules or subcellular components, which does not necessarily leads to a visual observable colorization.",
    name="labeled",
)
TissueSampleAttribute.mounted = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/mounted",
    definition="A specimen that has been put ('mounted') on e.g., a glass slide with mounting medium in order to be supported for further handling and/or long term preservation.",
    name="mounted",
)
TissueSampleAttribute.stained = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/stained",
    definition="A specimen that has been dyed using chemical or biochemical substances for general colorization of e.g., molecules or subcellular components, that can be visualized under the right light exposure.",
    name="stained",
)
TissueSampleAttribute.unstained = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/unstained",
    definition="A specimen that was not artificially modified in colorization using chemical or biochemical substances.",
    name="unstained",
)
TissueSampleAttribute.untreated = TissueSampleAttribute(
    id="https://openminds.ebrains.eu/instances/tissueSampleAttribute/untreated",
    definition="A specimen that has not been modified or treated (e.g., with chemicals) compared to its natural state.",
    name="untreated",
)
