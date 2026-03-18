"""
<description not available>
"""

# this file was auto-generated!

from datetime import datetime

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ServiceDeployment(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ServiceDeployment"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "depends_on",
            [
                "openminds.v5.computation.WorkflowRecipeVersion",
                "openminds.v5.core.DatasetVersion",
                "openminds.v5.core.MetaDataModelVersion",
                "openminds.v5.core.ModelVersion",
                "openminds.v5.core.SoftwareVersion",
                "openminds.v5.sands.AnatomicalAtlasVersion",
                "openminds.v5.sands.CommonCoordinateFrameworkVersion",
            ],
            "dependsOn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the software version and any other relevant research product version that was deployed.",
        ),
        Property(
            "deployment_type",
            "openminds.v5.controlled_terms.DeploymentEnvironmentType",
            "deploymentType",
            description="no description available",
            instructions="Enter the type of deployment environment, for example, 'production' or 'integration'.",
        ),
        Property(
            "end_time",
            datetime,
            "endTime",
            description="no description available",
            instructions="Enter the date and time at which this deployment ended, formatted according to ISO-8601.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the service deployment.",
            instructions="Enter a label for this service deployment.",
        ),
        Property(
            "provides",
            "openminds.v5.computation.DeployedInterface",
            "provides",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add the interfaces that have been deployed.",
        ),
        Property(
            "service",
            "openminds.v5.core.Service",
            "service",
            required=True,
            description="no description available",
            instructions="Add the service that has been deployed.",
        ),
        Property(
            "start_time",
            datetime,
            "startTime",
            required=True,
            description="no description available",
            instructions="Enter the date and time at which this deployment was started, formatted according to ISO-8601.",
        ),
        Property(
            "uses",
            [
                "openminds.v5.computation.WorkflowRecipeVersion",
                "openminds.v5.core.DatasetVersion",
                "openminds.v5.core.MetaDataModelVersion",
                "openminds.v5.core.ModelVersion",
                "openminds.v5.core.WebResource",
                "openminds.v5.sands.AnatomicalAtlasVersion",
                "openminds.v5.sands.CommonCoordinateFrameworkVersion",
            ],
            "uses",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the deployed interfaces and any other relevant research product versions that are used by this deployment.",
        ),
    ]

    def __init__(
        self,
        id=None,
        depends_on=None,
        deployment_type=None,
        end_time=None,
        name=None,
        provides=None,
        service=None,
        start_time=None,
        uses=None,
    ):
        return super().__init__(
            id=id,
            depends_on=depends_on,
            deployment_type=deployment_type,
            end_time=end_time,
            name=name,
            provides=provides,
            service=service,
            start_time=start_time,
            uses=uses,
        )
