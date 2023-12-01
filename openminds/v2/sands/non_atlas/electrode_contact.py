"""
Structured information on an electrode contact.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeContact(LinkedMetadata):
    """
    Structured information on an electrode contact.
    """

    type_ = "https://openminds.ebrains.eu/sands/ElectrodeContact"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "coordinate_point",
            "openminds.v2.sands.CoordinatePoint",
            "coordinatePoint",
            required=True,
            description="Pair or triplet of numbers defining the position in a particular two- or three dimensional plane or space.",
            instructions="Add the central coordinate of this electrode contact.",
        ),
        Property(
            "defined_in",
            "openminds.v2.core.File",
            "definedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a file instance in which something is stored.",
            instructions="Add one or several files in which the coordinate point and internal identifier of this electrode contact is defined in.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier used for this electrode contact within the file it is stored in.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this electrode contact that may help you to more easily find it again.",
        ),
        Property(
            "related_recordings",
            ["openminds.v2.core.File", "openminds.v2.core.FileBundle"],
            "relatedRecording",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the written, stored evidence of something.",
            instructions="Add one or several files in which the recordings from this electrode contact were stored.",
        ),
        Property(
            "related_stimulations",
            ["openminds.v2.core.File", "openminds.v2.core.FileBundle"],
            "relatedStimulation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the written, stored function used as a physiological stimulus.",
            instructions="Add one or several files in which the stimulations applied via this electrode contact were stored.",
        ),
        Property(
            "visualized_in",
            "openminds.v2.core.File",
            "visualizedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an image in which something is visible.",
            instructions="Add one or several image files in which the electrode contact is visualized in.",
        ),
    ]

    def __init__(
        self,
        id=None,
        coordinate_point=None,
        defined_in=None,
        internal_identifier=None,
        lookup_label=None,
        related_recordings=None,
        related_stimulations=None,
        visualized_in=None,
    ):
        return super().__init__(
            id=id,
            coordinate_point=coordinate_point,
            defined_in=defined_in,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            related_recordings=related_recordings,
            related_stimulations=related_stimulations,
            visualized_in=visualized_in,
        )
