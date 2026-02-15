"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Accessibility(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Accessibility"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "channel",
            "openminds.latest.controlled_terms.AccessChannel",
            "channel",
            required=True,
            description="no description available",
            instructions="Add the relevant access channel indicating where access takes place (physical, virtual, or hybrid).",
        ),
        Property(
            "eligibility",
            "openminds.latest.controlled_terms.AccessEligibilityType",
            "eligibility",
            required=True,
            description="no description available",
            instructions="Add the relevant access eligibility type indicating who is allowed to access (open, controlled, or restricted).",
        ),
        Property(
            "form",
            "openminds.latest.controlled_terms.AccessForm",
            "form",
            required=True,
            description="no description available",
            instructions="Add the relevant access form indicating whether the user interacts directly or through mediation.",
        ),
        Property(
            "payment_models",
            "openminds.latest.controlled_terms.PaymentModelType",
            "paymentModel",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all relevant payment model types indicating how access costs are determined. If no payment is requires, select zero-cost payment model.",
        ),
        Property(
            "process",
            "openminds.latest.controlled_terms.AccessProcessType",
            "process",
            required=True,
            description="no description available",
            instructions="Add the relevant access process type indicating how access is granted (immediate, registered, authenticated, or authorized).",
        ),
    ]

    def __init__(self, id=None, channel=None, eligibility=None, form=None, payment_models=None, process=None):
        return super().__init__(
            id=id,
            channel=channel,
            eligibility=eligibility,
            form=form,
            payment_models=payment_models,
            process=process,
        )
