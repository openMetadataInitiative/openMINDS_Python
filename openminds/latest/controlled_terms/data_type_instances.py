# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.data_type import DataType


DataType.associative_array = DataType(
    id="https://openminds.om-i.org/instances/dataType/associativeArray",
    definition="A 'associative array' is an abstract data type that associates keys (scalars) with values (scalars, lists or matrices).",
    name="associative array",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q80585"),
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
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q12139612"),
)

DataType.matrix = DataType(
    id="https://openminds.om-i.org/instances/dataType/matrix",
    definition="A 'matrix' is a list of lists.",
    name="matrix",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q44337"),
)

DataType.raster_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/rasterGraphic",
    definition="A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.",
    name="raster graphic",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q182270"),
    synonyms=["pixel data", "raster image"],
)

DataType.scalar = DataType(
    id="https://openminds.om-i.org/instances/dataType/scalar",
    definition="A 'scalar' represent a single value (e.g., integer, float, string, etc.).",
    name="scalar",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q1289248"),
)

DataType.table = DataType(
    id="https://openminds.om-i.org/instances/dataType/table",
    definition="A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.",
    name="table",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q496946"),
    synonyms=["tabular data"],
)

DataType.three_d_computer_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/3DComputerGraphic",
    definition="A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.",
    name="3D computer graphic",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q189177"),
)

DataType.time_series = DataType(
    id="https://openminds.om-i.org/instances/dataType/timeSeries",
    definition="A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.",
    name="time series",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q186588"),
    synonyms=["time-series"],
)

DataType.vector_graphic = DataType(
    id="https://openminds.om-i.org/instances/dataType/vectorGraphic",
    definition="A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.",
    name="vector graphic",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q170130"),
    synonyms=["vector image"],
)

DataType.voxel_data = DataType(
    id="https://openminds.om-i.org/instances/dataType/voxelData",
    definition="'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.",
    name="voxel data",
)
