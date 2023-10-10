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

    type_ = "https://openminds.ebrains.eu/chemicals/AmountOfChemical"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "amount",
            "openminds.v3.core.QuantitativeValue",
            "amount",
            description="no description available",
            instructions="When used in a mixture, enter the amount of the substance within the mixture (e.g., as concentration or as ratio). When used in its pure state, enter the used amount of the substance.",
        ),
        Property(
            "chemical_product",
            [
                "openminds.v3.chemicals.ChemicalMixture",
                "openminds.v3.chemicals.ChemicalSubstance",
                "openminds.v3.controlled_terms.MolecularEntity",
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
