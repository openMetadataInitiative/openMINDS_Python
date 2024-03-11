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


BiologicalOrder.carnivora = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/carnivora",
    definition="The biological order *Carnivora* (carnivore) belongs to the class *Mammalia* (mammals).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101675",
    name="Carnivora",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_33554",
    synonyms=["carnivore"],
)
BiologicalOrder.cypriniformes = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/cypriniformes",
    definition="The biological order *Cypriniformes* belongs to the class *Actinopterygii* (ray-finned fishes).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0737279",
    name="Cypriniformes",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0005508",
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
    interlex_identifier="http://uri.interlex.org/base/ilx_0107805",
    name="Nudibranchia",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_70849",
    synonyms=["nudibranchs"],
)
BiologicalOrder.primates = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/primates",
    definition="The biological order *Primates* belongs to the class *Mammalia* (mammals).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0486298",
    name="Primates",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0017579",
)
BiologicalOrder.rodentia = BiologicalOrder(
    id="https://openminds.ebrains.eu/instances/biologicalOrder/rodentia",
    definition="The biological order *Rodentia* (rodents) belongs to the class *Mammalia* (mammals).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0110175",
    name="Rodentia",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9989",
    synonyms=["rodents"],
)
