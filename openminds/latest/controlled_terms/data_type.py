"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DataType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/DataType"
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


DataType.associative_array = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/associativeArray",
    definition="A 'associative array' is an abstract data type that associates keys (scalars) with values (scalars, lists or matrices).",
    name="associative array",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q80585",
    synonyms=["dictionary"],
)
DataType.event_sequence = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/eventSequence",
    definition="An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.",
    name="event sequence",
)
DataType.list = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/list",
    definition="A 'list' is a series of ordered scalars and/or lists.",
    name="list",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q12139612",
)
DataType.matrix = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/matrix",
    definition="A 'matrix' is a list of lists.",
    name="matrix",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q44337",
)
DataType.raster_graphic = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/rasterGraphic",
    definition="A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.",
    name="raster graphic",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q182270",
    synonyms=["pixel data", "raster image"],
)
DataType.scalar = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/scalar",
    definition="A 'scalar' represent a single value (e.g., integer, float, string, etc.).",
    name="scalar",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q1289248",
)
DataType.table = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/table",
    definition="A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.",
    name="table",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q496946",
    synonyms=["tabular data"],
)
DataType.three_d_computer_graphic = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/3DComputerGraphic",
    definition="A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.",
    name="3D computer graphic",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q189177",
)
DataType.time_series = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/timeSeries",
    definition="A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.",
    name="time series",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q186588",
    synonyms=["time-series"],
)
DataType.vector_graphic = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/vectorGraphic",
    definition="A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.",
    name="vector graphic",
    preferred_ontology_identifier="https://www.wikidata.org/wiki/Q170130",
    synonyms=["vector image"],
)
DataType.voxel_data = DataType(
    id="https://openminds.ebrains.eu/instances/dataType/voxelData",
    definition="'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.",
    name="voxel data",
)
