"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class CustomAnnotation(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CustomAnnotation"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "best_view_point",
            "openminds.v2.sands.CoordinatePoint",
            "bestViewPoint",
            description="Coordinate point from which you get the best view of something.",
            instructions="Add the coordinate point identifying the best view of this custom annotation in space.",
        ),
        Property(
            "coordinate_space",
            ["openminds.v2.sands.CommonCoordinateSpace", "openminds.v2.sands.CustomCoordinateSpace"],
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this custom annotation exists.",
        ),
        Property(
            "criteria",
            "openminds.v2.core.ProtocolExecution",
            "criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to produce this custom annotation.",
        ),
        Property(
            "criteria_quality_type",
            "openminds.v2.controlled_terms.CriteriaQualityType",
            "criteriaQualityType",
            required=True,
            description="Distinct class that defines how the judgement or decision was made for a particular criteria.",
            instructions="Add the quality type of the stated criteria used to define this custom annotation.",
        ),
        Property(
            "display_color",
            str,
            "displayColor",
            formatting="text/plain",
            description="Preferred coloring.",
            instructions="Enter the preferred display color (HEX) for this custom annotation.",
        ),
        Property(
            "inspired_by",
            "openminds.v2.core.File",
            "inspiredBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an inspiring element.",
            instructions="Add one or several (source) files that inspired the definition of this custom annotation.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier used for this custom annotation within the file it is stored in.",
        ),
        Property(
            "lateralities",
            "openminds.v2.controlled_terms.Laterality",
            "laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both sides of the body, bilateral organ or bilateral organ part that this custom annotation is defined in.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this custom annotation that may help you to more easily find it again.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this custom annotation.",
        ),
        Property(
            "visualized_in",
            "openminds.v2.core.File",
            "visualizedIn",
            required=True,
            description="Reference to an image in which something is visible.",
            instructions="Add the (source) image file in which this custom annotation is visualized in.",
        ),
    ]

    def __init__(
        self,
        id=None,
        best_view_point=None,
        coordinate_space=None,
        criteria=None,
        criteria_quality_type=None,
        display_color=None,
        inspired_by=None,
        internal_identifier=None,
        lateralities=None,
        lookup_label=None,
        name=None,
        visualized_in=None,
    ):
        return super().__init__(
            id=id,
            best_view_point=best_view_point,
            coordinate_space=coordinate_space,
            criteria=criteria,
            criteria_quality_type=criteria_quality_type,
            display_color=display_color,
            inspired_by=inspired_by,
            internal_identifier=internal_identifier,
            lateralities=lateralities,
            lookup_label=lookup_label,
            name=name,
            visualized_in=visualized_in,
        )
