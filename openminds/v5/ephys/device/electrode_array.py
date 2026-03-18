"""
Structured information on an electrode array.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeArray(LinkedMetadata):
    """
    Structured information on an electrode array.
    """

    type_ = "https://openminds.om-i.org/types/ElectrodeArray"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "conductor_material",
            [
                "openminds.v5.chemicals.ChemicalMixture",
                "openminds.v5.chemicals.ChemicalSubstance",
                "openminds.v5.controlled_terms.MolecularEntity",
            ],
            "conductorMaterial",
            description="no description available",
            instructions="Add the conductor material of this electrode array.",
        ),
        Property(
            "contributions",
            ["openminds.v5.core.Organization", "openminds.v5.core.Person"],
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
            description="Longer statement or account giving the characteristics of the electrode array.",
            instructions="Enter a short description of the device. Describe the device itself for a custom-built device or note device-specific peculiarities or deviations from the standard product for a manufacturer-defined device.",
        ),
        Property(
            "electrode_identifiers",
            str,
            "electrodeIdentifier",
            multiple=True,
            unique_items=True,
            min_items=2,
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the identifiers for each electrode of this electrode array. Note that the number of identifiers should match the number of electrodes of the array as stated under 'numberOfElectrodes'.",
        ),
        Property(
            "insulator_material",
            [
                "openminds.v5.chemicals.ChemicalMixture",
                "openminds.v5.chemicals.ChemicalSubstance",
                "openminds.v5.controlled_terms.MolecularEntity",
            ],
            "insulatorMaterial",
            description="no description available",
            instructions="Add the insulator material of this electrode array.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the electrode array within a particular product.",
            instructions="Enter the identifier (or label) of this electrode array that is used within the corresponding data files to identify this electrode array.",
        ),
        Property(
            "intrinsic_resistance",
            ["openminds.v5.core.QuantitativeValue", "openminds.v5.core.QuantitativeValueRange"],
            "intrinsicResistance",
            description="no description available",
            instructions="Enter the intrinsic resistance of this electrode array.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the electrode array.",
            instructions="Enter a descriptive name for this device, preferably defined by the owner.",
        ),
        Property(
            "number_of_electrodes",
            int,
            "numberOfElectrodes",
            required=True,
            description="no description available",
            instructions="Enter the number of electrodes that belong to this electrode array.",
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
            ["openminds.v5.controlled_terms.DeviceType", "openminds.v5.core.HardwareProduct"],
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
        electrode_identifiers=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
        name=None,
        number_of_electrodes=None,
        serial_number=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            conductor_material=conductor_material,
            contributions=contributions,
            description=description,
            electrode_identifiers=electrode_identifiers,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            name=name,
            number_of_electrodes=number_of_electrodes,
            serial_number=serial_number,
            type=type,
        )
