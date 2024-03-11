"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CellType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/CellType"
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


CellType.aromatase_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/aromataseExpressingNeuron",
    definition="Any neuron that expresses aromatase.",
    name="aromatase expressing neuron",
    synonyms=["aromatase expressing cell", "aromatase-positive cell", "aromatase-positive neuron"],
)
CellType.astrocyte = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/astrocyte",
    definition="'Astrocytes' are a class of large, star-shaped neuroglial (macroglial) cells in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0100947",
    name="astrocyte",
    synonyms=["astroglial cell"],
)
CellType.basket_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/basketCell",
    definition="An inhibitory GABAergic interneurons of the brain, enmeshing the cell body of another neuron with its terminal axon ramifications.",
    name="basket cell",
)
CellType.calbindin_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/calbindinExpressingNeuron",
    definition="Any neuron that expresses calbindin.",
    name="calbindin expressing neuron",
    synonyms=[
        "CALB+ cell",
        "CALB+ neuron",
        "CALB-expressing cell",
        "CALB-expressing neuron",
        "CALB-positive cell",
        "CALB-positive neuron",
        "calbindin expressing cell",
        "calbindin-positive cell",
        "calbindin-positive neuron",
    ],
)
CellType.calretinin_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/calretininExpressingNeuron",
    definition="Any neuron that expresses calretinin.",
    name="calretinin expressing neuron",
    synonyms=[
        "calretinin expressing cell",
        "calretinin-positive cell",
        "calretinin-positive neuron",
        "CR+ cell",
        "CR+ neuron",
    ],
)
CellType.cerebellar_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellarInterneuron",
    name="cerebellar interneuron",
)
CellType.cerebellum_basket_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumBasketCell",
    definition="An inhibitory GABAergic interneurons of the cerebellum, enmeshing the cell body of another neuron with its terminal axon ramifications.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101964",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:666951243#cerebellum-basket-cell",
    name="cerebellum basket cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao666951243",
    synonyms=["cerebellar basket cell"],
)
CellType.cerebellum_golgi_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumGolgiCell",
    definition="An inhibitory interneuron found within the granular layer of the cerebellum.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101966",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:129#golgi-cell",
    name="cerebellum Golgi cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1415726815",
    synonyms=[
        "cerebellar Golgi cell",
        "cerebellar Golgi neuron",
        "cerebellum Golgi neuron",
        "Golgi cell",
        "Golgi neuron",
    ],
)
CellType.cerebellum_granule_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumGranuleCell",
    definition="'Cerebellum granule cells' form the thick granular layer of the cerebellar cortex and typically have small cell bodies but varying functions.",
    interlex_identifier="http://uri.interlex.org/ilx_0101967",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:128#cerebellum-granule-cell",
    name="cerebellum granule cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_128",
    synonyms=["cerebellar granule cell", "cerebellar granule neuron", "cerebellum granule neuron"],
)
CellType.cerebellum_stellate_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumStellateNeuron",
    definition="Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.",
    interlex_identifier="http://uri.interlex.org/ilx_0101975",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:130#cerebellum-stellate-cell",
    name="cerebellum stellate neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_130",
    synonyms=["cerebellar stellate cell", "cerebellar stellate neuron", "cerebellum stellate cell"],
)
CellType.cholecystokinin_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cholecystokininExpressingNeuron",
    definition="Any neuron that expresses cholecystokinin.",
    name="cholecystokinin expressing neuron",
    synonyms=[
        "CCK+ cell",
        "CCK+ neuron",
        "CCK-positive cell",
        "CCK-positive neuron",
        "cholecystokinin expressing cell",
    ],
)
CellType.choline_acetyltransferase_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cholineAcetyltransferaseExpressingNeuron",
    definition="Any neuron that expresses choline acetyltransferase.",
    name="choline acetyltransferase expressing neuron",
    synonyms=[
        "ChAT+ cell",
        "ChAT+ neuron",
        "ChAT-expressing cell",
        "ChAT-expressing neuron",
        "ChAT-positive cell",
        "ChAT-positive neuron",
        "choline acetyltransferase expressing cell",
        "choline acetyltransferase-positive cell",
        "choline acetyltransferase-positive neuron",
    ],
)
CellType.cholinergic_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cholinergicInterneuron",
    definition="An inhibitory interneuron which mainly uses the neurotrasmitter acetylcholine (ACh).",
    name="cholinergic interneuron",
    synonyms=["CIN"],
)
CellType.cholinergic_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cholinergicNeuron",
    definition="Any neuron that releases some acetylcholine as a neurotransmitter",
    interlex_identifier="http://uri.interlex.org/ilx_0102131",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXNEURNT:090802#cholinergic-neuron",
    name="cholinergic neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_148005",
    synonyms=["ACh neuron"],
)
CellType.cortical_basket_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/corticalBasketCell",
    definition="An inhibitory GABAergic interneurons of the cortex, enmeshing the cell body of another neuron with its terminal axon ramifications.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107351",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:56#neocortex-basket-cell",
    name="cortical basket cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_56",
    synonyms=["basket cell", "cortical basket neuron", "neocortex basket cell", "neocortical basket cell"],
)
CellType.cortical_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/corticalInterneuron",
    name="cortical interneuron",
)
CellType.d1_receptor_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/D1ReceptorExpressingNeuron",
    definition="Any neuron that expresses D1 receptors.",
    name="D1 receptor expressing neuron",
    synonyms=[
        "D1 dopamine receptor expressing cell",
        "D1 dopamine receptor expressing neuron",
        "D1 receptor expressing cell",
        "D1R expressing cell",
        "D1R expressing neuron",
        "dopamine receptor D1 expressing cell",
        "dopamine receptor D1 expressing neuron",
        "DRD1 expressing cell",
        "DRD1 expressing neuron",
    ],
)
CellType.d2_receptor_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/D2ReceptorExpressingNeuron",
    definition="Any neuron that expresses D2 receptors.",
    name="D2 receptor expressing neuron",
    synonyms=[
        "D2 dopamine receptor expressing cell",
        "D2 dopamine receptor expressing neuron",
        "D2 receptor expressing cell",
        "D2R expressing cell",
        "D2R expressing neuron",
        "dopamine receptor D2 expressing cell",
        "dopamine receptor D2 expressing neuron",
        "DRD2 expressing cell",
        "DRD2 expressing neuron",
    ],
)
CellType.dopaminergic_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/dopaminergicNeuron",
    definition="Any neuron that releases some dopamine as a neurotransmitter",
    interlex_identifier="http://uri.interlex.org/ilx_0103395",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXNEURNT:090806#dopaminergic-neuron",
    name="dopaminergic neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_147835",
    synonyms=["DA neuron"],
)
CellType.excitatory_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/excitatoryNeuron",
    definition="An 'excitatory neuron' releases neurotransmitters (e.g. glutamate) that have a deperpolarizing effect on the post-synaptic neuron, facilitating the generation of an action potential.",
    name="excitatory neuron",
    synonyms=["excitatory cell"],
)
CellType.fast_spiking_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/fastSpikingInterneuron",
    definition="A parvalbumin positive GABAergic interneuron with a high-frequency firing pattern.",
    name="fast spiking interneuron",
    synonyms=["FSI"],
)
CellType.glial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/glialCell",
    definition="A 'glial cell' is a non-neuronal cell of the nervous system. Glial cells provide physical support, respond to injury, regulate the ionic and chemical composition of the extracellular milieu, guide neuronal migration during development, and exchange metabolites with neurons.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104634",
    name="glial cell",
    synonyms=["neuroglial cell"],
)
CellType.granule_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/granuleNeuron",
    definition="The term 'granule neuron' refers to a set of neuron types typically found in granular layers across brain regions whose only common feature is that they all have very small cell bodies [[adapted from Wikipedia](https://en.wikipedia.org/wiki/Granule_cell)].",
    name="granule neuron",
    synonyms=["granule cell"],
)
CellType.hippocampus_ca1_pyramidal_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/hippocampusCA1PyramidalNeuron",
    definition="An excitatory neuron type with a pyramidal-shaped cell body that is located in the cornu ammonis 1 (CA1) of the hippocampus.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105031",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:830368389#hippocampus-ca1-pyramidal-cell",
    name="hippocampus CA1 pyramidal neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao830368389",
    synonyms=[
        "CA1 pyramidal neuron",
        "cornu ammonis 1 pyramidal neuron",
        "hippocampal CA1 pyramidal cell",
        "hippocampus CA1 pyramidal cell",
    ],
)
CellType.inhibitory_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/inhibitoryNeuron",
    definition="An 'inhibitory neuron' releases neurotransmitters (e.g. GABA) that have a hyperpolarizing effect on the post-synaptic neuron, making it difficult to generate an action potential.",
    name="inhibitory neuron",
    synonyms=["inhibitory cell"],
)
CellType.interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/interneuron",
    definition="An 'interneuron' is neuron that cannot be classified as sensory receptor or motor neuron.",
    name="interneuron",
)
CellType.macroglial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/macroglialCell",
    definition="'Macroglial cells' are large glial cells in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106438",
    name="macroglial cell",
)
CellType.microglial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/microglialCell",
    definition="'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106919",
    name="microglial cell",
)
CellType.motor_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/motorNeuron",
    name="motor neuron",
)
CellType.neocortex_layer2_3_pyramidal_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neocortexLayer2-3PyramidalNeuron",
    definition="An excitatory neuron type with a pyramidal-shaped cell body that is located in layer 2/3 of the neocortex.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107387",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:49#neocortex-pyramidal-cell-layer-2-3",
    name="neocortex layer 2/3 pyramidal neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_49",
    synonyms=[
        "layer 2/3 pyramidal cell",
        "layer 2/3 pyramidal neuron",
        "neocortex layer 2/3 pyramidal neuron",
        "neocortex pyramidal layer 2/3 cell",
        "superficial pyramidal neuron",
        "supericial pyramidal cell",
    ],
)
CellType.neocortex_layer5_tufted_pyramidal_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neocortexLayer5TuftedPyramidalNeuron",
    definition="An excitatory neuron type with a pyramidal-shaped cell body found in layer 5 of the neocortex and projects to subcortical areas.",
    interlex_identifier="http://uri.interlex.org/ilx_0738209",
    name="neocortex layer 5 tufted pyramidal neuron",
    synonyms=[
        "L5 TPC",
        "L5 tufted pyramidal cell",
        "layer 5 tufted pyramidal cell",
        "layer 5 tufted pyramidal neuron",
        "TL5 neuron",
    ],
)
CellType.neostriatum_cholinergic_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neostriatumCholinergicInterneuron",
    definition="An inhibitory interneuron in the caudate nucleus and putamen which mainly uses the neurotrasmitter acetylcholine (ACh).",
    interlex_identifier="http://uri.interlex.org/ilx_0107403",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:1866881837#neostriatum-cholinergic-cell",
    name="neostriatum cholinergic interneuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1866881837",
    synonyms=[
        "cholinergic striatal neuron",
        "CIN",
        "giant cholinergic interneuron",
        "large striatal aspiny neuron",
        "neostriatial cholinergic interneuron",
        "neostriatum cholinergic cell",
        "neostriatum giant cell of Kolliker",
        "striatal cholinergic interneuron",
    ],
)
CellType.neostriatum_direct_pathway_spiny_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neostriatumDirectPathwaySpinyNeuron",
    definition="The principal projection neuron of the caudate and putamen that excite their output structure.",
    interlex_identifier="http://uri.interlex.org/ilx_0107404",
    name="neostriatum direct pathway spiny neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_149135",
    synonyms=[
        "direct pathway medium spiny neuron",
        "direct pathway medium-sized spiny neuron",
        "dMSN",
        "neostriatial direct pathway spiny neuron",
        "striatal direct pathway spiny neuron",
    ],
)
CellType.neostriatum_indirect_pathway_spiny_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neostriatumIndirectPathwaySpinyNeuron",
    definition="The principal projection neuron of the caudate and putamen that inhibit their output structure.",
    interlex_identifier="http://uri.interlex.org/ilx_0107405",
    name="neostriatum indirect pathway spiny neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_149136",
    synonyms=[
        "iMSN",
        "indirect pathway medium spiny neuron",
        "indirect pathway medium-sized spiny neuron",
        "neostriatial indirect pathway spiny neuron",
        "striatal indirect pathway spiny neuron",
    ],
)
CellType.neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neuron",
    definition="A 'neuron' is a basic cellular unit of nervous tissue which can receive, conduct, and transmit electrical impulses.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107497",
    name="neuron",
    synonyms=["nerve cell", "neurone"],
)
CellType.neuropeptide_y_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neuropeptideYExpressingNeuron",
    definition="Any neuron that expresses neuropeptide Y.",
    name="neuropeptide Y expressing neuron",
    synonyms=[
        "neuropeptide Y expressing cell",
        "neuropeptide Y-positive cell",
        "neuropeptide Y-positive neuron",
        "NPY+ cell",
        "NPY+ neuron",
        "NPY-expressing cell",
        "NPY-expressing neuron",
        "NPY-positive cell",
        "NPY-positive neuron",
    ],
)
CellType.nitric_oxide_synthase_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/nitricOxideSynthaseExpressingNeuron",
    definition="Any neuron that expresses nitric oxide synthase.",
    name="nitric oxide synthase expressing neuron",
    synonyms=[
        "nitric oxide synthase expressing cell",
        "nitric oxide synthase-positive cell",
        "nitric oxide synthase-positive neuron",
        "NOS+ cell",
        "NOS+ neuron",
        "NOS-expressing cell",
        "NOS-expressing neuron",
        "NOS-positive cell",
        "NOS-positive neuron",
    ],
)
CellType.parvalbumin_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/parvalbuminExpressingNeuron",
    definition="Any neuron that expresses parvalbumin.",
    name="parvalbumin expressing neuron",
    synonyms=["parvalbumin expressing cell", "PV+ cell", "PV+ neuron", "PV-positive cell", "PV-positive neuron"],
)
CellType.postmitotic_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/postmitoticCell",
    definition="A 'postmitotic cell' is a fully differentiated, non-dividing mature cell that no longer undergoes mitosis.",
    name="postmitotic cell",
)
CellType.progenitor_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/progenitorCell",
    definition="A 'progenitor cell' is a descendent of a stem cell that further differentiate to create specialized cell types.",
    name="progenitor cell",
)
CellType.purkinje_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/PurkinjeCell",
    definition="A class of GABAergic inhibitory neurons located in the cerebellum with pear-shape cell bodies arranged in a single layer, typically one primary dendrites and an elaborate dendritic tree heavily invested with dendritic spines.",
    interlex_identifier="http://uri.interlex.org/ilx_0101974",
    name="Purkinje cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao471801888",
    synonyms=[
        "cerebellar Punkinje cell",
        "cerebellar Punkinje neuron",
        "cerebellum Purkinje cell",
        "cerebellum Purkinje neuron",
        "Corpuscles of Purkinje",
        "Purkinje neuron",
        "Purkinje's corpuscles",
        "Purkyne cell",
    ],
)
CellType.pyramidal_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/pyramidalNeuron",
    definition="A 'pyramidal neuron' is a type of multipolar neuron that is characterized by a pyramidal shaped cell body (soma) and two distinct dendritic trees.",
    name="pyramidal neuron",
    synonyms=["pyramidal cell"],
)
CellType.sensory_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/sensoryNeuron",
    name="sensory neuron",
)
CellType.somatostatin_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/somatostatinExpressingNeuron",
    definition="Any neuron that expresses somatostatin.",
    name="somatostatin expressing neuron",
    synonyms=[
        "somatostatin expressing cell",
        "somatostatin positive cell",
        "somatostatin positive neuron",
        "SST+ cell",
        "SST+ neuron",
        "SST-positive cell",
        "SST-positive neuron",
    ],
)
CellType.spinal_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/spinalInterneuron",
    name="spinal interneuron",
)
CellType.spiny_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/spinyNeuron",
    definition="Any neuron characterized by a high density of dendritic spines on the dendrites.",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXCELL:100601#spiny-neuron",
    name="spiny neuron",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_100601",
)
CellType.stellate_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/stellateNeuron",
    definition="Any neuron in the central nervous system that has a star-like shape formed by dendritic processes radiating from the cell body.",
    name="stellate neuron",
)
CellType.striatal_interneuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/striatalInterneuron",
    name="striatal interneuron",
)
CellType.striatum_medium_spiny_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/striatumMediumSpinyNeuron",
    definition="A special type of GABAergic neuron with large dendritic trees that is located in the striatum.",
    interlex_identifier="http://uri.interlex.org/ilx_0784362",
    name="striatum medium spiny neuron",
    preferred_ontology_identifier="http://uri.interlex.org/npo/uris/neurons/35",
    synonyms=["MSN", "spiny projection neuron", "SPN", "striatal medium spiny neuron"],
)
CellType.vascular_endothelial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/vascularEndothelialCell",
    definition="Cells that constitute the inner cellular lining of arteries, veins and capillaries.",
    interlex_identifier="http://uri.interlex.org/ilx_0112265",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:1543450574#vascular-endothelial-cell",
    name="vascular endothelial cell",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1543450574",
    synonyms=["endothelial cell"],
)
CellType.vascular_smooth_muscle_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/vascularSmoothMuscleCell",
    definition="A smooth muscle cell assocatiated with the vasculature.",
    name="vascular smooth muscle cell",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CL_0000359",
    synonyms=["vascular associated smooth muscle cell", "VSMC"],
)
CellType.vasoactive_intestinal_peptide_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/vasoactiveIntestinalPeptideExpressingNeuron",
    definition="Any neuron that expresses vasoactive-intestinal peptide.",
    name="vasoactive-intestinal peptide expressing neuron",
    synonyms=[
        "vasoactive-intestinal peptide expressing cell",
        "VIP+ cell",
        "VIP+ neuron",
        "VIP-positive cell",
        "VIP-positive neuron",
    ],
)
