"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Terminology(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Terminology"
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


Terminology.action_status_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/actionStatusType",
    name="action status type",
)
Terminology.age_category = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/ageCategory",
    definition="The age category describes a specific spatiotemporal part of the life cycle of an organism.",
    name="age category",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000105",
)
Terminology.analysis_technique = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/analysisTechnique",
    name="analysis technique",
)
Terminology.anatomical_axes_orientation = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/anatomicalAxesOrientation",
    name="anatomical axes orientation",
)
Terminology.anatomical_identification_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/anatomicalIdentificationType",
    definition="The type of identiciation that was used to determine an anatomical location.",
    name="anatomical identification type",
)
Terminology.anatomical_plane = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/anatomicalPlane",
    definition="A flat anatomical 2D surface that bisects an anatomical structure or an anatomical space.",
    interlex_identifier="http://uri.interlex.org/ilx_0725051",
    name="anatomical plane",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0035085",
    synonyms=["fiat anatomical surface"],
)
Terminology.annotation_criteria_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/annotationCriteriaType",
    definition="General classification of how data were annotated.",
    name="annotation criteria type",
)
Terminology.annotation_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/annotationType",
    definition="Geometrical classification of annotations into types.",
    name="annotation type",
)
Terminology.atlas_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/atlasType",
    name="atlas type",
)
Terminology.auditory_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/auditoryStimulusType",
    definition="An 'auditory stimulus type' groups similar auditory stimuli used across auditory stimulation techniques.",
    name="auditory stimulus type",
)
Terminology.biological_order = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/biologicalOrder",
    name="biological order",
)
Terminology.biological_sex = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/biologicalSex",
    name="biological sex",
)
Terminology.breeding_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/breedingType",
    definition="The breeding type describes how plants or animals have been sexually propagated.",
    name="breeding type",
)
Terminology.cell_culture_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/cellCultureType",
    definition="The type of a cell culture (e.g. primary, secondary)",
    name="cell culture type",
)
Terminology.cell_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/cellType",
    name="cell type",
)
Terminology.chemical_mixture_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/chemicalMixtureType",
    definition="A 'chemical mixture type' groups all mixtures with the same chemical and physical characteristics under a general term.",
    name="chemicalMixtureType",
)
Terminology.colormap = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/colormap",
    definition="A colormap is a lookup table specifying the colors to be used in rendering a palettized image, [adapted from [Wiktionary](https://en.wiktionary.org/wiki/colormap)].",
    name="colormap",
)
Terminology.contribution_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/contributionType",
    name="contribution type",
)
Terminology.cranial_window_construction_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/CranialWindowConstructionType",
    definition="The construction type of a cranial window.",
    name="cranial window construction type",
)
Terminology.cranial_window_reinforcement_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/CranialWindowReinforcementType",
    definition="The reinforcement type of a cranial window.",
    name="cranial window reinforcement type",
)
Terminology.criteria_quality_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/criteriaQualityType",
    name="criteria quality type",
)
Terminology.data_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/dataType",
    name="data type",
)
Terminology.device_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/deviceType",
    name="device type",
)
Terminology.difference_measure = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/differenceMeasure",
    definition="A measure of the difference between two things",
    description="This may be a numerical or physical quantity, a set of categories, etc. Examples include 'mean squared error', 't-statistic', 'p-value'.",
    name="difference measure",
)
Terminology.disease = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/disease",
    name="disease",
)
Terminology.disease_model = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/diseaseModel",
    name="disease model",
)
Terminology.educational_level = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/educationalLevel",
    definition="An 'educational level' defines the developmental stage of a student and how learning environments are structured. ",
    name="educational level",
)
Terminology.electrical_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/electricalStimulusType",
    definition="An 'electrical stimulus type' groups similar electrical stimuli used across electrical stimulation techniques.",
    name="electrical stimulus type",
)
Terminology.ethics_assessment = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/ethicsAssessment",
    name="ethics assessment",
)
Terminology.experimental_approach = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/experimentalApproach",
    name="experimental approach",
)
Terminology.file_bundle_grouping = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/fileBundleGrouping",
    name="file bundle grouping",
)
Terminology.file_repository_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/fileRepositoryType",
    name="file repository type",
)
Terminology.file_usage_role = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/fileUsageRole",
    name="file usage role",
)
Terminology.genetic_strain_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/geneticStrainType",
    definition="The genetic strain type describes the genetic background type of a strain.",
    name="genetic strain type",
)
Terminology.gustatory_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/gustatoryStimulusType",
    definition="A 'gustatory stimulus type' groups similar gustatory stimuli used across gustatory stimulation techniques.",
    name="gustatory stimulus type",
)
Terminology.handedness = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/handedness",
    name="handedness",
)
Terminology.language = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/language",
    name="language",
)
Terminology.laterality = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/laterality",
    name="laterality",
)
Terminology.learning_resource_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/learningResourceType",
    definition="A 'learning resource type' groups persistent resources that explicitly entail learning activities or learning experiences in a certain format (e.g., in a physical or digital presentation).",
    name="learning resource type",
)
Terminology.measured_quantity = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/measuredQuantity",
    definition="A qualified physical quantity that was measured/recorded",
    name="measured quantity",
)
Terminology.meta_data_model_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/metaDataModelType",
    name="(meta)data model type",
)
Terminology.model_abstraction_level = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/modelAbstractionLevel",
    name="model abstraction level",
)
Terminology.model_scope = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/modelScope",
    name="model scope",
)
Terminology.molecular_entity = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/molecularEntity",
    definition="Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107064",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:23367#molecular-entity",
    name="molecular entity",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_23367",
)
Terminology.olfactory_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/olfactoryStimulusType",
    definition="An 'olfactory stimulus type' groups similar olfactory stimuli used across olfactory stimulation techniques.",
    name="olfactory stimulus type",
)
Terminology.operating_device = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/operatingDevice",
    name="operating device",
)
Terminology.operating_system = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/operatingSystem",
    name="operating system",
)
Terminology.optical_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/opticalStimulusType",
    definition="An 'optical stimulus type' groups similar optical stimuli used across optical stimulation techniques.",
    name="optical stimulus type",
)
Terminology.organ = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/organ",
    definition="Anatomical structure that performs a specific function or group of functions.",
    description="The preferred ontology for 'organ' is UBERON.",
    name="organ",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UBERON_0000062",
)
Terminology.organism_substance = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/organismSubstance",
    definition="Any material anatomical entity in a gaseous, liquid, semisolid or solid state produced by or derived from an organism or parts of an organism.",
    description="The preferred ontology for 'organism substance' is UBERON.",
    name="organism substance",
)
Terminology.organism_system = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/organismSystem",
    definition="Any anatomical or functional system in an organism, regardless of scale.",
    name="organism system",
)
Terminology.patch_clamp_variation = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/patchClampVariation",
    definition="A variation of the patch clamp technique",
    name="patch clamp variation",
)
Terminology.preparation_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/preparationType",
    name="preparation type",
)
Terminology.product_accessibility = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/productAccessibility",
    name="product accessibility",
)
Terminology.programming_language = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/programmingLanguage",
    name="programming language",
)
Terminology.qualitative_overlap = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/qualitativeOverlap",
    name="qualitative overlap",
)
Terminology.semantic_data_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/semanticDataType",
    name="semantic data type",
)
Terminology.service = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/service",
    name="service",
)
Terminology.setup_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/setupType",
    definition="The setup type describes the overall purpose of arranging equipment in a certain way (setup).",
    name="setup type",
)
Terminology.software_application_category = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/softwareApplicationCategory",
    name="software application category",
)
Terminology.software_feature = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/softwareFeature",
    name="software feature",
)
Terminology.species = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/species",
    name="species",
)
Terminology.stimulation_approach = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/stimulationApproach",
    name="stimulation approach",
)
Terminology.stimulation_technique = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/stimulationTechnique",
    name="stimulation technique",
)
Terminology.subcellular_entity = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/subcellularEntity",
    definition="Entity derived from a cell or cells. The anatomical scale of these objects roughly corresponds to that which would be visible in high resolution light microscopy or conventional electron microscopy, e.g., nanometers to microns",
    interlex_identifier="http://uri.interlex.org/base/ilx_0111157",
    knowledge_space_link="https://knowledge-space.org/wiki/GO:0005575#iJ6UjX8BxpaxvvQA_2ri",
    name="subcellular entity",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/GO_0005575",
    synonyms=["cellular component"],
)
Terminology.subject_attribute = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/subjectAttribute",
    name="subject attribute",
)
Terminology.tactile_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/tactileStimulusType",
    definition="A 'tactile stimulus type' groups similar tactile stimuli used across tactile stimulation techniques.",
    name="tactile stimulus type",
)
Terminology.technique = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/technique",
    name="technique",
)
Terminology.tissue_sample_attribute = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/tissueSampleAttribute",
    name="tissue sample attribute",
)
Terminology.tissue_sample_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/tissueSampleType",
    name="tissue sample type",
)
Terminology.type_of_uncertainty = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/typeOfUncertainty",
    name="type of uncertainty",
)
Terminology.uberon_parcellation = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/UBERONParcellation",
    name="UBERON parcellation",
)
Terminology.unit_of_measurement = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/unitOfMeasurement",
    name="unit of measurement",
)
Terminology.visual_stimulus_type = Terminology(
    id="https://openminds.ebrains.eu/instances/terminology/visualStimulusType",
    definition="A 'visual stimulus type' groups similar visual stimuli used across visual stimulation techniques.",
    name="visual stimulus type",
)
