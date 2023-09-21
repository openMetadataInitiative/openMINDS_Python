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

    type_ = ["https://openminds.ebrains.eu/ephys/Pipette"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
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
            "openminds.latest.controlled_terms.DeviceType",
            "vocab:deviceType",
            required=True,
            description="no description available",
            instructions="Add the type of this device.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.RRID"],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this device.",
        ),
        Property(
            "external_diameter",
            "openminds.latest.core.QuantitativeValue",
            "vocab:externalDiameter",
            description="no description available",
            instructions="Enter the external diameter of the pipette.",
        ),
        Property(
            "internal_diameter",
            "openminds.latest.core.QuantitativeValue",
            "vocab:internalDiameter",
            description="no description available",
            instructions="Enter the internal diameter of the pipette.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this pipette that is used within the corresponding data files to identify this pipette.",
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
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this device.",
        ),
        Property(
            "material",
            [
                "openminds.latest.chemicals.ChemicalMixture",
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.controlled_terms.MolecularEntity",
            ],
            "vocab:material",
            description="no description available",
            instructions="Add the material that the pipette is made of.",
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
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
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
        description=None,
        device_type=None,
        digital_identifier=None,
        external_diameter=None,
        internal_diameter=None,
        internal_identifier=None,
        lookup_label=None,
        manufacturer=None,
        material=None,
        name=None,
        owner=None,
        serial_number=None,
    ):
        return super().__init__(
            id=id,
            description=description,
            device_type=device_type,
            digital_identifier=digital_identifier,
            external_diameter=external_diameter,
            internal_diameter=internal_diameter,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            manufacturer=manufacturer,
            material=material,
            name=name,
            owner=owner,
            serial_number=serial_number,
        )
