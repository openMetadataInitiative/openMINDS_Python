# this file was auto-generated!


from openminds.v5.controlled_terms.access_process_type import AccessProcessType


AccessProcessType.authenticated_access = AccessProcessType(
    id="https://openminds.om-i.org/instances/accessProcessType/authenticatedAccess",
    definition="Access following authentication through an account.",
    name="authenticated access",
)

AccessProcessType.authorized_access = AccessProcessType(
    id="https://openminds.om-i.org/instances/accessProcessType/authorizedAccess",
    definition="Access granted following an explicit authorisation decision based on assessment of the access request and, where applicable, acceptance or negotiation of relevant usage conditions.",
    name="authorized access",
)

AccessProcessType.immediate_access = AccessProcessType(
    id="https://openminds.om-i.org/instances/accessProcessType/immediateAccess",
    definition="Automatic access upon acceptance of the applicable terms.",
    name="immediate access",
)

AccessProcessType.registered_access = AccessProcessType(
    id="https://openminds.om-i.org/instances/accessProcessType/registeredAccess",
    definition="Access requires registration but no authentication.",
    name="registered access",
)
