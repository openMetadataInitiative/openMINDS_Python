"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeArray(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/ephys/ElectrodeArray"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "conductor_material",
            ['openminds.latest.chemicals.ChemicalMixture', 'openminds.latest.chemicals.ChemicalSubstance', 'openminds.latest.controlled_terms.MolecularEntity'],
            "vocab:conductorMaterial",
            description="no description available",
            instructions="Add the conductor material of this electrode array."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this device."
        ),
        Property(
            "device_type",
            "openminds.latest.controlled_terms.DeviceType",
            "vocab:deviceType",required=True,
            description="no description available",
            instructions="Add the type of this device."
        ),
        Property(
            "digital_identifier",
            ['openminds.latest.core.DOI', 'openminds.latest.core.RRID'],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this device."
        ),
        Property(
            "electrode_identifier",
            str,
            "vocab:electrodeIdentifier",
            multiple=True,
            unique_items=True,
            min_items=2,
            
            formatting="text/plain",
            
            required=True,
            description="no description available",
            instructions="Enter the identifiers for each electrode of this electrode array. Note that the number of identifiers should match the number of electrodes of the array as stated under 'numberOfElectrodes'."
        ),
        Property(
            "insulator_material",
            ['openminds.latest.chemicals.ChemicalMixture', 'openminds.latest.chemicals.ChemicalSubstance', 'openminds.latest.controlled_terms.MolecularEntity'],
            "vocab:insulatorMaterial",
            description="no description available",
            instructions="Add the insulator material of this electrode array."
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",formatting="text/plain",
            
            
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this electrode array that is used within the corresponding data files to identify this electrode array."
        ),
        Property(
            "intrinsic_resistance",
            ['openminds.latest.core.QuantitativeValue', 'openminds.latest.core.QuantitativeValueRange'],
            "vocab:intrinsicResistance",
            description="no description available",
            instructions="Enter the intrinsic resistance of this electrode array."
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter a lookup label for this device that may help you to find this instance more easily."
        ),
        Property(
            "manufacturer",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this device."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer."
        ),
        Property(
            "number_of_electrodes",
            int,
            "vocab:numberOfElectrodes",required=True,
            description="no description available",
            instructions="Enter the number of electrodes that belong to this electrode array."
        ),
        Property(
            "owner",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:owner",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all parties that legally own this device."
        ),
        Property(
            "serial_number",
            str,
            "vocab:serialNumber",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter the serial number of this device."
        ),
        
    ]

    def __init__(self, id=None, conductor_material=None, description=None, device_type=None, digital_identifier=None, electrode_identifier=None, insulator_material=None, internal_identifier=None, intrinsic_resistance=None, lookup_label=None, manufacturer=None, name=None, number_of_electrodes=None, owner=None, serial_number=None):
        return super().__init__(id=id,conductor_material=conductor_material,description=description,device_type=device_type,digital_identifier=digital_identifier,electrode_identifier=electrode_identifier,insulator_material=insulator_material,internal_identifier=internal_identifier,intrinsic_resistance=intrinsic_resistance,lookup_label=lookup_label,manufacturer=manufacturer,name=name,number_of_electrodes=number_of_electrodes,owner=owner,serial_number=serial_number,)

