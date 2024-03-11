"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ExperimentalApproach(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/ExperimentalApproach"
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


ExperimentalApproach.anatomy = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/anatomy",
    definition="Any experimental approach focused on the bodily structure of living organisms.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739411",
    name="anatomy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Anatomy",
    synonyms=["anatomical approach"],
)
ExperimentalApproach.behavior = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/behavior",
    definition="Any experimental approach focused on the mechanical activity or cognitive processes underlying mechanical activity of living organisms often in response to external sensory stimuli.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739413",
    name="behavior",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Behavior",
    synonyms=["behavioral approach"],
)
ExperimentalApproach.biophysics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/biophysics",
    definition="'Biophysics' covers any experimental approach that is traditionally used in physics, but applied and modified to study biological phenomena. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Biophysics)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0793772",
    name="biophysics",
)
ExperimentalApproach.cell_biology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/cellBiology",
    definition="Any experimental approach focused on structure, function, multiplication, pathology, and life history of biological cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739391",
    name="cell biology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Cellular",
    synonyms=["cellular approach"],
)
ExperimentalApproach.cell_morphology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/cellMorphology",
    definition="Any experimental approach focused on the shape and structure of individual cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739394",
    name="cell morphology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/CellMorphology",
)
ExperimentalApproach.cell_population_characterization = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/cellPopulationCharacterization",
    definition="Any experimental approach focused on biochemical, molecular and/or physiological characteristics of populations of cells as opposed to individual cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739408",
    name="cell population characterization",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationCharachterization",
)
ExperimentalApproach.cell_population_imaging = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/cellPopulationImaging",
    definition="Any experimental approach focused on imaging biochemical, molecular, or physiological characteristics of populations of cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739402",
    name="cell population imaging",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationImaging",
)
ExperimentalApproach.cell_population_manipulation = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/cellPopulationManipulation",
    definition="Any experimental approach focused on manipulation of biochemical, molecular, or physiological characteristics of populations of cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739398",
    name="cell population manipulation",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationManipulation",
)
ExperimentalApproach.chemogenetics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/chemogenetics",
    definition="Any experimental approach focused on using genetically encoded chemically sensitive proteins in combination with a specific agonist delivered systemically in order to manipulate the behavior of populations of cells.",
    name="chemogenetics",
)
ExperimentalApproach.clinical_research = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/clinicalResearch",
    definition="Any experimental approach focused on medical observation, treatment, or testing of patients.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739401",
    name="clinical research",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Clinical",
    synonyms=["clinical approach"],
)
ExperimentalApproach.computational_modeling = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/computationalModeling",
    definition="Any experimental approach focused on creating or characterizing computational models or simulations of experimentally observed phenomena.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739414",
    name="computational modeling",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/ComputationalModelling",
)
ExperimentalApproach.developmental_biology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/developmentalBiology",
    definition="Any experimental approach focused on life cycle, development, or developmental history of an organism.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739412",
    name="developmental biology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Developmental",
    synonyms=["developmental approach"],
)
ExperimentalApproach.ecology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/ecology",
    definition="Any experimental approach focused on interrelationship of organisms and their environments, including causes and consequences.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739389",
    name="ecology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Ecology",
    synonyms=["ecological approach"],
)
ExperimentalApproach.electrophysiology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/electrophysiology",
    definition="Any experimental approach focused on electrical phenomena associated with living systems, most notably the nervous system, cardiac system, and musculoskeletal system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741202",
    name="electrophysiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Electrophysiology",
)
ExperimentalApproach.epidemiology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/epidemiology",
    definition="Any experimental approach focused on incidence, distribution, and possible control of diseases and other factors relating to health.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739400",
    name="epidemiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Epidemiology",
    synonyms=["epidemiological approach"],
)
ExperimentalApproach.epigenomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/epigenomics",
    definition="Any experimental approach focused on processes that modulate transcription but that do not directly alter the primary sequences of an organism's DNA.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741207",
    name="epigenomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Epigenomics",
)
ExperimentalApproach.ethology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/ethology",
    definition="Any experimental approach focused on natural unmanipulated human or animal behavior and social organization from a biological, life history, and often evolutionary perspective.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739388",
    name="ethology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Ethology",
    synonyms=["ethological approach"],
)
ExperimentalApproach.evolutionary_biology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/evolutionaryBiology",
    definition="Any experimental approach focused on heritable characteristics of biological populations and their variation through the modification of developmental process to produce new forms and species.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739392",
    name="evolutionary biology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Evolution",
    synonyms=["evolutionary approach"],
)
ExperimentalApproach.expression = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/expression",
    definition="Any experimental approach focused on driving or detecting expression of genes in cells or tissues.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739397",
    name="expression",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Expression",
    synonyms=["molecular expression approach"],
)
ExperimentalApproach.expression_characterization = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/expressionCharacterization",
    definition="Any experimental approach focused on the cellular, anatomical, or morphological distribution of gene expression.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739409",
    name="expression characterization",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/ExpressionCharachterization",
)
ExperimentalApproach.genetics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/genetics",
    definition="Experimental approach that measures or manipulates some aspect of the genetic material of an organism.",
    name="genetics",
)
ExperimentalApproach.genomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/genomics",
    definition="Any experimental approach focused on structure, function, evolution, and mapping of genomes, the entiretiy of the genetic material of a single organism.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741204",
    name="genomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Genomics",
)
ExperimentalApproach.histology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/histology",
    definition="Any experimental approach focused on structure of biological tissue.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739399",
    name="histology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Histology",
    synonyms=["histological approach"],
)
ExperimentalApproach.informatics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/informatics",
    definition="Any experimental approach focused on collection, classification, storage, retrieval, analysis, visualization, and dissemination of recorded knowledge in computational systems.",
    name="informatics",
)
ExperimentalApproach.metabolomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/metabolomics",
    definition="Any experimental approach focused on chemical processes involving metabolites, the small molecule substrates, intermediates and products of cell metabolism.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741203",
    name="metabolomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Metabolomics",
)
ExperimentalApproach.microscopy = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/microscopy",
    definition="Any experimental approach focused on using differential contrast of microscopic structures to form an image.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739404",
    name="microscopy",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Microscopy",
)
ExperimentalApproach.morphology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/morphology",
    definition="Any experimental approach focused on the shape and structure of living organisms or their parts.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739403",
    name="morphology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Morphology",
    synonyms=["morphological approach"],
)
ExperimentalApproach.multimodal_research = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/multimodalResearch",
    definition="Any experimental approach that employs multiple experimental approaches in significant ways.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739395",
    name="multimodal research",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Multimodal",
    synonyms=["multimodal approach"],
)
ExperimentalApproach.multiomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/multiomics",
    definition="Any experimental approach that employs multiple omics approaches in significant ways.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739407",
    name="multiomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Multiomics",
)
ExperimentalApproach.neural_connectivity = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/neuralConnectivity",
    definition="Any experimental approach focused on functional or anatomical connections between single neurons or populations of neurons in defined anatomical regions.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739393",
    name="neural connectivity",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Connectivity",
)
ExperimentalApproach.neuroimaging = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/neuroimaging",
    definition="Any experimental approach focused on the non-invasive direct or indirect imaging of the structure, function, or pharmacology of the nervous system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741206",
    name="neuroimaging",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Neuroimaging",
)
ExperimentalApproach.omics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/omics",
    definition="Any experimental approach focused on characterization and quantification of biological molecules that give rise to the structure, function, and dynamics of organisms or their parts.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739405",
    name="omics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Omics",
)
ExperimentalApproach.optogenetics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/optogenetics",
    definition="Any experimental approach focused on using genetically encoded light-sensitive proteins in combination with targeted delivery of light in order to manipulate the behavior of populations of cells.",
    name="optogenetics",
)
ExperimentalApproach.pharmacology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/pharmacology",
    definition="'Pharmacology' is an experimental approach in which the composition, properties, functions, sources, synthesis and design of drugs (any artificial, natural, or endogenous molecule) and their biochemical or physiological effect (normal or abnormal) on a cell, tissue, organ, or organism are studied. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Pharmacology)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0108784",
    name="pharmacology",
    preferred_ontology_identifier="http://edamontology.org/topic_0202",
)
ExperimentalApproach.physiology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/physiology",
    definition="Any experimental approach focused on normal functions of living organisms and their parts.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739410",
    name="physiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Physiology",
    synonyms=["physiological approach"],
)
ExperimentalApproach.proteomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/proteomics",
    definition="Any experimental approach focused on the composition, structure, and activity of an entire set of proteins in organisms or their parts.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0741205",
    name="proteomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Proteomics",
)
ExperimentalApproach.radiology = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/radiology",
    definition="Any experimental approach focused on using non-invasive techniques that use intrinsic or induced contrast to form images. Also covers purely clinical domains such as nuclear medicine.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739390",
    name="radiology",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Radiology",
)
ExperimentalApproach.spatial_transcriptomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/spatialTranscriptomics",
    definition="Any experimental approach focused on mapping the spatial location of gene activity in biological tissue.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739396",
    name="spatial transcriptomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/SpatialTranscriptomics",
)
ExperimentalApproach.transcriptomics = ExperimentalApproach(
    id="https://openminds.ebrains.eu/instances/experimentalApproach/transcriptomics",
    definition="Any experimental approach focused on the transcriptome (all RNA transcripts) of one or more cells, tissues, or organisms.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0739406",
    name="transcriptomics",
    preferred_ontology_identifier="http://uri.interlex.org/tgbugs/uris/readable/modality/Transcriptomics",
)
