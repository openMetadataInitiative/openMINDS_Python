"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SignalDirectionality(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SignalDirectionality"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
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
            description="Longer statement or account giving the characteristics of the signal directionality.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the signal directionality.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "other_cross_references",
            str,
            "otherCrossReference",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.",
        ),
        Property(
            "other_ontology_identifiers",
            str,
            "otherOntologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.",
        ),
        Property(
            "preferred_cross_reference",
            IRI,
            "preferredCrossReference",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).",
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
        name=None,
        other_cross_references=None,
        other_ontology_identifiers=None,
        preferred_cross_reference=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            name=name,
            other_cross_references=other_cross_references,
            other_ontology_identifiers=other_ontology_identifiers,
            preferred_cross_reference=preferred_cross_reference,
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
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


SignalDirectionality.signal_receiving = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-receiving",
    definition="A signal directionality mode in which a device detects and acquires incoming signals from an external source or medium.",
    description="In signal-receiving mode, the device operates as a passive or semi-passive sensor of external signals. It converts physical signal energy into measurable electrical or digital representations. Sensitivity and noise characteristics determine reception performance. Received signals are commonly amplified, filtered, and digitized for analysis. This mode is used in monitoring, imaging, and data acquisition systems.",
    name="signal-receiving",
    synonyms=["receiving", "receive-only"],
)
SignalDirectionality.signal_transceiving = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-transceiving",
    definition="A signal directionality mode in which a device both emits and detects signals within the same system or operational context.",
    description="In signal-transceiving mode, the device integrates transmitting and receiving functions. It alternates between emission and detection or performs both simultaneously depending on system design. Switching and isolation mechanisms are used to prevent self-interference. Operational timing is coordinated to manage bidirectional signal flow. This mode is common in imaging, communication, and active sensing technologies.",
    name="signal-transceiving",
    synonyms=["transceiving", "transmit–receive", "transmitting–receiving"],
)
SignalDirectionality.signal_transmitting = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-transmitting",
    definition="A signal directionality mode in which a device generates and emits signals toward an external system, medium, or target.",
    description="In signal-transmitting mode, the device functions as an active source of signal energy or information. It produces controlled waveforms or data streams for delivery to another system or environment. The emitted signal may be electromagnetic, electrical, acoustic, or optical in nature. Transmission parameters such as power, timing, and modulation are typically configurable. This mode is used in applications including stimulation, communication, and active sensing.",
    name="signal-transmitting",
    synonyms=["transmitting", "transmit-only"],
)
