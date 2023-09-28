"""
Structured information about an execution of a computational workflow.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class WorkflowExecution(LinkedMetadata):
    """
    Structured information about an execution of a computational workflow.
    """

    type_ = "https://openminds.ebrains.eu/computation/WorkflowExecution"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "configuration",
            ["openminds.v3_0.core.Configuration", "openminds.v3_0.core.File"],
            "vocab:configuration",
            description="no description available",
            instructions="Add the configuration information for this workflow execution.",
        ),
        Property(
            "recipe",
            "openminds.v3_0.computation.WorkflowRecipeVersion",
            "vocab:recipe",
            description="no description available",
            instructions="Add the workflow recipe version used for this workflow execution.",
        ),
        Property(
            "stage",
            [
                "openminds.v3_0.computation.DataAnalysis",
                "openminds.v3_0.computation.DataCopy",
                "openminds.v3_0.computation.GenericComputation",
                "openminds.v3_0.computation.ModelValidation",
                "openminds.v3_0.computation.Optimization",
                "openminds.v3_0.computation.Simulation",
                "openminds.v3_0.computation.Visualization",
            ],
            "vocab:stage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all stages that were performed in this workflow execution.",
        ),
        Property(
            "started_by",
            ["openminds.v3_0.computation.SoftwareAgent", "openminds.v3_0.core.Person"],
            "vocab:startedBy",
            description="no description available",
            instructions="Add the agent that started this workflow execution.",
        ),
    ]

    def __init__(self, id=None, configuration=None, recipe=None, stage=None, started_by=None):
        return super().__init__(
            id=id,
            configuration=configuration,
            recipe=recipe,
            stage=stage,
            started_by=started_by,
        )
