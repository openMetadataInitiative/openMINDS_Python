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

    type_ = "https://openminds.om-i.org/types/ModelScope"
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
            description="Longer statement or account giving the characteristics of the model scope.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the model scope.",
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


ModelScope.network = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/network",
    definition="A model of a neuronal network",
    name="network",
)
ModelScope.network_brain_region = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/network-brainRegion",
    definition="A model of one or more brain regions",
    name="network: brain region",
)
ModelScope.network_microcircuit = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/network-microcircuit",
    definition="A model of a neuronal microcircuit",
    name="network: microcircuit",
)
ModelScope.network_whole_brain = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/network-wholeBrain",
    definition="A model of an entire brain",
    name="network: whole brain",
)
ModelScope.single_cell = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/singleCell",
    definition="A model of a single cell",
    name="single cell",
)
ModelScope.subcellular = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/subcellular",
    definition="A model of an entity or process contained within a cell",
    name="subcellular",
)
ModelScope.subcellular_ion_channel = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/subcellular-ionChannel",
    definition="A model of an ion channel",
    name="subcellular: ion channel",
)
ModelScope.subcellular_molecular = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/subcellular-molecular",
    definition="A model of the structure or behaviour of molecules",
    name="subcellular: molecular",
)
ModelScope.subcellular_signalling = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/subcellular-signalling",
    definition="A model of sub-cellular signalling pathways",
    name="subcellular: signalling",
)
ModelScope.subcellular_spine = ModelScope(
    id="https://openminds.om-i.org/instances/modelScope/subcellular-spine",
    definition="A model of a dendritic spine, or of a dendritic region containing several spines",
    name="subcellular: spine",
)
