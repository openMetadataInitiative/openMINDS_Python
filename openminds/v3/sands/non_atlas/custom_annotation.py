"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class CustomAnnotation(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CustomAnnotation"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "anchor_points",
            "openminds.v3.core.QuantitativeValue",
            "anchorPoint",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=3,
            description="no description available",
            instructions="Enter the coordinates of the anchor point for this annotation (e.g., its centroid in two dimensional space as [x, y] or in three dimensional space as [x, y, z]).",
        ),
        Property(
            "coordinate_space",
            ["openminds.v3.sands.CommonCoordinateSpaceVersion", "openminds.v3.sands.CustomCoordinateSpace"],
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space for this custom annotation.",
        ),
        Property(
            "criteria",
            "openminds.v3.core.ProtocolExecution",
            "criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to produce this annotation.",
        ),
        Property(
            "criteria_quality_type",
            "openminds.v3.controlled_terms.CriteriaQualityType",
            "criteriaQualityType",
            required=True,
            description="Distinct class that defines how the judgement or decision was made for a particular criteria.",
            instructions="Add the quality type of the stated criteria used to define this annotation.",
        ),
        Property(
            "criteria_type",
            "openminds.v3.controlled_terms.AnnotationCriteriaType",
            "criteriaType",
            required=True,
            description="no description available",
            instructions="Add the criteria type for this annotation.",
        ),
        Property(
            "inspired_by",
            "openminds.v3.core.File",
            "inspiredBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an inspiring element.",
            instructions="Add all (source) files that inspired the definition of this annotation.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this annotation that is used within the corresponding data files to identify this annotation.",
        ),
        Property(
            "lateralities",
            "openminds.v3.controlled_terms.Laterality",
            "laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both sides of the body, bilateral organ or bilateral organ part that this annotation is defined in.",
        ),
        Property(
            "preferred_visualization",
            "openminds.v3.sands.ViewerSpecification",
            "preferredVisualization",
            description="no description available",
            instructions="Add the preferred viewer specification to visualize this annotation.",
        ),
        Property(
            "specification",
            ["openminds.v3.core.File", "openminds.v3.core.PropertyValueList"],
            "specification",
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Add the non-parametric or parametric specification of this annotation.",
        ),
        Property(
            "type",
            "openminds.v3.controlled_terms.AnnotationType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the geometry type of this annotation.",
        ),
    ]

    def __init__(
        self,
        anchor_points=None,
        coordinate_space=None,
        criteria=None,
        criteria_quality_type=None,
        criteria_type=None,
        inspired_by=None,
        internal_identifier=None,
        lateralities=None,
        preferred_visualization=None,
        specification=None,
        type=None,
    ):
        return super().__init__(
            anchor_points=anchor_points,
            coordinate_space=coordinate_space,
            criteria=criteria,
            criteria_quality_type=criteria_quality_type,
            criteria_type=criteria_type,
            inspired_by=inspired_by,
            internal_identifier=internal_identifier,
            lateralities=lateralities,
            preferred_visualization=preferred_visualization,
            specification=specification,
            type=type,
        )
