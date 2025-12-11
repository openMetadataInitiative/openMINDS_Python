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
            description="Longer statement or account giving the characteristics of the software feature.",
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
            description="Word or phrase that constitutes the distinctive designation of the software feature.",
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


SoftwareFeature.application_programming_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/applicationProgrammingInterface",
    definition="A set of rules and protocols that allows different software applications to communicate with each other, enabling them to access specific functions or data.",
    name="application programming interface",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q165194"),
    synonyms=["API"],
)
SoftwareFeature.augmented_reality = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/augmentedReality",
    name="augmented reality",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q254183"),
)
SoftwareFeature.command_line_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/commandLineInterface",
    definition="A text-based system that enables users to interact with a computer or software by entering commands, allowing them to perform specific tasks or operations.",
    name="command line interface",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q189053"),
    synonyms=["CLI"],
)
SoftwareFeature.control = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/control",
    name="control",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q29017603"),
)
SoftwareFeature.data_acquisition = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/dataAcquisition",
    name="data acquisition",
)
SoftwareFeature.data_processing = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/dataProcessing",
    name="data processing",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q6661985"),
)
SoftwareFeature.desktop_environment = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/desktopEnvironment",
    name="desktop environment",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q56155"),
)
SoftwareFeature.graph_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/graphDataTypes",
    name="graph data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q2479726"),
)
SoftwareFeature.graphical_user_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/graphicalUserInterface",
    definition="A visual system that enables users to interact with a computer or software through graphical elements like windows, icons, and menus, allowing them to perform specific tasks or operations.",
    name="graphical user interface",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q782543"),
    synonyms=["GUI"],
)
SoftwareFeature.heterogeneous_architecture = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/heterogeneousArchitecture",
    name="heterogeneous architecture",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q17111997"),
)
SoftwareFeature.interactive_analysis = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/interactiveAnalysis",
    name="interactive analysis",
)
SoftwareFeature.matrix_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/matrixDataTypes",
    name="matrix data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q44337"),
)
SoftwareFeature.metadata_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/metadataDataTypes",
    name="metadata data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q180160"),
)
SoftwareFeature.mobile_device = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/mobileDevice",
    name="mobile device",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q5082128"),
)
SoftwareFeature.modelling = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/modelling",
    name="modelling",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1116876"),
)
SoftwareFeature.parallel_programming = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/parallelProgramming",
    name="parallel programming",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q232661"),
)
SoftwareFeature.performance_measurement = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/performanceMeasurement",
    name="performance measurement",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1771949"),
)
SoftwareFeature.positional_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/positionalDataTypes",
    name="positional data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1477538"),
)
SoftwareFeature.presentation_visualisation = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/presentationVisualisation",
    name="presentation visualisation",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q451553"),
)
SoftwareFeature.profiling = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/profiling",
    name="profiling",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1138496"),
)
SoftwareFeature.provenance = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/provenance",
    name="provenance",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q30105403"),
)
SoftwareFeature.raster_image_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/rasterImageDataTypes",
    name="raster image data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q182270"),
)
SoftwareFeature.scripting_interface = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/scriptingInterface",
    name="scripting interface",
)
SoftwareFeature.simulation = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/simulation",
    name="simulation",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q925667"),
)
SoftwareFeature.statistical_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/statisticalDataTypes",
    name="statistical data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q7604387"),
)
SoftwareFeature.tensor_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/tensorDataTypes",
    name="tensor data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q188524"),
)
SoftwareFeature.three_d_geometry_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/3DGeometryDataTypes",
    name="3D geometry data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q189177"),
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
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q186588"),
)
SoftwareFeature.vector_image_data_types = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/vectorImageDataTypes",
    name="vector image data types",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q170130"),
)
SoftwareFeature.virtual_reality = SoftwareFeature(
    id="https://openminds.ebrains.eu/instances/softwareFeature/virtualReality",
    name="virtual reality",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q170519"),
)
