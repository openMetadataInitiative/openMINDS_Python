"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Contribution(LinkedMetadata):
    """
    Structured information on the contribution made to a research product.
    """

    type_ = "https://openminds.ebrains.eu/core/Contribution"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "contribution_type",
            "openminds.v1_0.controlled_terms.ContributionType",
            "contributionType",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct class of what was given or supplied as a part or share.",
            instructions="Add one or several type of contributions made by the stated contributor.",
        ),
        Property(
            "contributor",
            ["openminds.v1_0.core.Organization", "openminds.v1_0.core.Person"],
            "contributor",
            required=True,
            description="Legal person that gave or supplied something as a part or share.",
            instructions="Add the contributing person or organization.",
        ),
    ]

    def __init__(self, id=None, contribution_type=None, contributor=None):
        return super().__init__(
            id=id,
            contribution_type=contribution_type,
            contributor=contributor,
        )
