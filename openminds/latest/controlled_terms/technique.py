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

    type_ = "https://openminds.om-i.org/types/Technique"
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
            description="Longer statement or account giving the characteristics of the technique.",
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
            description="Word or phrase that constitutes the distinctive designation of the technique.",
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


Technique.activity_modulation_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/activityModulationTechnique",
    name="activity modulation technique",
)
Technique.anaesthesia_administration = Technique(
    id="https://openminds.om-i.org/instances/technique/anaesthesiaAdministration",
    name="anaesthesia administration",
)
Technique.anaesthesia_monitoring = Technique(
    id="https://openminds.om-i.org/instances/technique/anaesthesiaMonitoring",
    name="anaesthesia monitoring",
)
Technique.anaesthesia_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/anaesthesiaTechnique",
    name="anaesthesia technique",
)
Technique.angiography = Technique(
    id="https://openminds.om-i.org/instances/technique/angiography",
    definition="Imaging technique for anatomical and structural details of the vascular system [adapted from [National Library of Medicine](https://www.ncbi.nlm.nih.gov/books/NBK557477/)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739420"),
    name="angiography",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/87"),
    synonyms=["angiographic technique"],
)
Technique.anterograde_tracing = Technique(
    id="https://openminds.om-i.org/instances/technique/anterogradeTracing",
    definition="Anterograde tracing is a technique used to trace axonal projections from their source (the cell body or soma) to their point of termination (the synapse).",
    description="Anterograde tracers are taken up by neuronal cell bodies at the injection site and travel to the axon terminals. Anterograde tracing techniques allow for a detailed assessment of neuronal connections between a target population of neurons and their outputs throughout the nervous system.",
    name="anterograde tracing",
)
Technique.autoradiography = Technique(
    id="https://openminds.om-i.org/instances/technique/autoradiography",
    definition="'Autoradiography' is a photography technique that creates images of a radioactive source (e.g., molecules or fragments of molecules that have been radioactively labeled) by the direct exposure to an imaging media (e.g., X-ray film or nuclear emulsion)",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0439300"),
    name="autoradiography",
)
Technique.avidin_biotin_complex_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/avidinBiotinComplexStaining",
    name="avidin-biotin complex staining",
    synonyms=["ABC staining"],
)
Technique.beta_galactosidase_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/beta-galactosidaseStaining",
    name="beta-galactosidase staining",
)
Technique.biocytin_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/biocytinStaining",
    definition="In 'biocytin staining' the chemical compound biocytin is used to highlight morphological details of nerve cells.",
    description="Biocytin staining is a technique commonly used in combination with intracellular electrophysiology for post-hoc recovery of morphological details of the studied neurons. For this, the chemical compound biocytin is included in the electrode in order to fill the studied cell. It allows for the visualisation of the dendritic arborization and the regions targeted by the axons of the studied neurons.",
    name="biocytin staining",
    synonyms=["biocytin filling", "biocytin labeling"],
)
Technique.blood_sampling = Technique(
    id="https://openminds.om-i.org/instances/technique/bloodSampling",
    definition="'Blood sampling' is the process of obtaining blood from a body for purpose of medical diagnosis and/or evaluation of an indication for treatment, further medical tests or other procedures.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0782225"),
    name="blood sampling",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_1110095"),
    synonyms=["blood collection", "blood harvesting"],
)
Technique.brightfield_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/brightfieldMicroscopy",
    definition="Brightfield microscopy is an optical microscopy techniques, in which illumination light is transmitted through the sample and the contrast is generated by the absorption of light in dense areas of the specimen.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739719"),
    name="brightfield microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/238"),
)
Technique.calcium_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/calciumImaging",
    name="calcium imaging",
)
Technique.callosotomy = Technique(
    id="https://openminds.om-i.org/instances/technique/callosotomy",
    name="callosotomy",
)
Technique.cell_attached_patch_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/cellAttachedPatchClamp",
    definition="'Cell-attached patch clamp' is an intracellular electrophysiology technique that fully preserves the intracellular integrity by forming a megaohm or gigaohm seal, leaving the cell membrane intact.",
    description="Cell-attached patch clamp is a patch clamp recording technique used in electrophysiology in which the intracellular integrity of the cell is preserved. Patches are formed using either a ‘loose seal’ (mega ohm resistance) or a ‘tight seal’ (giga ohm resistance) without rupturing the cell membrane. A loose seal is used for recording action potential currents, whereas a tight seal is required for evoking action potentials in the attached cell and for recording resting and synaptic potentials.",
    name="cell attached patch clamp",
)
Technique.clarity_tde = Technique(
    id="https://openminds.om-i.org/instances/technique/CLARITY_TDE",
    name="CLARITY/TDE",
)
Technique.coherent_anti_stokes_raman_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/coherentAntiStokesRamanSpectroscopy",
    definition="A nonlinear Raman spectroscopy technique that employs multiple photons to address molecular vibrations, and produces a coherent signal. It uses a Stokes frequency stimulation beam and an anti-Stokes frequency beam is observed [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Coherent_anti-Stokes_Raman_spectroscopy)].",
    name="coherent anti-Stokes Raman spectroscopy",
    synonyms=["coherent anti-Stokes Raman scattering spectroscopy", "CARS"],
)
Technique.coherent_stokes_raman_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/coherentStokesRamanSpectroscopy",
    definition="A nonlinear Raman spectroscopy technique that employs multiple photons to address molecular vibrations, and produces a coherent signal. It uses an anti-Stokes frequency stimulation beam and a Stokes frequency beam is observed [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Coherent_anti-Stokes_Raman_spectroscopy)].",
    name="coherent Stokes Raman spectroscopy",
    synonyms=["CSRS"],
)
Technique.computer_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/computerTomography",
    definition="'Computer tomogoraphy' is a noninvasive medical imaging technique where a computer generates multiple X-ray scans to obtain detailed internal 3D image of the body.",
    name="computer tomography",
    synonyms=["CAT", "computed axial tomography", "computed tomography", "computertomography", "CT"],
)
Technique.confocal_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/confocalMicroscopy",
    definition="Confocal microscopy is a specialized fluorescence microscopy technique that uses pinholes to reject out-of-focus light.",
    description="Confocal microscopy focuses light onto a defined spot at a specific depth within a fluorescent sample to eliminate out-of-focus glare, and increase resolution and contrast in the micrographs.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739731"),
    name="confocal microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/157"),
    synonyms=["confocal microscopy technique"],
)
Technique.contrast_agent_administration = Technique(
    id="https://openminds.om-i.org/instances/technique/contrastAgentAdministration",
    definition="A 'contrast agent administration' is a (typically) oral or intraveneous administration of a chemical compound to improve the visibility of internal body structures of a subject in a subsequent imaging technique.",
    name="contrast agent administration",
)
Technique.contrast_enhancement = Technique(
    id="https://openminds.om-i.org/instances/technique/contrastEnhancement",
    name="contrast enhancement",
)
Technique.cortico_cortical_evoked_potential_mapping = Technique(
    id="https://openminds.om-i.org/instances/technique/cortico-corticalEvokedPotentialMapping",
    definition="Cortico-cortical evoked potential (CCEP) mapping is used to identify the effective connectivity between distinct neuronal populations based on multiple CCEP measurements across (parts of) the brain in response to direct electrical stimulation (typically at various locations).",
    name="cortico-cortical evoked potential mapping",
    synonyms=["CCEP mapping"],
)
Technique.craniotomy = Technique(
    id="https://openminds.om-i.org/instances/technique/craniotomy",
    name="craniotomy",
)
Technique.cryosectioning = Technique(
    id="https://openminds.om-i.org/instances/technique/cryosectioning",
    definition="Cutting of specimen in cryo/freezing conditions typically resulting in micromillimeter thin slices.",
    name="cryosectioning",
    synonyms=["cryosection procedure", "frozen section procedure"],
)
Technique.current_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/currentClamp",
    definition="Current clamp is a technique in which the amount of current injected into the cell is controlled, which allows for the detection of changes in the transmembrane voltage resulting from ion channel activity.",
    name="current clamp",
)
Technique.da_pi_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/DAPiStaining",
    definition="A nuclear-specific staining technique where DAPi (4′,6-diamidino-2-phenylindole) is used as a dye.",
    description="DAPi, or 4′,6-diamidino-2-phenylindole, is a blue fluorescent dye that bind strongly to adenine-thymine (AT) rich regions in DNA. It is used extensively in fluorescence microscopy and can be used on both fixated and living cells.",
    name="DAPi staining",
    synonyms=["4′,6-diamidino-2-phenylindole staining", "DAPi stain"],
)
Technique.dab_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/DABStaining",
    definition="In a 'DAB staining', the organic compound DAB (3, 3'-diaminobenzidine) is oxidized in presence of peroxidase and hydrogen peroxide resulting in deposition of a brown, alcohol-insoluble precipitate which can be used in immunohistochemical and blotting applications.",
    name="DAB staining",
    synonyms=["3,3′-Diaminobenzidine staining"],
)
Technique.darkfield_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/darkfieldMicroscopy",
    definition="Darkfield microscopy is an optical microscopy technique in which illumination light is transmitted through the sample so that it does not directly enter the optics and contrast is generated by the differential scattering of light within the specimen.",
    description="Darkfield microscopy is an optical microscopy technique that generates contrast by differentially filtering scatter and unscattered light. Specifically it transmits scattered light and blocks unscattered light. The effect is to make the areas of a transparent sample that scatter light appear brighter than those that do not scatter light. A dark background is used (i.e. the light source is not directly behind the sample in the optical path) so that unscattered light does not overwhelm the scattered light.",
    name="darkfield microscopy",
    synonyms=["dark-field microscopy", "dark field microscopy"],
)
Technique.differential_interference_contrast_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/differentialInterferenceContrastMicroscopy",
    definition="An optical microscopy technique, used to enhance the contrast in unstained, transparent samples [taken from [Wikipedia](https://en.wikipedia.org/wiki/Differential_interference_contrast_microscopy)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739494"),
    name="differential interference contrast microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/IRDIC"),
    synonyms=["IR DIC video microscopy", "IR-DIC", "DIC microscopy", "DIC"],
)
Technique.diffusion_fixation_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/diffusionFixationTechnique",
    definition="Diffusion fixation is a fixation technique to preserve specimen permanently as faithfully as possible compared to the living state by submerging specimen in a fixative.",
    name="diffusion fixation technique",
    synonyms=["drop fixation"],
)
Technique.diffusion_spectrum_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/diffusionSpectrumMagneticResonanceImaging",
    definition="Advanced magnetic resonance imaging (MRI) and image processing technique that enhances the contrast of fiber crossings and complex intravoxel fiber orientation distributions [[Zhang et al., 2018](https://doi.org/10.1371/journal.pone.0203271), [Wedeen et al., 2008](https://doi.org/10.1016/j.neuroimage.2008.03.036), [Wedeen et al., 2000](https://cds.ismrm.org/ismrm-2000/PDF1/0082.pdf)].",
    name="diffusion spectrum magnetic resonance imaging",
    synonyms=[
        "diffusion spectrum imaging",
        "diffusion spectrum image processing",
        "DSI",
        "Fourier diffusion magnetic resonance imaging",
        "Fourier diffusion MRI",
        "Fourier-transform diffusion magnetic resonance imaging",
        "Fourier-transform diffusion MRI",
    ],
)
Technique.diffusion_tensor_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/diffusionTensorImaging",
    name="diffusion tensor imaging",
)
Technique.diffusion_weighted_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/diffusionWeightedImaging",
    name="diffusion-weighted imaging",
)
Technique.dna_methylation_analysis = Technique(
    id="https://openminds.om-i.org/instances/technique/DNAMethylationAnalysis",
    definition="A 'DNA methylation analysis' studies chromosomal patterns of DNA or histone modification by methyl groups ([modified from Nature.com](https://www.nature.com/subjects/methylation-analysis)).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0779582"),
    name="DNA methylation analysis",
    synonyms=["methylation analysis"],
)
Technique.dna_sequencing = Technique(
    id="https://openminds.om-i.org/instances/technique/DNASequencing",
    definition="'DNA sequencing' refers to a group of techniques that are used to determine the order of nucleotides (nucleic acid sequence) in DNA. [adapted from [wikipedia](https://en.wikipedia.org/wiki/DNA_sequencing)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0783031"),
    name="DNA sequencing",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_0000626"),
    synonyms=[
        "deoxyribonucleic acid sequencing",
        "deoxyribonucleic acid sequencing assay",
        "DNA sequencing assay",
        "DNA-Seq",
    ],
)
Technique.dual_view_inverted_selective_plane_illumination_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/dualViewInvertedSelectivePlaneIlluminationMicroscopy",
    definition="Dual-view inverted selective plane illumination microscopy is a specialized light sheet microscopy technique that allows for dual views of the samples while mounted on an inverted microscope.",
    name="dual-view inverted selective plane illumination microscopy",
    synonyms=[
        "diSPIM",
        "dual-view inverted light sheet fluorescence microscopy",
        "dual-view inverted light sheet microscopy",
    ],
)
Technique.electrocardiography = Technique(
    id="https://openminds.om-i.org/instances/technique/electrocardiography",
    definition="Electrocardiography is a non-invasive technique used to record the electrical activity of a heart using electrodes placed on the skin. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Electrocardiography)]",
    name="electrocardiography",
    synonyms=["ECG"],
)
Technique.electrocorticography = Technique(
    id="https://openminds.om-i.org/instances/technique/electrocorticography",
    definition="'Electrocorticography', short ECoG, is an intracranial electroencephalography technique in which electrodes are placed (subdural or epidural) on the exposed surface of the brain to record electrical activity from the cerebral cortex.",
    name="electrocorticography",
    synonyms=["ECoG"],
)
Technique.electroencephalography = Technique(
    id="https://openminds.om-i.org/instances/technique/electroencephalography",
    name="electroencephalography",
)
Technique.electromyography = Technique(
    id="https://openminds.om-i.org/instances/technique/electromyography",
    name="electromyography",
)
Technique.electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/electronMicroscopy",
    definition="Electron microscopy describes any microscopy technique that uses electrons to generate contrast.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739513"),
    name="electron microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/electronMicroscopy"),
    synonyms=["EM"],
)
Technique.electron_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/electronTomography",
    definition="Electron tomography is a microscopy technique that takes a series of images of a thick sample at different angles (tilts) so that tomography can be applied to increase the resolution of the ticker sample.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0461087"),
    name="electron tomography",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0512939"),
    synonyms=["electron microscope tomography"],
)
Technique.electrooculography = Technique(
    id="https://openminds.om-i.org/instances/technique/electrooculography",
    name="electrooculography",
)
Technique.electroporation = Technique(
    id="https://openminds.om-i.org/instances/technique/electroporation",
    definition="A microbiology technique in which an electrical field is applied to cells in order to increase the permeability of the cell membrane.",
    description="'Electroporation' is a process in which a significant increase in the electrical conductivity and permeability of the cell plasma membrane is caused by an externally applied electrical field. It is usually used in molecular biology as a way of introducing some substance into a cell, such as loading it with a molecular probe, a drug that can change the cell's function, or a piece of coding DNA.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739748"),
    name="electroporation",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/electroporation"),
    synonyms=["electropermeabilization"],
)
Technique.enzyme_linked_immunosorbent_assay = Technique(
    id="https://openminds.om-i.org/instances/technique/enzymeLinkedImmunosorbentAssay",
    definition="The 'enzyme-linked immunosorbent assay' is a commonly used analytical biochemistry assay for the quantitative determination of antibodies, first described by [Engvall and Perlmann (1972)](https://www.jimmunol.org/content/109/1/129.abstract). [adapted from [wikipedia](https://en.wikipedia.org/wiki/ELISA)]",
    description="This immunoassay utilizes an antibody labeled with an enzyme marker such as horseradish peroxidase. While either the enzyme or the antibody is bound to an immunosorbent substrate, they both retain their biologic activity; the change in enzyme activity as a result of the enzyme-antibody-antigen reaction is proportional to the concentration of the antigen and can be measured spectrophotometrically or with the naked eye. Many variations of the method have been developed.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0484188"),
    name="enzyme-linked immunosorbent assay",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0007526"),
    synonyms=["ELISA"],
)
Technique.epidermal_electrophysiology_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/epidermalElectrophysiologyTechnique",
    definition="The term 'epidermal electrophysiology technique' describes a subclass of non-invasive electrophysiology techniques where one or several electrodes are placed on the outermost cell layer of an organism (epidermis) to measure electrical properties.",
    name="epidermal electrophysiology technique",
    synonyms=["epidermal electrophysiology"],
)
Technique.epidural_electrocorticography = Technique(
    id="https://openminds.om-i.org/instances/technique/epiduralElectrocorticography",
    name="epidural electrocorticography",
)
Technique.epifluorescent_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/epifluorescentMicroscopy",
    definition="Epifluorescent microscopy comprises all widefield microscopy techniques in which fluorescent molecules of an entire sample are excited through a permanent exposure of a light source of a specific wavelength.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739632"),
    name="epifluorescent microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/243"),
    synonyms=[
        "epifluorescence microscopy",
        "WFM",
        "widefield epifluorescence microscopy",
        "widefield fluorescence microscopy",
    ],
)
Technique.extracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/extracellularElectrophysiology",
    definition="In 'extracellular electrophysiology' electrodes are inserted into living tissue, but remain outside the cells in the extracellular environment to measure or stimulate electrical activity coming from adjacent cells, usually neurons.",
    name="extracellular electrophysiology",
)
Technique.eye_movement_tracking = Technique(
    id="https://openminds.om-i.org/instances/technique/eyeMovementTracking",
    definition="'Eye movement tracking' refers to a group of techniques used to record the eye movement and/or position of a living specimen over a given period of time.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0417680"),
    name="eye movement tracking",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0493574"),
    synonyms=["eye motion tracking", "eye tracking"],
)
Technique.fixation_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/fixationTechnique",
    definition="Fixation is a technique to preserve specimen permanently as faithfully as possible compared to the living state.",
    description="Fixation is a two-step process in which 1) all normal life functions are terminated and 2) the structure of the tissue is stabilized (preserved). The fixation of tissue can be achieved by chemical or physical (e.g. heating, freezing) means.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739717"),
    name="fixation technique",
)
Technique.fluorescence_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/fluorescenceMicroscopy",
    definition="Fluorescence microscopy comprises any type of microscopy where the specimen can be made to fluoresce (emit energy as visible light), typically by illuminating it with light of specific wavelengths.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0780848"),
    name="fluorescence microscopy",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/CHMO_0000087"),
)
Technique.focused_ion_beam_scanning_electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/focusedIonBeamScanningElectronMicroscopy",
    definition="Focused ion beam scanning electron microscopy is a serial section scanning electron microscopy technique where a focused ion beam is used to ablate the surface of a specimen.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739434"),
    name="focused ion beam scanning electron microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/245"),
    synonyms=["FIB-SEM", "FIB/SEM", "FIBSEM", "focused ion beam scanning electron microscoscopy technique"],
)
Technique.functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/functionalMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that generates multiple images over time of some physiological processes of a specimen.",
    name="functional magnetic resonance imaging",
    synonyms=["fMRI", "functional MRI"],
)
Technique.gene_expression_measurement = Technique(
    id="https://openminds.om-i.org/instances/technique/geneExpressionMeasurement",
    name="gene expression measurement",
)
Technique.gene_knockin = Technique(
    id="https://openminds.om-i.org/instances/technique/geneKnockin",
    name="gene knockin",
)
Technique.gene_knockout = Technique(
    id="https://openminds.om-i.org/instances/technique/geneKnockout",
    name="gene knockout",
)
Technique.genome_wide_association_study = Technique(
    id="https://openminds.om-i.org/instances/technique/genomeWideAssociationStudy",
    definition="A 'genome-wide association study' is an analysis technique comparing the allele frequencies of all available (or a whole genome representative set of) polymorphic markers in unrelated individuals with a specific symptom or disease condition, and those of healthy controls to identify markers associated with a specific disease or condition.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0104603"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/NLXINV:1005075#genome-association-studies"),
    name="genome-wide association study",
    preferred_ontology_identifier=IRI("http://edamontology.org/topic_3517"),
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
Technique.golgi_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/GolgiStaining",
    definition="'Golgi staining' includes several silver staining techniques in which fixed tissue is impregnated with silver nitrate and potassium dichromate resulting in the complete staining of some nerve cells while other cells are not stained at all. [adapted from InterLex](http://uri.interlex.org/ilx_0104713)",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0104713"),
    name="Golgi staining",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_2243"),
    synonyms=["Golgi method", "black reaction"],
)
Technique.he_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/HEStaining",
    definition="An 'H&E staining' combines the two histological stains hematoxylin and eosin which highlight a large portion of microscopic anatomy in a tissue. It is therefore the most widely used stain in medical and histopathological diagnosis.",
    name="H&E staining",
    synonyms=["HE staining", "hematoxylin and eosin staining", "hematoxylin-eosin staining"],
)
Technique.heavy_metal_negative_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/heavyMetalNegativeStaining",
    definition="In a 'heavy metal negative staining', a thin and amorphous film of heavy metal salts (e.g. uranyl acetate) is applied on a sample to reveal its structural details for electron microscopy.",
    name="heavy metal negative staining",
    synonyms=["heavy metal salt staining", "heavy metal staining", "negative staining"],
)
Technique.high_density_electroencephalography = Technique(
    id="https://openminds.om-i.org/instances/technique/highDensityElectroencephalography",
    name="high-density electroencephalography",
)
Technique.high_field_functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/highFieldFunctionalMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that generates multiple images over time of some physiological processes of a specimen typically employing a magnetic field strength of 3 Tesla (or higher but below 7 Tesla).",
    name="high-field functional magnetic resonance imaging",
    synonyms=[
        "HF fMRI",
        "HF functional magnetic resonance imaging",
        "HF functional MRI",
        "high-field fMRI",
        "high-field functional MRI",
    ],
)
Technique.high_field_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/highFieldMagneticResonanceImaging",
    definition="Any medical imaging technique that typically uses a magnetic field strength of 3 Tesla (or higher but below 7 Tesla) to generate images of a specimen based on the principle of nuclear magnetic resonance.",
    name="high-field magnetic resonance imaging",
    synonyms=[
        "HF MRI",
        "high-field MRI",
        "HF magnetic resonance imaging",
        "HF unspecified magnetic resonance imaging",
        "high-field unspecified magnetic resonance imaging",
    ],
)
Technique.high_field_structural_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/highFieldStructuralMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that typically uses a magnetic field strength of 3 Tesla (or higher but below 7 Tesla) to generate images with static information of the scanned body.",
    name="high-field structural magnetic resonance imaging",
    synonyms=[
        "HF sMRI",
        "HF structural MRI",
        "HF structural magnetic resonance imaging",
        "high-field structural MRI",
        "HF MRI",
        "high-field MRI",
        "HF magnetic resonance imaging",
        "high-field magnetic resonance imaging",
    ],
)
Technique.high_resolution_scanning = Technique(
    id="https://openminds.om-i.org/instances/technique/high-resolutionScanning",
    name="high-resolution scanning",
)
Technique.high_speed_video_recording = Technique(
    id="https://openminds.om-i.org/instances/technique/high-speedVideoRecording",
    name="high-speed video recording",
)
Technique.high_throughput_scanning = Technique(
    id="https://openminds.om-i.org/instances/technique/highThroughputScanning",
    definition="'High-throughput scanning' is a technique for automatic creation of analog or digital images of a large number of samples.",
    name="high-throughput scanning",
    synonyms=["high throughput scanning"],
)
Technique.histochemistry = Technique(
    id="https://openminds.om-i.org/instances/technique/histochemistry",
    name="histochemistry",
)
Technique.hoechst_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/HoechstStaining",
    definition="A nuclear-specific staining technique where a Hoechst dye is used.",
    description="Hoechst dyes are part of a family of blue fluorescent dye that bind to DNA. It acts similarly as DAPi and can also be used on both fixated and living cells.",
    name="Hoechst staining",
    synonyms=["Hoechst stain"],
)
Technique.hpc_simulation = Technique(
    id="https://openminds.om-i.org/instances/technique/HPCSimulation",
    name="HPC simulation",
    synonyms=["High Performance Computing simulation"],
)
Technique.immunohistochemistry = Technique(
    id="https://openminds.om-i.org/instances/technique/immunohistochemistry",
    definition="In 'immunohistochemistry' antigens or haptens are detected and visualized in cells of a tissue sections by exploiting the principle of antibodies binding specifically to antigens in biological tissues.",
    name="immunohistochemistry",
    synonyms=["IHC"],
)
Technique.immunoprecipitation = Technique(
    id="https://openminds.om-i.org/instances/technique/immunoprecipitation",
    name="immunoprecipitation",
)
Technique.implant_surgery = Technique(
    id="https://openminds.om-i.org/instances/technique/implantSurgery",
    name="implant surgery",
)
Technique.in_situ_hybridisation = Technique(
    id="https://openminds.om-i.org/instances/technique/inSituHybridisation",
    name="in situ hybridisation",
)
Technique.infrared_differential_interference_contrast_video_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/infraredDifferentialInterferenceContrastVideoMicroscopy",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739494"),
    name="infrared differential interference contrast video microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/IRDIC"),
    synonyms=["IR DIC video microscopy", "IR-DIC"],
)
Technique.injection = Technique(
    id="https://openminds.om-i.org/instances/technique/injection",
    name="injection",
)
Technique.intracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/intracellularElectrophysiology",
    definition="A technique used to measure electrical properties of a single cell, e.g. a neuron.",
    description="'Intracellular electrophysiology' describes a group of techniques used to measure with precision the voltage across, or electrical currents passing through, neuronal or other cellular membranes by inserting an electrode inside the neuron.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739521"),
    name="intracellular electrophysiology",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/222"),
    synonyms=["intracellular recording"],
)
Technique.intracellular_injection = Technique(
    id="https://openminds.om-i.org/instances/technique/intracellularInjection",
    name="intracellular injection",
)
Technique.intracranial_electroencephalography = Technique(
    id="https://openminds.om-i.org/instances/technique/intracranialElectroencephalography",
    name="intracranial electroencephalography",
)
Technique.intraperitoneal_injection = Technique(
    id="https://openminds.om-i.org/instances/technique/intraperitonealInjection",
    definition="An 'intraperitoneal injection' is the administration of a substance into the peritoneum (abdominal cavity) via a needle or tube.",
    name="intraperitoneal injection",
    synonyms=["i.p.", "i.p. injection", "IP", "IP injection"],
)
Technique.intravenous_injection = Technique(
    id="https://openminds.om-i.org/instances/technique/intravenousInjection",
    definition="An 'intravenous injection' is the administration of a substance into a vein or veins via a needle or tube.",
    name="intravenous injection",
    synonyms=["i.v.", "i.v. injection", "IV", "IV injection"],
)
Technique.iontophoresis = Technique(
    id="https://openminds.om-i.org/instances/technique/iontophoresis",
    name="iontophoresis",
)
Technique.iontophoretic_microinjection = Technique(
    id="https://openminds.om-i.org/instances/technique/iontophoreticMicroinjection",
    name="iontophoretic microinjection",
)
Technique.light_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/lightMicroscopy",
    definition="Light microscopy, also referred to as optical microscopy, comprises any type of microscopy technique that uses visible light to generate magnified images of small objects.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0780269"),
    name="light microscopy",
    preferred_ontology_identifier=IRI("http://edamontology.org/topic_3385"),
    synonyms=["LM", "optical microscopy"],
)
Technique.light_sheet_fluorescence_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/lightSheetFluorescenceMicroscopy",
    definition="Lightsheet fluorescence microscopy is a fluorescence microscopy technique that uses a thin sheet of light to excite only fluorophores within the plane of illumination.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739693"),
    name="light sheet fluorescence microscopy",
    preferred_ontology_identifier=IRI(
        "http://uri.interlex.org/tgbugs/uris/readable/technique/lightSheetMicroscopyFluorescent"
    ),
    synonyms=["light sheet microscopy", "LSFM", "selective plane illumination microscopy", "SPIM"],
)
Technique.magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/magneticResonanceImaging",
    definition="Any medical imaging technique that uses strong magnetic fields, magnetic field gradients, and radio waves to generate images of a specimen based on the principle of nuclear magnetic resonance.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0741208"),
    name="magnetic resonance imaging",
    synonyms=["MRI", "unspecified magnetic resonance imaging"],
)
Technique.magnetic_resonance_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/magneticResonanceSpectroscopy",
    name="magnetic resonance spectroscopy",
)
Technique.magnetization_transfer_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/magnetizationTransferImaging",
    definition="A magnetic resonance imaging technique that exploits the contrast between tissues where 1H protons are (i) bound to macromolecules, (ii) in free water, and (iii) in water of hydration layer between macromolecules and free water.",
    name="magnetization transfer imaging",
    synonyms=["MTI", "MT imaging"],
)
Technique.magnetoencephalography = Technique(
    id="https://openminds.om-i.org/instances/technique/magnetoencephalography",
    definition="'Magnetoencephalography' is a noninvasive neuroimaging technique for studying brain activity by recording magnetic fields produced by electrical currents occurring naturally in the brain, using very sensitive magnetometers. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Magnetoencephalography)]",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0741209"),
    name="magnetoencephalography",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/163"),
    synonyms=["MEG"],
)
Technique.mass_spectrometry = Technique(
    id="https://openminds.om-i.org/instances/technique/massSpectrometry",
    name="mass spectrometry",
)
Technique.micro_computed_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/microComputedTomography",
    definition="'Micro computed tomography' uses X-rays to create cross-sections of physical objects with resolution in the micrometer range that can be used to recreate 3-dimensional models [adapted from [Wikipedia](https://en.wikipedia.org/wiki/X-ray_microtomography)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0489243"),
    name="micro computed tomography",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0514122"),
    synonyms=["micro CT", "microtomography", "X-ray microtomography", "X-ray micro computed tomography"],
)
Technique.microtome_sectioning = Technique(
    id="https://openminds.om-i.org/instances/technique/microtomeSectioning",
    definition="A technique used to cut specimen in thin slices using a microtome.",
    description="The microtome cutting thickness can range between 50 nanometer and 100 micrometer.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739422"),
    name="microtome sectioning",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/212"),
    synonyms=["microtomy"],
)
Technique.motion_capture = Technique(
    id="https://openminds.om-i.org/instances/technique/motionCapture",
    definition="'Motion capture' refers to a group of techniques used to measure the movement and/or position of an object, specimen, or anatomical parts of a specimen over a given period of time.",
    name="motion capture",
    synonyms=["motion tracking", "movement tracking"],
)
Technique.multi_compartment_modeling = Technique(
    id="https://openminds.om-i.org/instances/technique/multi-compartmentModeling",
    name="multi-compartment modeling",
)
Technique.multi_electrode_extracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/multiElectrodeExtracellularElectrophysiology",
    name="multi-electrode extracellular electrophysiology",
)
Technique.multi_photon_fluorescence_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/multiPhotonFluorescenceMicroscopy",
    definition="Multi photon fluorescence microscopy is a fluorescence microscopy technique for living tissue which is based on the simultaneous excitation by two or more photons with longer wavelength than the emitted light.",
    name="multi photon fluorescence microscopy",
    synonyms=["multi photon microscopy", "multi-photon microscopy", "MPM", "multi-photon fluorescence microscopy"],
)
Technique.multiple_whole_cell_patch_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/multipleWholeCellPatchClamp",
    name="multiple whole cell patch clamp",
)
Technique.myelin_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/myelinStaining",
    definition="A technique used to selectively alter the appearance of myelin (sheaths) that surround the nerve cell axons.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107265"),
    name="myelin staining",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_2248"),
)
Technique.myelin_water_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/myelinWaterImaging",
    definition="A magnetic resonance imaging technique that provides in vivo measurement of myelin.",
    name="myelin water imaging",
    synonyms=["MWI"],
)
Technique.near_infrared_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/nearInfraredSpectroscopy",
    definition="A noninvasive technique that uses the differential absorption properties of hemoglobin and myoglobin to evaluate tissue oxygenation and indirectly can measure regional hemodynamics and blood flow [taken from [Interlex](http://uri.interlex.org/base/ilx_0488397)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0488397"),
    name="near infrared spectroscopy",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0028692"),
)
Technique.neuromorphic_simulation = Technique(
    id="https://openminds.om-i.org/instances/technique/neuromorphicSimulation",
    name="neuromorphic simulation",
)
Technique.nissl_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/NisslStaining",
    definition="The term 'Nissl staining' refers to various basic dyes (e.g., aniline, thionine, cresyl violet) that selectively label negatively charged molecules (e.g., DNA, RNA) and are therefore typically used to highlight important structural features of cell bodies.",
    name="Nissl staining",
    synonyms=["Nissl", "Nissl method"],
)
Technique.nonlinear_optical_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/nonlinearOpticalMicroscopy",
    definition="Microscopic imaging techniques that utilize nonlinear responses of light-matter interactions which occur with high-intensity illumination, such as from lasers, and specialized light signal detection instrumentation to produce images without the need for dyes or fluorescent labels. [taken from [Interlex](http://uri.interlex.org/base/ilx_0436517)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0436517"),
    name="nonlinear optical microscopy",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M000623844"),
)
Technique.nucleic_acid_extraction = Technique(
    id="https://openminds.om-i.org/instances/technique/nucleicAcidExtraction",
    definition="'Nucleic acid extraction' refers to a group of techniques that all separate nucleic acids from proteins and lipids using three major processes: isolation, purification, and concentration.",
    name="nucleic acid extraction",
)
Technique.optical_coherence_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/opticalCoherenceTomography",
    definition="Imaging technique that combines interferometry with short-coherence-length light to obtain micrometer-level depth resolution. Transverse scanning of the light beam is used to form two- and three-dimensional images, reflected from biological tissue or scattering media [Adapted from [Wikipedia](https://en.wikipedia.org/wiki/Optical_coherence_tomography)].",
    name="optical coherence tomography",
    synonyms=["OCT"],
)
Technique.optical_coherence_tomography_angiography = Technique(
    id="https://openminds.om-i.org/instances/technique/opticalCoherenceTomographyAngiography",
    definition="Imaging technique that uses laser light reflectance of the surface from moving red blood cells to create detailed images of blood vessels over time [Adapted from [EyeWiki](https://eyewiki.aao.org/Optical_Coherence_Tomography_Angiography)].",
    name="optical coherence tomography angiography",
    synonyms=["OCT-A"],
)
Technique.optogenetic_inhibition = Technique(
    id="https://openminds.om-i.org/instances/technique/optogeneticInhibition",
    definition="Optogenetic inhibition is a genetic technique in which the activity of specific neuron populations is decreased using light of a particular wavelength. This can be achieved by expressing light-sensitive ion channels, pumps or enzymes specifically in the target neurons.",
    name="optogenetic inhibition",
)
Technique.oral_administration = Technique(
    id="https://openminds.om-i.org/instances/technique/oralAdministration",
    definition="In an 'oral administration' a substance is taken through the mouth.",
    name="oral administration",
    synonyms=["p.o.", "per os", "PO"],
)
Technique.organ_extraction = Technique(
    id="https://openminds.om-i.org/instances/technique/organExtraction",
    name="organ extraction",
)
Technique.patch_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/patchClamp",
    name="patch clamp",
)
Technique.perfusion_fixation_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/perfusionFixationTechnique",
    definition="Perfusion fixation is a fixation technique to preserve specimen permanently as faithfully as possible compared to the living state by using the vascular system to distribute fixatives throughout the tissue.",
    name="perfusion fixation technique",
)
Technique.perfusion_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/perfusionTechnique",
    definition="Perfusion is a technique to distribute fluid through the circulatory system or lymphatic system to an organ or a tissue.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739602"),
    name="perfusion technique",
)
Technique.perturbational_complexity_index_measurement = Technique(
    id="https://openminds.om-i.org/instances/technique/perturbationalComplexityIndexMeasurement",
    name="perturbational complexity index measurement",
)
Technique.phase_contrast_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/phaseContrastMicroscopy",
    definition="Optical microscopy technique that converts phase shifts in light passing through a transparent specimen to brightness changes in the image [taken from [Wikipedia](https://en.wikipedia.org/wiki/Phase-contrast_microscopy)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739510"),
    name="phase contrast microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/158"),
    synonyms=["phase-contrast microscopy", "PCM"],
)
Technique.phase_contrast_x_ray_computed_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/phaseContrastXRayComputedTomography",
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
    id="https://openminds.om-i.org/instances/technique/phaseContrastXRayImaging",
    definition="'Phase-contrast x-ray imaging' is a general term for different x-ray techniques that use changes in the phase of an x-ray beam passing through an object leading to images with improved soft tissue contrast without the application of a contrast medium. (adapted from [Wikipedia](https://en.wikipedia.org/wiki/Phase-contrast_X-ray_imaging))",
    name="phase-contrast x-ray imaging",
    synonyms=["phase-sensitive x-ray imaging"],
)
Technique.photoactivation = Technique(
    id="https://openminds.om-i.org/instances/technique/photoactivation",
    name="photoactivation",
)
Technique.photoinactivation = Technique(
    id="https://openminds.om-i.org/instances/technique/photoinactivation",
    name="photoinactivation",
)
Technique.photoplethysmography = Technique(
    id="https://openminds.om-i.org/instances/technique/photoplethysmography",
    definition="Photoplethysmography is a non-invasive technique to optically detect blood volume changes in the micro-vascular bed of tissue by measuring the transmissive absorption and/or the reflection of light by the skin.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0487650"),
    name="photoplethysmography",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0026056"),
    synonyms=["PPG"],
)
Technique.polarized_light_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/polarizedLightMicroscopy",
    definition="Polarized light microscopy comprises all optical microscopy techniques involving polarized light.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0485478"),
    name="polarized light microscopy",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0013816"),
    synonyms=["polarized-light microscopy"],
)
Technique.population_receptive_field_mapping = Technique(
    id="https://openminds.om-i.org/instances/technique/populationReceptiveFieldMapping",
    name="population receptive field mapping",
)
Technique.positron_emission_tomography = Technique(
    id="https://openminds.om-i.org/instances/technique/positronEmissionTomography",
    name="positron emission tomography",
)
Technique.pressure_injection = Technique(
    id="https://openminds.om-i.org/instances/technique/pressureInjection",
    definition="Pressure injection uses either air compression or mechanical pressure to eject a substance from a micropipette (from Veith et al., 2016; J.Vis.Exp. (109):53724; doi: 10.3791/53724).",
    name="pressure injection",
)
Technique.primary_antibody_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/primaryAntibodyStaining",
    name="primary antibody staining",
)
Technique.pseudo_continuous_arterial_spin_labeling = Technique(
    id="https://openminds.om-i.org/instances/technique/pseudoContinuousArterialSpinLabeling",
    name="pseudo-continuous arterial spin labeling",
)
Technique.psychological_testing = Technique(
    id="https://openminds.om-i.org/instances/technique/psychologicalTesting",
    definition="'Psychological testing' is a psychometric measurement to evaluate a person's response to a psychological test according to carefully prescribed guidelines. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Psychological_testing)]",
    name="psychological testing",
)
Technique.pupillometry = Technique(
    id="https://openminds.om-i.org/instances/technique/pupillometry",
    definition="Pupillometry is the measurement of minute fluctuations in pupil diameter in response to a stimulus.",
    name="pupillometry",
)
Technique.quantification = Technique(
    id="https://openminds.om-i.org/instances/technique/quantification",
    name="quantification",
)
Technique.quantitative_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/quantitativeMagneticResonanceImaging",
    definition="Any magnetic resonance imaging technique that generates images of a specimen based on the physical parameters of the local tissue microstructural environment.",
    name="quantitative magnetic resonance imaging",
    synonyms=["qMRI", "quantitative MRI"],
)
Technique.quantitative_susceptibility_mapping = Technique(
    id="https://openminds.om-i.org/instances/technique/quantitativeSusceptibilityMapping",
    definition="MRI technique, where the voxel intensity is linear proportional to the underlying tissue [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Quantitative_susceptibility_mapping)].",
    name="quantitative susceptibility mapping",
    synonyms=["QSM"],
)
Technique.raman_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/RamanSpectroscopy",
    definition="A spectroscopic technique where scattered light is used to measure the vibrational energy modes of a sample. It relies upon inelastic scattering of photons (Raman scattering) and can provide both chemical and structural information.",
    name="Raman spectroscopy",
)
Technique.receptive_field_mapping = Technique(
    id="https://openminds.om-i.org/instances/technique/receptiveFieldMapping",
    definition="In 'receptive field mapping' a distinct set of physiological stimuli is used to evoke a sensory neuronal response in specific organisms to define its respective sensory space (receptive field).",
    name="receptive field mapping",
    synonyms=["RF mapping"],
)
Technique.reporter_gene_based_expression_measurement = Technique(
    id="https://openminds.om-i.org/instances/technique/reporterGeneBasedExpressionMeasurement",
    name="reporter gene based expression measurement",
)
Technique.reporter_protein_based_expression_measurement = Technique(
    id="https://openminds.om-i.org/instances/technique/reporterProteinBasedExpressionMeasurement",
    name="reporter protein based expression measurement",
)
Technique.retinotopic_mapping = Technique(
    id="https://openminds.om-i.org/instances/technique/retinotopicMapping",
    definition="In 'retinotopic mapping' the retina is repeatedly stimulated in such a way that the response of neurons, particularly within the visual stream, can be mapped to the location of the stimulus on the retina.",
    name="retinotopic mapping",
    synonyms=["retinal mapping"],
)
Technique.retrograde_tracing = Technique(
    id="https://openminds.om-i.org/instances/technique/retrogradeTracing",
    definition="Retrograde tracing is a technique used to trace neural connections from their point of termination (the synapse) to their source (the cell body).",
    description="In 'retrograde tracing' a tracer substance is taken up by synaptic terminals (and sometimes by axons) of neurons in the region where it is injected. Retrograde tracing techniques allow for a detailed assessment of neuronal connections between a target population of neurons and their inputs throughout the nervous system.",
    name="retrograde tracing",
)
Technique.rna_sequencing = Technique(
    id="https://openminds.om-i.org/instances/technique/RNASequencing",
    definition="'RNA sequencing' refers to a group of techniques that are used to (directly or indirectly) determine the order of nucleotides (nucleic acid sequence) in RNA.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0782092"),
    name="RNA sequencing",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_0001177"),
    synonyms=["ribonucleic acid sequencing", "ribonucleic acid sequencing assay", "RNA sequencing assay", "RNA-Seq"],
)
Technique.rule_based_modeling = Technique(
    id="https://openminds.om-i.org/instances/technique/rule-basedModeling",
    name="rule-based modeling",
)
Technique.scanning_electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/scanningElectronMicroscopy",
    definition="Scanning electron microscopy is a microscopy technique to produce images of a specimen by scanning the surface with focused beam of electrons.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739710"),
    name="scanning electron microscopy",
    preferred_ontology_identifier=IRI(
        "http://uri.interlex.org/tgbugs/uris/readable/technique/scanningElectronMicroscopy"
    ),
    synonyms=["SEM", "scanning electron microscopy technique"],
)
Technique.scattered_light_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/scatteredLightImaging",
    name="scattered light imaging",
)
Technique.sds_digested_freeze_fracture_replica_labeling = Technique(
    id="https://openminds.om-i.org/instances/technique/SDSDigestedFreezeFractureReplicaLabeling",
    name="SDS-digested freeze-fracture replica labeling",
)
Technique.secondary_antibody_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/secondaryAntibodyStaining",
    name="secondary antibody staining",
)
Technique.serial_block_face_scanning_electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/serialBlockFaceScanningElectronMicroscopy",
    definition="Serial block face scanning electron microscopy is a serial section scanning electron microscopy technique where an ultramicrotome is used to remove the surface layer of a specimen.",
    name="serial block face scanning electron microscopy",
    synonyms=["SB-SEM", "SBEM", "serial blockface SEM"],
)
Technique.serial_section_transmission_electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/serialSectionTransmissionElectronMicroscopy",
    definition="Serial section transmission electron microscopy is a microscopy technique in which a beam of electrons is transmitted through multiple successive slices of a volumetric sample to produce images of the slices (e.g. for later 3D reconstruction).",
    name="serial section transmission electron microscopy",
)
Technique.sharp_electrode_intracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/sharpElectrodeIntracellularElectrophysiology",
    definition="An intracellular electrophysiology technique where a microelectrode/micropipette is used to measure electrical properties of a single cell, e.g. a neuron.",
    description="This technique uses a fine-tipped micropipette/microelectrode that is inserted into the neuron, allowing direct recording of electrical events generated by the neuron (membrane potential, resistance, time constant, synaptic potentials and action potentials).",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739713"),
    name="sharp electrode intracellular electrophysiology",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/sharpElectrodeEphys"),
    synonyms=[
        "sharp electrode technique",
        "sharp intracellular electrode technique",
        "sharp electrode recording",
        "sharp intracellular electrode recording",
    ],
)
Technique.silver_staining = Technique(
    id="https://openminds.om-i.org/instances/technique/silverStaining",
    definition="A technique where the appearance of biological subcellular targets (e.g. proteins, RNA or DNA) is selectively alter by use of silver.",
    description="Silver can be used to stain subcellular targets such as proteins, peptide, carbohydrates, RNA or DNA. This techniques is typically used on histological sections prior to light microscopy, for the detection of proteins and peptides in polyacrylamide gels or gel electrophoresis.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0110626"),
    name="silver staining",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_152217"),
    synonyms=["silver stain"],
)
Technique.simulation = Technique(
    id="https://openminds.om-i.org/instances/technique/simulation",
    name="simulation",
)
Technique.single_cell_rna_sequencing = Technique(
    id="https://openminds.om-i.org/instances/technique/singleCellRNASequencing",
    name="single cell RNA sequencing",
)
Technique.single_electrode_extracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/singleElectrodeExtracellularElectrophysiology",
    name="single electrode extracellular electrophysiology",
)
Technique.single_electrode_juxtacellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/singleElectrodeJuxtacellularElectrophysiology",
    name="single electrode juxtacellular electrophysiology",
)
Technique.single_gene_analysis = Technique(
    id="https://openminds.om-i.org/instances/technique/singleGeneAnalysis",
    definition="A 'single gene analysis' is a genetic test (sequencing technique) to check for any genetic changes in a specific gene.",
    name="single gene analysis",
    synonyms=["single gene sequencing", "single gene test"],
)
Technique.single_nucleotide_polymorphism_detection = Technique(
    id="https://openminds.om-i.org/instances/technique/singleNucleotidePolymorphismDetection",
    definition="'Single nucleotide polymorphism detection' refers to a group of techniques that are used to scan for new polymorphisms and to determine the allele(s) of a known polymorphism in target sequences (adapted from [Kwok and Chen, 2003](https://doi.org/10.21775/cimb.005.043)).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0780321"),
    name="single nucleotide polymorphism detection",
    preferred_ontology_identifier=IRI("http://edamontology.org/operation_0484"),
    synonyms=["SNP calling", "SNP detection", "SNP discovery"],
)
Technique.sodium_mri = Technique(
    id="https://openminds.om-i.org/instances/technique/sodiumMRI",
    definition="'Sodium MRI' is a specialised magnetic resonance imaging technique that uses strong magnetic fields, magnetic field gradients, and radio waves to generate images of the distribution of sodium in the body. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Sodium_MRI)]",
    name="sodium MRI",
    synonyms=["Na MRI", "Na-MRI", "Sodium-MRI"],
)
Technique.sonography = Technique(
    id="https://openminds.om-i.org/instances/technique/sonography",
    name="sonography",
)
Technique.standardization = Technique(
    id="https://openminds.om-i.org/instances/technique/standardization",
    definition="'Standardization' is the process of providing (meta)data according to a consensus of different parties (e.g., firms, users, interest groups, organizations and governments).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0479520"),
    name="standardization",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0018674"),
)
Technique.stereoelectroencephalography = Technique(
    id="https://openminds.om-i.org/instances/technique/stereoelectroencephalography",
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
    id="https://openminds.om-i.org/instances/technique/stereology",
    definition="An imaging assay that is used for the three-dimensional interpretation of planar sections of materials or tissues.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739729"),
    name="stereology",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/79"),
)
Technique.stereotactic_surgery = Technique(
    id="https://openminds.om-i.org/instances/technique/stereotacticSurgery",
    name="stereotactic surgery",
)
Technique.structural_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/structuralMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that uses strong magnetic fields, magnetic field gradients, and radio waves to generate images with static information of the scanned body.",
    name="structural magnetic resonance imaging",
    synonyms=["sMRI", "structural MRI", "MRI", "magnetic resonance imaging"],
)
Technique.structural_neuroimaging = Technique(
    id="https://openminds.om-i.org/instances/technique/structuralNeuroimaging",
    name="structural neuroimaging",
)
Technique.subcutaneous_injection = Technique(
    id="https://openminds.om-i.org/instances/technique/subcutaneousInjection",
    definition="An 'subcutenous injection' is the administration of a substance under all the layers of the skin via a needle or tube.",
    name="subcutaneous injection",
    synonyms=["s.c.", "s.c. injection", "SC", "SC injection"],
)
Technique.subdural_electrocorticography = Technique(
    id="https://openminds.om-i.org/instances/technique/subduralElectrocorticography",
    name="subdural electrocorticography",
)
Technique.super_resolution_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/superResolutionMicroscopy",
    definition="Techniques in optical microscopy that allow images to have resolutions higher than those imposed by the diffraction limit, due to the diffraction of light [taken from [Wikipedia](https://en.wikipedia.org/wiki/Super-resolution_microscopy)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739445"),
    name="super resolution microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/218"),
    synonyms=["super-resolution microscopy"],
)
Technique.susceptibility_weighted_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/susceptibilityWeightedImaging",
    definition="MRI sequence, used with fully flow compensated, long echo, gradient recalled echo (GRE) pulse sequence. Acquires images sensitive to venous blood, hemorrhage and iron storage. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Susceptibility_weighted_imaging)].",
    name="susceptibility weighted imaging",
    synonyms=["SWI", "BOLD venographic imaging"],
)
Technique.switch_immunohistochemistry = Technique(
    id="https://openminds.om-i.org/instances/technique/SWITCHImmunohistochemistry",
    name="SWITCH immunohistochemistry",
)
Technique.tde_clearing = Technique(
    id="https://openminds.om-i.org/instances/technique/TDEClearing",
    name="TDE clearing",
)
Technique.tetrode_extracellular_electrophysiology = Technique(
    id="https://openminds.om-i.org/instances/technique/tetrodeExtracellularElectrophysiology",
    name="tetrode extracellular electrophysiology",
)
Technique.three_d_computer_graphic_modeling = Technique(
    id="https://openminds.om-i.org/instances/technique/3DComputerGraphicModeling",
    name="3D computer graphic modeling",
)
Technique.three_d_polarized_light_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/3DPolarizedLightImaging",
    definition="'3D polarized light imaging' (synonym: 3D-PLI) is a 3D reconstruction process of high-resoluted image data originating from polorized light microscopy.",
    name="3D polarized light imaging",
)
Technique.three_d_scanning = Technique(
    id="https://openminds.om-i.org/instances/technique/3DScanning",
    name="3D scanning",
)
Technique.time_of_flight_magnetic_resonance_angiography = Technique(
    id="https://openminds.om-i.org/instances/technique/time-of-flightMagneticResonanceAngiography",
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
    id="https://openminds.om-i.org/instances/technique/TimmsStaining",
    definition="A technique used to selectively visualize a variety of metals (e.g. zinc, copper, iron) in biological tissue based on sulphide-precipitation of metals in the tissue.",
    description="The principle of this technique is that metals in the tissue can be transformed histochemically to metal sulphide. Subsequently, metal sulphide catalyze the reduction of silver ions by a reducing agent to metallic grains that are visible under a light or electron microscope.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0107265"),
    name="Timm's staining",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_2248"),
    synonyms=["Timm's stain", "Timm's sulfide silver staining"],
)
Technique.tissue_clearing = Technique(
    id="https://openminds.om-i.org/instances/technique/tissueClearing",
    name="tissue clearing",
)
Technique.tract_tracing = Technique(
    id="https://openminds.om-i.org/instances/technique/tractTracing",
    name="tract tracing",
)
Technique.transcardial_perfusion_fixation_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/transcardialPerfusionFixationTechnique",
    definition="Transcardial perfusion fixation is a technique to distribute fixatives throughout tissue via the heart.",
    name="transcardial perfusion fixation technique",
    synonyms=["intracardiac perfusion fixation technique", "intracardial perfusion fixation technique"],
)
Technique.transcardial_perfusion_technique = Technique(
    id="https://openminds.om-i.org/instances/technique/transcardialPerfusionTechnique",
    definition="Transcardial perfusion is a technique to distribute fluid throughout tissue via the heart.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739695"),
    name="transcardial perfusion technique",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/167"),
    synonyms=["intracardiac perfusion technique", "intracardial perfusion technique"],
)
Technique.transmission_electron_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/transmissionElectronMicroscopy",
    definition="Transmission electron microscopy is a microscopy technique in which a beam of electrons is transmitted through a specimen to produce an image.",
    name="transmission electron microscopy",
    synonyms=["TEM"],
)
Technique.two_photon_fluorescence_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/twoPhotonFluorescenceMicroscopy",
    definition="Two-photon fluorescence microscopy is a fluorescence microscopy technique for living tissue which is based on the simultaneous excitation by two photons with longer wavelength than the emitted light.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739658"),
    name="two-photon fluorescence microscopy",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/twoPhoton"),
    synonyms=[
        "2-photon excitation microscopy",
        "2-photon fluorescence microscopy",
        "2-photon microscopy",
        "2PEF",
        "TPEF",
        "TPM",
        "two-photon excitation fluorescence microscopy",
        "two-photon excitation microscopy",
        "two-photon microscopy",
    ],
)
Technique.ultra_high_field_functional_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/ultraHighFieldFunctionalMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that generates multiple images over time of some physiological processes of a specimen typically employing a magnetic field strength of 7 Tesla (or higher).",
    name="ultra high-field functional magnetic resonance imaging",
    synonyms=[
        "UHF fMRI",
        "UHF functional magnetic resonance imaging",
        "UHF functional MRI",
        "ultra high-field fMRI",
        "ultra high-field functional MRI",
    ],
)
Technique.ultra_high_field_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/ultraHighFieldMagneticResonanceImaging",
    definition="Any medical imaging technique that typically uses a magnetic field strength of 7 Tesla (or higher) to generate images of a specimen based on the principle of nuclear magnetic resonance.",
    name="ultra high-field magnetic resonance imaging",
    synonyms=[
        "UHF MRI",
        "UHF magnetic resonance imaging",
        "UHF unspecified magnetic resonance imaging",
        "ultra high-field MRI",
        "ultra high-field unspecified magnetic resonance imaging",
    ],
)
Technique.ultra_high_field_magnetic_resonance_spectroscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/ultraHighFieldMagneticResonanceSpectroscopy",
    definition="'Ultra high-field magnetic resonance spectroscopy' comprises all MRS techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.",
    name="ultra high-field magnetic resonance spectroscopy",
)
Technique.ultra_high_field_structural_magnetic_resonance_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/ultraHighFieldStructuralMagneticResonanceImaging",
    definition="A magnetic resonance imaging technique that typically uses a magnetic field strength of 7 Tesla (or higher) to generate images with static information of the scanned body.",
    name="ultra high-field structural magnetic resonance imaging",
    synonyms=[
        "UHF sMRI",
        "UHF structural MRI",
        "ultra high-field structural MRI",
        "UHF structural magnetic resonance imaging",
        "UHF MRI",
        "ultra high-field MRI",
        "UHF magnetic resonance imaging",
        "ultra high-field magnetic resonance imaging",
    ],
)
Technique.vibratome_sectioning = Technique(
    id="https://openminds.om-i.org/instances/technique/vibratomeSectioning",
    name="vibratome sectioning",
)
Technique.video_oculography = Technique(
    id="https://openminds.om-i.org/instances/technique/video-oculography",
    name="video-oculography",
)
Technique.video_tracking = Technique(
    id="https://openminds.om-i.org/instances/technique/videoTracking",
    name="video tracking",
)
Technique.virus_mediated_transfection = Technique(
    id="https://openminds.om-i.org/instances/technique/virus-mediatedTransfection",
    name="virus-mediated transfection",
)
Technique.voltage_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/voltageClamp",
    definition="'Voltage clamp' comprises all experimental techniques in which the membrane potential (voltage) is constantly changed to a desired value by adding the necessary current to the cell.",
    name="voltage clamp",
)
Technique.voltage_sensitive_dye_imaging = Technique(
    id="https://openminds.om-i.org/instances/technique/voltageSensitiveDyeImaging",
    definition="'Voltage sensitive dye imaging' is an experimental technique to measure neuronal population activity from in vivo brains or live brain slices by transducing changes in the cell membrane potential into changes of fluorescence emission by an employed exogenous chemical agent.",
    name="voltage sensitive dye imaging",
)
Technique.weighted_correlation_network_analysis = Technique(
    id="https://openminds.om-i.org/instances/technique/weightedCorrelationNetworkAnalysis",
    definition="Weighted correlation network analysis is a widely used data mining method for studying networks based on pairwise correlations between variables. While it can be applied to most high-dimensional data sets, it has been most widely used in genomic applications. [adopted from: [wikipedia](https://en.wikipedia.org/wiki/Weighted_correlation_network_analysis)]",
    name="weighted correlation network analysis",
    synonyms=["weighted gene co-expression network analysis", "WGCNA"],
)
Technique.whole_cell_patch_clamp = Technique(
    id="https://openminds.om-i.org/instances/technique/wholeCellPatchClamp",
    definition="'Whole cell patch clamp' is a patch clamp technique where the pipette is sealed onto a cell membrane applying enough suction to rupture the membrane patch in order to provide access from the interior of the pipette to the intracellular space of the cell.",
    name="whole cell patch clamp",
)
Technique.whole_genome_sequencing = Technique(
    id="https://openminds.om-i.org/instances/technique/wholeGenomeSequencing",
    definition="'Whole genome sequencing' is a genetic test (sequencing technique) to determine the entire, or nearly the entire, DNA sequence of an organism's genome at a single time. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Whole_genome_sequencing)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0492452"),
    name="whole genome sequencing",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M000621306"),
    synonyms=["complete genome sequencing", "entire genome sequencing", "full genome sequencing", "WGS"],
)
Technique.widefield_fluorescence_microscopy = Technique(
    id="https://openminds.om-i.org/instances/technique/widefieldFluorescenceMicroscopy",
    definition="'Widefield fluorescence microscopy' comprises all microscopy techniques in which fluorescent molecules of an entire sample are excited through a permanent exposure of a light source of a specific wavelength.",
    name="widefield fluorescence microscopy",
)
