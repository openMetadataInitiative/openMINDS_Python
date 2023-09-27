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

    type_ = ["https://openminds.ebrains.eu/ephys/Electrode"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "conductor_material",
            [
                "openminds.v3_0.chemicals.ChemicalMixture",
                "openminds.v3_0.chemicals.ChemicalSubstance",
                "openminds.v3_0.controlled_terms.MolecularEntity",
            ],
            "vocab:conductorMaterial",
            description="no description available",
            instructions="Add the conductor material of this electrode.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this device.",
        ),
        Property(
            "device_type",
            "openminds.v3_0.controlled_terms.DeviceType",
            "vocab:deviceType",
            required=True,
            description="no description available",
            instructions="Add the type of this device.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v3_0.core.DOI", "openminds.v3_0.core.RRID"],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this device.",
        ),
        Property(
            "insulator_material",
            [
                "openminds.v3_0.chemicals.ChemicalMixture",
                "openminds.v3_0.chemicals.ChemicalSubstance",
                "openminds.v3_0.controlled_terms.MolecularEntity",
            ],
            "vocab:insulatorMaterial",
            description="no description available",
            instructions="Add the insulator material of this electrode.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this electrode that is used within the corresponding data files to identify this electrode.",
        ),
        Property(
            "intrinsic_resistance",
            ["openminds.v3_0.core.QuantitativeValue", "openminds.v3_0.core.QuantitativeValueRange"],
            "vocab:intrinsicResistance",
            description="no description available",
            instructions="Enter the intrinsic resistance of this electrode.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device that may help you to find this instance more easily.",
        ),
        Property(
            "manufacturer",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this device.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer.",
        ),
        Property(
            "owner",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:owner",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all parties that legally own this device.",
        ),
        Property(
            "serial_number",
            str,
            "vocab:serialNumber",
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
        manufacturer=None,
        name=None,
        owner=None,
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
            manufacturer=manufacturer,
            name=name,
            owner=owner,
            serial_number=serial_number,
        )
