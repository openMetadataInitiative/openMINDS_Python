"""
Structured information on a research project.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Protocol(LinkedMetadata):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.ebrains.eu/core/Protocol"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the protocol.",
            instructions="Enter a description of this protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the protocol.",
            instructions="Enter a descriptive name for this protocol.",
        ),
        Property(
            "study_options",
            [
                "openminds.v2.controlled_terms.AuditoryStimulusType",
                "openminds.v2.controlled_terms.BiologicalOrder",
                "openminds.v2.controlled_terms.BiologicalSex",
                "openminds.v2.controlled_terms.BreedingType",
                "openminds.v2.controlled_terms.CellCultureType",
                "openminds.v2.controlled_terms.CellType",
                "openminds.v2.controlled_terms.Disease",
                "openminds.v2.controlled_terms.DiseaseModel",
                "openminds.v2.controlled_terms.ElectricalStimulusType",
                "openminds.v2.controlled_terms.GeneticStrainType",
                "openminds.v2.controlled_terms.GustatoryStimulusType",
                "openminds.v2.controlled_terms.Handedness",
                "openminds.v2.controlled_terms.MolecularEntity",
                "openminds.v2.controlled_terms.OlfactoryStimulusType",
                "openminds.v2.controlled_terms.OpticalStimulusType",
                "openminds.v2.controlled_terms.Organ",
                "openminds.v2.controlled_terms.OrganismSubstance",
                "openminds.v2.controlled_terms.OrganismSystem",
                "openminds.v2.controlled_terms.Species",
                "openminds.v2.controlled_terms.SubcellularEntity",
                "openminds.v2.controlled_terms.TactileStimulusType",
                "openminds.v2.controlled_terms.TermSuggestion",
                "openminds.v2.controlled_terms.TissueSampleType",
                "openminds.v2.controlled_terms.UBERONParcellation",
                "openminds.v2.controlled_terms.VisualStimulusType",
                "openminds.v2.sands.CustomAnatomicalEntity",
                "openminds.v2.sands.ParcellationEntity",
            ],
            "studyOption",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all study options this protocol offers.",
        ),
        Property(
            "techniques",
            "openminds.v2.controlled_terms.Technique",
            "technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques that were used in this protocol.",
        ),
    ]

    def __init__(self, id=None, description=None, name=None, study_options=None, techniques=None):
        return super().__init__(
            id=id,
            description=description,
            name=name,
            study_options=study_options,
            techniques=techniques,
        )
