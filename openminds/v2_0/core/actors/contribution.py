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

    type_ = ["https://openminds.ebrains.eu/core/Contribution"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "contribution_type",
            "openminds.v2_0.controlled_terms.ContributionType",
            "vocab:contributionType",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct class of what was given or supplied as a part or share.",
            instructions="Add one or several type of contributions made by the stated contributor.",
        ),
        Property(
            "contributor",
            ["openminds.v2_0.core.Organization", "openminds.v2_0.core.Person"],
            "vocab:contributor",
            required=True,
            description="Legal person that gave or supplied something as a part or share.",
            instructions="Add the contributing person or organization.",
        ),
    ]

    def __init__(self, contribution_type=None, contributor=None):
        return super().__init__(
            contribution_type=contribution_type,
            contributor=contributor,
        )
