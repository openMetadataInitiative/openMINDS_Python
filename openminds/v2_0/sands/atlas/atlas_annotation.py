"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class AtlasAnnotation(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/sands/AtlasAnnotation"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "best_view_point",
            "openminds.v2_0.sands.CoordinatePoint",
            "vocab:bestViewPoint",
            description="Coordinate point from which you get the best view of something.",
            instructions="Add the coordinate point identifying the best view of this atlas annotation in space.",
        ),
        Property(
            "criteria",
            "openminds.v2_0.core.ProtocolExecution",
            "vocab:criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to produce this atlas annotation.",
        ),
        Property(
            "criteria_quality_type",
            "openminds.v2_0.controlled_terms.CriteriaQualityType",
            "vocab:criteriaQualityType",
            required=True,
            description="Distinct class that defines how the judgement or decision was made for a particular criteria.",
            instructions="Add the quality type of the stated criteria used to define this atlas annotation.",
        ),
        Property(
            "display_color",
            str,
            "vocab:displayColor",
            formatting="text/plain",
            description="Preferred coloring.",
            instructions="Enter the preferred display color (HEX) for this atlas annotation.",
        ),
        Property(
            "inspired_by",
            "openminds.v2_0.core.File",
            "vocab:inspiredBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an inspiring element.",
            instructions="Add one or several (source) files that inspired the definition of this atlas annotation.",
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
            "openminds.v2_0.controlled_terms.Laterality",
            "vocab:laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both sides of the body, bilateral organ or bilateral organ part that this atlas annotation is defined in.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this atlas annotation that may help you to more easily find it again.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this atlas annotation.",
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this atlas annotation.",
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description of the novelties/peculiarities of this atlas annotation.",
        ),
        Property(
            "visualized_in",
            "openminds.v2_0.core.File",
            "vocab:visualizedIn",
            description="Reference to an image in which something is visible.",
            instructions="Add the (source) image file in which this atlas annotation is visualized in.",
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
        lookup_label=None,
        name=None,
        version_identifier=None,
        version_innovation=None,
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
            lookup_label=lookup_label,
            name=name,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
            visualized_in=visualized_in,
        )