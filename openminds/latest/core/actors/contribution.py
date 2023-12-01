"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Contribution(EmbeddedMetadata):
    """
    Structured information on the contribution made to a research product.
    """

    type_ = "https://openminds.ebrains.eu/core/Contribution"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "contributor",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "contributor",
            required=True,
            description="Legal person that gave or supplied something as a part or share.",
            instructions="Add all types of contribution made by the stated 'contributor'.",
        ),
        Property(
            "types",
            "openminds.latest.controlled_terms.ContributionType",
            "type",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the party that performed the contribution.",
        ),
    ]

    def __init__(self, contributor=None, types=None):
        return super().__init__(
            contributor=contributor,
            types=types,
        )
