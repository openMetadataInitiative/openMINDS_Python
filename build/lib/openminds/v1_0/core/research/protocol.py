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
    type_ = ["https://openminds.ebrains.eu/core/Protocol"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "behavioral_task",
            "openminds.v1_0.controlled_terms.BehavioralTask",
            "vocab:behavioralTask",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject.",
            instructions="Add all behavioral tasks that were executed as part of this protocol."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this protocol."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this protocol."
        ),
        Property(
            "study_target",
            ['openminds.v1_0.controlled_term.BiologicalSex', 'openminds.v1_0.controlled_term.Disease', 'openminds.v1_0.controlled_term.Genotype', 'openminds.v1_0.controlled_term.Phenotype', 'openminds.v1_0.controlled_term.Species', 'openminds.v1_0.controlled_term.TermSuggestion', 'openminds.v1_0.sands.AnatomicalEntity'],
            "vocab:studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this model version."
        ),
        Property(
            "technique",
            "openminds.v1_0.controlled_terms.Technique",
            "vocab:technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques that were used in this protocol."
        ),
        
    ]

    def __init__(self, id=None, behavioral_task=None, description=None, name=None, study_target=None, technique=None):
        return super().__init__(id=id,behavioral_task=behavioral_task,description=description,name=name,study_target=study_target,technique=technique,)

