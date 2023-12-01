"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Electrode(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/ephys/Electrode"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
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
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this device.",
        ),
        Property(
            "device_type",
            "openminds.latest.controlled_terms.DeviceType",
            "deviceType",
            required=True,
            description="no description available",
            instructions="Add the type of this device.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this device.",
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
            description="Term or code that identifies someone or something within a particular product.",
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
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device that may help you to find this instance more easily.",
        ),
        Property(
            "manufacturers",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this device.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer.",
        ),
        Property(
            "owners",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "owner",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all parties that legally own this device.",
        ),
        Property(
            "serial_number",
            str,
            "serialNumber",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the serial number of this device.",
        ),
    ]

    def __init__(
        self,
        id=None,
        conductor_material=None,
        description=None,
        device_type=None,
        digital_identifier=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
        lookup_label=None,
        manufacturers=None,
        name=None,
        owners=None,
        serial_number=None,
    ):
        return super().__init__(
            id=id,
            conductor_material=conductor_material,
            description=description,
            device_type=device_type,
            digital_identifier=digital_identifier,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            lookup_label=lookup_label,
            manufacturers=manufacturers,
            name=name,
            owners=owners,
            serial_number=serial_number,
        )
