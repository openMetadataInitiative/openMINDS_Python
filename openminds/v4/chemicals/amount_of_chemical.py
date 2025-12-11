"""
Structured information about the amount of a given chemical that was used.
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class AmountOfChemical(EmbeddedMetadata):
    """
    Structured information about the amount of a given chemical that was used.
    """

    type_ = "https://openminds.om-i.org/types/AmountOfChemical"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "amount",
            "openminds.v4.core.QuantitativeValue",
            "amount",
            description="no description available",
            instructions="When used in a mixture, enter the amount of the substance within the mixture (e.g., as concentration or as ratio). When used in its pure state, enter the used amount of the substance.",
        ),
        Property(
            "chemical_product",
            [
                "openminds.v4.chemicals.ChemicalMixture",
                "openminds.v4.chemicals.ChemicalSubstance",
                "openminds.v4.controlled_terms.MolecularEntity",
            ],
            "chemicalProduct",
            required=True,
            description="no description available",
            instructions="Add the chemical product that was used.",
        ),
    ]

    def __init__(self, amount=None, chemical_product=None):
        return super().__init__(
            amount=amount,
            chemical_product=chemical_product,
        )
