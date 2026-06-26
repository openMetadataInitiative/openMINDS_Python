# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.subcellular_entity import SubcellularEntity


SubcellularEntity.asymmetric_synapse = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/asymmetricSynapse",
    definition="An 'asymmetric synapse' is characterized by rounded vesicles in the presynaptic cell and a prominent postsynaptic density. Asymmetric synapses are typically excitatory.",
    name="asymmetric synapse",
)

SubcellularEntity.axon = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/axon",
    definition="An 'axon' is the long process of a neuron that conducts nerve impulses, usually away from the cell body to the terminals which are the site of storage and release of neurotransmitter (Gene Ontology).",
    name="axon",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1770195789"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0101043"),
    synonyms=["fiber"],
)

SubcellularEntity.axon_terminal = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/axonTerminal",
    definition="The distal terminations of axons which are specialized for the release of neurotransmitters.",
    description="Also included are varicosities along the course of axons which have similar specializations and also release transmitters. Presynaptic terminals in both the central and peripheral nervous systems are included (MSH).",
    name="axon terminal",
    other_cross_references=["http://uri.neuinfo.org/nif/nifstd/sao2007137787"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/GO:0043679#axon-terminus"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0101049"),
    synonyms=["axon terminus"],
)

SubcellularEntity.dendrite = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/dendrite",
    definition="A 'dendrite' is a branching protoplasmic process of a neuron that receives and integrates signals coming from axons of other neurons, and conveys the resulting signal to the body of the cell (Gene Ontology).",
    name="dendrite",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1211023249"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0103021"),
    synonyms=["dendritic branch"],
)

SubcellularEntity.dendritic_spine = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/dendriticSpine",
    definition="A 'dendritic spine' is a protrusion from a dendrite. Spines are specialised subcellular compartments involved in the synaptic transmission.",
    name="dendritic spine",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1799103720"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0103030"),
)

SubcellularEntity.mitochondrion = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/mitochondrion",
    definition="A 'mitochondrion' is a semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration (Gene Ontology).",
    name="mitochondrion",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1860313010"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0107028"),
)

SubcellularEntity.nerve_fiber = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/nerveFiber",
    definition="A threadlike extension of a nerve cell within the nervous system which consists of an axon and, if myelinated, a myelin sheath.",
    name="nerve fiber",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0485634"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0006134#nerve-fiber"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0006134"),
    synonyms=["neurofibra", "neurofibrum"],
)

SubcellularEntity.neurite = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/neurite",
    definition="A 'neurite' is a small neuronal process on developing neurons that ultimately grow out into axons or dendrites under the control of growth stimulating or inhibiting factors from their direct extracellular environment.",
    name="neurite",
    synonyms=["neurite outgrowth", "neuronal process"],
)

SubcellularEntity.neurofilament = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/neurofilament",
    definition="A 'neurofilament' is a type of intermediate filament found in the core of neuronal axons. Neurofilaments are responsible for the radial growth of an axon and determine axonal diameter.",
    name="neurofilament",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1316272517"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0107475"),
    synonyms=["type IV intermediate filament"],
)

SubcellularEntity.nucleus = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/nucleus",
    definition="A 'nucleus' is a membrane-bounded organelle of eukaryotic cells that contains the chromosomes. It is the primary site of DNA replication and RNA synthesis in the cell (Gene Ontology)",
    name="nucleus",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1702920020"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0107735"),
    synonyms=["cell nucleus"],
)

SubcellularEntity.symmetric_synapse = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/symmetricSynapse",
    definition="A 'symmetric synapse' has flattened or elongated vesicles, and does not contain a prominent postsynaptic density. Symmetric synapses are typically inhibitory.",
    name="symmetric synapse",
)

SubcellularEntity.synaptic_bouton = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/synapticBouton",
    definition="A 'synaptic bouton' is a terminal pre-synaptic ending of an axon or axon collateral.",
    name="synaptic bouton",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao187426937"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0111400"),
    synonyms=["pre-synaptic bouton"],
)

SubcellularEntity.synaptic_protein = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/synapticProtein",
    definition="A 'synaptic protein' belongs to a family of neuron-specific phosphoric proteins associated with synaptic vesicles. Synaptic proteins are present on the surface of almost all synaptic particles and bind to the cytoskeleton.",
    name="synaptic protein",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao936599761"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0111412"),
    synonyms=["synaptic vesicle associated protein"],
)

SubcellularEntity.synaptic_vesicle = SubcellularEntity(
    id="https://openminds.om-i.org/instances/subcellularEntity/synapticVesicle",
    definition="A 'synaptic vesicle' is a secretory organelle (~ 50 nm in diameter) released from the pre-synaptic nerve terminal. It accumulates high concentrations of neurotransmitters and secretes these into the synaptic cleft by fusion with the 'active zone' of the pre-synaptic plasma membrane (modified from Gene Ontology).",
    name="synaptic vesicle",
    preferred_cross_reference=IRI("http://uri.neuinfo.org/nif/nifstd/sao1071221672"),
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0111411"),
)
