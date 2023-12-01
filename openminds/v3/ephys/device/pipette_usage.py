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
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "anatomical_location",
            [
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.sands.CustomAnatomicalEntity",
                "openminds.v3.sands.ParcellationEntity",
                "openminds.v3.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocation",
            description="no description available",
            instructions="Add the anatomical entity that semantically best describes the anatomical location of the pipette tip.",
        ),
        Property(
            "chloride_reversal_potentials",
            "openminds.v3.core.Measurement",
            "chlorideReversalPotential",
            multiple=True,
            unique_items=False,
            min_items=1,
            description="no description available",
            instructions="Enter all chloride reversal potentials for the intracellular solution(s) of the pipette measured during its use.",
        ),
        Property(
            "compensation_current",
            "openminds.v3.core.Measurement",
            "compensationCurrent",
            description="no description available",
            instructions="Enter the compensation current for the series resistance of the pipette measured during its use.",
        ),
        Property(
            "device",
            "openminds.v3.ephys.Pipette",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the pipette used.",
        ),
        Property(
            "end_membrane_potential",
            "openminds.v3.core.Measurement",
            "endMembranePotential",
            description="no description available",
            instructions="Enter the membrane potential of e.g., a patched cell at the end of a recording measured during the use of this pipette.",
        ),
        Property(
            "holding_potential",
            "openminds.v3.core.Measurement",
            "holdingPotential",
            description="no description available",
            instructions="Enter the holding membrane potential of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "input_resistance",
            "openminds.v3.core.Measurement",
            "inputResistance",
            description="no description available",
            instructions="Enter the input resistance of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "labeling_compound",
            [
                "openminds.v3.chemicals.ChemicalMixture",
                "openminds.v3.chemicals.ChemicalSubstance",
                "openminds.v3.controlled_terms.MolecularEntity",
            ],
            "labelingCompound",
            description="no description available",
            instructions="Add the used compound for labelling e.g., a patched cell during the use of this pipette. ",
        ),
        Property(
            "liquid_junction_potential",
            "openminds.v3.core.Measurement",
            "liquidJunctionPotential",
            description="no description available",
            instructions="Enter the liquid junction potential of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_locations",
            ["openminds.v3.core.File", "openminds.v3.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "pipette_resistance",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "pipetteResistance",
            description="no description available",
            instructions="Enter the resistance of the pipette during its use.",
        ),
        Property(
            "pipette_solution",
            "openminds.v3.chemicals.ChemicalMixture",
            "pipetteSolution",
            required=True,
            description="no description available",
            instructions="Enter the solution with which the pipette was filled during its use.",
        ),
        Property(
            "seal_resistance",
            "openminds.v3.core.Measurement",
            "sealResistance",
            description="no description available",
            instructions="Enter the seal resistance of e.g., a patched cell measured during the use of this pipette.",
        ),
        Property(
            "series_resistance",
            "openminds.v3.core.Measurement",
            "seriesResistance",
            description="no description available",
            instructions="Enter the series resistance of the pipette measured during its use.",
        ),
        Property(
            "spatial_location",
            "openminds.v3.sands.CoordinatePoint",
            "spatialLocation",
            description="no description available",
            instructions="Add the coordinate point that best describes the spatial location of the pipette tip during its use.",
        ),
        Property(
            "start_membrane_potential",
            "openminds.v3.core.Measurement",
            "startMembranePotential",
            description="no description available",
            instructions="Enter the membrane potential of e.g., a patched cell at the beginning of a recording measured during the use of this pipette.",
        ),
        Property(
            "used_specimen",
            ["openminds.v3.core.SubjectState", "openminds.v3.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_location=None,
        chloride_reversal_potentials=None,
        compensation_current=None,
        device=None,
        end_membrane_potential=None,
        holding_potential=None,
        input_resistance=None,
        labeling_compound=None,
        liquid_junction_potential=None,
        lookup_label=None,
        metadata_locations=None,
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
            chloride_reversal_potentials=chloride_reversal_potentials,
            compensation_current=compensation_current,
            device=device,
            end_membrane_potential=end_membrane_potential,
            holding_potential=holding_potential,
            input_resistance=input_resistance,
            labeling_compound=labeling_compound,
            liquid_junction_potential=liquid_junction_potential,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            pipette_resistance=pipette_resistance,
            pipette_solution=pipette_solution,
            seal_resistance=seal_resistance,
            series_resistance=series_resistance,
            spatial_location=spatial_location,
            start_membrane_potential=start_membrane_potential,
            used_specimen=used_specimen,
        )
