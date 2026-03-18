"""
Structured information on an electrode.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Electrode(LinkedMetadata):
    """
    Structured information on an electrode.
    """

    type_ = "https://openminds.om-i.org/types/Electrode"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "conductor_material",
            [
                "openminds.latest.chemicals.ChemicalMixture",
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.controlled_terms.MolecularEntity",
            ],
            "conductorMaterial",
            description="no description available",
            instructions="Add the conductor material of this electrode.",
        ),
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
            description="Longer statement or account giving the characteristics of the electrode.",
            instructions="Enter a short description of the device. Describe the device itself for a custom-built device or note device-specific peculiarities or deviations from the standard product for a manufacturer-defined device.",
        ),
        Property(
            "insulator_material",
            [
                "openminds.latest.chemicals.ChemicalMixture",
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.controlled_terms.MolecularEntity",
            ],
            "insulatorMaterial",
            description="no description available",
            instructions="Add the insulator material of this electrode.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the electrode within a particular product.",
            instructions="Enter the identifier (or label) of this electrode that is used within the corresponding data files to identify this electrode.",
        ),
        Property(
            "intrinsic_resistance",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "intrinsicResistance",
            description="no description available",
            instructions="Enter the intrinsic resistance of this electrode.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the electrode.",
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
        conductor_material=None,
        contributions=None,
        description=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
        name=None,
        serial_number=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            conductor_material=conductor_material,
            contributions=contributions,
            description=description,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            name=name,
            serial_number=serial_number,
            type=type,
        )
