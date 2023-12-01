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
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "configuration",
            ["openminds.latest.core.Configuration", "openminds.latest.core.File"],
            "configuration",
            description="no description available",
            instructions="Add the configuration information for this workflow execution.",
        ),
        Property(
            "recipe",
            "openminds.latest.computation.WorkflowRecipeVersion",
            "recipe",
            description="no description available",
            instructions="Add the workflow recipe version used for this workflow execution.",
        ),
        Property(
            "stages",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "stage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all stages that were performed in this workflow execution.",
        ),
        Property(
            "started_by",
            ["openminds.latest.computation.SoftwareAgent", "openminds.latest.core.Person"],
            "startedBy",
            description="no description available",
            instructions="Add the agent that started this workflow execution.",
        ),
    ]

    def __init__(self, id=None, configuration=None, recipe=None, stages=None, started_by=None):
        return super().__init__(
            id=id,
            configuration=configuration,
            recipe=recipe,
            stages=stages,
            started_by=started_by,
        )
