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
    schema_version = "v4.0"

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
            "openminds.v4.controlled_terms.MeasuredQuantity",
            "measuredQuantity",
            required=True,
            description="no description available",
            instructions="Add the quantity that was measured during this measurement.",
        ),
        Property(
            "measured_with",
            [
                "openminds.v4.ephys.ElectrodeArrayUsage",
                "openminds.v4.ephys.ElectrodeUsage",
                "openminds.v4.ephys.PipetteUsage",
                "openminds.v4.specimen_prep.SlicingDeviceUsage",
            ],
            "measuredWith",
            description="no description available",
            instructions="Add the device that was used during this measurement.",
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
            ["openminds.v4.core.QuantitativeValue", "openminds.v4.core.QuantitativeValueRange"],
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
        self, additional_remarks=None, measured_quantity=None, measured_with=None, timestamp=None, values=None
    ):
        return super().__init__(
            additional_remarks=additional_remarks,
            measured_quantity=measured_quantity,
            measured_with=measured_with,
            timestamp=timestamp,
            values=values,
        )
