"""
Structured information on an image annotation.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Annotation(LinkedMetadata):
    """
    Structured information on an image annotation.
    """

    type_ = ["https://openminds.ebrains.eu/sands/Annotation"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "best_view_point",
            "openminds.v1_0.sands.CoordinatePoint",
            "vocab:bestViewPoint",
            description="Coordinate point from which you get the best view of something.",
            instructions="Add the coordinate point identifying the best view of this annotation in space.",
        ),
        Property(
            "criteria",
            "openminds.v1_0.core.ProtocolExecution",
            "vocab:criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to produce this annotation.",
        ),
        Property(
            "criteria_quality_type",
            "openminds.v1_0.controlled_terms.CriteriaQualityType",
            "vocab:criteriaQualityType",
            required=True,
            description="Distinct class that defines how the judgement or decision was made for a particular criteria.",
            instructions="Add the quality type of the stated criteria used to define this annotation.",
        ),
        Property(
            "display_color",
            int,
            "vocab:displayColor",
            multiple=True,
            unique_items=False,
            min_items=3,
            max_items=3,
            description="Preferred coloring.",
            instructions="Enter the preferred display color (RGB) for this annotation.",
        ),
        Property(
            "inspired_by",
            "openminds.v1_0.sands.Image",
            "vocab:inspiredBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an inspiring element.",
            instructions="Add one or several (source) images that inspired the definition of this annotation.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier used for this annotation within the file it is stored in.",
        ),
        Property(
            "laterality",
            "openminds.v1_0.controlled_terms.Laterality",
            "vocab:laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            required=True,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both sides of the body or bilateral organ that this annotation is defined in.",
        ),
        Property(
            "naming_term",
            "openminds.v1_0.sands.AnatomicalEntity",
            "vocab:namingTerm",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Word or expression that has a precise meaning within a science, art, profession, or subject.",
            instructions="Add one or several anatomical entities that name this annotation.",
        ),
        Property(
            "related_atlas_term",
            "openminds.v1_0.sands.AnatomicalEntity",
            "vocab:relatedAtlasTerm",
            multiple=True,
            unique_items=False,
            min_items=1,
            description="Reference to a related naming term of an anatomical structure that is defined in a particular brain atlas.",
            instructions="Add one or several anatomical entities of registered brain atlas annotations to which this annotation is related to.",
        ),
        Property(
            "visualized_in",
            "openminds.v1_0.sands.Image",
            "vocab:visualizedIn",
            description="Reference to an image in which something is visible.",
            instructions="Add the image in which this annotation is visualized in.",
        ),
    ]

    def __init__(
        self,
        id=None,
        best_view_point=None,
        criteria=None,
        criteria_quality_type=None,
        display_color=None,
        inspired_by=None,
        internal_identifier=None,
        laterality=None,
        naming_term=None,
        related_atlas_term=None,
        visualized_in=None,
    ):
        return super().__init__(
            id=id,
            best_view_point=best_view_point,
            criteria=criteria,
            criteria_quality_type=criteria_quality_type,
            display_color=display_color,
            inspired_by=inspired_by,
            internal_identifier=internal_identifier,
            laterality=laterality,
            naming_term=naming_term,
            related_atlas_term=related_atlas_term,
            visualized_in=visualized_in,
        )