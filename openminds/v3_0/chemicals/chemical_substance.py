"""
Structured information about a chemical substance.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ChemicalSubstance(LinkedMetadata):
    """
    Structured information about a chemical substance.
    """

    type_ = "https://openminds.ebrains.eu/chemicals/ChemicalSubstance"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering this chemical substance.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this chemical substance that may help you to find this instance more easily.",
        ),
        Property(
            "molecular_entity",
            "openminds.v3_0.controlled_terms.MolecularEntity",
            "vocab:molecularEntity",
            required=True,
            description="no description available",
            instructions="Add the molecular entity that makes up this chemical substance.",
        ),
        Property(
            "product_source",
            "openminds.v3_0.chemicals.ProductSource",
            "vocab:productSource",
            description="no description available",
            instructions="Add the source of this chemical substance.",
        ),
        Property(
            "purity",
            ["openminds.v3_0.core.QuantitativeValue", "openminds.v3_0.core.QuantitativeValueRange"],
            "vocab:purity",
            description="no description available",
            instructions="Enter the purity of this chemical substance.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        lookup_label=None,
        molecular_entity=None,
        product_source=None,
        purity=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            lookup_label=lookup_label,
            molecular_entity=molecular_entity,
            product_source=product_source,
            purity=purity,
        )
