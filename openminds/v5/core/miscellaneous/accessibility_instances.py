# this file was auto-generated!


from openminds.v5.controlled_terms.access_channel import AccessChannel

from openminds.v5.controlled_terms.access_eligibility_type import AccessEligibilityType

from openminds.v5.controlled_terms.access_form import AccessForm

from openminds.v5.controlled_terms.access_process_type import AccessProcessType

from openminds.v5.controlled_terms.payment_model_type import PaymentModelType

from openminds.v5.core.miscellaneous.accessibility import Accessibility


Accessibility.direct_physical_single_payment_model_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directPhysicalSingle-paymentModelControlledAccess",
    channel=AccessChannel.physical_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.single_payment_model],
    process=AccessProcessType.immediate_access,
)

Accessibility.direct_virtual_authenticated_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualAuthenticatedControlledAccess",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authenticated_access,
)

Accessibility.direct_virtual_authorized_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualAuthorizedControlledAccess",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authorized_access,
)

Accessibility.direct_virtual_open_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualOpenAccess",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.open_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.immediate_access,
)

Accessibility.mediated_virtual_authorized_restricted_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/mediatedVirtualAuthorizedRestrictedAccess",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.restricted_access,
    form=AccessForm.mediated_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authorized_access,
)
