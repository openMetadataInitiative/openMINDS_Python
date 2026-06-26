# this file was auto-generated!


from openminds.latest.controlled_terms.access_eligibility_type import AccessEligibilityType


AccessEligibilityType.controlled_access = AccessEligibilityType(
    id="https://openminds.om-i.org/instances/accessEligibilityType/controlledAccess",
    definition="Access limited to registered and/or authenticated users meeting defined eligibility criteria.",
    name="controlled access",
)

AccessEligibilityType.open_access = AccessEligibilityType(
    id="https://openminds.om-i.org/instances/accessEligibilityType/openAccess",
    definition="Access without prior registration, authentication, or authorisation.",
    name="open access",
)

AccessEligibilityType.restricted_access = AccessEligibilityType(
    id="https://openminds.om-i.org/instances/accessEligibilityType/restrictedAccess",
    definition="Access limited to authenticated and specifically authorised users meeting enhanced legal, ethical, contractual, or governance requirements.",
    name="restricted access",
)
