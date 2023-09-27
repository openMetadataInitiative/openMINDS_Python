"""
<description not available>
"""

# this file was auto-generated!

from datetime import datetime, time

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodePlacement(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/ephys/ElectrodePlacement"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "custom_property_set",
            "openminds.v3_0.core.CustomPropertySet",
            "vocab:customPropertySet",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this activity.",
        ),
        Property(
            "device",
            [
                "openminds.v3_0.ephys.ElectrodeArrayUsage",
                "openminds.v3_0.ephys.ElectrodeUsage",
                "openminds.v3_0.ephys.PipetteUsage",
                "openminds.v3_0.specimen_prep.SlicingDeviceUsage",
            ],
            "vocab:device",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add all electrodes placed during this activity.",
        ),
        Property(
            "end_time",
            [datetime, time],
            "vocab:endTime",
            description="no description available",
            instructions="Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "input",
            ["openminds.v3_0.core.TissueSampleState", "openminds.v3_0.core.SubjectState"],
            "vocab:input",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that is put into or participates in a process or machine.",
            instructions="Add the state of the specimen that the device is being placed in or on during this activity.",
        ),
        Property(
            "is_part_of",
            "openminds.v3_0.core.DatasetVersion",
            "vocab:isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the dataset version in which this activity was conducted.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this activity that may help you to find this instance more easily.",
        ),
        Property(
            "output",
            ["openminds.v3_0.core.TissueSampleState", "openminds.v3_0.core.SubjectState"],
            "vocab:output",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that comes out of, is delivered or produced by a process or machine.",
            instructions="Add all states of the specimen(s) that the device was placed in or on as a result of this activity.",
        ),
        Property(
            "performed_by",
            ["openminds.v3_0.computation.SoftwareAgent", "openminds.v3_0.core.Person"],
            "vocab:performedBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all agents that performed this activity.",
        ),
        Property(
            "preparation_design",
            "openminds.v3_0.controlled_terms.PreparationType",
            "vocab:preparationDesign",
            description="no description available",
            instructions="Add the initial preparation type for this activity.",
        ),
        Property(
            "protocol",
            "openminds.v3_0.core.Protocol",
            "vocab:protocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Plan that describes the process of a scientific or medical experiment, treatment, or procedure.",
            instructions="Add all protocols used during this activity.",
        ),
        Property(
            "start_time",
            [datetime, time],
            "vocab:startTime",
            description="no description available",
            instructions="Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "study_target",
            [
                "openminds.v3_0.controlled_terms.AuditoryStimulusType",
                "openminds.v3_0.controlled_terms.BiologicalOrder",
                "openminds.v3_0.controlled_terms.BiologicalSex",
                "openminds.v3_0.controlled_terms.BreedingType",
                "openminds.v3_0.controlled_terms.CellCultureType",
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Disease",
                "openminds.v3_0.controlled_terms.DiseaseModel",
                "openminds.v3_0.controlled_terms.ElectricalStimulusType",
                "openminds.v3_0.controlled_terms.GeneticStrainType",
                "openminds.v3_0.controlled_terms.GustatoryStimulusType",
                "openminds.v3_0.controlled_terms.Handedness",
                "openminds.v3_0.controlled_terms.MolecularEntity",
                "openminds.v3_0.controlled_terms.OlfactoryStimulusType",
                "openminds.v3_0.controlled_terms.OpticalStimulusType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.OrganismSystem",
                "openminds.v3_0.controlled_terms.Species",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.TactileStimulusType",
                "openminds.v3_0.controlled_terms.TermSuggestion",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.controlled_terms.VisualStimulusType",
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this activity.",
        ),
        Property(
            "target_position",
            "openminds.v3_0.sands.AnatomicalTargetPosition",
            "vocab:targetPosition",
            description="no description available",
            instructions="Enter the anatomical target position for the placement of the device.",
        ),
    ]

    def __init__(
        self,
        id=None,
        custom_property_set=None,
        description=None,
        device=None,
        end_time=None,
        input=None,
        is_part_of=None,
        lookup_label=None,
        output=None,
        performed_by=None,
        preparation_design=None,
        protocol=None,
        start_time=None,
        study_target=None,
        target_position=None,
    ):
        return super().__init__(
            id=id,
            custom_property_set=custom_property_set,
            description=description,
            device=device,
            end_time=end_time,
            input=input,
            is_part_of=is_part_of,
            lookup_label=lookup_label,
            output=output,
            performed_by=performed_by,
            preparation_design=preparation_design,
            protocol=protocol,
            start_time=start_time,
            study_target=study_target,
            target_position=target_position,
        )
