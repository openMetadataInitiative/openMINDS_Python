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
            "behavioral_tasks",
            "openminds.v2.controlled_terms.BehavioralTask",
            "behavioralTask",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject.",
            instructions="Add all behavioral tasks that were executed as part of this protocol.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this protocol.",
        ),
        Property(
            "study_options",
            [
                "openminds.v2.controlled_terms.BiologicalSex",
                "openminds.v2.controlled_terms.CellType",
                "openminds.v2.controlled_terms.Disease",
                "openminds.v2.controlled_terms.DiseaseModel",
                "openminds.v2.controlled_terms.Handedness",
                "openminds.v2.controlled_terms.Organ",
                "openminds.v2.controlled_terms.Phenotype",
                "openminds.v2.controlled_terms.Species",
                "openminds.v2.controlled_terms.Strain",
                "openminds.v2.controlled_terms.TermSuggestion",
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

    def __init__(
        self, id=None, behavioral_tasks=None, description=None, name=None, study_options=None, techniques=None
    ):
        return super().__init__(
            id=id,
            behavioral_tasks=behavioral_tasks,
            description=description,
            name=name,
            study_options=study_options,
            techniques=techniques,
        )
