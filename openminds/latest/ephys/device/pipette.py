"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Pipette(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Pipette"
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
            description="Longer statement or account giving the characteristics of the pipette.",
            instructions="Enter a short description of the device. Describe the device itself for a custom-built device or note device-specific peculiarities or deviations from the standard product for a manufacturer-defined device.",
        ),
        Property(
            "external_diameter",
            "openminds.latest.core.QuantitativeValue",
            "externalDiameter",
            description="no description available",
            instructions="Enter the external diameter of the pipette.",
        ),
        Property(
            "internal_diameter",
            "openminds.latest.core.QuantitativeValue",
            "internalDiameter",
            description="no description available",
            instructions="Enter the internal diameter of the pipette.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the pipette within a particular product.",
            instructions="Enter the identifier (or label) of this pipette that is used within the corresponding data files to identify this pipette.",
        ),
        Property(
            "material",
            [
                "openminds.latest.chemicals.ChemicalMixture",
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.controlled_terms.MolecularEntity",
            ],
            "material",
            description="no description available",
            instructions="Add the material that the pipette is made of.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the pipette.",
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
        external_diameter=None,
        internal_diameter=None,
        internal_identifier=None,
        material=None,
        name=None,
        serial_number=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            contributions=contributions,
            description=description,
            external_diameter=external_diameter,
            internal_diameter=internal_diameter,
            internal_identifier=internal_identifier,
            material=material,
            name=name,
            serial_number=serial_number,
            type=type,
        )
