"""
Structured information on the species.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Species(LinkedMetadata):
    """
    Structured information on the species.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Species"
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


Species.berghia_stephanieae = Species(
    id="https://openminds.ebrains.eu/instances/species/berghiaStephanieae",
    definition="The species *Berghia stephanieae* belongs to the family of *aeolidiidae* (family of sea slugs, shell-less marine gastropod molluscs).",
    name="Berghia stephanieae",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_1287507",
    synonyms=["aeolidiella stephanieae"],
)
Species.callithrix_jacchus = Species(
    id="https://openminds.ebrains.eu/instances/species/callithrixJacchus",
    definition="The species *Callithrix jacchus* (common marmoset) belongs to the family of *callitrichidae* (new world monkeys).",
    name="Callithrix jacchus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9483",
    synonyms=[
        "callithrix jacchus jacchus",
        "common marmoset",
        "white ear-tufted marmoset",
        "white-tufted-ear marmoset",
    ],
)
Species.chlorocebus_aethiops_sabaeus = Species(
    id="https://openminds.ebrains.eu/instances/species/chlorocebusAethiopsSabaeus",
    definition="The species *Chlorocebus aethiops sabaeus* (green monkey) belongs to the family of *cercopithecidae* (old world monkeys).",
    name="Chlorocebus aethiops sabaeus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_60711",
    synonyms=[
        "cercopithecus aethiops sabaeus",
        "cercopithecus sabaeus",
        "cercopithecus sabeus",
        "chlorocebus aethiops sabeus",
        "chlorocebus sabaeus",
        "chlorocebus sabeus",
        "green monkey",
    ],
)
Species.chlorocebus_pygerythrus = Species(
    id="https://openminds.ebrains.eu/instances/species/chlorocebusPygerythrus",
    definition="The species *Chlorocebus pygerythrus* (vervet marmoset) belongs to the family of *cercopithecidae* (old world monkeys).",
    name="Chlorocebus pygerythrus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_60710",
    synonyms=[
        "cercopithecus aethiops pygerythrus",
        "cercopithecus pygerythrus",
        "chlorocebus aethiops pygerythrus",
        "vervet",
        "vervet marmoset",
        "vervet monkey",
    ],
)
Species.danio_rerio = Species(
    id="https://openminds.ebrains.eu/instances/species/danioRerio",
    definition="The species *Danio rerio* (zebrafish) belongs to the family of *cyprinidae* (cyprinids, freshwater fish).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0783580",
    knowledge_space_link="https://knowledge-space.org/wiki/NCBITaxon:7955#danio-rerio",
    name="Danio rerio",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_7955",
    synonyms=[
        "Brachydanio rerio",
        "Brachydanio rerio frankei",
        "Cyprinus rerio",
        "Danio frankei",
        "Danio rerio frankei",
        "leopard danio",
        "zebra danio",
        "zebra fish",
        "zebrafish",
    ],
)
Species.felis_catus = Species(
    id="https://openminds.ebrains.eu/instances/species/felisCatus",
    definition="The species *Felis catus* (domestic cat) belongs to the family of *Felidae*, subfamily *Felinae*.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101690",
    name="Felis catus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9685",
    synonyms=["cat", "house cat", "domestic cat", "Felis silvestris catus", "Felis domesticus"],
)
Species.homo_sapiens = Species(
    id="https://openminds.ebrains.eu/instances/species/homoSapiens",
    definition="The species *Homo sapiens* (humans) belongs to the family of *hominidae* (great apes).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105114",
    knowledge_space_link="https://knowledge-space.org/wiki/NCBITaxon:9606#human",
    name="Homo sapiens",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9606",
    synonyms=["homo sapien", "human", "man"],
)
Species.macaca_fascicularis = Species(
    id="https://openminds.ebrains.eu/instances/species/macacaFascicularis",
    definition="The species *Macaca fascicularis* (crab-eating macaque) belongs to the family of *cercopithecidae* (old world monkeys).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0485278",
    name="Macaca fascicularis",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9541",
    synonyms=[
        "crab eating macaque",
        "crab-eating macaque",
        "cynomolgus macaque",
        "cynomolgus monkey",
        "long-tailed macaque",
        "macaca cynomolgus",
        "macaca irus",
    ],
)
Species.macaca_fuscata = Species(
    id="https://openminds.ebrains.eu/instances/species/macacaFuscata",
    definition="The species *Macaca fuscata* (Japanese macaque) belongs to the family of *cercopithecidae* (old world monkeys).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105773",
    name="Macaca fuscata",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9542",
    synonyms=["japanese macaque", "japanese monkey"],
)
Species.macaca_mulatta = Species(
    id="https://openminds.ebrains.eu/instances/species/macacaMulatta",
    definition="The species *Macaca mulatta* (rhesus macaque) belongs to the family of *cercopithecidae* (old world monkeys).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0110118",
    name="Macaca mulatta",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9544",
    synonyms=["rhesus macaque", "rhesus monkey"],
)
Species.monodelphis_domestica = Species(
    id="https://openminds.ebrains.eu/instances/species/monodelphisDomestica",
    definition="The species *Monodelphis domestica* (gray short-tailed opossum) belongs to the family of *didelphidae* (American possums).",
    name="Monodelphis domestica",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_13616",
    synonyms=["gray short-tailed opossum"],
)
Species.mus_musculus = Species(
    id="https://openminds.ebrains.eu/instances/species/musMusculus",
    definition="The species *Mus musculus* (house mouse) belongs to the family of *muridae* (murids).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107134",
    knowledge_space_link="https://knowledge-space.org/wiki/NCBITaxon:10090#mouse",
    name="Mus musculus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_10090",
    synonyms=["house mouse", "mouse"],
)
Species.mustela_putorius = Species(
    id="https://openminds.ebrains.eu/instances/species/mustelaPutorius",
    definition="The species *Mustela putorius* (European polecat) belongs to the family of *mustelidae* (mustelids).",
    name="Mustela putorius",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9668",
    synonyms=["european polecat", "putorius putorius"],
)
Species.mustela_putorius_furo = Species(
    id="https://openminds.ebrains.eu/instances/species/mustelaPutoriusFuro",
    definition="The species *Mustela putorius furo* (domestic ferret) belongs to the family of *mustelidae* (mustelids).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104165",
    name="Mustela putorius furo",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9669",
    synonyms=["black ferret", "domestic ferret", "ferret", "mustela furo"],
)
Species.ovis_aries = Species(
    id="https://openminds.ebrains.eu/instances/species/ovisAries",
    definition="The species *Ovis aries* (domestic sheep) belongs to the family of bovidae (bovids).",
    name="Ovis aries",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9940",
    synonyms=["domestic sheep", "sheep"],
)
Species.rattus_norvegicus = Species(
    id="https://openminds.ebrains.eu/instances/species/rattusNorvegicus",
    definition="The species *Rattus norvegicus* (brown rat) belongs to the family of *muridae* (murids).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0109658",
    knowledge_space_link="https://knowledge-space.org/wiki/NCBITaxon:10116#rat",
    name="Rattus norvegicus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_10116",
    synonyms=["brown rat", "norway rat", "rat"],
)
Species.sus_scrofa_domesticus = Species(
    id="https://openminds.ebrains.eu/instances/species/susScrofaDomesticus",
    definition="The species *Sus scrofa domesticus* (domestic pig) belongs to the family of suidae (suids).",
    interlex_identifier="http://uri.interlex.org/ilx_0739770",
    knowledge_space_link="https://knowledge-space.org/wiki/NCBITaxon:9825#sus-scrofa-domesticus",
    name="Sus scrofa domesticus",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_9825",
    synonyms=["domestic pig", "sus domestica", "sus domesticus", "sus scrofa domestica"],
)
Species.trachemys_scripta_elegans = Species(
    id="https://openminds.ebrains.eu/instances/species/trachemysScriptaElegans",
    definition="The red-eared slider or red-eared terrapin (Trachemys scripta elegans) is a subspecies of the pond slider (Trachemys scripta), a semiaquatic turtle belonging to the family Emydidae ([Wikipedia](https://en.wikipedia.org/wiki/Red-eared_slider)).",
    name="Trachemys scripta elegans",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NCBITaxon_31138",
    synonyms=[
        "Pseudemys scripta elegans",
        "Chrysemys scripta elegans",
        "Emys elegans",
        "red-eared slider",
        "red-eared terrapin",
        "pond slider",
    ],
)
