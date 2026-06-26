# this file was auto-generated!


from openminds.v5.controlled_terms.deployment_environment_type import DeploymentEnvironmentType


DeploymentEnvironmentType.development = DeploymentEnvironmentType(
    id="https://openminds.om-i.org/instances/deploymentEnvironmentType/development",
    definition="A working environment for developers to build, test, and debug new features or changes; usually more flexible and less restricted than other environments.",
    name="development",
    synonyms=["dev", "development environment"],
)

DeploymentEnvironmentType.integration = DeploymentEnvironmentType(
    id="https://openminds.om-i.org/instances/deploymentEnvironmentType/integration",
    definition="An environment in which multiple components or services are integrated and tested together to ensure interoperability and to detect issues early.",
    name="integration",
    synonyms=["int", "integration environment"],
)

DeploymentEnvironmentType.pre_production = DeploymentEnvironmentType(
    id="https://openminds.om-i.org/instances/deploymentEnvironmentType/pre-production",
    definition="A near-final environment used to validate releases before moving to production; typically mirrors the production setup closely and is used for final checks.",
    name="pre-production",
    synonyms=["pprod", "preprod", "pre-prod", "pre-production environment"],
)

DeploymentEnvironmentType.production = DeploymentEnvironmentType(
    id="https://openminds.om-i.org/instances/deploymentEnvironmentType/production",
    definition="The live environment where an application is fully deployed and accessed by end users; it requires high stability, performance, and monitoring.",
    name="production",
    synonyms=["prod", "production environment"],
)

DeploymentEnvironmentType.staging = DeploymentEnvironmentType(
    id="https://openminds.om-i.org/instances/deploymentEnvironmentType/staging",
    definition="An isolated environment that replicates the production environment for final integration and validation; often used for release candidate testing.",
    name="staging",
    synonyms=["staging environment"],
)
