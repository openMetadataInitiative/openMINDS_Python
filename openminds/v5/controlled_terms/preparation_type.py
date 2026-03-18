"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PreparationType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/PreparationType"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

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
            description="Longer statement or account giving the characteristics of the preparation type.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the preparation type.",
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


PreparationType.ex_vivo = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/exVivo",
    definition="Something happening or existing outside a living body.",
    name="ex vivo",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739736"),
    synonyms=["ex vivo technique"],
)
PreparationType.in_silico = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inSilico",
    definition="Conducted or produced by means of computer modelling or simulation.",
    name="in silico",
    other_ontology_identifiers=["http://uri.interlex.org/ilx_0494742"],
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0572590"),
)
PreparationType.in_situ = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inSitu",
    definition="Something happening or being examined in the original place instead of being moved to another place",
    name="in situ",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/ilx_0739593"),
    synonyms=["in situ technique"],
)
PreparationType.in_utero = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inUtero",
    definition="Something happening in, within, or while inside the uterus.",
    name="in utero",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/ilx_0739675"),
    synonyms=["in utero technique"],
)
PreparationType.in_vitro = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inVitro",
    definition="Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).",
    name="in vitro",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739568"),
    synonyms=["in vitro technique"],
)
PreparationType.in_vivo = PreparationType(
    id="https://openminds.om-i.org/instances/preparationType/inVivo",
    definition="Something happening or existing inside a living body.",
    name="in vivo",
    other_ontology_identifiers=["http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89"],
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0739622"),
    synonyms=["in vivo technique"],
)
