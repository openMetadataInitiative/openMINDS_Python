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
    schema_version = "v3.0"

    properties = [
        Property(
            "configuration",
            ["openminds.v3.core.Configuration", "openminds.v3.core.File"],
            "configuration",
            description="no description available",
            instructions="Add the configuration information for this workflow execution.",
        ),
        Property(
            "recipe",
            "openminds.v3.computation.WorkflowRecipeVersion",
            "recipe",
            description="no description available",
            instructions="Add the workflow recipe version used for this workflow execution.",
        ),
        Property(
            "stages",
            [
                "openminds.v3.computation.DataAnalysis",
                "openminds.v3.computation.DataCopy",
                "openminds.v3.computation.GenericComputation",
                "openminds.v3.computation.ModelValidation",
                "openminds.v3.computation.Optimization",
                "openminds.v3.computation.Simulation",
                "openminds.v3.computation.Visualization",
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
            ["openminds.v3.computation.SoftwareAgent", "openminds.v3.core.Person"],
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
