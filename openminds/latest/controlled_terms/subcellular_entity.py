"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubcellularEntity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/SubcellularEntity"
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


SubcellularEntity.asymmetric_synapse = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/asymmetricSynapse",
    definition="An 'asymmetric synapse' is characterized by rounded vesicles in the presynaptic cell and a prominent postsynaptic density. Asymmetric synapses are typically excitatory.",
    name="asymmetric synapse",
)
SubcellularEntity.axon = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/axon",
    definition="An 'axon' is the long process of a neuron that conducts nerve impulses, usually away from the cell body to the terminals which are the site of storage and release of neurotransmitter (Gene Ontology).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101043",
    name="axon",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1770195789",
    synonyms=["fiber"],
)
SubcellularEntity.axon_terminal = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/axonTerminal",
    definition="The distal terminations of axons which are specialized for the release of neurotransmitters.",
    description="Also included are varicosities along the course of axons which have similar specializations and also release transmitters. Presynaptic terminals in both the central and peripheral nervous systems are included (MSH).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101049",
    knowledge_space_link="https://knowledge-space.org/wiki/GO:0043679#axon-terminus",
    name="axon terminal",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao2007137787",
    synonyms=["axon terminus"],
)
SubcellularEntity.dendrite = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/dendrite",
    definition="A 'dendrite' is a branching protoplasmic process of a neuron that receives and integrates signals coming from axons of other neurons, and conveys the resulting signal to the body of the cell (Gene Ontology).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103021",
    name="dendrite",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1211023249",
    synonyms=["dendritic branch"],
)
SubcellularEntity.dendritic_spine = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/dendriticSpine",
    definition="A 'dendritic spine' is a protrusion from a dendrite. Spines are specialised subcellular compartments involved in the synaptic transmission.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103030",
    name="dendritic spine",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1799103720",
)
SubcellularEntity.mitochondrion = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/mitochondrion",
    definition="A 'mitochondrion' is a semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration (Gene Ontology).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107028",
    name="mitochondrion",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1860313010",
)
SubcellularEntity.nerve_fiber = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/nerveFiber",
    definition="A threadlike extension of a nerve cell within the nervous system which consists of an axon and, if myelinated, a myelin sheath.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0485634",
    knowledge_space_link="https://knowledge-space.org/wiki/UBERON:0006134#nerve-fiber",
    name="nerve fiber",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0006134",
    synonyms=["neurofibra", "neurofibrum"],
)
SubcellularEntity.neurite = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/neurite",
    definition="A 'neurite' is a small neuronal process on developing neurons that ultimately grow out into axons or dendrites under the control of growth stimulating or inhibiting factors from their direct extracellular environment.",
    name="neurite",
    synonyms=["neurite outgrowth", "neuronal process"],
)
SubcellularEntity.neurofilament = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/neurofilament",
    definition="A 'neurofilament' is a type of intermediate filament found in the core of neuronal axons. Neurofilaments are responsible for the radial growth of an axon and determine axonal diameter.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107475",
    name="neurofilament",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1316272517",
    synonyms=["type IV intermediate filament"],
)
SubcellularEntity.nucleus = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/nucleus",
    definition="A 'nucleus' is a membrane-bounded organelle of eukaryotic cells that contains the chromosomes. It is the primary site of DNA replication and RNA synthesis in the cell (Gene Ontology)",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107735",
    name="nucleus",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1702920020",
    synonyms=["cell nucleus"],
)
SubcellularEntity.symmetric_synapse = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/symmetricSynapse",
    definition="A 'symmetric synapse' has flattened or elongated vesicles, and does not contain a prominent postsynaptic density. Symmetric synapses are typically inhibitory.",
    name="symmetric synapse",
)
SubcellularEntity.synaptic_bouton = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/synapticBouton",
    definition="A 'synaptic bouton' is a terminal pre-synaptic ending of an axon or axon collateral.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0111400",
    name="synaptic bouton",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao187426937",
    synonyms=["pre-synaptic bouton"],
)
SubcellularEntity.synaptic_protein = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/synapticProtein",
    definition="A 'synaptic protein' belongs to a family of neuron-specific phosphoric proteins associated with synaptic vesicles. Synaptic proteins are present on the surface of almost all synaptic particles and bind to the cytoskeleton.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0111412",
    name="synaptic protein",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao936599761",
    synonyms=["synaptic vesicle associated protein"],
)
SubcellularEntity.synaptic_vesicle = SubcellularEntity(
    id="https://openminds.ebrains.eu/instances/subcellularEntity/synapticVesicle",
    definition="A 'synaptic vesicle' is a secretory organelle (~ 50 nm in diameter) released from the pre-synaptic nerve terminal. It accumulates high concentrations of neurotransmitters and secretes these into the synaptic cleft by fusion with the 'active zone' of the pre-synaptic plasma membrane (modified from Gene Ontology).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0111411",
    name="synaptic vesicle",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1071221672",
)
