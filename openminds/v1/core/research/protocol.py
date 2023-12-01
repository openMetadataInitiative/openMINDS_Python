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
    schema_version = "v1.0"

    properties = [
        Property(
            "behavioral_tasks",
            "openminds.v1.controlled_terms.BehavioralTask",
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
            "study_targets",
            [
                "openminds.v1.controlled_term.BiologicalSex",
                "openminds.v1.controlled_term.Disease",
                "openminds.v1.controlled_term.Genotype",
                "openminds.v1.controlled_term.Phenotype",
                "openminds.v1.controlled_term.Species",
                "openminds.v1.controlled_term.TermSuggestion",
                "openminds.v1.sands.AnatomicalEntity",
            ],
            "studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this model version.",
        ),
        Property(
            "techniques",
            "openminds.v1.controlled_terms.Technique",
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
        self, id=None, behavioral_tasks=None, description=None, name=None, study_targets=None, techniques=None
    ):
        return super().__init__(
            id=id,
            behavioral_tasks=behavioral_tasks,
            description=description,
            name=name,
            study_targets=study_targets,
            techniques=techniques,
        )
