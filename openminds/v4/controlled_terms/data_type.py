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

    type_ = "https://openminds.om-i.org/types/DataType"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
            description="Longer statement or account giving the characteristics of the data type.",
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
            description="Word or phrase that constitutes the distinctive designation of the data type.",
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


DataType.associative_array = DataType(
    id="https://openminds.om-i.org/instances/dataType/associativeArray",
    definition="A 'associative array' is an abstract data type that associates keys (scalars) with values (scalars, lists or matrices).",
    name="associative array",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q80585"),
    synonyms=["dictionary"],
)
DataType.event_sequence = DataType(
    id="https://openminds.om-i.org/instances/dataType/eventSequence",
    definition="An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.",
    name="event sequence",
)
DataType.list = DataType(
    id="https://openminds.om-i.org/instances/dataType/list",
    definition="A 'list' is a series of ordered scalars and/or lists.",
    name="list",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q12139612"),
)
DataType.matrix = DataType(
    id="https://openminds.om-i.org/instances/dataType/matrix",
    definition="A 'matrix' is a list of lists.",
    name="matrix",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q44337"),
)
DataType.raster_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/rasterGraphic",
    definition="A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.",
    name="raster graphic",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q182270"),
    synonyms=["pixel data", "raster image"],
)
DataType.scalar = DataType(
    id="https://openminds.om-i.org/instances/dataType/scalar",
    definition="A 'scalar' represent a single value (e.g., integer, float, string, etc.).",
    name="scalar",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1289248"),
)
DataType.table = DataType(
    id="https://openminds.om-i.org/instances/dataType/table",
    definition="A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.",
    name="table",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q496946"),
    synonyms=["tabular data"],
)
DataType.three_d_computer_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/3DComputerGraphic",
    definition="A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.",
    name="3D computer graphic",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q189177"),
)
DataType.time_series = DataType(
    id="https://openminds.om-i.org/instances/dataType/timeSeries",
    definition="A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.",
    name="time series",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q186588"),
    synonyms=["time-series"],
)
DataType.vector_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/vectorGraphic",
    definition="A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.",
    name="vector graphic",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q170130"),
    synonyms=["vector image"],
)
DataType.voxel_data = DataType(
    id="https://openminds.om-i.org/instances/dataType/voxelData",
    definition="'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.",
    name="voxel data",
)
