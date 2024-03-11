"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class QualitativeOverlap(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/QualitativeOverlap"
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


QualitativeOverlap.is_homologous_to = QualitativeOverlap(
    id="https://openminds.ebrains.eu/instances/qualitativeOverlap/isHomologousTo",
    definition="A set/object (A) has the same relative position, function, or structure as a set/object (B).",
    name="is homologous to",
)
QualitativeOverlap.is_identical_to = QualitativeOverlap(
    id="https://openminds.ebrains.eu/instances/qualitativeOverlap/isIdenticalTo",
    definition="A set/object (A) is identical to another set/object (B) if they look exactly the same.",
    name="is identical to",
)
QualitativeOverlap.is_subset_of = QualitativeOverlap(
    id="https://openminds.ebrains.eu/instances/qualitativeOverlap/isSubsetOf",
    definition="A set/object (A) is a subset of another set/object (B) if (A) and (B) are not equal, but all elements/incidents of (A) are also elements/incidents of (B).",
    name="is subset of",
)
QualitativeOverlap.is_superset_of = QualitativeOverlap(
    id="https://openminds.ebrains.eu/instances/qualitativeOverlap/isSupersetOf",
    definition="A set/object (A) is a superset of another set/object (B) if (A) and (B) are not equal, but all elements/incidents of (B) are also elements/incidents of (A).",
    name="is superset of",
)
QualitativeOverlap.partially_overlaps_with = QualitativeOverlap(
    id="https://openminds.ebrains.eu/instances/qualitativeOverlap/partiallyOverlapsWith",
    definition="Two sets/objects (A and B) partially overlap when some elements/incidents are part of both original objects (A and B).",
    name="partially overlaps with",
)
