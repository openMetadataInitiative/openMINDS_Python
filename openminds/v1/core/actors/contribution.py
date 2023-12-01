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
    schema_version = "v1.0"

    properties = [
        Property(
            "contribution_types",
            "openminds.v1.controlled_terms.ContributionType",
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
            ["openminds.v1.core.Organization", "openminds.v1.core.Person"],
            "contributor",
            required=True,
            description="Legal person that gave or supplied something as a part or share.",
            instructions="Add the contributing person or organization.",
        ),
    ]

    def __init__(self, id=None, contribution_types=None, contributor=None):
        return super().__init__(
            id=id,
            contribution_types=contribution_types,
            contributor=contributor,
        )
