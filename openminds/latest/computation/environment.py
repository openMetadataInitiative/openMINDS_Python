"""
Structured information on the computer system or set of systems in which a computation is deployed and executed.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Environment(LinkedMetadata):
    """
    Structured information on the computer system or set of systems in which a computation is deployed and executed.
    """

    type_ = ["https://openminds.ebrains.eu/computation/Environment"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "configuration",
            "openminds.latest.core.Configuration",
            "vocab:configuration",
            description="no description available",
            instructions="Add the configuration of this computational environment.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this computational environment.",
        ),
        Property(
            "hardware",
            "openminds.latest.computation.HardwareSystem",
            "vocab:hardware",
            required=True,
            description="no description available",
            instructions="Add the hardware system on which this computational environment runs.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this computational environment.",
        ),
        Property(
            "software",
            "openminds.latest.core.SoftwareVersion",
            "vocab:software",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all software versions available in this computational environment.",
        ),
    ]

    def __init__(self, id=None, configuration=None, description=None, hardware=None, name=None, software=None):
        return super().__init__(
            id=id,
            configuration=configuration,
            description=description,
            hardware=hardware,
            name=name,
            software=software,
        )