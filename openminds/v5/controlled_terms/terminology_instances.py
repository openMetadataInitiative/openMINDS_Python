# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.terminology import Terminology


Terminology.access_channel = Terminology(
    id="https://openminds.om-i.org/instances/terminology/accessChannel",
    definition="Terminology defining the location or medium through which a resource can be accessed.",
    description="The terminology defining access channel specifies whether a resource is accessible remotely through digital means (virtual), requires physical presence at a specific location (on-site), or is available through both means (hybrid).",
    name="access channel",
)

Terminology.access_eligibility_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/accessEligibilityType",
    definition="The terminology defining access eligibility type specifies whether a resource is openly available to anyone, requires authentication, or authorization.",
    name="access eligibility type",
)

Terminology.access_form = Terminology(
    id="https://openminds.om-i.org/instances/terminology/accessForm",
    definition="Terminology defining the manner in which access to a resource is facilitated.",
    description="The terminology defining access form specifies whether users obtain access directly without intermediaries or through mediation by a third party.",
    name="access form",
)

Terminology.access_process_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/accessProcessType",
    definition="Terminology defining the workflow or mechanism through which access to a resource is granted.",
    name="access process type",
)

Terminology.action_status_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/actionStatusType",
    name="action status type",
)

Terminology.age_category = Terminology(
    id="https://openminds.om-i.org/instances/terminology/ageCategory",
    definition="The age category describes a specific spatiotemporal part of the life cycle of an organism.",
    name="age category",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000105"),
)

Terminology.age_reference = Terminology(
    id="https://openminds.om-i.org/instances/terminology/ageReference",
    definition="A terminology concept denoting a biologically or clinically defined boundary event used to anchor the measurement or interpretation of age in relation to an organism’s life cycle.",
    name="age reference",
)

Terminology.analysis_technique = Terminology(
    id="https://openminds.om-i.org/instances/terminology/analysisTechnique",
    name="analysis technique",
)

Terminology.anatomical_axes_orientation = Terminology(
    id="https://openminds.om-i.org/instances/terminology/anatomicalAxesOrientation",
    name="anatomical axes orientation",
)

Terminology.anatomical_cavity = Terminology(
    id="https://openminds.om-i.org/instances/terminology/anatomicalCavity",
    definition="Terminology defining anatomical cavities and internal spaces within an organism that contain organs, tissues, or fluids, excluding blood and lymph vessels.",
    description="This terminology includes naturally occurring enclosed or semi-enclosed spaces within the body that serve as compartments for anatomical structures or fluids. These spaces may support organ placement, permit movement of structures, or allow circulation of non-vascular fluids such as cerebrospinal fluid. Examples include body cavities, ventricular spaces, and other internal anatomical compartments. The terminology focuses on spatial anatomical entities rather than the tissues forming their boundaries. Vascular conduits responsible for blood or lymph transport are represented separately under vascular structures.",
    name="anatomical cavity",
)

Terminology.anatomical_identification_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/anatomicalIdentificationType",
    definition="The type of identiciation that was used to determine an anatomical location.",
    name="anatomical identification type",
)

Terminology.anatomical_plane = Terminology(
    id="https://openminds.om-i.org/instances/terminology/anatomicalPlane",
    definition="A flat anatomical 2D surface that bisects an anatomical structure or an anatomical space.",
    name="anatomical plane",
    other_ontology_identifiers=["http://uri.interlex.org/ilx_0725051"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035085"),
    synonyms=["fiat anatomical surface"],
)

Terminology.annotation_criteria_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/annotationCriteriaType",
    definition="General classification of how data were annotated.",
    name="annotation criteria type",
)

Terminology.annotation_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/annotationType",
    definition="Geometrical classification of annotations into types.",
    name="annotation type",
)

Terminology.atlas_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/atlasType",
    name="atlas type",
)

Terminology.auditory_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/auditoryStimulusType",
    definition="An 'auditory stimulus type' groups similar auditory stimuli used across auditory stimulation techniques.",
    name="auditory stimulus type",
)

Terminology.biological_order = Terminology(
    id="https://openminds.om-i.org/instances/terminology/biologicalOrder",
    name="biological order",
)

Terminology.biological_sex = Terminology(
    id="https://openminds.om-i.org/instances/terminology/biologicalSex",
    name="biological sex",
)

Terminology.breeding_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/breedingType",
    definition="The breeding type describes how plants or animals have been sexually propagated.",
    name="breeding type",
)

Terminology.cell_culture_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/cellCultureType",
    definition="The type of a cell culture (e.g. primary, secondary)",
    name="cell culture type",
)

Terminology.cell_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/cellType",
    name="cell type",
)

Terminology.chemical_mixture_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/chemicalMixtureType",
    definition="A 'chemical mixture type' groups all mixtures with the same chemical and physical characteristics under a general term.",
    name="chemicalMixtureType",
)

Terminology.colormap = Terminology(
    id="https://openminds.om-i.org/instances/terminology/colormap",
    definition="A colormap is a lookup table specifying the colors to be used in rendering a palettized image, [adapted from [Wiktionary](https://en.wiktionary.org/wiki/colormap)].",
    name="colormap",
)

Terminology.contribution_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/contributionType",
    definition="A functional role characterized by a specific activity or responsibility realized by a role-bearing entity in relation to a target entity and its life cycle.",
    description="A contribution type denotes a functional role realized by a role-bearing entity, which may be a person, organization, consortium, hardware system, software system, service, or another entity capable of performing an activity or assuming a responsibility. The activity or responsibility is directed toward a target entity, which may represent a wide range of entities such as a person, specimen, dataset, software system, model, document, infrastructure component, or another resource.",
    name="contribution type",
)

Terminology.cranial_window_construction_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/cranialWindowConstructionType",
    definition="The construction type of a cranial window.",
    name="cranial window construction type",
)

Terminology.cranial_window_reinforcement_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/cranialWindowReinforcementType",
    definition="The reinforcement type of a cranial window.",
    name="cranial window reinforcement type",
)

Terminology.criteria_quality_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/criteriaQualityType",
    name="criteria quality type",
)

Terminology.data_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/dataType",
    name="data type",
)

Terminology.device_mounting_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/deviceMountingType",
    definition="A terminology defining methods for mechanically attaching devices based on structural integration, compliance, and geometric conformity to the host structure.",
    name="device mounting type",
)

Terminology.device_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/deviceType",
    name="device type",
)

Terminology.difference_measure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/differenceMeasure",
    definition="A measure of the difference between two things",
    description="This may be a numerical or physical quantity, a set of categories, etc. Examples include 'mean squared error', 't-statistic', 'p-value'.",
    name="difference measure",
)

Terminology.disease = Terminology(
    id="https://openminds.om-i.org/instances/terminology/disease",
    name="disease",
)

Terminology.disease_model = Terminology(
    id="https://openminds.om-i.org/instances/terminology/diseaseModel",
    name="disease model",
)

Terminology.educational_level = Terminology(
    id="https://openminds.om-i.org/instances/terminology/educationalLevel",
    definition="An 'educational level' defines the developmental stage of a student and how learning environments are structured. ",
    name="educational level",
)

Terminology.electrical_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/electricalStimulusType",
    definition="An 'electrical stimulus type' groups similar electrical stimuli used across electrical stimulation techniques.",
    name="electrical stimulus type",
)

Terminology.experimental_approach = Terminology(
    id="https://openminds.om-i.org/instances/terminology/experimentalApproach",
    name="experimental approach",
)

Terminology.external_body_region = Terminology(
    id="https://openminds.om-i.org/instances/terminology/externalBodyRegion",
    definition="Terminology defining anatomical regions located on the external surface of an organism’s body.",
    description="This terminology includes body surface areas that are externally visible or directly accessible without reference to internal organs or cavities. These regions are typically defined by morphological boundaries used in anatomy, clinical description, or anatomical orientation. Examples include regions of the head, trunk, and limbs. The terms provide a standardized way to reference surface locations across species. They support anatomical localization and mapping of externally observable features.",
    name="external body region",
)

Terminology.file_bundle_grouping = Terminology(
    id="https://openminds.om-i.org/instances/terminology/fileBundleGrouping",
    name="file bundle grouping",
)

Terminology.file_repository_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/fileRepositoryType",
    name="file repository type",
)

Terminology.file_usage_role = Terminology(
    id="https://openminds.om-i.org/instances/terminology/fileUsageRole",
    name="file usage role",
)

Terminology.genetic_strain_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/geneticStrainType",
    definition="The genetic strain type describes the genetic background type of a strain.",
    name="genetic strain type",
)

Terminology.gustatory_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/gustatoryStimulusType",
    definition="A 'gustatory stimulus type' groups similar gustatory stimuli used across gustatory stimulation techniques.",
    name="gustatory stimulus type",
)

Terminology.handedness = Terminology(
    id="https://openminds.om-i.org/instances/terminology/handedness",
    name="handedness",
)

Terminology.language = Terminology(
    id="https://openminds.om-i.org/instances/terminology/language",
    name="language",
)

Terminology.laterality = Terminology(
    id="https://openminds.om-i.org/instances/terminology/laterality",
    name="laterality",
)

Terminology.learning_resource_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/learningResourceType",
    definition="A 'learning resource type' groups persistent resources that explicitly entail learning activities or learning experiences in a certain format (e.g., in a physical or digital presentation).",
    name="learning resource type",
)

Terminology.measured_quantity = Terminology(
    id="https://openminds.om-i.org/instances/terminology/measuredQuantity",
    definition="A qualified physical quantity that was measured/recorded",
    name="measured quantity",
)

Terminology.measured_signal_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/measuredSignalType",
    definition="The types of biological electrical and non-electrical signals that vary in time and/or space and can be measured.",
    name="measured signal type",
)

Terminology.meta_data_model_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/metaDataModelType",
    name="(meta)data model type",
)

Terminology.model_abstraction_level = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modelAbstractionLevel",
    name="model abstraction level",
)

Terminology.model_scope = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modelScope",
    name="model scope",
)

Terminology.modification_consent_requirement = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modificationConsentRequirement",
    definition="Terminology for specifying whose agreement is required for a contract modification to be legally valid.",
    name="modification consent requirement",
)

Terminology.modification_constraint = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modificationConstraint",
    definition="Terminology for specifying procedural conditions or prohibitions that limit how modifications may be made.",
    name="modification constraint",
)

Terminology.modification_form = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modificationForm",
    definition="Terminology for specifying the formal method by which consent to a modification must be expressed.",
    name="modification form",
)

Terminology.modification_scope = Terminology(
    id="https://openminds.om-i.org/instances/terminology/modificationScope",
    definition="Terminology for specifying which parts or aspects of an agreement may be modified.",
    name="modification scope",
)

Terminology.molecular_entity = Terminology(
    id="https://openminds.om-i.org/instances/terminology/molecularEntity",
    definition="Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.",
    name="molecular entity",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0107064"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/CHEBI:23367#molecular-entity"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/CHEBI_23367"),
)

Terminology.mr_spatial_encoding = Terminology(
    id="https://openminds.om-i.org/instances/terminology/MRSpatialEncoding",
    definition="MR spatial encoding type defines the method by which imaging data is collected, determining the spatial encoding strategy and affecting resolution, scan time, and overall image quality.",
    description="MR spatial encoding dictates how spatial and temporal information is encoded during image acquisition. It is classified based on the number of encoded dimensions: 2D acquisition captures individual slices sequentially using frequency * phase encoding, while 3D acquisition collects an entire volume in a single scan with frequency * phase * phase encoding, offering higher resolution and isotropic reconstruction. In rare cases, 1D acquisition is used for specialized applications like MR spectroscopy, encoding data along a single frequency dimension. The choice of acquisition type depends on clinical and research needs, balancing factors such as scan efficiency, spatial resolution, and signal-to-noise ratio.",
    name="MR spatial encoding",
    synonyms=["MRI acquisition type"],
)

Terminology.mri_fat_suppression_technique = Terminology(
    id="https://openminds.om-i.org/instances/terminology/MRIFatSuppressionTechnique",
    definition="A terminology defining methods for reducing or separating fat signal in MRI using spectral, inversion recovery, or water–fat decomposition techniques.",
    name="MRI fat suppression technique",
)

Terminology.mri_pulse_sequence = Terminology(
    id="https://openminds.om-i.org/instances/terminology/MRIPulseSequence",
    definition="An 'MRI pulse sequence' is a particular setting of pulse sequences and pulsed field gradients, resulting in a particular image appearance [adapted from [Wikipedia](https://en.wikipedia.org/wiki/MRI_pulse_sequence)].",
    name="MRI pulse sequence",
)

Terminology.mri_spoiling_technique = Terminology(
    id="https://openminds.om-i.org/instances/terminology/MRISpoilingTechnique",
    definition="A terminology defining methods for suppressing residual transverse magnetization in MRI through radiofrequency, gradient, or combined spoiling mechanisms.",
    name="MRI spoiling technique",
)

Terminology.mri_weighting = Terminology(
    id="https://openminds.om-i.org/instances/terminology/MRIWeighting",
    definition="Class of imaging techniques where the image contrast is generated from a specific intrinsic tissue parameter (T1, T2, etc.).",
    name="MRI weighting",
)

Terminology.muscular_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/muscularStructure",
    definition="Terminology defining anatomical structures composed primarily of muscle tissue that contribute to body movement or internal mechanical function.",
    description="This terminology includes skeletal muscles and other anatomical structures formed predominantly from muscle tissue. These structures generate force and enable movement of the body or movement within organs. The terminology focuses on structural muscle entities rather than cellular muscle tissue components. Examples include limb muscles and muscles associated with specific anatomical regions. It supports standardized anatomical referencing of muscular components.",
    name="muscular structure",
)

Terminology.nervous_system_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/nervousSystemStructure",
    definition="Terminology defining anatomical structures that are components of the nervous system.",
    description="This terminology includes regions, nuclei, tracts, nerves, and other anatomical components that form part of the central or peripheral nervous system. These structures participate in thr processing, transmission, and integration of information within an organism. The terms cover both macroscopic regions and specialized structural subdivisions of neural anatomy. They are typically derived from cross-species anatomical ontologies such as Uberon. The terminology supports standardized referencing of neural structures in anatomical atlases and datasets.",
    name="nervous system structure",
)

Terminology.olfactory_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/olfactoryStimulusType",
    definition="An 'olfactory stimulus type' groups similar olfactory stimuli used across olfactory stimulation techniques.",
    name="olfactory stimulus type",
)

Terminology.operating_device = Terminology(
    id="https://openminds.om-i.org/instances/terminology/operatingDevice",
    name="operating device",
)

Terminology.operating_system = Terminology(
    id="https://openminds.om-i.org/instances/terminology/operatingSystem",
    name="operating system",
)

Terminology.optical_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/opticalStimulusType",
    definition="An 'optical stimulus type' groups similar optical stimuli used across optical stimulation techniques.",
    name="optical stimulus type",
)

Terminology.organ = Terminology(
    id="https://openminds.om-i.org/instances/terminology/organ",
    definition="Terminology defining whole anatomical organs that function as discrete structural and functional units within an organism.",
    description="This terminology includes complete organs composed of multiple coordinated tissue types organized into a distinct anatomical entity. Only whole organs are included, excluding internal parts or subdivisions of organs. Examples include the heart, liver, lung, and kidney. These entities represent the primary functional units within many biological systems. The terminology provides a standardized reference set for complete organs across species.",
    name="organ",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000062"),
)

Terminology.organ_system_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/organSystemStructure",
    definition="Terminology defining anatomical components and structural parts that belong to or form part of an organ system.",
    description="This terminology includes anatomical structures that are components or subdivisions of organs or other structures within an organ system. These entities are typically smaller structural units that contribute to the organization or function of the system but do not constitute whole organs themselves. Examples may include ducts, chambers, segments, and other system-associated structural components. The terminology focuses on parts that structurally belong to a broader system context. It supports detailed representation of anatomical organization within biological systems.",
    name="organ system structure",
)

Terminology.organism_substance = Terminology(
    id="https://openminds.om-i.org/instances/terminology/organismSubstance",
    definition="Terminology defining biological substances produced by or contained within an organism.",
    description="This terminology includes naturally occurring materials or substances that exist within anatomical contexts of an organism. These may include fluids, secreted substances, or other biological materials associated with tissues or organs. The terms represent substances rather than structural anatomical entities. Examples may include biological fluids or mineralized materials produced by tissues. The terminology enables representation of organism-derived substances in anatomical datasets.",
    name="organism substance",
)

Terminology.organism_system = Terminology(
    id="https://openminds.om-i.org/instances/terminology/organismSystem",
    definition="Terminology defining biological systems composed of multiple interacting anatomical structures that together perform a major physiological function.",
    description="This terminology includes coordinated groups of organs and structures that operate collectively to carry out essential biological processes. Examples include the nervous system, digestive system, and circulatory system. These systems organize anatomical structures into functional frameworks. The terminology represents high-level biological organization within the body. It supports cross-species representation of major physiological systems.",
    name="organism system",
)

Terminology.organization_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/organizationType",
    definition="Terminology for classifying an organization based on its legal status or position within a larger entity.",
    name="organization type",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q17197366"),
)

Terminology.patch_clamp_variation = Terminology(
    id="https://openminds.om-i.org/instances/terminology/patchClampVariation",
    definition="A variation of the patch clamp technique",
    name="patch clamp variation",
)

Terminology.payment_model_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/paymentModelType",
    definition="Terminology defining the pricing structure or financial model associated with accessing a resource.",
    name="payment model type",
)

Terminology.preparation_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/preparationType",
    name="preparation type",
)

Terminology.programming_language = Terminology(
    id="https://openminds.om-i.org/instances/terminology/programmingLanguage",
    name="programming language",
)

Terminology.project_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/projectType",
    definition="Terminology characterizing a project according to its primary grounding, organizational basis, and driving objectives.",
    name="project type",
)

Terminology.publication_status = Terminology(
    id="https://openminds.om-i.org/instances/terminology/publicationStatus",
    definition="Terminology defining the status of a resource in the publication lifecycle.",
    name="publication status",
)

Terminology.pulse_shape = Terminology(
    id="https://openminds.om-i.org/instances/terminology/pulseShape",
    definition="A terminology defining the temporal amplitude profiles of excitation, stimulation, or modulation pulses based on their mathematical or functional form.",
    name="pulse shape",
)

Terminology.qualitative_overlap = Terminology(
    id="https://openminds.om-i.org/instances/terminology/qualitativeOverlap",
    name="qualitative overlap",
)

Terminology.semantic_data_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/semanticDataType",
    name="semantic data type",
)

Terminology.setup_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/setupType",
    definition="The setup type describes the overall purpose of arranging equipment in a certain way (setup).",
    name="setup type",
)

Terminology.skeletal_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/skeletalStructure",
    definition="Terminology defining anatomical structures that form part of the skeletal system.",
    description="This terminology includes bones, cartilaginous elements, and other structural components that contribute to the mechanical framework of the body. These structures provide support, protection, and attachment points for muscles and other tissues. The terminology may include both individual skeletal elements and structural subdivisions of those elements. Examples include bones of the skull, vertebrae, and limb skeleton. It enables consistent representation of the skeletal framework across species.",
    name="skeletal structure",
)

Terminology.software_application_category = Terminology(
    id="https://openminds.om-i.org/instances/terminology/softwareApplicationCategory",
    name="software application category",
)

Terminology.software_feature = Terminology(
    id="https://openminds.om-i.org/instances/terminology/softwareFeature",
    name="software feature",
)

Terminology.sovereign_state = Terminology(
    id="https://openminds.om-i.org/instances/terminology/sovereignState",
    definition="A political entity that possesses supreme governing authority within a defined territory and is not legally subordinate to another state.",
    description="State that has the highest authority over a territory. [Based on the 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q3624078)]",
    name="sovereign state",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q3624078"),
    synonyms=["country", "nation", "sovereign country", "sovereign nation", "Westphalian state"],
)

Terminology.spatial_encoding = Terminology(
    id="https://openminds.om-i.org/instances/terminology/spatialEncoding",
    definition="A terminology defining methods for representing spatial position in signals through frequency-, phase-, or combined encoding mechanisms across one or more dimensions.",
    name="spatial encoding",
)

Terminology.species = Terminology(
    id="https://openminds.om-i.org/instances/terminology/species",
    name="species",
)

Terminology.stimulation_approach = Terminology(
    id="https://openminds.om-i.org/instances/terminology/stimulationApproach",
    name="stimulation approach",
)

Terminology.stimulation_technique = Terminology(
    id="https://openminds.om-i.org/instances/terminology/stimulationTechnique",
    name="stimulation technique",
)

Terminology.subcellular_entity = Terminology(
    id="https://openminds.om-i.org/instances/terminology/subcellularEntity",
    definition="Entity derived from a cell or cells. The anatomical scale of these objects roughly corresponds to that which would be visible in high resolution light microscopy or conventional electron microscopy, e.g., nanometers to microns",
    name="subcellular entity",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0111157"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/GO:0005575#iJ6UjX8BxpaxvvQA_2ri"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/GO_0005575"),
    synonyms=["cellular component"],
)

Terminology.subject_attribute = Terminology(
    id="https://openminds.om-i.org/instances/terminology/subjectAttribute",
    name="subject attribute",
)

Terminology.supranational_body = Terminology(
    id="https://openminds.om-i.org/instances/terminology/supranationalBody",
    definition="An institutional entity created by sovereign states to which they delegate or pool defined aspects of their governing authority for common decision-making that is binding on the member states.",
    description="Political and government system, where several sovereign states give up and share part of their sovereignty for their common governance. [Based on the 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q1335818)]",
    name="supranational body",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q1335818"),
    synonyms=["supranational entity", "supranational union", "supranationalism"],
)

Terminology.tactile_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/tactileStimulusType",
    definition="A 'tactile stimulus type' groups similar tactile stimuli used across tactile stimulation techniques.",
    name="tactile stimulus type",
)

Terminology.technique = Terminology(
    id="https://openminds.om-i.org/instances/terminology/technique",
    name="technique",
)

Terminology.tissue_sample_attribute = Terminology(
    id="https://openminds.om-i.org/instances/terminology/tissueSampleAttribute",
    name="tissue sample attribute",
)

Terminology.tissue_sample_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/tissueSampleType",
    name="tissue sample type",
)

Terminology.tissue_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/tissueStructure",
    definition="Terminology defining anatomical structures composed of integumentary or connective tissues that form protective coverings, structural support, or separating boundaries within an organism.",
    description="This terminology includes structures formed by integumentary and connective tissues such as membranes, coverings, barriers, and supporting connective components. These structures contribute to protection, mechanical support, compartmentalization, and attachment within the body. Examples may include meninges, connective sheaths, and structural tissue layers. The terminology excludes organs, organ parts, and specialized system-specific structures. It provides a cross-species reference for anatomical structures primarily defined by integumentary or connective tissue composition.",
    name="tissue structure",
)

Terminology.type_of_uncertainty = Terminology(
    id="https://openminds.om-i.org/instances/terminology/typeOfUncertainty",
    name="type of uncertainty",
)

Terminology.unit_of_measurement = Terminology(
    id="https://openminds.om-i.org/instances/terminology/unitOfMeasurement",
    name="unit of measurement",
)

Terminology.vascular_structure = Terminology(
    id="https://openminds.om-i.org/instances/terminology/vascularStructure",
    definition="Terminology defining anatomical structures that form the circulatory vessel networks responsible for transporting blood or lymph within an organism.",
    description="This terminology includes blood vessels such as arteries, veins, and capillaries as well as lymphatic vessels and related conduits of the lymphatic circulation. These structures form interconnected networks that distribute fluids throughout the body. They contribute to physiological processes including nutrient delivery, waste removal, fluid balance, and immune transport. The terminology may include specialized vascular or lymphatic subdivisions associated with particular organs or regions. It provides a cross-species anatomical reference for vessel-based components of the circulatory system.",
    name="vascular structure",
)

Terminology.visual_stimulus_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/visualStimulusType",
    definition="A 'visual stimulus type' groups similar visual stimuli used across visual stimulation techniques.",
    name="visual stimulus type",
)

Terminology.weight_type = Terminology(
    id="https://openminds.om-i.org/instances/terminology/weightType",
    definition="A terminology that specifies the biological or processing state of a specimen at the time its mass was measured.",
    name="weight type",
)
