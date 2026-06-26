# this file was auto-generated!


from openminds.v5.controlled_terms.payment_model_type import PaymentModelType


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
