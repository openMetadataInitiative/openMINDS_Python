"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class EphysStimulus(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/stimulation/EphysStimulus"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "delivered_by",
            [
                "openminds.v3.ephys.ElectrodeArrayUsage",
                "openminds.v3.ephys.ElectrodeUsage",
                "openminds.v3.ephys.PipetteUsage",
                "openminds.v3.specimen_prep.SlicingDeviceUsage",
            ],
            "deliveredBy",
            description="no description available",
            instructions="Add the device used to deliver this stimulus.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the ephys stimulus.",
            instructions="Enter a short text describing this stimulus.",
        ),
        Property(
            "epoch",
            "openminds.v3.core.QuantitativeValue",
            "epoch",
            description="no description available",
            instructions="Enter the total epoch length of this stimulus.",
        ),
        Property(
            "generated_by",
            [
                "openminds.v3.ephys.ElectrodeArrayUsage",
                "openminds.v3.ephys.ElectrodeUsage",
                "openminds.v3.ephys.PipetteUsage",
                "openminds.v3.specimen_prep.SlicingDeviceUsage",
            ],
            "generatedBy",
            description="no description available",
            instructions="Add the device used to generate this stimulus.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies the ephys stimulus within a particular product.",
            instructions="Enter the identifier (or label) of this stimulus that is used within the corresponding data files to identify this stimulus.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this stimulus that may help you to find this instance more easily.",
        ),
        Property(
            "specifications",
            [
                "openminds.v3.core.Configuration",
                "openminds.v3.core.File",
                "openminds.v3.core.FileBundle",
                "openminds.v3.core.PropertyValueList",
            ],
            "specification",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Add the specification information for this stimulus.",
        ),
        Property(
            "type",
            "openminds.v3.controlled_terms.ElectricalStimulusType",
            "type",
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type that describe this electrical stimulus.",
        ),
    ]

    def __init__(
        self,
        id=None,
        delivered_by=None,
        description=None,
        epoch=None,
        generated_by=None,
        internal_identifier=None,
        lookup_label=None,
        specifications=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            delivered_by=delivered_by,
            description=description,
            epoch=epoch,
            generated_by=generated_by,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            specifications=specifications,
            type=type,
        )
