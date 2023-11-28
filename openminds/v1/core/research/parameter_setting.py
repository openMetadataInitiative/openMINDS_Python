"""
Structured information on a used parameter setting.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParameterSetting(LinkedMetadata):
    """
    Structured information on a used parameter setting.
    """

    type_ = "https://openminds.ebrains.eu/core/ParameterSetting"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this parameter setting.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this parameter setting.",
        ),
        Property(
            "relevant_for",
            ["openminds.v1.controlled_terms.BehavioralTask", "openminds.v1.controlled_terms.Technique"],
            "relevantFor",
            required=True,
            description="Reference to what or whom something or someone bears significance.",
            instructions="Add the technique or behavioral task where this parameter setting is used in.",
        ),
        Property(
            "unit",
            "openminds.v1.controlled_terms.UnitOfMeasurement",
            "unit",
            description="Determinate quantity adopted as a standard of measurement.",
            instructions="Add the unit of measurement used for the value of this parameter setting.",
        ),
        Property(
            "value",
            ["float", "str"],
            "value",
            required=True,
            description="Entry for a property.",
            instructions="Enter the value of this parameter setting.",
        ),
    ]

    def __init__(self, id=None, description=None, name=None, relevant_for=None, unit=None, value=None):
        return super().__init__(
            id=id,
            description=description,
            name=name,
            relevant_for=relevant_for,
            unit=unit,
            value=value,
        )
