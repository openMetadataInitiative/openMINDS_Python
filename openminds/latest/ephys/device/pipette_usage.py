"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class PipetteUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/ephys/PipetteUsage"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "anatomical_location",
            [
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.sands.CustomAnatomicalEntity",
                "openminds.latest.sands.ParcellationEntity",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocation",
            description="no description available",
            instructions="Add the anatomical entity that semantically best describes the anatomical location of the pipette tip.",
        ),
        Property(
            "chloride_reversal_potential",
            "openminds.latest.core.Measurement",
            "vocab:chlorideReversalPotential",
            multiple=True,
            unique_items=False,
            min_items=1,
            description="no description available",
            instructions="Enter all chloride reversal potentials for the intracellular solution(s) of the pipette measured during its use.",
        ),
        Property(
            "compensation_current",
            "openminds.latest.core.Measurement",
            "vocab:compensationCurrent",
            description="no description available",
            instructions="Enter the compensation current for the series resistance of the pipette measured during its use.",
        ),
        Property(
            "device",
            "openminds.latest.ephys.Pipette",
            "vocab:device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the pipette used.",
        ),
        Property(
            "end_membrane_potential",
            "openminds.latest.core.Measurement",
            "vocab:endMembranePotential",
            description="no description available",
            instructions="Enter the membrane potential of e.g., a patched cell at the end of a recording measured during the use of this pipette.",
        ),
        Property(
            "holding_potential",
            "openminds.latest.core.Measurement",
            "vocab:holdingPotential",
            description="no description available",
            instructions="Enter the holding membrane potential of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "input_resistance",
            "openminds.latest.core.Measurement",
            "vocab:inputResistance",
            description="no description available",
            instructions="Enter the input resistance of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "labeling_compound",
            [
                "openminds.latest.chemicals.ChemicalMixture",
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.controlled_terms.MolecularEntity",
            ],
            "vocab:labelingCompound",
            description="no description available",
            instructions="Add the used compound for labelling e.g., a patched cell during the use of this pipette. ",
        ),
        Property(
            "liquid_junction_potential",
            "openminds.latest.core.Measurement",
            "vocab:liquidJunctionPotential",
            description="no description available",
            instructions="Enter the liquid junction potential of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_location",
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "vocab:metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "pipette_resistance",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "vocab:pipetteResistance",
            description="no description available",
            instructions="Enter the resistance of the pipette during its use.",
        ),
        Property(
            "pipette_solution",
            "openminds.latest.chemicals.ChemicalMixture",
            "vocab:pipetteSolution",
            required=True,
            description="no description available",
            instructions="Enter the solution with which the pipette was filled during its use.",
        ),
        Property(
            "seal_resistance",
            "openminds.latest.core.Measurement",
            "vocab:sealResistance",
            description="no description available",
            instructions="Enter the seal resistance of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "series_resistance",
            "openminds.latest.core.Measurement",
            "vocab:seriesResistance",
            description="no description available",
            instructions="Enter the series resistance of the pipette measured during its use.",
        ),
        Property(
            "spatial_location",
            "openminds.latest.sands.CoordinatePoint",
            "vocab:spatialLocation",
            description="no description available",
            instructions="Add the coordinate point that best describes the spatial location of the pipette tip during its use.",
        ),
        Property(
            "start_membrane_potential",
            "openminds.latest.core.Measurement",
            "vocab:startMembranePotential",
            description="no description available",
            instructions="Enter the membrane potential of e.g., a patched cell at the beginning of a recording measured during the use of this pipette.",
        ),
        Property(
            "used_specimen",
            ["openminds.latest.core.SubjectState", "openminds.latest.core.TissueSampleState"],
            "vocab:usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_location=None,
        chloride_reversal_potential=None,
        compensation_current=None,
        device=None,
        end_membrane_potential=None,
        holding_potential=None,
        input_resistance=None,
        labeling_compound=None,
        liquid_junction_potential=None,
        lookup_label=None,
        metadata_location=None,
        pipette_resistance=None,
        pipette_solution=None,
        seal_resistance=None,
        series_resistance=None,
        spatial_location=None,
        start_membrane_potential=None,
        used_specimen=None,
    ):
        return super().__init__(
            id=id,
            anatomical_location=anatomical_location,
            chloride_reversal_potential=chloride_reversal_potential,
            compensation_current=compensation_current,
            device=device,
            end_membrane_potential=end_membrane_potential,
            holding_potential=holding_potential,
            input_resistance=input_resistance,
            labeling_compound=labeling_compound,
            liquid_junction_potential=liquid_junction_potential,
            lookup_label=lookup_label,
            metadata_location=metadata_location,
            pipette_resistance=pipette_resistance,
            pipette_solution=pipette_solution,
            seal_resistance=seal_resistance,
            series_resistance=series_resistance,
            spatial_location=spatial_location,
            start_membrane_potential=start_membrane_potential,
            used_specimen=used_specimen,
        )
