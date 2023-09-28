"""
Structured information on a used parameter set.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class ParameterSet(EmbeddedMetadata):
    """
    Structured information on a used parameter set.
    """

    type_ = "https://openminds.ebrains.eu/core/ParameterSet"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "context",
            str,
            "vocab:context",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the common context for the parameters grouped in this set.",
        ),
        Property(
            "parameter",
            ["openminds.v2_0.core.NumericalParameter", "openminds.v2_0.core.StringParameter"],
            "vocab:parameter",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Digital or physical property determining a particular function, characteristic or behavior of something.",
            instructions="Add all numerical and string parameters that belong to this parameter set.",
        ),
        Property(
            "relevant_for",
            ["openminds.v2_0.controlled_terms.BehavioralTask", "openminds.v2_0.controlled_terms.Technique"],
            "vocab:relevantFor",
            required=True,
            description="Reference to what or whom something or someone bears siginificance.",
            instructions="Add the technique or behavioral task where this set of parameters is used in.",
        ),
    ]

    def __init__(self, context=None, parameter=None, relevant_for=None):
        return super().__init__(
            context=context,
            parameter=parameter,
            relevant_for=relevant_for,
        )
