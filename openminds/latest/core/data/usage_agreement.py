"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class UsageAgreement(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/UsageAgreement"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "authoring_partys",
            ["openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "authoringParty",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all natural persons and legal entities (in display order) responsible for creating and establishing this usage agreement.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the usage agreement.",
            instructions="Enter the full name of this usage agreement.",
        ),
        Property(
            "jurisdiction",
            [
                "openminds.latest.controlled_terms.SovereignState",
                "openminds.latest.controlled_terms.SupranationalBody",
            ],
            "jurisdiction",
            required=True,
            description="no description available",
            instructions="Enter the jurisdiction in which this usage agreement was issued.",
        ),
        Property(
            "modification_profiles",
            [
                "openminds.latest.controlled_terms.ModificationConsentRequirement",
                "openminds.latest.controlled_terms.ModificationConstraint",
                "openminds.latest.controlled_terms.ModificationForm",
                "openminds.latest.controlled_terms.ModificationScope",
            ],
            "modificationProfile",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all the types of modifications that are allowed under this usage agreement.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the usage agreement.",
            instructions="Enter a short name (or alias) for this usage agreement that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "sources",
            ["openminds.latest.core.License", "openminds.latest.core.UsageAgreement"],
            "source",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all licenses or usage agreements that served as references in the creation of this usage agreement.",
        ),
        Property(
            "support_channels",
            str,
            "supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which users can obtain support and initiate negotiations regarding this usage agreement with the authoring party.",
        ),
        Property(
            "template",
            "openminds.latest.core.WebResource",
            "template",
            required=True,
            description="no description available",
            instructions="Add the web resource that supplies the template for this usage agreement.",
        ),
    ]

    def __init__(
        self,
        id=None,
        authoring_partys=None,
        full_name=None,
        jurisdiction=None,
        modification_profiles=None,
        short_name=None,
        sources=None,
        support_channels=None,
        template=None,
    ):
        return super().__init__(
            id=id,
            authoring_partys=authoring_partys,
            full_name=full_name,
            jurisdiction=jurisdiction,
            modification_profiles=modification_profiles,
            short_name=short_name,
            sources=sources,
            support_channels=support_channels,
            template=template,
        )
