"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DependencyImpact(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/DependencyImpact"
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
            description="Longer statement or account giving the characteristics of the dependency impact.",
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
            description="Word or phrase that constitutes the distinctive designation of the dependency impact.",
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


DependencyImpact.complete_outage = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/completeOutage",
    definition="A thing becomes entirely nonfunctional if the thing it depends on is unavailable.",
    name="complete outage",
)
DependencyImpact.critical_function_loss = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/criticalFunctionLoss",
    definition="Essential or mission-critical features of a thing stop working if the thing it depends on is unavailable.",
    name="critical function loss",
)
DependencyImpact.data_staleness = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/dataStaleness",
    definition="A thing must rely on cached or outdated data because fresh data cannot be retrieved if the thing it depends on is unavailable.",
    name="data staleness",
)
DependencyImpact.data_unavailability = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/dataUnavailability",
    definition="A thing cannot retrieve any required data, causing operations to halt or fail, if the thing it depends on is unavailable.",
    name="data unavailability",
)
DependencyImpact.error_propagation = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/errorPropagation",
    definition="A thing emits errors that surface to users or downstream systems if the thing it depends on is unavailable.",
    name="error propagation",
)
DependencyImpact.fallback_mode_activation = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/fallbackModeActivation",
    definition="A thing switches to an intentionally designed degraded or alternate operating mode if the thing it depends on is unavailable.",
    name="fallback mode activation",
)
DependencyImpact.non_critical_function_loss = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/non-criticalFunctionLoss",
    definition="Secondary or optional features of a thing stop working while core functions continue if the thing it depends on is unavailable.",
    name="non-critical function loss",
)
DependencyImpact.queue_build_up = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/queueBuild-up",
    definition="Requests or tasks directed to a thing accumulate because normal processing cannot proceed if the thing it depends on is unavailable.",
    name="queue build-up",
)
DependencyImpact.reduced_performance = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/reducedPerformance",
    definition="A thing remains functional but responds more slowly or with higher latency if the thing it depends on is unavailable.",
    name="reduced performance",
)
