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

    type_ = "https://openminds.om-i.org/types/WorkflowExecution"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "configuration",
            ["openminds.v5.core.Configuration", "openminds.v5.core.File"],
            "configuration",
            description="no description available",
            instructions="Add the configuration information for this workflow execution.",
        ),
        Property(
            "recipe",
            "openminds.v5.computation.WorkflowRecipeVersion",
            "recipe",
            description="no description available",
            instructions="Add the workflow recipe version used for this workflow execution.",
        ),
        Property(
            "stages",
            [
                "openminds.v5.computation.DataAnalysis",
                "openminds.v5.computation.DataCopy",
                "openminds.v5.computation.GenericComputation",
                "openminds.v5.computation.ModelValidation",
                "openminds.v5.computation.Optimization",
                "openminds.v5.computation.Simulation",
                "openminds.v5.computation.Visualization",
            ],
            "stage",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all stages that were performed in this workflow execution.",
        ),
        Property(
            "started_by",
            ["openminds.v5.computation.SoftwareAgent", "openminds.v5.core.Person"],
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
