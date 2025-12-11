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
            description="Longer statement or account giving the characteristics of the cell type.",
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
            description="Word or phrase that constitutes the distinctive designation of the cell type.",
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


CellType.aromatase_expressing_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/aromataseExpressingNeuron",
    definition="Any neuron that expresses aromatase.",
    name="aromatase expressing neuron",
    synonyms=["aromatase expressing cell", "aromatase-positive cell", "aromatase-positive neuron"],
)
CellType.astrocyte = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/astrocyte",
    definition="'Astrocytes' are a class of large, star-shaped neuroglial (macroglial) cells in the central nervous system.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0100947"),
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
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101964"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/SAO:666951243#cerebellum-basket-cell"),
    name="cerebellum basket cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao666951243"),
    synonyms=["cerebellar basket cell"],
)
CellType.cerebellum_golgi_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumGolgiCell",
    definition="An inhibitory interneuron found within the granular layer of the cerebellum.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101966"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:129#golgi-cell"),
    name="cerebellum Golgi cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao1415726815"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0101967"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:128#cerebellum-granule-cell"),
    name="cerebellum granule cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_128"),
    synonyms=["cerebellar granule cell", "cerebellar granule neuron", "cerebellum granule neuron"],
)
CellType.cerebellum_stellate_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/cerebellumStellateNeuron",
    definition="Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0101975"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:130#cerebellum-stellate-cell"),
    name="cerebellum stellate neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_130"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0102131"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NLXNEURNT:090802#cholinergic-neuron"),
    name="cholinergic neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_148005"),
    synonyms=["ACh neuron"],
)
CellType.cortical_basket_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/corticalBasketCell",
    definition="An inhibitory GABAergic interneurons of the cortex, enmeshing the cell body of another neuron with its terminal axon ramifications.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107351"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:56#neocortex-basket-cell"),
    name="cortical basket cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_56"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0103395"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NLXNEURNT:090806#dopaminergic-neuron"),
    name="dopaminergic neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_147835"),
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
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0104634"),
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
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0105031"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/SAO:830368389#hippocampus-ca1-pyramidal-cell"),
    name="hippocampus CA1 pyramidal neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao830368389"),
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
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106438"),
    name="macroglial cell",
)
CellType.main_olfactory_bulb_deep_tufted_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbDeepTuftedNeuron",
    definition="A subclass of neurons situated in the innermost (deep) layer of the external plexiform layer of the main olfactory bulb.",
    name="main olfactory bulb deep tufted neuron",
    synonyms=[
        "deep tufted cell of the main olfactory bulb",
        "main olfactory bulb deep tufted cell",
        "deep tufted neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_external_tufted_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbExternalTuftedNeuron",
    definition="An excitatory neuron type found predominately at the glomerular layer of the main olfactory bulb.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107943"),
    name="main olfactory bulb external tufted neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_82555"),
    synonyms=[
        "olfactory bulb main tufted cell external",
        "olfactory bulb external tufted cell",
        "external tuftes cell of the main olfactory bulb",
        "main olfactory bulb external tufted cell",
        "external tuftes neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_granule_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbGranuleNeuron",
    definition="Axonless inhibitory interneurons and form the majority of neurons in the vertebrate main olfactory bulb [adapted from [Egger et al. (2003)](https://doi.org/10.1523/JNEUROSCI.23-20-07551.2003)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107930"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:123#olfactory-bulb-main-granule-cell"),
    name="main olfactory bulb granule neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_123"),
    synonyms=[
        "granule cell of the olfactory bulb",
        "olfactory bulb granule neuron",
        "granule neuron of the olfactory bulb",
        "olfactory bulb (main) granule cell",
        "main olfactory bulb granule cell",
        "granule cell of the main olfactory bulb",
        "granule neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_middle_tufted_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbMiddleTuftedNeuron",
    definition="A subclass of neurons situated in the middle layer of the external plexiform layer of the main olfactory bulb.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107935"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:121#olfactory-bulb-main-tufted-cell"),
    name="main olfactory bulb middle tufted neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_121"),
    synonyms=[
        "olfactory bulb (main) tufted cell (middle)",
        "middle tufted cell of the main olfactory bulb",
        "main olfactory bulb middle tufted cell",
        "middle tufted neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_mitral_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbMitralNeuron",
    definition="Neuronal cell type in the mammalian olfactory bulb, distinguished by the position of their somata located in an orderly row in the mitral cell layer of the bulb. [from [Wikipedia](https://en.wikipedia.org/wiki/Mitral_cell#Structure)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107933"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:120#olfactory-bulb-main-mitral-cell"),
    name="main olfactory bulb mitral neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_120"),
    synonyms=[
        "olfactory bulb (main) mitral cell",
        "olfactory bulb (main) mitral neuron",
        "mitral neuron",
        "main olfactory bulb mitral cell",
        "mitral neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_periglomerular_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbPeriglomerularNeuron",
    definition="Small intrinsic neurons in the glomerular layer of the main olfactory bulb, with cell bodies surrounding the olfactory glomerulus. [adapted from [InterLex](http://uri.interlex.org/base/ilx_0107934)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107934"),
    knowledge_space_link=IRI(
        "https://knowledge-space.org/wiki/NLXCELL:091202#olfactory-bulb-main-periglomerular-cell"
    ),
    name="main olfactory bulb periglomerular neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_cell_091202"),
    synonyms=[
        "periglomerular neuron",
        "PGC",
        "PG cell",
        "main olfactory bulb periglomerular cell",
        "periglomerular cell of the main olfactory bulb",
        "periglomerular neuron of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_superficial_tufted_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbSuperficialTuftedNeuron",
    definition="A subclass of neurons situated in the outermost (superficial) layer of the external plexiform layer of the main olfactory bulb.",
    name="main olfactory bulb superficial tufted neuron",
    synonyms=[
        "main olfactory bulb superficial tufted cell",
        "superficial tufted neuron of the main olfactory bulb",
        "superficial tufted cell of the main olfactory bulb",
    ],
)
CellType.main_olfactory_bulb_tufted_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/mainOlfactoryBulbTuftedNeuron",
    definition="Principle neurons of the mammalian main olfactory bulb.",
    name="main olfactory bulb tufted neuron",
    synonyms=[
        "main olfactory bulb tufted cell",
        "tufted cell of the main olfactory bulb",
        "tufted neuron of the main olfactory bulb",
    ],
)
CellType.microglial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/microglialCell",
    definition="'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106919"),
    name="microglial cell",
)
CellType.motor_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/motorNeuron",
    name="motor neuron",
)
CellType.neocortex_layer2_3_pyramidal_neuron = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/neocortexLayer2-3PyramidalNeuron",
    definition="An excitatory neuron type with a pyramidal-shaped cell body that is located in layer 2/3 of the neocortex.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107387"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NIFEXT:49#neocortex-pyramidal-cell-layer-2-3"),
    name="neocortex layer 2/3 pyramidal neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nifext_49"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0738209"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107403"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/SAO:1866881837#neostriatum-cholinergic-cell"),
    name="neostriatum cholinergic interneuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao1866881837"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107404"),
    name="neostriatum direct pathway spiny neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_149135"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107405"),
    name="neostriatum indirect pathway spiny neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_149136"),
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
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0107497"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0101974"),
    name="Purkinje cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao471801888"),
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
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NLXCELL:100601#spiny-neuron"),
    name="spiny neuron",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_100601"),
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
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0784362"),
    name="striatum medium spiny neuron",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/npo/uris/neurons/35"),
    synonyms=["MSN", "spiny projection neuron", "SPN", "striatal medium spiny neuron"],
)
CellType.vascular_endothelial_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/vascularEndothelialCell",
    definition="Cells that constitute the inner cellular lining of arteries, veins and capillaries.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0112265"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/SAO:1543450574#vascular-endothelial-cell"),
    name="vascular endothelial cell",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/sao1543450574"),
    synonyms=["endothelial cell"],
)
CellType.vascular_smooth_muscle_cell = CellType(
    id="https://openminds.ebrains.eu/instances/cellType/vascularSmoothMuscleCell",
    definition="A smooth muscle cell assocatiated with the vasculature.",
    name="vascular smooth muscle cell",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/CL_0000359"),
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
