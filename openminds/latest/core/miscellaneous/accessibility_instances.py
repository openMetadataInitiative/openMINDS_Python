# this file was auto-generated!


from openminds.latest.controlled_terms.access_channel import AccessChannel

from openminds.latest.controlled_terms.access_eligibility_type import AccessEligibilityType

from openminds.latest.controlled_terms.access_form import AccessForm

from openminds.latest.controlled_terms.access_process_type import AccessProcessType

from openminds.latest.controlled_terms.payment_model_type import PaymentModelType

from openminds.latest.core.miscellaneous.accessibility import Accessibility


Accessibility.direct_physical_single_payment_model_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directPhysicalSingle-paymentModelControlledAccess",
    application="Select when a physical research product can be obtained or used directly after a single payment, without prior registration, authentication, or a separate authorization procedure. Example: purchasing a printed book or another tangible research product for a one-time price.",
    channel=AccessChannel.physical_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.single_payment_model],
    process=AccessProcessType.immediate_access,
)

Accessibility.direct_virtual_authenticated_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualAuthenticatedControlledAccess",
    application="Select when a research product can be accessed directly online at no cost by users whose identity, account, affiliation, or other qualifying status has been authenticated. No separate authorization decision is required. Example: access through an authenticated institutional account or single sign-on.",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authenticated_access,
)

Accessibility.direct_virtual_authorized_controlled_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualAuthorizedControlledAccess",
    application="Select when a research product can be accessed directly online at no cost only by users who have been authenticated and explicitly authorized under defined access conditions. Example: access granted by a project owner or repository administrator to approved project members.",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.controlled_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authorized_access,
)

Accessibility.direct_virtual_open_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/directVirtualOpenAccess",
    application="Select when anyone can access the research product directly online at no cost, without registration, authentication, authorization, or mediation. Example: an openly available publication, dataset, software package, or downloadable research file.",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.open_access,
    form=AccessForm.direct_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.immediate_access,
)

Accessibility.mediated_virtual_authorized_restricted_access = Accessibility(
    id="https://openminds.om-i.org/instances/accessibilities/mediatedVirtualAuthorizedRestrictedAccess",
    application="Select when a research product is available online at no cost only to authenticated and explicitly authorized users who satisfy enhanced legal, ethical, contractual, security, or governance requirements, and when access must be facilitated, prepared, delivered, or supervised by an intermediary. Example: an approved researcher receiving a curated data extract, using a managed analysis service, or accessing sensitive data through a supervised process.",
    channel=AccessChannel.virtual_access,
    eligibility=AccessEligibilityType.restricted_access,
    form=AccessForm.mediated_access,
    payment_models=[PaymentModelType.zero_cost_payment_model],
    process=AccessProcessType.authorized_access,
)
