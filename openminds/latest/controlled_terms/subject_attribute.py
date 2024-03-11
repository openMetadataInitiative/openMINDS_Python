"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubjectAttribute(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/SubjectAttribute"
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


SubjectAttribute.alert = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/alert",
    definition="A temporary state of an organism in which it can quickly perceive and act.",
    name="alert",
)
SubjectAttribute.alive = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/alive",
    definition="An organism that is not dead.",
    name="alive",
)
SubjectAttribute.anaesthetized = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/anaesthetized",
    definition="A temporary state of an organism induced by anaestetic substances that cause the reduction or loss of pain sensation with or without loss of consciousness.",
    name="anaesthetized",
)
SubjectAttribute.asleep = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/asleep",
    definition="A periodic, readily reversible state of an organism with reduced awareness and typically lower metabolic activity.",
    name="asleep",
)
SubjectAttribute.awake = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/awake",
    definition="A temporary state of an organism in which it is fully alert and aware.",
    name="awake",
)
SubjectAttribute.comatose = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/comatose",
    definition="A deep state of prolonged unconsciousness in which the organism cannot be awakened (temporarily or terminally), is unresponsive and typically displays depressed cerebral activity.",
    name="comatose",
)
SubjectAttribute.control = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/control",
    definition="An organism that is part of a study and does not receive the treatment being tested.",
    name="control",
)
SubjectAttribute.deceased = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/deceased",
    definition="An organism that is no longer living.",
    name="deceased",
    synonyms=["dead"],
)
SubjectAttribute.drugged = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/drugged",
    definition="A temporary state of an organism in which it is under the influence of a sedative, narcotic or any other typye of drug.",
    name="drugged",
    synonyms=["dosed", "drug treated"],
)
SubjectAttribute.freely_moving = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/freelyMoving",
    definition="An organism that can move easily, without any obstacles or resistance.",
    name="freely moving",
)
SubjectAttribute.has_implanted_device = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/hasImplantedDevice",
    definition="A typically chronic state of an organism after surgical implantation of a device (e.g., an electrode, a pacemaker) to measure or stimulate bodily functions.",
    name="has implanted device",
)
SubjectAttribute.has_inserted_device = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/hasInsertedDevice",
    definition="A typically temporary state of an organism during which a device (e.g., an electrode) is inserted to measure or stimulate bodily functions.",
    name="has inserted device",
)
SubjectAttribute.head_restrained = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/headRestrained",
    definition="An organism that has been restrained on the head causing e.g., decreased motion range and/or increased resistance in movement.",
    name="head restrained",
)
SubjectAttribute.knockin = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/knockin",
    definition="An organism that underwent a targeted insertation of foreign genetic material in the existing genetic material (i.e. a gene).",
    name="knockin",
)
SubjectAttribute.knockout = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/knockout",
    definition="An organism that underwent a targeted excision or silencing/inactivation of existing genetic material (i.e. a gene).",
    name="knockout",
)
SubjectAttribute.postoperative = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/postoperative",
    definition="A temporary state of an organism in the time period that immediately follows a surgical procedure.",
    name="postoperative",
)
SubjectAttribute.preoperative = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/preoperative",
    definition="A temporary state of an organism in the time period between the decision to have surgery and the beginning of the surgical procedure.",
    name="preoperative",
)
SubjectAttribute.restrained = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/restrained",
    definition="An organism that has been restrained in any way causing e.g., decreased motion range and/or increased resistance in movement.",
    name="restrained",
)
SubjectAttribute.treated = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/treated",
    definition="A subject that is in a permanently or temporarily altered state compared to its natural state following some kind of treatment.",
    name="treated",
)
SubjectAttribute.untreated = SubjectAttribute(
    id="https://openminds.ebrains.eu/instances/subjectAttribute/untreated",
    definition="A subject in its natural state which has not been exposed to any kind of state-altering treatment.",
    name="untreated",
)
