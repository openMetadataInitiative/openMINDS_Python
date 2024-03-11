"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SoftwareFeature(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/SoftwareFeature"
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


SoftwareFeature.augmented_reality = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/augmentedReality",
    name="augmented reality",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q254183",
)
SoftwareFeature.commandline_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/commandlineInterface",
    name="commandline interface",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q189053",
)
SoftwareFeature.control = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/control",
    name="control",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q29017603",
)
SoftwareFeature.data_acquisition = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/dataAcquisition",
    name="data acquisition",
)
SoftwareFeature.data_processing = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/dataProcessing",
    name="data processing",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q6661985",
)
SoftwareFeature.desktop_environment = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/desktopEnvironment",
    name="desktop environment",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q56155",
)
SoftwareFeature.graph_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/graphDataTypes",
    name="graph data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q2479726",
)
SoftwareFeature.graphical_user_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/graphicalUserInterface",
    name="graphical user interface",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q782543",
)
SoftwareFeature.heterogeneous_architecture = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/heterogeneousArchitecture",
    name="heterogeneous architecture",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q17111997",
)
SoftwareFeature.interactive_analysis = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/interactiveAnalysis",
    name="interactive analysis",
)
SoftwareFeature.matrix_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/matrixDataTypes",
    name="matrix data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q44337",
)
SoftwareFeature.metadata_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/metadataDataTypes",
    name="metadata data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q180160",
)
SoftwareFeature.mobile_device = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/mobileDevice",
    name="mobile device",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q5082128",
)
SoftwareFeature.modelling = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/modelling",
    name="modelling",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q1116876",
)
SoftwareFeature.parallel_programming = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/parallelProgramming",
    name="parallel programming",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q232661",
)
SoftwareFeature.performance_measurement = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/performanceMeasurement",
    name="performance measurement",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q1771949",
)
SoftwareFeature.positional_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/positionalDataTypes",
    name="positional data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q1477538",
)
SoftwareFeature.presentation_visualisation = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/presentationVisualisation",
    name="presentation visualisation",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q451553",
)
SoftwareFeature.profiling = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/profiling",
    name="profiling",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q1138496",
)
SoftwareFeature.provenance = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/provenance",
    name="provenance",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q30105403",
)
SoftwareFeature.raster_image_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/rasterImageDataTypes",
    name="raster image data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q182270",
)
SoftwareFeature.scripting_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/scriptingInterface",
    name="scripting interface",
)
SoftwareFeature.simulation = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/simulation",
    name="simulation",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q925667",
)
SoftwareFeature.statistical_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/statisticalDataTypes",
    name="statistical data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q7604387",
)
SoftwareFeature.tensor_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/tensorDataTypes",
    name="tensor data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q188524",
)
SoftwareFeature.three_d_geometry_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/3DGeometryDataTypes",
    name="3D geometry data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q189177",
)
SoftwareFeature.three_d_scalar_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/3DScalarDataTypes",
    name="3D scalar data types",
)
SoftwareFeature.three_d_vector_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/3DVectorDataTypes",
    name="3D vector data types",
)
SoftwareFeature.tiled_display_wall = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/tiledDisplayWall",
    name="tiled display wall",
)
SoftwareFeature.time_series_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/timeSeriesDataTypes",
    name="time series data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q186588",
)
SoftwareFeature.vector_image_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/vectorImageDataTypes",
    name="vector image data types",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q170130",
)
SoftwareFeature.virtual_reality = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/virtualReality",
    name="virtual reality",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q170519",
)
