"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BiologicalOrder(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/BiologicalOrder"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

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
            description="Longer statement or account giving the characteristics of the biological order.",
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
            description="Word or phrase that constitutes the distinctive designation of the biological order.",
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
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


BiologicalOrder.carnivora = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/carnivora",
    definition="The biological order *Carnivora* (carnivore) belongs to the class *Mammalia* (mammals).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101675"),
    name="Carnivora",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/NCBITaxon_33554"),
    synonyms=["carnivore"],
)
BiologicalOrder.cypriniformes = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/cypriniformes",
    definition="The biological order *Cypriniformes* belongs to the class *Actinopterygii* (ray-finned fishes).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0737279"),
    name="Cypriniformes",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0005508"),
)
BiologicalOrder.didelphimorphia = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/didelphimorphia",
    definition="The biological order *Didelphimorphia* (opossums) belongs to the class *Mammalia* (mammals).",
    name="Didelphimorphia",
    synonyms=["opossums"],
)
BiologicalOrder.nudibranchia = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/nudibranchia",
    definition="The biological order *Nudibranchia* (nudibranchs) belongs to the class *Gastropoda* (gastropods).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107805"),
    name="Nudibranchia",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/NCBITaxon_70849"),
    synonyms=["nudibranchs"],
)
BiologicalOrder.primates = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/primates",
    definition="The biological order *Primates* belongs to the class *Mammalia* (mammals).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0486298"),
    name="Primates",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0017579"),
)
BiologicalOrder.rodentia = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/rodentia",
    definition="The biological order *Rodentia* (rodents) belongs to the class *Mammalia* (mammals).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0110175"),
    name="Rodentia",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/NCBITaxon_9989"),
    synonyms=["rodents"],
)
