"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueCulturePreparation(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/specimenPrep/TissueCulturePreparation"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "culture_medium",
            "openminds.latest.chemicals.ChemicalMixture",
            "vocab:cultureMedium",
            required=True,
            description="no description available",
            instructions="Add the culture medium used during this tissue culture preparation.",
        ),
        Property(
            "culture_type",
            "openminds.latest.controlled_terms.CellCultureType",
            "vocab:cultureType",
            required=True,
            description="no description available",
            instructions="Add the cell culture type of the resulting tissue cell culture.",
        ),
        Property(
            "input",
            [
                "openminds.latest.core.TissueSampleState",
                "openminds.latest.core.TissueSampleCollectionState",
                "openminds.latest.core.SubjectGroupState",
                "openminds.latest.core.SubjectState",
            ],
            "vocab:input",
            description="Something or someone that is put into or participates in a process or machine.",
            instructions="Add the state of the specimen before it was prepared as culture in this activity.",
        ),
        Property(
            "output",
            "openminds.latest.core.TissueSampleState",
            "vocab:output",
            description="Something or someone that comes out of, is delivered or produced by a process or machine.",
            instructions="Add the state of the prepared tissue sample culture that resulted from this activity.",
        ),
    ]

    def __init__(self, id=None, culture_medium=None, culture_type=None, input=None, output=None):
        return super().__init__(
            id=id,
            culture_medium=culture_medium,
            culture_type=culture_type,
            input=input,
            output=output,
        )
