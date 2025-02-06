"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MeasuredSignalType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MeasuredSignalType"
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
            description="Longer statement or account giving the characteristics of the measured signal type.",
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
            description="Word or phrase that constitutes the distinctive designation of the measured signal type.",
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


MeasuredSignalType.alpha_activity = MeasuredSignalType(
    id="https://openminds.om-i.org/instances/measuredSignalType/alphaActivity",
    definition="A neural oscillation in the low frequency range (typically between 8-12 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Alpha_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0100494"),
    name="alpha activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0100494"),
    synonyms=["alpha-wave", "alpha wave", "alpha", "alpha oscillation", "alpha rhythm"],
)
MeasuredSignalType.beta_activity = MeasuredSignalType(
    id="https://openminds.om-i.org/instances/measuredSignalType/betaActivity",
    definition="A neural oscillation in the mid frequency range (typically between 12-30 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Beta_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101243"),
    name="beta activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0101243"),
    synonyms=["beta-wave", "beta wave", "beta", "beta oscillation", "beta rhythm"],
)
MeasuredSignalType.gamma_activity = MeasuredSignalType(
    id="https://openminds.om-i.org/instances/measuredSignalType/gammaActivity",
    definition="A neural oscillation in the high frequency range (typically between 30-150 Hz) arising from synchronous and coherent electrical activity in the brain. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Gamma_wave)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0104539"),
    name="gamma activity",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0104539"),
    synonyms=["gamma-wave", "gamma wave", "gamma", "gamma oscillation", "gamma rhythm"],
)
