"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SlicingDevice(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SlicingDevice"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "contributions",
            ["openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "contribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all relevant contributions (e.g., ownership, maintenance) for this device.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the slicing device.",
            instructions="Enter a short description of the device. Describe the device itself for a custom-built device or note device-specific peculiarities or deviations from the standard product for a manufacturer-defined device.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the slicing device within a particular product.",
            instructions="Enter the identifier (or label) of this device that is used by the owner to identify or reference this device.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the slicing device.",
            instructions="Enter a descriptive name for this device, preferably defined by the owner.",
        ),
        Property(
            "serial_number",
            str,
            "serialNumber",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the serial number of this device.",
        ),
        Property(
            "type",
            ["openminds.latest.controlled_terms.DeviceType", "openminds.latest.core.HardwareProduct"],
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the device classification reference. Identify a device type for a custom-built device, or a hardware product for a device corresponding to a manufacturer-defined product model.",
        ),
    ]

    def __init__(
        self,
        id=None,
        contributions=None,
        description=None,
        internal_identifier=None,
        name=None,
        serial_number=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            contributions=contributions,
            description=description,
            internal_identifier=internal_identifier,
            name=name,
            serial_number=serial_number,
            type=type,
        )
