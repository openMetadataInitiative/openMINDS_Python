"""
<description not available>
"""

# this file was auto-generated!

from datetime import datetime, time

from openminds.base import LinkedMetadata
from openminds.properties import Property


class StimulationActivity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/stimulation/StimulationActivity"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "custom_property_sets",
            "openminds.v3.core.CustomPropertySet",
            "customPropertySet",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this activity.",
        ),
        Property(
            "end_time",
            [datetime, time],
            "endTime",
            description="no description available",
            instructions="Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "inputs",
            [
                "openminds.v3.core.SubjectGroupState",
                "openminds.v3.core.SubjectState",
                "openminds.v3.core.TissueSampleCollectionState",
                "openminds.v3.core.TissueSampleState",
            ],
            "input",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that is put into or participates in a process or machine.",
            instructions="Add all states of the specimen(s) that are being stimulated during this activity.",
        ),
        Property(
            "is_part_of",
            "openminds.v3.core.DatasetVersion",
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the dataset version in which this activity was conducted.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this activity that may help you to find this instance more easily.",
        ),
        Property(
            "outputs",
            [
                "openminds.v3.core.SubjectGroupState",
                "openminds.v3.core.SubjectState",
                "openminds.v3.core.TissueSampleCollectionState",
                "openminds.v3.core.TissueSampleState",
            ],
            "output",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that comes out of, is delivered or produced by a process or machine.",
            instructions="Add all states of the specimen(s) that were stimulated as a result of this activity.",
        ),
        Property(
            "performed_by",
            ["openminds.v3.computation.SoftwareAgent", "openminds.v3.core.Person"],
            "performedBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all agents that performed this activity.",
        ),
        Property(
            "preparation_design",
            "openminds.v3.controlled_terms.PreparationType",
            "preparationDesign",
            description="no description available",
            instructions="Add the initial preparation type for this activity.",
        ),
        Property(
            "protocols",
            "openminds.v3.core.Protocol",
            "protocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Plan that describes the process of a scientific or medical experiment, treatment, or procedure.",
            instructions="Add all protocols used during this activity.",
        ),
        Property(
            "setup",
            "openminds.v3.core.Setup",
            "setup",
            description="no description available",
            instructions="Add the setup used during this stimulation activity.",
        ),
        Property(
            "start_time",
            [datetime, time],
            "startTime",
            description="no description available",
            instructions="Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "stimuli",
            [],
            "stimulus",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all stimuli used during this activity.",
        ),
        Property(
            "study_targets",
            [
                "openminds.v3.controlled_terms.AuditoryStimulusType",
                "openminds.v3.controlled_terms.BiologicalOrder",
                "openminds.v3.controlled_terms.BiologicalSex",
                "openminds.v3.controlled_terms.BreedingType",
                "openminds.v3.controlled_terms.CellCultureType",
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Disease",
                "openminds.v3.controlled_terms.DiseaseModel",
                "openminds.v3.controlled_terms.ElectricalStimulusType",
                "openminds.v3.controlled_terms.GeneticStrainType",
                "openminds.v3.controlled_terms.GustatoryStimulusType",
                "openminds.v3.controlled_terms.Handedness",
                "openminds.v3.controlled_terms.MolecularEntity",
                "openminds.v3.controlled_terms.OlfactoryStimulusType",
                "openminds.v3.controlled_terms.OpticalStimulusType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.OrganismSystem",
                "openminds.v3.controlled_terms.Species",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.TactileStimulusType",
                "openminds.v3.controlled_terms.TermSuggestion",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.controlled_terms.VisualStimulusType",
                "openminds.v3.sands.CustomAnatomicalEntity",
                "openminds.v3.sands.ParcellationEntity",
                "openminds.v3.sands.ParcellationEntityVersion",
            ],
            "studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this activity.",
        ),
    ]

    def __init__(
        self,
        id=None,
        custom_property_sets=None,
        description=None,
        end_time=None,
        inputs=None,
        is_part_of=None,
        lookup_label=None,
        outputs=None,
        performed_by=None,
        preparation_design=None,
        protocols=None,
        setup=None,
        start_time=None,
        stimuli=None,
        study_targets=None,
    ):
        return super().__init__(
            id=id,
            custom_property_sets=custom_property_sets,
            description=description,
            end_time=end_time,
            inputs=inputs,
            is_part_of=is_part_of,
            lookup_label=lookup_label,
            outputs=outputs,
            performed_by=performed_by,
            preparation_design=preparation_design,
            protocols=protocols,
            setup=setup,
            start_time=start_time,
            stimuli=stimuli,
            study_targets=study_targets,
        )
