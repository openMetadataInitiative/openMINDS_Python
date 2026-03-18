"""
Structured information about a measurement performed during a scientific experiment.
"""

# this file was auto-generated!

from datetime import datetime

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Measurement(EmbeddedMetadata):
    """
    Structured information about a measurement performed during a scientific experiment.
    """

    type_ = "https://openminds.om-i.org/types/Measurement"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this measurement.",
        ),
        Property(
            "measured_quantity",
            "openminds.v5.controlled_terms.MeasuredQuantity",
            "measuredQuantity",
            required=True,
            description="no description available",
            instructions="Add the quantity that was measured during this measurement.",
        ),
        Property(
            "obtained_with",
            [
                "openminds.v5.ephys.ElectrodeArrayUsage",
                "openminds.v5.ephys.ElectrodeUsage",
                "openminds.v5.ephys.PipetteUsage",
                "openminds.v5.neuroimaging.MRICoilUsage",
                "openminds.v5.neuroimaging.MRIScannerUsage",
                "openminds.v5.specimen_prep.SlicingDeviceUsage",
            ],
            "obtainedWith",
            description="no description available",
            instructions="Add the used device for obtaining this measurement.",
        ),
        Property(
            "timestamp",
            datetime,
            "timestamp",
            description="no description available",
            instructions="Enter the date and time on which this measurement was made, formatted as '2023-02-07T16:00:00+00:00'.",
        ),
        Property(
            "values",
            ["openminds.v5.core.QuantitativeValue", "openminds.v5.core.QuantitativeValueRange"],
            "value",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Entry for a property.",
            instructions="Enter all values that were measured at the same time and are of the same measured quantity.",
        ),
    ]

    def __init__(
        self, additional_remarks=None, measured_quantity=None, obtained_with=None, timestamp=None, values=None
    ):
        return super().__init__(
            additional_remarks=additional_remarks,
            measured_quantity=measured_quantity,
            obtained_with=obtained_with,
            timestamp=timestamp,
            values=values,
        )
