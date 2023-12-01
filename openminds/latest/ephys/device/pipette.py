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

    type_ = "https://openminds.ebrains.eu/ephys/Pipette"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
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
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this pipette that is used within the corresponding data files to identify this pipette.",
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
        description=None,
        device_type=None,
        digital_identifier=None,
        external_diameter=None,
        internal_diameter=None,
        internal_identifier=None,
        lookup_label=None,
        manufacturers=None,
        material=None,
        name=None,
        owners=None,
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
            manufacturers=manufacturers,
            material=material,
            name=name,
            owners=owners,
            serial_number=serial_number,
        )
