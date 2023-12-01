"""
Structured information about the launch of a computational process.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class LaunchConfiguration(LinkedMetadata):
    """
    Structured information about the launch of a computational process.
    """

    type_ = "https://openminds.ebrains.eu/computation/LaunchConfiguration"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "arguments",
            str,
            "argument",
            multiple=True,
            unique_items=False,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all command line arguments for this launch configuration.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this launch configuration.",
        ),
        Property(
            "environment_variable",
            "openminds.latest.core.PropertyValueList",
            "environmentVariable",
            description="no description available",
            instructions="Add any environment variables defined by this launch configuration.",
        ),
        Property(
            "executable",
            str,
            "executable",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the path to the command-line executable.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this launch configuration.",
        ),
    ]

    def __init__(
        self, id=None, arguments=None, description=None, environment_variable=None, executable=None, name=None
    ):
        return super().__init__(
            id=id,
            arguments=arguments,
            description=description,
            environment_variable=environment_variable,
            executable=executable,
            name=name,
        )
