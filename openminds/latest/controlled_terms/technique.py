"""
Structured information on the technique.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Technique(LinkedMetadata):
    """
    Structured information on the technique.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Technique"
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


Technique.activation_likelihood_estimation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/activationLikelihoodEstimation",
    definition="An 'activation likelihood estimation' is a coordinate-based meta-analysis of neuroimaging data that determines the above-chance convergence of activation probabilities between experiments (i.e., not between foci). [adapted from [Eickhoff et al., 2011](https://dx.doi.org/10.1016%2Fj.neuroimage.2011.09.017)]",
    name="activation likelihood estimation",
    synonyms=[
        "activation likelihood estimation analysis",
        "activation likelihood estimation meta-analysis",
        "ALE",
        "ALE analysis",
        "ALE meta-analysis",
    ],
)
Technique.activity_modulation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/activityModulationTechnique",
    name="activity modulation technique",
)
Technique.affine_image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/affineImageRegistration",
    definition="A 'affine image registration' is a process of bringing a set of images into the same coordinate system using affine transformation.",
    name="affine image registration",
)
Technique.affine_transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/affineTransformation",
    definition="An 'affine transformation' is a specific linear transformation using combinations of rotations, translations, reflections, scaling and shearing to map coordinates between two coordinate spaces.",
    name="affine transformation",
)
Technique.anaesthesia_administration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/anaesthesiaAdministration",
    name="anaesthesia administration",
)
Technique.anaesthesia_monitoring = Technique(
    id="https://openminds.ebrains.eu/instances/technique/anaesthesiaMonitoring",
    name="anaesthesia monitoring",
)
Technique.anaesthesia_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/anaesthesiaTechnique",
    name="anaesthesia technique",
)
Technique.anatomical_delineation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/anatomicalDelineationTechnique",
    name="anatomical delineation technique",
)
Technique.anterograde_tracing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/anterogradeTracing",
    definition="Anterograde tracing is a technique used to trace axonal projections from their source (the cell body or soma) to their point of termination (the synapse).",
    description="Anterograde tracers are taken up by neuronal cell bodies at the injection site and travel to the axon terminals. Anterograde tracing techniques allow for a detailed assessment of neuronal connections between a target population of neurons and their outputs throughout the nervous system.",
    name="anterograde tracing",
)
Technique.autoradiography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/autoradiography",
    definition="'Autoradiography' is a photography technique that creates images of a radioactive source (e.g., molecules or fragments of molecules that have been radioactively labeled) by the direct exposure to an imaging media (e.g., X-ray film or nuclear emulsion)",
    interlex_identifier="http://uri.interlex.org/base/ilx_0439300",
    name="autoradiography",
)
Technique.average_linkage_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/averageLinkageClustering",
    name="average linkage clustering",
)
Technique.avidin_biotin_complex_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/avidinBiotinComplexStaining",
    name="avidin-biotin complex staining",
    synonyms=["ABC staining"],
)
Technique.beta_galactosidase_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/beta-galactosidaseStaining",
    name="beta-galactosidase staining",
)
Technique.bias_field_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/biasFieldCorrection",
    definition="A 'bias field correction' is a mathematical technique to remove a corrupting, low frequency signal from magnetic resonance images. This bias field signal is typically caused by inhomogeneities in the magnetic ﬁelds of the magnetic resonance imaging machine.",
    name="bias field correction",
    synonyms=["BFC"],
)
Technique.biocytin_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/biocytinStaining",
    definition="In 'biocytin staining' the chemical compound biocytin is used to highlight morphological details of nerve cells.",
    description="Biocytin staining is a technique commonly used in combination with intracellular electrophysiology for post-hoc recovery of morphological details of the studied neurons. For this, the chemical compound biocytin is included in the electrode in order to fill the studied cell. It allows for the visualisation of the dendritic arborization and the regions targeted by the axons of the studied neurons.",
    name="biocytin staining",
    synonyms=["biocytin filling", "biocytin labeling"],
)
Technique.blood_sampling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/bloodSampling",
    definition="'Blood sampling' is the process of obtaining blood from a body for purpose of medical diagnosis and/or evaluation of an indication for treatment, further medical tests or other procedures.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0782225",
    name="blood sampling",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/OBI_1110095",
    synonyms=["blood collection", "blood harvesting"],
)
Technique.bootstrapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/bootstrapping",
    name="bootstrapping",
)
Technique.boundary_based_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/boundaryBasedRegistration",
    definition="The term 'boundary-based registration' refers to feature based image registration methods which utilize a boundary which can be identified in the source and target image.",
    name="boundary-based registration",
    synonyms=["BBR"],
)
Technique.brightfield_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/brightfieldMicroscopy",
    definition="Brightfield microscopy is an optical microscopy techniques, in which illumination light is transmitted through the sample and the contrast is generated by the absorption of light in dense areas of the specimen.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739719",
    name="brightfield microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/238",
)
Technique.calcium_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/calciumImaging",
    name="calcium imaging",
)
Technique.callosotomy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/callosotomy",
    name="callosotomy",
)
Technique.cell_attached_patch_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/cellAttachedPatchClamp",
    definition="'Cell-attached patch clamp' is an intracellular electrophysiology technique that fully preserves the intracellular integrity by forming a megaohm or gigaohm seal, leaving the cell membrane intact.",
    description="Cell-attached patch clamp is a patch clamp recording technique used in electrophysiology in which the intracellular integrity of the cell is preserved. Patches are formed using either a ‘loose seal’ (mega ohm resistance) or a ‘tight seal’ (giga ohm resistance) without rupturing the cell membrane. A loose seal is used for recording action potential currents, whereas a tight seal is required for evoking action potentials in the attached cell and for recording resting and synaptic potentials.",
    name="cell attached patch clamp",
)
Technique.clarity_tde = Technique(
    id="https://openminds.ebrains.eu/instances/technique/CLARITY_TDE",
    name="CLARITY/TDE",
)
Technique.cluster_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/clusterAnalysis",
    name="cluster analysis",
)
Technique.combined_volume_surface_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/combinedVolumeSurfaceRegistration",
    definition="The term 'combined volume-surface registration' refers to an image registration framework which utilizes information from the brain surface and the brain volume to perform the registration (cf. [Postelnicu et al. (2009)](https://doi.org/10.1109/TMI.2008.2004426)).",
    name="combined volume–surface registration",
    synonyms=["CVS registration"],
)
Technique.communication_profiling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/communicationProfiling",
    name="communication profiling",
)
Technique.computer_tomography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/computerTomography",
    definition="'Computer tomogoraphy' is a noninvasive medical imaging technique where a computer generates multiple X-ray scans to obtain detailed internal 3D image of the body.",
    name="computer tomography",
    synonyms=["CAT", "computed axial tomography", "computed tomography", "computertomography", "CT"],
)
Technique.confocal_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/confocalMicroscopy",
    definition="Confocal microscopy is a specialized fluorescence microscopy technique that uses pinholes to reject out-of-focus light.",
    description="Confocal microscopy focuses light onto a defined spot at a specific depth within a fluorescent sample to eliminate out-of-focus glare, and increase resolution and contrast in the micrographs.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739731",
    name="confocal microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/157",
    synonyms=["confocal microscopy technique"],
)
Technique.conjunction_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/conjunctionAnalysis",
    name="conjunction analysis",
)
Technique.connected_component_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/connected-componentAnalysis",
    definition="'connected-component analysis' is an algorithmic application of graph theory, where subsets of connected components are uniquely labeled based on a given heuristic. [adapted from: [wikipedia](https://en.wikipedia.org/wiki/Connected-component_labeling)]",
    name="connected-component analysis",
    synonyms=["CCA", "CCL", "connected-component labeling"],
)
Technique.connectivity_based_parcellation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/connectivityBasedParcellationTechnique",
    name="connectivity based parcellation technique",
)
Technique.contrast_agent_administration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/contrastAgentAdministration",
    definition="A 'contrast agent administration' is a (typically) oral or intraveneous administration of a chemical compound to improve the visibility of internal body structures of a subject in a subsequent imaging technique.",
    name="contrast agent administration",
)
Technique.contrast_enhancement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/contrastEnhancement",
    name="contrast enhancement",
)
Technique.convolution = Technique(
    id="https://openminds.ebrains.eu/instances/technique/convolution",
    definition="In functional analysis, 'convolution' is a mathematical operation on two functions (f and g) producing a third function (f * g) that expresses how the shape of one is modified by the other. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Convolution)]",
    name="convolution",
    synonyms=["convolution technique"],
)
Technique.correlation_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/correlationAnalysis",
    name="correlation analysis",
)
Technique.cortico_cortical_evoked_potential_mapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/cortico-corticalEvokedPotentialMapping",
    definition="Cortico-cortical evoked potential (CCEP) mapping is used to identify the effective connectivity between distinct neuronal populations based on multiple CCEP measurements across (parts of) the brain in response to direct electrical stimulation (typically at various locations).",
    name="cortico-cortical evoked potential mapping",
    synonyms=["CCEP mapping"],
)
Technique.covariance_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/covarianceAnalysis",
    name="covariance analysis",
)
Technique.craniotomy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/craniotomy",
    name="craniotomy",
)
Technique.cryosectioning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/cryosectioning",
    definition="Cutting of specimen in cryo/freezing conditions typically resulting in micromillimeter thin slices.",
    name="cryosectioning",
    synonyms=["cryosection procedure", "frozen section procedure"],
)
Technique.current_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/currentClamp",
    definition="Current clamp is a technique in which the amount of current injected into the cell is controlled, which allows for the detection of changes in the transmembrane voltage resulting from ion channel activity.",
    name="current clamp",
)
Technique.current_source_density_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/currentSourceDensityAnalysis",
    name="current source density analysis",
)
Technique.cytoarchitectonic_mapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/cytoarchitectonicMapping",
    definition="'Cytoarchitectonic mapping' is a delineation technique that defines regional borders based on histological analysis of the cellular composition of the studied tissue.",
    name="cytoarchitectonic mapping",
)
Technique.da_pi_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/DAPiStaining",
    definition="A nuclear-specific staining technique where DAPi (4′,6-diamidino-2-phenylindole) is used as a dye.",
    description="DAPi, or 4′,6-diamidino-2-phenylindole, is a blue fluorescent dye that bind strongly to adenine-thymine (AT) rich regions in DNA. It is used extensively in fluorescence microscopy and can be used on both fixated and living cells.",
    name="DAPi staining",
    synonyms=["4′,6-diamidino-2-phenylindole staining", "DAPi stain"],
)
Technique.dab_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/DABStaining",
    definition="In a 'DAB staining', the organic compound DAB (3, 3'-diaminobenzidine) is oxidized in presence of peroxidase and hydrogen peroxide resulting in deposition of a brown, alcohol-insoluble precipitate which can be used in immunohistochemical and blotting applications.",
    name="DAB staining",
    synonyms=["3,3′-Diaminobenzidine staining"],
)
Technique.deep_learning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/deepLearning",
    name="deep learning",
)
Technique.density_measurement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/densityMeasurement",
    name="density measurement",
)
Technique.dictionary_learning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/dictionaryLearning",
    definition="'Dictionary learning' is a branch of signal processing and machine learning that aims at finding a frame (called dictionary) in which some training data admits a sparse representation.",
    name="dictionary learning",
    synonyms=["sparse dictionary learning"],
)
Technique.diffeomorphic_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/diffeomorphicRegistration",
    definition="'Diffeomorphic registration' refers to a suite of algorithms that register or build correspondences between dense coordinate systems in medical imaging by ensuring the solutions are diffeomorphic.",
    name="diffeomorphic registration",
    synonyms=["diffeomorphic mapping", "large deformation diffeomorphic metric mapping"],
)
Technique.diffusion_fixation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/diffusionFixationTechnique",
    definition="Diffusion fixation is a fixation technique to preserve specimen permanently as faithfully as possible compared to the living state by submerging specimen in a fixative.",
    name="diffusion fixation technique",
    synonyms=["drop fixation"],
)
Technique.diffusion_tensor_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/diffusionTensorImaging",
    name="diffusion tensor imaging",
)
Technique.diffusion_weighted_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/diffusionWeightedImaging",
    name="diffusion-weighted imaging",
)
Technique.dna_methylation_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/DNAMethylationAnalysis",
    definition="A 'DNA methylation analysis' studies chromosomal patterns of DNA or histone modification by methyl groups ([modified from Nature.com](https://www.nature.com/subjects/methylation-analysis)).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0779582",
    name="DNA methylation analysis",
    synonyms=["methylation analysis"],
)
Technique.dna_sequencing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/DNASequencing",
    definition="'DNA sequencing' refers to a group of techniques that are used to determine the order of nucleotides (nucleic acid sequence) in DNA. [adapted from [wikipedia](https://en.wikipedia.org/wiki/DNA_sequencing)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0783031",
    name="DNA sequencing",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/OBI_0000626",
    synonyms=[
        "deoxyribonucleic acid sequencing",
        "deoxyribonucleic acid sequencing assay",
        "DNA sequencing assay",
        "DNA-Seq",
    ],
)
Technique.dual_view_inverted_selective_plane_illumination_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/dualViewInvertedSelectivePlaneIlluminationMicroscopy",
    definition="Dual-view inverted selective plane illumination microscopy is a specialized light sheet microscopy technique that allows for dual views of the samples while mounted on an inverted microscope.",
    name="dual-view inverted selective plane illumination microscopy",
    synonyms=[
        "diSPIM",
        "dual-view inverted light sheet fluorescence microscopy",
        "dual-view inverted light sheet microscopy",
    ],
)
Technique.echo_planar_pulse_sequence = Technique(
    id="https://openminds.ebrains.eu/instances/technique/echoPlanarPulseSequence",
    definition="In magnetic resonance imaging, a 'echo-planar pulse sequence' is a contrasting technique where each radio frequency field (RF) excitation is followed by a train of gradient echoes with different spatial encoding allowing for very rapid scanning. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Physics_of_magnetic_resonance_imaging#Echo-planar_imaging)]",
    name="echo planar pulse sequence",
    synonyms=["echo-planar imaging"],
)
Technique.electrocardiography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electrocardiography",
    definition="Electrocardiography is a non-invasive technique used to record the electrical activity of a heart using electrodes placed on the skin. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Electrocardiography)]",
    name="electrocardiography",
    synonyms=["ECG"],
)
Technique.electrocorticography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electrocorticography",
    definition="'Electrocorticography', short ECoG, is an intracranial electroencephalography technique in which electrodes are placed (subdural or epidural) on the exposed surface of the brain to record electrical activity from the cerebral cortex.",
    name="electrocorticography",
    synonyms=["ECoG"],
)
Technique.electroencephalography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electroencephalography",
    name="electroencephalography",
)
Technique.electromyography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electromyography",
    name="electromyography",
)
Technique.electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electronMicroscopy",
    definition="Electron microscopy describes any microscopy technique that uses electrons to generate contrast.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739513",
    name="electron microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/electronMicroscopy",
    synonyms=["EM"],
)
Technique.electron_tomography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electronTomography",
    definition="Electron tomography is a microscopy technique that takes a series of images of a thick sample at different angles (tilts) so that tomography can be applied to increase the resolution of the ticker sample.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0461087",
    name="electron tomography",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0512939",
    synonyms=["electron microscope tomography"],
)
Technique.electrooculography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electrooculography",
    name="electrooculography",
)
Technique.electroporation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/electroporation",
    definition="A microbiology technique in which an electrical field is applied to cells in order to increase the permeability of the cell membrane.",
    description="'Electroporation' is a process in which a significant increase in the electrical conductivity and permeability of the cell plasma membrane is caused by an externally applied electrical field. It is usually used in molecular biology as a way of introducing some substance into a cell, such as loading it with a molecular probe, a drug that can change the cell's function, or a piece of coding DNA.",
    interlex_identifier="http://uri.interlex.org/ilx_0739748",
    name="electroporation",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/electroporation",
    synonyms=["electropermeabilization"],
)
Technique.enzyme_linked_immunosorbent_assay = Technique(
    id="https://openminds.ebrains.eu/instances/technique/enzymeLinkedImmunosorbentAssay",
    definition="The 'enzyme-linked immunosorbent assay' is a commonly used analytical biochemistry assay for the quantitative determination of antibodies, first described by [Engvall and Perlmann (1972)](https://www.jimmunol.org/content/109/1/129.abstract). [adapted from [wikipedia](https://en.wikipedia.org/wiki/ELISA)]",
    description="This immunoassay utilizes an antibody labeled with an enzyme marker such as horseradish peroxidase. While either the enzyme or the antibody is bound to an immunosorbent substrate, they both retain their biologic activity; the change in enzyme activity as a result of the enzyme-antibody-antigen reaction is proportional to the concentration of the antigen and can be measured spectrophotometrically or with the naked eye. Many variations of the method have been developed.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0484188",
    name="enzyme-linked immunosorbent assay",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0007526",
    synonyms=["ELISA"],
)
Technique.epidermal_electrophysiology_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/epidermalElectrophysiologyTechnique",
    definition="The term 'epidermal electrophysiology technique' describes a subclass of non-invasive electrophysiology techniques where one or several electrodes are placed on the outermost cell layer of an organism (epidermis) to measure electrical properties.",
    name="epidermal electrophysiology technique",
    synonyms=["epidermal electrophysiology"],
)
Technique.epidural_electrocorticography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/epiduralElectrocorticography",
    name="epidural electrocorticography",
)
Technique.epifluorescent_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/epifluorescentMicroscopy",
    definition="Epifluorescent microscopy comprises all widefield microscopy techniques in which fluorescent molecules of an entire sample are excited through a permanent exposure of a light source of a specific wavelength.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739632",
    name="epifluorescent microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/243",
    synonyms=[
        "epifluorescence microscopy",
        "WFM",
        "widefield epifluorescence microscopy",
        "widefield fluorescence microscopy",
    ],
)
Technique.extracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/extracellularElectrophysiology",
    definition="In 'extracellular electrophysiology' electrodes are inserted into living tissue, but remain outside the cells in the extracellular environment to measure or stimulate electrical activity coming from adjacent cells, usually neurons.",
    name="extracellular electrophysiology",
)
Technique.eye_movement_tracking = Technique(
    id="https://openminds.ebrains.eu/instances/technique/eyeMovementTracking",
    definition="'Eye movement tracking' refers to a group of techniques used to measure the eye movement and/or position of a living specimen over a given period of time.",
    interlex_identifier="http://uri.interlex.org/ilx_0417680",
    name="eye movement tracking",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0493574",
    synonyms=["eye motion tracking", "eye tracking"],
)
Technique.fixation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/fixationTechnique",
    definition="Fixation is a technique to preserve specimen permanently as faithfully as possible compared to the living state.",
    description="Fixation is a two-step process in which 1) all normal life functions are terminated and 2) the structure of the tissue is stabilized (preserved). The fixation of tissue can be achieved by chemical or physical (e.g. heating, freezing) means.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739717",
    name="fixation technique",
)
Technique.fluorescence_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/fluorescenceMicroscopy",
    definition="Fluorescence microscopy comprises any type of microscopy where the specimen can be made to fluoresce (emit energy as visible light), typically by illuminating it with light of specific wavelengths.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0780848",
    name="fluorescence microscopy",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHMO_0000087",
)
Technique.focused_ion_beam_scanning_electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/focusedIonBeamScanningElectronMicroscopy",
    definition="Focused ion beam scanning electron microscopy is a serial section scanning electron microscopy technique where a focused ion beam is used to ablate the surface of a specimen.",
    interlex_identifier="http://uri.interlex.org/ilx_0739434",
    name="focused ion beam scanning electron microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/245",
    synonyms=["FIB-SEM", "FIB/SEM", "FIBSEM", "focused ion beam scanning electron microscoscopy technique"],
)
Technique.four_points_congruent_sets_alignment = Technique(
    id="https://openminds.ebrains.eu/instances/technique/4PointsCongruentSetsAlignment",
    definition="4-points congruent sets alignment is a fast and robust alignment technique for 3D point sets without pre-filtering or denoising the data, even if the data are noisy and/or contaminated with outliers ([Aiger et al., 2008](https://doi.org/10.1145/1360612.1360684)).",
    name="4-points congruent sets alignment",
    synonyms=[
        "4-points congruent sets",
        "4-points congruent sets registration",
        "4PCS",
        "4PCS alignment",
        "4PCS registration",
    ],
)
Technique.functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/functionalMagneticResonanceImaging",
    name="functional magnetic resonance imaging",
)
Technique.gene_expression_measurement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/geneExpressionMeasurement",
    name="gene expression measurement",
)
Technique.gene_knockin = Technique(
    id="https://openminds.ebrains.eu/instances/technique/geneKnockin",
    name="gene knockin",
)
Technique.gene_knockout = Technique(
    id="https://openminds.ebrains.eu/instances/technique/geneKnockout",
    name="gene knockout",
)
Technique.general_linear_modeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/generalLinearModeling",
    name="general linear modeling",
)
Technique.genetic_correlation_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/geneticCorrelationAnalysis",
    name="genetic correlation analysis",
)
Technique.genetic_risk_score = Technique(
    id="https://openminds.ebrains.eu/instances/technique/geneticRiskScore",
    definition="A genetic risk score is an estimate of the cumulative contribution of genetic factors to a specific outcome of interest in an individual (Igo et al, 2019).",
    description="[described in: Igo, R. P., Jr, Kinzy, T. G., & Cooke Bailey, J. N. (2019). Genetic Risk Scores. Current protocols in human genetics, 104(1), e95. https://doi.org/10.1002/cphg.95]",
    name="genetic risk score",
    synonyms=["GRS"],
)
Technique.genome_wide_association_study = Technique(
    id="https://openminds.ebrains.eu/instances/technique/genomeWideAssociationStudy",
    definition="A 'genome-wide association study' is an analysis technique comparing the allele frequencies of all available (or a whole genome representative set of) polymorphic markers in unrelated individuals with a specific symptom or disease condition, and those of healthy controls to identify markers associated with a specific disease or condition.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104603",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXINV:1005075#genome-association-studies",
    name="genome-wide association study",
    preferred_ontology_identifier="http://edamontology.org/topic_3517",
    synonyms=[
        "genetic association study",
        "genome association studies",
        "GWAS",
        "GWAS analysis",
        "GWA study",
        "whole genome association study",
        "WGA study",
        "WGAS",
    ],
)
Technique.global_signal_regression = Technique(
    id="https://openminds.ebrains.eu/instances/technique/globalSignalRegression",
    definition="A 'global signal regression' is a denoising technique where the global signal is removed from the time series of each voxel through linear regression. [adapted from: [Murphy & Fox, 2017](https://dx.doi.org/10.1016%2Fj.neuroimage.2016.11.052)]",
    name="global signal regression",
    synonyms=["GSR"],
)
Technique.golgi_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/GolgiStaining",
    definition="'Golgi staining' includes several silver staining techniques in which fixed tissue is impregnated with silver nitrate and potassium dichromate resulting in the complete staining of some nerve cells while other cells are not stained at all. [adapted from InterLex](http://uri.interlex.org/ilx_0104713)",
    interlex_identifier="http://uri.interlex.org/ilx_0104713",
    name="Golgi staining",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/birnlex_2243",
    synonyms=["Golgi method", "black reaction"],
)
Technique.gradient_echo_pulse_sequence = Technique(
    id="https://openminds.ebrains.eu/instances/technique/gradientEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'gradient-echo pulse sequence' is a contrast generation technique that rapidly induces bulk changes in the spin magnetization of a sample by applying a series of carefully constructed pulses so that the change in the gradient of the magnetic field is maximized, trading contrast for speed (cf. [Hargreaves (2012)](https://doi.org/10.1002/jmri.23742)).",
    name="gradient-echo pulse sequence",
    synonyms=["GRE pulse sequence"],
)
Technique.grubbs_test = Technique(
    id="https://openminds.ebrains.eu/instances/technique/GrubbsTest",
    definition="The 'Grubbs test' is a statistical test, first published by [Grubbs (1950)](https://doi.org/10.1214/aoms/1177729885), used to detect outliers in univariate data that are assumed to come from a normally distributed population. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Grubbs%27s_test)]",
    name="Grubbs' test",
    synonyms=["extreme studentized deviate test", "Grubbs test", "maximum normalized residual test"],
)
Technique.he_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/HEStaining",
    definition="An 'H&E staining' combines the two histological stains hematoxylin and eosin which highlight a large portion of microscopic anatomy in a tissue. It is therefore the most widely used stain in medical and histopathological diagnosis.",
    name="H&E staining",
    synonyms=["HE staining", "hematoxylin and eosin staining", "hematoxylin-eosin staining"],
)
Technique.heavy_metal_negative_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/heavyMetalNegativeStaining",
    definition="In a 'heavy metal negative staining', a thin and amorphous film of heavy metal salts (e.g. uranyl acetate) is applied on a sample to reveal its structural details for electron microscopy.",
    name="heavy metal negative staining",
    synonyms=["heavy metal salt staining", "heavy metal staining", "negative staining"],
)
Technique.hierarchical_agglomerative_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/hierarchicalAgglomerativeClustering",
    name="hierarchical agglomerative clustering",
)
Technique.hierarchical_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/hierarchicalClustering",
    name="hierarchical clustering",
)
Technique.hierarchical_divisive_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/hierarchicalDivisiveClustering",
    name="hierarchical divisive clustering",
)
Technique.high_density_electroencephalography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/highDensityElectroencephalography",
    name="high-density electroencephalography",
)
Technique.high_field_functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/highFieldFunctionalMagneticResonanceImaging",
    name="high-field functional magnetic resonance imaging",
)
Technique.high_field_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/highFieldMagneticResonanceImaging",
    name="high-field magnetic resonance imaging",
)
Technique.high_resolution_scanning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/high-resolutionScanning",
    name="high-resolution scanning",
)
Technique.high_speed_video_recording = Technique(
    id="https://openminds.ebrains.eu/instances/technique/high-speedVideoRecording",
    name="high-speed video recording",
)
Technique.high_throughput_scanning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/highThroughputScanning",
    definition="'High-throughput scanning' is a technique for automatic creation of analog or digital images of a large number of samples.",
    name="high-throughput scanning",
    synonyms=["high throughput scanning"],
)
Technique.histochemistry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/histochemistry",
    name="histochemistry",
)
Technique.hoechst_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/HoechstStaining",
    definition="A nuclear-specific staining technique where a Hoechst dye is used.",
    description="Hoechst dyes are part of a family of blue fluorescent dye that bind to DNA. It acts similarly as DAPi and can also be used on both fixated and living cells.",
    name="Hoechst staining",
    synonyms=["Hoechst stain"],
)
Technique.hpc_simulation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/HPCSimulation",
    name="HPC simulation",
    synonyms=["High Performance Computing simulation"],
)
Technique.ica_based_denoising_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/ICABasedDenoisingTechnique",
    definition="An 'ICA based denoising technique' removes independent components from input data to reduce noise while preserving the features of interest in the data.",
    name="ICA based denoising technique",
    synonyms=[
        "ICA based denoising",
        "ICA based denoising method",
        "ICA-based denoising",
        "ICA-based denoising method",
        "ICA-based denoising technique",
        "independent component analysis based denoising technique",
    ],
)
Technique.image_distortion_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/imageDistortionCorrection",
    definition="'Image distortion correction' is the general term for any image processing technique correcting optical or perspective aberrations of an image.",
    name="image distortion correction",
)
Technique.image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/imageRegistration",
    definition="An 'image registration' is a process of bringing a set of images into the same coordinate system.",
    name="image registration",
    synonyms=["spatial registration"],
)
Technique.immunohistochemistry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/immunohistochemistry",
    definition="In 'immunohistochemistry' antigens or haptens are detected and visualized in cells of a tissue sections by exploiting the principle of antibodies binding specifically to antigens in biological tissues.",
    name="immunohistochemistry",
    synonyms=["IHC"],
)
Technique.immunoprecipitation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/immunoprecipitation",
    name="immunoprecipitation",
)
Technique.implant_surgery = Technique(
    id="https://openminds.ebrains.eu/instances/technique/implantSurgery",
    name="implant surgery",
)
Technique.in_situ_hybridisation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/inSituHybridisation",
    name="in situ hybridisation",
)
Technique.independent_component_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/independentComponentAnalysis",
    name="independent component analysis",
)
Technique.infrared_differential_interference_contrast_video_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/infraredDifferentialInterferenceContrastVideoMicroscopy",
    interlex_identifier="http://uri.interlex.org/ilx_0739494",
    name="infrared differential interference contrast video microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/IRDIC",
    synonyms=["IR DIC video microscopy", "IR-DIC"],
)
Technique.injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/injection",
    name="injection",
)
Technique.inter_subject_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/interSubjectAnalysis",
    name="inter-subject analysis",
)
Technique.interpolation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/interpolation",
    definition="An 'interpolation' is an analysis technique that delivers estimates for new data points based on a range of a discrete set of known data points.",
    name="interpolation",
)
Technique.intra_subject_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intraSubjectAnalysis",
    name="intra-subject analysis",
)
Technique.intracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intracellularElectrophysiology",
    definition="A technique used to measure electrical properties of a single cell, e.g. a neuron.",
    description="'Intracellular electrophysiology' describes a group of techniques used to measure with precision the voltage across, or electrical currents passing through, neuronal or other cellular membranes by inserting an electrode inside the neuron.",
    interlex_identifier="http://uri.interlex.org/ilx_0739521",
    name="intracellular electrophysiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/222",
    synonyms=["intracellular recording"],
)
Technique.intracellular_injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intracellularInjection",
    name="intracellular injection",
)
Technique.intracranial_electroencephalography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intracranialElectroencephalography",
    name="intracranial electroencephalography",
)
Technique.intraperitoneal_injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intraperitonealInjection",
    definition="An 'intraperitoneal injection' is the administration of a substance into the peritoneum (abdominal cavity) via a needle or tube.",
    name="intraperitoneal injection",
    synonyms=["i.p.", "i.p. injection", "IP", "IP injection"],
)
Technique.intravenous_injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/intravenousInjection",
    definition="An 'intravenous injection' is the administration of a substance into a vein or veins via a needle or tube.",
    name="intravenous injection",
    synonyms=["i.v.", "i.v. injection", "IV", "IV injection"],
)
Technique.iontophoresis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/iontophoresis",
    name="iontophoresis",
)
Technique.iontophoretic_microinjection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/iontophoreticMicroinjection",
    name="iontophoretic microinjection",
)
Technique.k_means_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/k-meansClustering",
    definition="'k-means clustering' is a centroid-based cluster analysis technique that aims to partition n observations into a pre-defined number of k clusters by assigning each observation to the cluster with the nearest mean (centroid).",
    name="k-means clustering",
    synonyms=["k-means", "k-means cluster analysis"],
)
Technique.light_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/lightMicroscopy",
    definition="Light microscopy, also referred to as optical microscopy, comprises any type of microscopy technique that uses visible light to generate magnified images of small objects.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0780269",
    name="light microscopy",
    preferred_ontology_identifier="http://edamontology.org/topic_3385",
    synonyms=["LM", "optical microscopy"],
)
Technique.light_sheet_fluorescence_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/lightSheetFluorescenceMicroscopy",
    definition="Lightsheet fluorescence microscopy is a fluorescence microscopy technique that uses a thin sheet of light to excite only fluorophores within the plane of illumination.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739693",
    name="light sheet fluorescence microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/lightSheetMicroscopyFluorescent",
    synonyms=["light sheet microscopy", "LSFM", "selective plane illumination microscopy", "SPIM"],
)
Technique.linear_image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/linearImageRegistration",
    definition="A 'linear image registration' is a process of bringing a set of images into the same coordinate system using linear transformation.",
    name="linear image registration",
)
Technique.linear_regression = Technique(
    id="https://openminds.ebrains.eu/instances/technique/linearRegression",
    definition="A 'linear regression' is an analysis approach for modelling the linear relationship between a scalar response and one or more explanatory variables.",
    name="linear regression",
)
Technique.linear_transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/linearTransformation",
    definition="A 'linear transformation' is a linear mathematical function to map coordinates between two different coordinate systems while preserving straight lines.",
    name="linear transformation",
)
Technique.literature_mining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/literatureMining",
    name="literature mining",
)
Technique.magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/magneticResonanceImaging",
    definition="'Magnetic resonance imaging' is a medical imaging technique that uses strong magnetic fields, magnetic field gradients, and radio waves to generate images of the anatomy and the physiological processes of the body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741208",
    name="magnetic resonance imaging",
)
Technique.magnetic_resonance_spectroscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/magneticResonanceSpectroscopy",
    name="magnetic resonance spectroscopy",
)
Technique.magnetoencephalography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/magnetoencephalography",
    definition="'Magnetoencephalography' is a noninvasive neuroimaging technique for studying brain activity by recording magnetic fields produced by electrical currents occurring naturally in the brain, using very sensitive magnetometers. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Magnetoencephalography)]",
    interlex_identifier="http://uri.interlex.org/ilx_0741209",
    name="magnetoencephalography",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/163",
    synonyms=["MEG"],
)
Technique.manifold_learning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/manifoldLearning",
    definition="'manifold learning' refers to a group of machine learning algorithms for non-linear dimensionality reduction of high-dimensionalty data.",
    name="manifold learning",
)
Technique.mann_whitney_u_test = Technique(
    id="https://openminds.ebrains.eu/instances/technique/MannWhitneyUTest",
    definition="The 'Mann–Whitney U test' is a nonparametric test of the null hypothesis that, for randomly selected values X and Y from two populations, the probability of X being greater than Y is equal to the probability of Y being greater than X. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)]",
    name="Mann–Whitney U test",
    synonyms=[
        "Mann–Whitney–Wilcoxon test",
        "MWU test",
        "MWW test",
        "Wilcoxon rank-sum test",
        "Wilcoxon–Mann–Whitney test",
        "WMW test",
    ],
)
Technique.mass_spectrometry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/massSpectrometry",
    name="mass spectrometry",
)
Technique.mass_univariate_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/massUnivariateAnalysis",
    definition="A 'mass univariate analysis' is the statistical analysis of a massive number of simultaneously measured dependent variables via the performance of univariate hypothesis tests.",
    name="mass univariate analysis",
)
Technique.maximum_likelihood_estimation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/maximumLikelihoodEstimation",
    definition="'Maximum likelihood estimation' is a statistical analysis technique that estimates the parameters of an assumed probability distribution for some observed data by maximizing a likelihood function so that, under the assumed statistical model, the observed data is most probable. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)]",
    name="maximum likelihood estimation technique",
    synonyms=["MLE", "maximum likelihood estimation technique"],
)
Technique.maximum_probability_projection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/maximumProbabilityProjection",
    name="maximum probability projection",
)
Technique.meta_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/metaAnalysis",
    name="meta-analysis",
)
Technique.meta_analytic_connectivity_modeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/metaAnalyticConnectivityModeling",
    name="meta-analytic connectivity modeling",
)
Technique.metadata_parsing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/metadataParsing",
    name="metadata parsing",
)
Technique.microtome_sectioning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/microtomeSectioning",
    definition="A technique used to cut specimen in thin slices using a microtome.",
    description="The microtome cutting thickness can range between 50 nanometer and 100 micrometer.",
    interlex_identifier="http://uri.interlex.org/ilx_0739422",
    name="microtome sectioning",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/212",
    synonyms=["microtomy"],
)
Technique.model_based_stimulation_artifact_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/modelBasedStimulationArtifactCorrection",
    definition="The 'model-based stimulation artifact correction' is a model-based analysis technique for removing stimulation artifacts from intracranial electroencephalography signals to uncover the cortico-cortical evoked potentials caused by the stimulation (cf. [Trebaul et al. (2016)](https://doi.org/10.1016/j.jneumeth.2016.03.002)).",
    name="model-based stimulation artifact correction",
    synonyms=["model-based artifact correction"],
)
Technique.morphometric_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/morphometricAnalysis",
    name="morphometric analysis",
)
Technique.morphometry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/morphometry",
    name="morphometry",
)
Technique.motion_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/motionCorrection",
    definition="'Motion correction' is the general term for any preprocessing analysis technique used to correct for motion artifacts in imaging time-series.",
    name="motion correction",
)
Technique.movement_tracking = Technique(
    id="https://openminds.ebrains.eu/instances/technique/movementTracking",
    definition="'Movement tracking' refers to a group of techniques used to measure the movement and/or position of an object, specimen, or anatomical parts of a specimen over a given period of time.",
    name="movement tracking",
    synonyms=["motion tracking"],
)
Technique.multi_compartment_modeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multi-compartmentModeling",
    name="multi-compartment modeling",
)
Technique.multi_electrode_extracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multiElectrodeExtracellularElectrophysiology",
    name="multi-electrode extracellular electrophysiology",
)
Technique.multi_scale_individual_component_clustering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multi-scaleIndividualComponentClustering",
    definition="'multi-scale individual component clustering' is a multi-scale, unsupervised cluster analysis technique to group individual, independent components of a single-object/single-subject independent component analysis (ICA) from an object-pool/subject-pool (cf. [Naveau et al, 2012](https://doi.org/10.1007/s12021-012-9145-2)).",
    name="multi-scale individual component clustering",
    synonyms=["MICCA", "multi-scale individual component cluster algorithm"],
)
Technique.multi_voxel_pattern_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multiVoxelPatternAnalysis",
    definition="A 'multi-voxel pattern analysis' is considered as a supervised classification problem where a classifier attempts to capture the relationships between spatial patterns of functional magnetic resonance imaging activity and experimental conditions ([Mahmoudi et al., 2012](https://doi.org/10.1155/2012/961257), [Davatzikos et al., 2005](https://doi.org/10.1016/j.neuroimage.2005.08.009)).",
    name="multi-voxel pattern analysis",
    synonyms=["MVPA"],
)
Technique.multiple_linear_regression = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multipleLinearRegression",
    definition="A 'multiple linear regression' is a linear approach for modelling the relationship between a scalar response and multiple explanatory variables. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Linear_regression)]",
    name="multiple linear regression",
    synonyms=["MLR", "multi-linear regression", "multilinear regression", "multiple regression"],
)
Technique.multiple_whole_cell_patch_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/multipleWholeCellPatchClamp",
    name="multiple whole cell patch clamp",
)
Technique.myelin_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/myelinStaining",
    definition="A technique used to selectively alter the appearance of myelin (sheaths) that surround the nerve cell axons.",
    interlex_identifier="http://uri.interlex.org/ilx_0107265",
    name="myelin staining",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/birnlex_2248",
)
Technique.neuromorphic_simulation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/neuromorphicSimulation",
    name="neuromorphic simulation",
)
Technique.nissl_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/NisslStaining",
    definition="The term 'Nissl staining' refers to various basic dyes (e.g., aniline, thionine, cresyl violet) that selectively label negatively charged molecules (e.g., DNA, RNA) and are therefore typically used to highlight important structural features of cell bodies.",
    name="Nissl staining",
    synonyms=["Nissl", "Nissl method"],
)
Technique.nonlinear_image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nonlinearImageRegistration",
    definition="A 'nonlinear image registration' is a process of bringing a set of images into the same coordinate system using nonlinear transformation.",
    name="nonlinear image registration",
    synonyms=["non-linear image registration"],
)
Technique.nonlinear_transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nonlinearTransformation",
    definition="A 'nonlinear transformation' is a mathematical function to map coordinates between two different coordinate systems, not preserving straight lines.",
    name="nonlinear transformation",
    synonyms=["non-linear transformation"],
)
Technique.nonrigid_image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nonrigidImageRegistration",
    definition="A 'nonrigid image registration' is a process of bringing a set of images into the same coordinate system using nonrigid transformation.",
    name="nonrigid image registration",
    synonyms=["non-rigid image registration"],
)
Technique.nonrigid_motion_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nonrigidMotionCorrection",
    name="nonrigid motion correction",
    synonyms=["non-rigid motion correction"],
)
Technique.nonrigid_transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nonrigidTransformation",
    definition="A 'nonrigid transformation' is a specific linear transformation using combinations of rotations, translations, reflections, scaling, shearing, and perspective projections to map coordinates between two coordinate spaces.",
    name="nonrigid transformation",
    synonyms=["non-rigid transformation"],
)
Technique.nucleic_acid_extraction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nucleicAcidExtraction",
    definition="'Nucleic acid extraction' refers to a group of techniques that all separate nucleic acids from proteins and lipids using three major processes: isolation, purification, and concentration.",
    name="nucleic acid extraction",
)
Technique.nuisance_regression = Technique(
    id="https://openminds.ebrains.eu/instances/technique/nuisanceRegression",
    definition="'Nuisance regression' is an image processing technique which seeks to attenuate non-neural BOLD fluctuations from measurable noise sources such as scanner drift and head motion, as well as periodic physiological signals. [adapted from [Hallquist et al. 2013](https://doi.org/10.1016%2Fj.neuroimage.2013.05.116)]",
    name="nuisance regression",
    synonyms=["NR"],
)
Technique.optogenetic_inhibition = Technique(
    id="https://openminds.ebrains.eu/instances/technique/optogeneticInhibition",
    definition="Optogenetic inhibition is a genetic technique in which the activity of specific neuron populations is decreased using light of a particular wavelength. This can be achieved by expressing light-sensitive ion channels, pumps or enzymes specifically in the target neurons.",
    name="optogenetic inhibition",
)
Technique.oral_administration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/oralAdministration",
    definition="In an 'oral administration' a substance is taken through the mouth.",
    name="oral administration",
    synonyms=["p.o.", "per os", "PO"],
)
Technique.organ_extraction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/organExtraction",
    name="organ extraction",
)
Technique.patch_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/patchClamp",
    name="patch clamp",
)
Technique.pathway_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/pathwayAnalysis",
    definition="A 'pathway analysis' refers to a group of techniques that aim to discover what biological themes, and which biomolecules, are crucial to understand biological pathways of (typically) high-throughput biological data (adapted from [García-Campos et al., 2015](https://doi.org/10.3389/fphys.2015.00383)).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0778897",
    name="pathway analysis",
    preferred_ontology_identifier="http://edamontology.org/operation_3928",
    synonyms=[
        "biological pathway modelling",
        "biological pathway prediction",
        "functional enrichment analysis",
        "functional pathway analysis",
        "PA",
        "pathway comparison",
        "pathway modelling",
        "pathway prediction",
        "pathway simulation",
    ],
)
Technique.performance_profiling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/performanceProfiling",
    name="performance profiling",
)
Technique.perfusion_fixation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/perfusionFixationTechnique",
    definition="Perfusion fixation is a fixation technique to preserve specimen permanently as faithfully as possible compared to the living state by using the vascular system to distribute fixatives throughout the tissue.",
    name="perfusion fixation technique",
)
Technique.perfusion_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/perfusionTechnique",
    definition="Perfusion is a technique to distribute fluid through the circulatory system or lymphatic system to an organ or a tissue.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739602",
    name="perfusion technique",
)
Technique.perturbational_complexity_index_measurement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/perturbationalComplexityIndexMeasurement",
    name="perturbational complexity index measurement",
)
Technique.phase_contrast_x_ray_computed_tomography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/phaseContrastXRayComputedTomography",
    definition="'Phase-contrast x-ray computed tomography' is a non-invasive x-ray imaging technique for three-dimensional observation of organic matter without application of a contrast medium ([Momose, Takeda, and Itai (1995)](https://doi.org/10.1063/1.1145931)).",
    name="phase‐contrast x‐ray computed tomography",
    synonyms=[
        "PCT",
        "PCX‐CT",
        "phase‐contrast computed tomography",
        "phase‐contrast CT",
        "x-ray phase-contrast computed tomography",
    ],
)
Technique.phase_contrast_x_ray_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/phaseContrastXRayImaging",
    definition="'Phase-contrast x-ray imaging' is a general term for different x-ray techniques that use changes in the phase of an x-ray beam passing through an object leading to images with improved soft tissue contrast without the application of a contrast medium. (adapted from [Wikipedia](https://en.wikipedia.org/wiki/Phase-contrast_X-ray_imaging))",
    name="phase-contrast x-ray imaging",
    synonyms=["phase-sensitive x-ray imaging"],
)
Technique.phase_synchronization_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/phaseSynchronizationAnalysis",
    definition="A 'phase synchronization analysis' detects and quantifies synchronization between two time series.",
    name="phase synchronization analysis",
    synonyms=["PS analysis", "PSA"],
)
Technique.photoactivation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/photoactivation",
    name="photoactivation",
)
Technique.photoinactivation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/photoinactivation",
    name="photoinactivation",
)
Technique.photoplethysmography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/photoplethysmography",
    definition="Photoplethysmography is a non-invasive technique to optically detect blood volume changes in the micro-vascular bed of tissue by measuring the transmissive absorption and/or the reflection of light by the skin.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0487650",
    name="photoplethysmography",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0026056",
    synonyms=["PPG"],
)
Technique.polarized_light_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/polarizedLightMicroscopy",
    definition="Polarized light microscopy comprises all optical microscopy techniques involving polarized light.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0485478",
    name="polarized light microscopy",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0013816",
)
Technique.population_receptive_field_mapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/populationReceptiveFieldMapping",
    name="population receptive field mapping",
)
Technique.positron_emission_tomography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/positronEmissionTomography",
    name="positron emission tomography",
)
Technique.pressure_injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/pressureInjection",
    definition="Pressure injection uses either air compression or mechanical pressure to eject a substance from a micropipette (from Veith et al., 2016; J.Vis.Exp. (109):53724; doi: 10.3791/53724).",
    name="pressure injection",
)
Technique.primary_antibody_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/primaryAntibodyStaining",
    name="primary antibody staining",
)
Technique.principal_component_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/principalComponentAnalysis",
    definition="A 'principal component analysis' is a statistical technique for reducing the dimensionality of a dataset by linearly transforming the data into a new coordinate system where (most of) the variation in the data can be described with fewer dimensions than the initial data. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)]",
    name="principal component analysis",
    synonyms=["PCA"],
)
Technique.probabilistic_anatomical_parcellation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/probabilisticAnatomicalParcellationTechnique",
    name="probabilistic anatomical parcellation technique",
)
Technique.probabilistic_diffusion_tractography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/probabilisticDiffusionTractography",
    name="probabilistic diffusion tractography",
)
Technique.pseudo_continuous_arterial_spin_labeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/pseudoContinuousArterialSpinLabeling",
    name="pseudo-continuous arterial spin labeling",
)
Technique.psychological_testing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/psychologicalTesting",
    definition="'Psychological testing' is a psychometric measurement to evaluate a person's response to a psychological test according to carefully prescribed guidelines. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Psychological_testing)]",
    name="psychological testing",
)
Technique.pupillometry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/pupillometry",
    definition="Pupillometry is the measurement of minute fluctuations in pupil diameter in response to a stimulus.",
    name="pupillometry",
)
Technique.qualitative_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/qualitativeAnalysis",
    definition="'Qualitative analysis' uses subjective judgment to analyze data based on non-quantifiable information. The resulting data are typically nonnumerical.",
    name="qualitative analysis",
)
Technique.quantification = Technique(
    id="https://openminds.ebrains.eu/instances/technique/quantification",
    name="quantification",
)
Technique.quantitative_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/quantitativeAnalysis",
    name="quantitative analysis",
)
Technique.quantitative_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/quantitativeMagneticResonanceImaging",
    name="quantitative magnetic resonance imaging",
)
Technique.receptive_field_mapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/receptiveFieldMapping",
    definition="In 'receptive field mapping' a distinct set of physiological stimuli is used to evoke a sensory neuronal response in specific organisms to define its respective sensory space (receptive field).",
    name="receptive field mapping",
    synonyms=["RF mapping"],
)
Technique.reconstruction_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/reconstructionTechnique",
    definition="A 'reconstruction technique' is able to re-build, re-assemble, re-create, or re-imagine something by applying (often mathematical) principles to physical evidence.",
    name="reconstruction technique",
)
Technique.reporter_gene_based_expression_measurement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/reporterGeneBasedExpressionMeasurement",
    name="reporter gene based expression measurement",
)
Technique.reporter_protein_based_expression_measurement = Technique(
    id="https://openminds.ebrains.eu/instances/technique/reporterProteinBasedExpressionMeasurement",
    name="reporter protein based expression measurement",
)
Technique.retinotopic_mapping = Technique(
    id="https://openminds.ebrains.eu/instances/technique/retinotopicMapping",
    definition="In 'retinotopic mapping' the retina is repeatedly stimulated in such a way that the response of neurons, particularly within the visual stream, can be mapped to the location of the stimulus on the retina.",
    name="retinotopic mapping",
    synonyms=["retinal mapping"],
)
Technique.retrograde_tracing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/retrogradeTracing",
    definition="Retrograde tracing is a technique used to trace neural connections from their point of termination (the synapse) to their source (the cell body).",
    description="In 'retrograde tracing' a tracer substance is taken up by synaptic terminals (and sometimes by axons) of neurons in the region where it is injected. Retrograde tracing techniques allow for a detailed assessment of neuronal connections between a target population of neurons and their inputs throughout the nervous system.",
    name="retrograde tracing",
)
Technique.rigid_image_registration = Technique(
    id="https://openminds.ebrains.eu/instances/technique/rigidImageRegistration",
    definition="A 'rigid image registration' is a process of bringing a set of images into the same coordinate system using rigid transformation.",
    name="rigid image registration",
)
Technique.rigid_motion_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/rigidMotionCorrection",
    name="rigid motion correction",
)
Technique.rigid_transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/rigidTransformation",
    definition="A 'rigid transformation' is a specific linear transformation using combinations of rotations, translations, and reflections to map coordinates between two coordinate spaces, leaving the object congruent.",
    name="rigid transformation",
)
Technique.rna_sequencing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/RNASequencing",
    definition="'RNA sequencing' refers to a group of techniques that are used to (directly or indirectly) determine the order of nucleotides (nucleic acid sequence) in RNA.",
    interlex_identifier="http://uri.interlex.org/ilx_0782092",
    name="RNA sequencing",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/OBI_0001177",
    synonyms=["ribonucleic acid sequencing", "ribonucleic acid sequencing assay", "RNA sequencing assay", "RNA-Seq"],
)
Technique.rule_based_modeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/rule-basedModeling",
    name="rule-based modeling",
)
Technique.scanning_electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/scanningElectronMicroscopy",
    definition="Scanning electron microscopy is a microscopy technique to produce images of a specimen by scanning the surface with focused beam of electrons.",
    interlex_identifier="http://uri.interlex.org/ilx_0739710",
    name="scanning electron microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/scanningElectronMicroscopy",
    synonyms=["SEM", "scanning electron microscopy technique"],
)
Technique.scattered_light_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/scatteredLightImaging",
    name="scattered light imaging",
)
Technique.sds_digested_freeze_fracture_replica_labeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/SDSDigestedFreezeFractureReplicaLabeling",
    name="SDS-digested freeze-fracture replica labeling",
)
Technique.secondary_antibody_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/secondaryAntibodyStaining",
    name="secondary antibody staining",
)
Technique.seed_based_correlation_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/seed-basedCorrelationAnalysis",
    name="seed-based correlation analysis",
)
Technique.semantic_anchoring = Technique(
    id="https://openminds.ebrains.eu/instances/technique/semanticAnchoring",
    name="semantic anchoring",
)
Technique.semiquantitative_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/semiquantitativeAnalysis",
    definition="An analysis technique which constitutes or involves less than quantitative precision.",
    name="semiquantitative analysis",
)
Technique.serial_block_face_scanning_electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/serialBlockFaceScanningElectronMicroscopy",
    definition="Serial block face scanning electron microscopy is a serial section scanning electron microscopy technique where an ultramicrotome is used to remove the surface layer of a specimen.",
    name="serial block face scanning electron microscopy",
    synonyms=["SB-SEM", "SBEM", "serial blockface SEM"],
)
Technique.serial_section_transmission_electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/serialSectionTransmissionElectronMicroscopy",
    definition="Serial section transmission electron microscopy is a microscopy technique in which a beam of electrons is transmitted through multiple successive slices of a volumetric sample to produce images of the slices (e.g. for later 3D reconstruction).",
    name="serial section transmission electron microscopy",
)
Technique.shapiro_wilk_test = Technique(
    id="https://openminds.ebrains.eu/instances/technique/ShapiroWilkTest",
    definition="The 'Shapiro–Wilk test' is a statistical test of normality of a complete sample, first described by [Shapiro and Wilk (1965)](https://doi.org/10.1093/biomet/52.3-4.591). [adapted from [wikipedia](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)]",
    name="Shapiro-Wilk test",
    synonyms=["Shapiro-Wilk normality test"],
)
Technique.sharp_electrode_intracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/sharpElectrodeIntracellularElectrophysiology",
    definition="An intracellular electrophysiology technique where a microelectrode/micropipette is used to measure electrical properties of a single cell, e.g. a neuron.",
    description="This technique uses a fine-tipped micropipette/microelectrode that is inserted into the neuron, allowing direct recording of electrical events generated by the neuron (membrane potential, resistance, time constant, synaptic potentials and action potentials).",
    interlex_identifier="http://uri.interlex.org/ilx_0739713",
    name="sharp electrode intracellular electrophysiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/sharpElectrodeEphys",
    synonyms=[
        "sharp electrode technique",
        "sharp intracellular electrode technique",
        "sharp electrode recording",
        "sharp intracellular electrode recording",
    ],
)
Technique.signal_filtering_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/signalFilteringTechnique",
    definition="'Signal filtering' is a signal processing technique used to remove or suppress unwanted components or features (e.g., certain frequencies) from a measured signal. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Filter_(signal_processing))]",
    interlex_identifier="http://uri.interlex.org/ilx_0739623",
    name="signal filtering technique",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/151",
    synonyms=["filtering", "signal filtering"],
)
Technique.signal_processing_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/signalProcessingTechnique",
    definition="'Signal processing' refers to a class of analysis techniques used to improve transmission, storage efficiency and subjective quality as well as to emphasize or detect components of interest in a measured signal. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Signal_processing)]",
    interlex_identifier="http://uri.interlex.org/ilx_0739633",
    name="signal processing technique",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/sigproc",
    synonyms=["signal processing"],
)
Technique.silver_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/silverStaining",
    definition="A technique where the appearance of biological subcellular targets (e.g. proteins, RNA or DNA) is selectively alter by use of silver.",
    description="Silver can be used to stain subcellular targets such as proteins, peptide, carbohydrates, RNA or DNA. This techniques is typically used on histological sections prior to light microscopy, for the detection of proteins and peptides in polyacrylamide gels or gel electrophoresis.",
    interlex_identifier="http://uri.interlex.org/ilx_0110626",
    name="silver staining",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_152217",
    synonyms=["silver stain"],
)
Technique.simulation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/simulation",
    name="simulation",
)
Technique.single_cell_rna_sequencing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/singleCellRNASequencing",
    name="single cell RNA sequencing",
)
Technique.single_electrode_extracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/singleElectrodeExtracellularElectrophysiology",
    name="single electrode extracellular electrophysiology",
)
Technique.single_electrode_juxtacellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/singleElectrodeJuxtacellularElectrophysiology",
    name="single electrode juxtacellular electrophysiology",
)
Technique.single_gene_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/singleGeneAnalysis",
    definition="A 'single gene analysis' is a genetic test (sequencing technique) to check for any genetic changes in a specific gene.",
    name="single gene analysis",
    synonyms=["single gene sequencing", "single gene test"],
)
Technique.single_nucleotide_polymorphism_detection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/singleNucleotidePolymorphismDetection",
    definition="'Single nucleotide polymorphism detection' refers to a group of techniques that are used to scan for new polymorphisms and to determine the allele(s) of a known polymorphism in target sequences (adapted from [Kwok and Chen, 2003](https://doi.org/10.21775/cimb.005.043)).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0780321",
    name="single nucleotide polymorphism detection",
    preferred_ontology_identifier="http://edamontology.org/operation_0484",
    synonyms=["SNP calling", "SNP detection", "SNP discovery"],
)
Technique.slice_timing_correction = Technique(
    id="https://openminds.ebrains.eu/instances/technique/sliceTimingCorrection",
    definition="'Slice timing correction' is a preprocessing technique applied to functional magnetic resonance image data in order to correct for temporal offsets between 2D image slices during the data acquisition. [adapted from [Parker and Razlighi, 2019](https://doi.org/10.3389/fnins.2019.00821)]",
    name="slice timing correction",
    synonyms=["STC"],
)
Technique.sodium_mri = Technique(
    id="https://openminds.ebrains.eu/instances/technique/sodiumMRI",
    definition="'Sodium MRI' is a specialised magnetic resonance imaging technique that uses strong magnetic fields, magnetic field gradients, and radio waves to generate images of the distribution of sodium in the body. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Sodium_MRI)]",
    name="sodium MRI",
    synonyms=["Na MRI", "Na-MRI", "Sodium-MRI"],
)
Technique.sonography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/sonography",
    name="sonography",
)
Technique.spearmans_rank_order_correlation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/SpearmansRankOrderCorrelation",
    definition="The 'Spearman's rank-order correlation' is the nonparametric version of the Pearson product-moment correlation measuring the strength and direction of association between a set of two ranked variables. [adapted from [Laerd.com](https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php)]",
    name="Spearman's rank-order correlation",
    synonyms=["Spearman’s correlation", "Spearman’s correlation test", "Spearman’s rank correlation"],
)
Technique.spectral_power_auto_segmentation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/spectralPowerAutoSegmentationTechnique",
    definition="A 'spectral power auto-segmentation technique' makes use of the power spectrum along the time axis of individual pixels or voxels in an image to automatically generate a segmentation.",
    name="spectral power auto-segmentation technique",
    synonyms=["spectral power image auto-segmentation technique"],
)
Technique.spike_sorting = Technique(
    id="https://openminds.ebrains.eu/instances/technique/spikeSorting",
    definition="'Spike sorting' is a class of techniques used in the analysis of extracellular electrophysiological data to extract the activity of one or more neurons from the background electrical noise by making use of the typical waveforms action potentials (spikes) create in the recorded neuronal signal.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739628",
    name="spike sorting",
    synonyms=["spike sorting technique"],
)
Technique.spin_echo_pulse_sequence = Technique(
    id="https://openminds.ebrains.eu/instances/technique/spinEchoPulseSequence",
    definition="In magnetic resonance imaging, a 'spin echo pulse sequence' is a contrast generation technique that induces bulk changes in the spin magnetization of a sample by applying sequential pulses of resonant electromagnetic waves at different angles (cf. [Fonseca (2013)](https://doi.org/10.5772/53693)).",
    name="spin echo pulse sequence",
    synonyms=["SE pulse sequence"],
)
Technique.stereoelectroencephalography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/stereoelectroencephalography",
    definition="In 'stereoelectroencephalography' depth electrodes (typically linear electrode arrays) are stereotactically implanted in the brain of a subject in order to record or stimulate electrographic activity of otherwise inaccessible brain regions. [cf. [wikipedia](https://en.wikipedia.org/wiki/Stereoelectroencephalography), or [Gholipour et al. 2020](https://doi.org/10.1016/j.clineuro.2019.105640)]",
    name="stereoelectroencephalography",
    synonyms=[
        "sEEG",
        "SEEG",
        "stereo-EEG",
        "stereotactic-EEG",
        "stereo electroencephalogaphy",
        "stereotactic electroencephalogaphy",
    ],
)
Technique.stereology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/stereology",
    definition="An imaging assay that is used for the three-dimensional interpretation of planar sections of materials or tissues.",
    interlex_identifier="http://uri.interlex.org/ilx_0739729",
    name="stereology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/79",
)
Technique.stereotactic_surgery = Technique(
    id="https://openminds.ebrains.eu/instances/technique/stereotacticSurgery",
    name="stereotactic surgery",
)
Technique.stochastic_online_matrix_factorization = Technique(
    id="https://openminds.ebrains.eu/instances/technique/stochasticOnlineMatrixFactorization",
    definition="'Stochastic online matrix factorization' is a matrix-factorization algorithm that scales to input matrices with both huge number of rows and columns [(Mensch et al., 2018)](https://doi.org/10.1109/TSP.2017.2752697).",
    name="stochastic online matrix factorization",
    synonyms=["SOMF"],
)
Technique.structural_covariance_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/structuralCovarianceAnalysis",
    name="structural covariance analysis",
)
Technique.structural_neuroimaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/structuralNeuroimaging",
    name="structural neuroimaging",
)
Technique.subcutaneous_injection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/subcutaneousInjection",
    definition="An 'subcutenous injection' is the administration of a substance under all the layers of the skin via a needle or tube.",
    name="subcutaneous injection",
    synonyms=["s.c.", "s.c. injection", "SC", "SC injection"],
)
Technique.subdural_electrocorticography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/subduralElectrocorticography",
    name="subdural electrocorticography",
)
Technique.support_vector_machine_classifier = Technique(
    id="https://openminds.ebrains.eu/instances/technique/supportVectorMachineClassifier",
    definition="A 'support-vector machine classifier' is a supervised machine learning technique that analyzes data for classification.",
    name="support-vector machine classifier",
    synonyms=[
        "support-vector machine",
        "support-vector machine learning",
        "SVC",
        "SVM",
        "SVM classifier",
        "SVM learning",
    ],
)
Technique.support_vector_machine_regression = Technique(
    id="https://openminds.ebrains.eu/instances/technique/supportVectorMachineRegression",
    definition="A 'Support-Vector Regression Algorithm' is a supervised machine learning technique used to estimate the relationship between a dependent and a number of independent variables.",
    name="support-vector regression algorithm",
    synonyms=[
        "support vector regression",
        "support vector regression algorithm",
        "support-vector regression",
        "SVR",
        "SVR algorithm",
    ],
)
Technique.surface_projection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/surfaceProjection",
    name="surface projection",
    synonyms=["surface texture projection"],
)
Technique.switch_immunohistochemistry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/SWITCHImmunohistochemistry",
    name="SWITCH immunohistochemistry",
)
Technique.t1_pulse_sequence = Technique(
    id="https://openminds.ebrains.eu/instances/technique/T1PulseSequence",
    definition="In magnetic resonance imaging, a 'T1 pulse sequence' is a contrasting technique that allows the magnetization of the specimen or object to recover (spin-lattice relaxation) before measuring the magnetic resonance signal by changing the repetition time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/MRI_sequence)]",
    name="T1 pulse sequence",
    synonyms=[
        "T1 weighted imaging",
        "T1 weighted magnetic resonance imaging",
        "T1 weighted MRI",
        "T1w imaging",
        "T1w magnetic resonance imaging",
        "T1w MRI",
    ],
)
Technique.t2_pulse_sequence = Technique(
    id="https://openminds.ebrains.eu/instances/technique/T2PulseSequence",
    definition="In magnetic resonance imaging, a 'T2 pulse sequence' is a contrasting technique that allows the magnetization of the specimen or object to decay (spin-spin relaxation) before measuring the magnetic resonance signal by changing the echo time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/MRI_sequence)]",
    name="T2 pulse sequence",
    synonyms=[
        "T2 weighted imaging",
        "T2 weighted magnetic resonance imaging",
        "T2 weighted MRI",
        "T2w imaging",
        "T2w magnetic resonance imaging",
        "T2w MRI",
    ],
)
Technique.tde_clearing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/TDEClearing",
    name="TDE clearing",
)
Technique.temporal_filtering = Technique(
    id="https://openminds.ebrains.eu/instances/technique/temporalFiltering",
    definition="'Temporal filtering' is a functional image signal processing technique that aims to remove or attenuate frequencies that vary along the time axis of the raw signal. [adapted from [Wikibooks](https://en.wikibooks.org/wiki/Neuroimaging_Data_Processing/Processing/Steps/Temporal_Filtering)]",
    name="temporal filtering",
    synonyms=["temporal filtering technique", "temporal image filtering", "temporal image filtering technique"],
)
Technique.tetrode_extracellular_electrophysiology = Technique(
    id="https://openminds.ebrains.eu/instances/technique/tetrodeExtracellularElectrophysiology",
    name="tetrode extracellular electrophysiology",
)
Technique.three_d_computer_graphic_modeling = Technique(
    id="https://openminds.ebrains.eu/instances/technique/3DComputerGraphicModeling",
    name="3D computer graphic modeling",
)
Technique.three_d_polarized_light_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/3DPolarizedLightImaging",
    definition="'3D polarized light imaging' (synonym: 3D-PLI) is a 3D reconstruction process of high-resoluted image data originating from polorized light microscopy.",
    name="3D polarized light imaging",
)
Technique.three_d_scanning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/3DScanning",
    name="3D scanning",
)
Technique.time_of_flight_magnetic_resonance_angiography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/time-of-flightMagneticResonanceAngiography",
    definition="'Time-of-flight magnetic resonance angiography' is a non-invasive, non-contrast-enhanced technique used to visualize both arterial and venous vessels with high spatial resolution. Note: it provides no information regarding directionality nor flow velocity quantification. [adapted from:  [Ferreira and Ramalho, 2013](https://doi.org/10.1002/9781118434550.ch7)]",
    name="time-of-flight magnetic resonance angiography",
    synonyms=[
        "time-of-flight",
        "time-of-flight angiography",
        "time-of-flight MR angiography",
        "time-of-flight MRA",
        "TOF",
        "TOF angiography",
        "TOF magnetic resonance angiography",
        "TOF MRA",
    ],
)
Technique.timms_staining = Technique(
    id="https://openminds.ebrains.eu/instances/technique/TimmsStaining",
    definition="A technique used to selectively visualize a variety of metals (e.g. zinc, copper, iron) in biological tissue based on sulphide-precipitation of metals in the tissue.",
    description="The principle of this technique is that metals in the tissue can be transformed histochemically to metal sulphide. Subsequently, metal sulphide catalyze the reduction of silver ions by a reducing agent to metallic grains that are visible under a light or electron microscope.",
    interlex_identifier="http://uri.interlex.org/ilx_0107265",
    name="Timm's staining",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/birnlex_2248",
    synonyms=["Timm's stain", "Timm's sulfide silver staining"],
)
Technique.tissue_clearing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/tissueClearing",
    name="tissue clearing",
)
Technique.tract_tracing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/tractTracing",
    name="tract tracing",
)
Technique.tractography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/tractography",
    name="tractography",
)
Technique.transcardial_perfusion_fixation_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/transcardialPerfusionFixationTechnique",
    definition="Transcardial perfusion fixation is a technique to distribute fixatives throughout tissue via the heart.",
    name="transcardial perfusion fixation technique",
    synonyms=["intracardiac perfusion fixation technique", "intracardial perfusion fixation technique"],
)
Technique.transcardial_perfusion_technique = Technique(
    id="https://openminds.ebrains.eu/instances/technique/transcardialPerfusionTechnique",
    definition="Transcardial perfusion is a technique to distribute fluid throughout tissue via the heart.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739695",
    name="transcardial perfusion technique",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/167",
    synonyms=["intracardiac perfusion technique", "intracardial perfusion technique"],
)
Technique.transformation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/transformation",
    definition="A 'transformation' is a mathematical function to map coordinates between two different coordinate systems.",
    name="transformation",
)
Technique.transmission_electron_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/transmissionElectronMicroscopy",
    definition="Transmission electron microscopy is a microscopy technique in which a beam of electrons is transmitted through a specimen to produce an image.",
    name="transmission electron microscopy",
    synonyms=["TEM"],
)
Technique.two_photon_fluorescence_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/twoPhotonFluorescenceMicroscopy",
    definition="Two-photon fluorescence microscopy is a fluorescence microscopy technique for living tissue which is based on the simultaneous excitation by two photons with longer wavelength than the emitted light.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739658",
    name="two-photon fluorescence microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/technique/twoPhoton",
    synonyms=[
        "2-photon excitation microscopy",
        "2-photon fluorescence microscopy",
        "2-photon miscroscopy",
        "2PEF",
        "TPEF",
        "TPM",
        "two-photon excitation fluorescence microscopy",
        "two-photon excitation microscopy",
        "two-photon miscroscopy",
    ],
)
Technique.ultra_high_field_functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/ultraHighFieldFunctionalMagneticResonanceImaging",
    definition="'Ultra high-field functional magnetic resonance imaging' comprises all functional MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.",
    name="ultra high-field functional magnetic resonance imaging",
)
Technique.ultra_high_field_magnetic_resonance_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/ultraHighFieldMagneticResonanceImaging",
    definition="'Ultra high-field magnetic resonance imaging' comprises all structural MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.",
    name="ultra high-field magnetic resonance imaging",
)
Technique.ultra_high_field_magnetic_resonance_spectroscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/ultraHighFieldMagneticResonanceSpectroscopy",
    definition="'Ultra high-field magnetic resonance spectroscopy' comprises all MRS techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.",
    name="ultra high-field magnetic resonance spectroscopy",
)
Technique.vibratome_sectioning = Technique(
    id="https://openminds.ebrains.eu/instances/technique/vibratomeSectioning",
    name="vibratome sectioning",
)
Technique.video_annotation = Technique(
    id="https://openminds.ebrains.eu/instances/technique/videoAnnotation",
    name="video annotation",
)
Technique.video_oculography = Technique(
    id="https://openminds.ebrains.eu/instances/technique/video-oculography",
    name="video-oculography",
)
Technique.video_tracking = Technique(
    id="https://openminds.ebrains.eu/instances/technique/videoTracking",
    name="video tracking",
)
Technique.virus_mediated_transfection = Technique(
    id="https://openminds.ebrains.eu/instances/technique/virus-mediatedTransfection",
    name="virus-mediated transfection",
)
Technique.voltage_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/voltageClamp",
    definition="'Voltage clamp' comprises all experimental techniques in which the membrane potential (voltage) is constantly changed to a desired value by adding the necessary current to the cell.",
    name="voltage clamp",
)
Technique.voltage_sensitive_dye_imaging = Technique(
    id="https://openminds.ebrains.eu/instances/technique/voltageSensitiveDyeImaging",
    definition="'Voltage sensitive dye imaging' is an experimental technique to measure neuronal population activity from in vivo brains or live brain slices by transducing changes in the cell membrane potential into changes of fluorescence emission by an employed exogenous chemical agent.",
    name="voltage sensitive dye imaging",
)
Technique.voxel_based_morphometry = Technique(
    id="https://openminds.ebrains.eu/instances/technique/voxel-basedMorphometry",
    name="voxel-based morphometry",
)
Technique.weighted_correlation_network_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/weightedCorrelationNetworkAnalysis",
    definition="Weighted correlation network analysis is a widely used data mining method for studying networks based on pairwise correlations between variables. While it can be applied to most high-dimensional data sets, it has been most widely used in genomic applications. [adopted from: [wikipedia](https://en.wikipedia.org/wiki/Weighted_correlation_network_analysis)]",
    name="weighted correlation network analysis",
    synonyms=["weighted gene co-expression network analysis", "WGCNA"],
)
Technique.whole_cell_patch_clamp = Technique(
    id="https://openminds.ebrains.eu/instances/technique/wholeCellPatchClamp",
    definition="'Whole cell patch clamp' is a patch clamp technique where the pipette is sealed onto a cell membrane applying enough suction to rupture the membrane patch in order to provide access from the interior of the pipette to the intracellular space of the cell.",
    name="whole cell patch clamp",
)
Technique.whole_genome_sequencing = Technique(
    id="https://openminds.ebrains.eu/instances/technique/wholeGenomeSequencing",
    definition="'Whole genome sequencing' is a genetic test (sequencing technique) to determine the entire, or nearly the entire, DNA sequence of an organism's genome at a single time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Whole_genome_sequencing)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0492452",
    name="whole genome sequencing",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M000621306",
    synonyms=["complete genome sequencing", "entire genome sequencing", "full genome sequencing", "WGS"],
)
Technique.widefield_fluorescence_microscopy = Technique(
    id="https://openminds.ebrains.eu/instances/technique/widefieldFluorescenceMicroscopy",
    definition="'Widefield fluorescence microscopy' comprises all microscopy techniques in which fluorescent molecules of an entire sample are excited through a permanent exposure of a light source of a specific wavelength.",
    name="widefield fluorescence microscopy",
)
Technique.z_score_analysis = Technique(
    id="https://openminds.ebrains.eu/instances/technique/zScoreAnalysis",
    definition="The 'z-score analysis' is a statistical normalization technique where the z-score is calculated by subtracting the population mean from an individual raw score (observed data point) and dividing the difference by the population standard deviation. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Standard_score)]",
    name="z-score analysis",
    synonyms=["standard score analysis"],
)
