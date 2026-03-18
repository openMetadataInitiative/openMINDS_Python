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

    type_ = "https://openminds.om-i.org/types/Contribution"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "contributors",
            ["openminds.v5.core.Consortium", "openminds.v5.core.Organization", "openminds.v5.core.Person"],
            "contributor",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person that gave or supplied something as a part or share.",
            instructions="Add all contributors who made this contribution, in the desired display order.",
        ),
        Property(
            "type",
            "openminds.v5.controlled_terms.ContributionType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of contribution.",
        ),
    ]

    def __init__(self, contributors=None, type=None):
        return super().__init__(
            contributors=contributors,
            type=type,
        )
