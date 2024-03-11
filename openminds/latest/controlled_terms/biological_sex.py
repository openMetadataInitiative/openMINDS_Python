"""
Structured information on the biological sex of a subject.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BiologicalSex(LinkedMetadata):
    """
    Structured information on the biological sex of a subject.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/BiologicalSex"
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


BiologicalSex.female = BiologicalSex(
    id="https://openminds.ebrains.eu/instances/biologicalSex/female",
    definition="Biological sex that produces egg cells (ova).",
    description="A female organism typically has the capacity to produce relatively large, usually immobile gametes (reproductive cells), called egg cells (or ova). In the process of fertilization, an egg cell (ovum) fuses with a smaller, usually mobile male gametes, called sperm cells (or spermatozoa).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104150",
    name="female",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PATO_0000383",
)
BiologicalSex.hermaphrodite = BiologicalSex(
    id="https://openminds.ebrains.eu/instances/biologicalSex/hermaphrodite",
    definition="Biological sex with both male and female reproductive organs.",
    description="A hermaphrodite is an animal or plant that can produce gametes (reproductive cells) of both, male and female sexes. In sexually dimorphic organisms, hermaphroditism may occur because of variations in the genetic code. The term *hermaphrodite* is considered to be misleading, stigmatizing, and scientifically specious in reference to humans. For this reason, in humans the term *intersex* is typically used.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104963",
    name="hermaphrodite",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PATO_0001340",
    synonyms=["intersex"],
)
BiologicalSex.male = BiologicalSex(
    id="https://openminds.ebrains.eu/instances/biologicalSex/male",
    definition="Biological sex that produces sperm cells (spermatozoa).",
    description="A male organism typically has the capacity to produce relatively small, usually mobile gametes (reproductive cells), called sperm cells (or spermatozoa). In the process of fertilization, these sperm cells fuse with a larger, usually immobile female gamete, called egg cell (or ovum).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106489",
    name="male",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PATO_0000384",
)
BiologicalSex.not_detectable = BiologicalSex(
    id="https://openminds.ebrains.eu/instances/biologicalSex/notDetectable",
    definition="Can be stated if the biological sex in visually not detectable at a specific point in time.",
    name="not detectable",
)
