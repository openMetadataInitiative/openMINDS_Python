"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ChemicalMixtureType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/ChemicalMixtureType"
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


ChemicalMixtureType.colloid = ChemicalMixtureType(
    id="https://openminds.ebrains.eu/instances/chemicalMixtureType/colloid",
    definition="A 'colloid' is a heterogeneous mixture in which one substance consisting of microscopically dispersed insoluble particles is suspended throughout another substance. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Colloid)]",
    description="A colloid is a mixture where very small particles of one substance are evenly distributed throughout another substance. They appear very similar to solutions, but the particles are suspended in the solvent rather than fully dissolved. The difference between a colloid and a suspension is that the particles will not settle to the bottom over a period of time, they will stay suspended or float.",
    name="colloid",
)
ChemicalMixtureType.solution = ChemicalMixtureType(
    id="https://openminds.ebrains.eu/instances/chemicalMixtureType/solution",
    definition="A 'solution' is a special type of homogeneous mixture where at least one substance, called solute, is fully dissolved in another substance, known as a solvent. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Solution_(chemistry))",
    description="A solution is a homogeneous mixture of two or more substances. The particles of solute in a solution cannot be seen by the naked eye. A solution does not cause beams of light to scatter. A solution is stable; solutes will not precipitate unless added in excess of the mixture's solubility, at which point the excess would remain in its solid phase, referred to as hypersaturation. The solute from a solution cannot be separated by filtration (or mechanically). It is composed of only one phase. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Solution_(chemistry))",
    name="solution",
)
ChemicalMixtureType.suspension = ChemicalMixtureType(
    id="https://openminds.ebrains.eu/instances/chemicalMixtureType/suspension",
    definition="A 'suspension' is a heterogeneous mixture of a fluid that contains solid particles sufficiently large for sedimentation and may even be visible to the naked eye. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Suspension_(chemistry))]",
    description="A suspension is a heterogeneous mixture in which the solute particles do not dissolve, but get suspended throughout the bulk of the solvent, left floating around freely in the medium. Solute particles are usually larger than one micrometer, and will eventually settle, although the mixture is only classified as a suspension when and while the particles have not settled out. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Suspension_(chemistry))]",
    name="suspension",
)
