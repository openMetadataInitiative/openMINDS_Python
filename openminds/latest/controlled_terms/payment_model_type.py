"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PaymentModelType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/PaymentModelType"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the payment model type.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the payment model type.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


PaymentModelType.allowance_overage_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/allowance-overagePaymentModel",
    definition="Payment includes an allowance of billable units (entitlement, consumption, event, monetary value, outcome, or capacity units), with charges for excess units.",
    name="allowance-overage payment model",
)
PaymentModelType.consumption_based_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/consumption-basedPaymentModel",
    definition="Payment is based on measured consumption units (e.g., data volume, compute time, storage space, network bandwidth).",
    name="consumption-based payment model",
)
PaymentModelType.fixed_recurring_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/fixed-recurringPaymentModel",
    definition="Time-recurring payment grants shared access, independent of billable units (entitlement, consumption, event, monetary value, outcome, or capacity units).",
    name="fixed-recurring payment model",
)
PaymentModelType.performance_based_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/performance-basedPaymentModel",
    definition="Payment is triggered by achievement of defined outcome units (e.g., qualified leads, completed projects, conversions, performance targets).",
    name="performance-based payment model",
)
PaymentModelType.retainer_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/retainerPaymentModel",
    definition="Time-recurring payment reserves dedicated capacity units (e.g., staff hours, server instances, support slots).",
    name="retainer payment model",
)
PaymentModelType.revenue_split_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/revenue-splitPaymentModel",
    definition="Payment is determined by dividing aggregated monetary value among participating parties according to predefined shares.",
    name="revenue-split payment model",
)
PaymentModelType.single_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/single-paymentModel",
    definition="Payment is made once for access, independent of any billable units (entitlement, consumption, event, monetary value, outcome, or capacity units).",
    name="single-payment model",
)
PaymentModelType.step_pricing_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/step-pricingPaymentModel",
    definition="Payment is determined by predefined thresholds of billable units (entitlement, consumption, event, monetary value, outcome, or capacity units).",
    name="step-pricing payment model",
)
PaymentModelType.take_rate_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/take-ratePaymentModel",
    definition="Payment is calculated as a fixed percentage of the monetary value of each user transaction, so the user pays more when transaction amounts increase and less when they decrease.",
    name="take-rate payment model",
)
PaymentModelType.transaction_based_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/transaction-basedPaymentModel",
    definition="Payment is based on counted event units (e.g., processing operations, message deliveries, document generations).",
    name="transaction-based payment model",
)
PaymentModelType.unit_based_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/unit-basedPaymentModel",
    definition="Payment is based on allocated entitlement units (e.g., users, licenses, devices, seats).",
    name="unit-based payment model",
)
PaymentModelType.zero_cost_payment_model = PaymentModelType(
    id="https://openminds.om-i.org/instances/paymentModelType/zero-costPaymentModel",
    definition="No payment is required for any billable units (entitlement, consumption, event, monetary value, outcome, or capacity units).",
    name="zero-cost payment model",
)
