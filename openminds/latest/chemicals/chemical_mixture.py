"""
Structured information about a mixture of chemical substances.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ChemicalMixture(LinkedMetadata):
    """
    Structured information about a mixture of chemical substances.
    """

    type_ = "https://openminds.ebrains.eu/chemicals/ChemicalMixture"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this chemical mixture.",
        ),
        Property(
            "has_parts",
            "openminds.latest.chemicals.AmountOfChemical",
            "hasPart",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="no description available",
            instructions="Enter all components, including other mixtures, that are part of this chemical mixture.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this chemical mixture.",
        ),
        Property(
            "product_source",
            "openminds.latest.chemicals.ProductSource",
            "productSource",
            description="no description available",
            instructions="Add the source of this chemical mixture.",
        ),
        Property(
            "type",
            "openminds.latest.controlled_terms.ChemicalMixtureType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this mixture.",
        ),
    ]

    def __init__(self, id=None, additional_remarks=None, has_parts=None, name=None, product_source=None, type=None):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            has_parts=has_parts,
            name=name,
            product_source=product_source,
            type=type,
        )
