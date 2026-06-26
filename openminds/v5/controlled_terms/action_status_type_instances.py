# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.action_status_type import ActionStatusType


ActionStatusType.active = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/active",
    definition="An in-progress action.",
    name="active",
    preferred_ontology_identifier=IRI("https://schema.org/ActiveActionStatus"),
    synonyms=["active action status", "active action"],
)

ActionStatusType.completed = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/completed",
    definition="An action that has already taken place with a successful outcome.",
    name="completed",
    preferred_ontology_identifier=IRI("https://schema.org/CompletedActionStatus"),
    synonyms=["completed action status", "completed action", "finished successfully"],
)

ActionStatusType.failed = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/failed",
    definition="An action that failed to complete or completed but produced an error.",
    name="failed",
    preferred_ontology_identifier=IRI("https://schema.org/FailedActionStatus"),
    synonyms=["failed action status", "failed action", "finished unsuccessfully", "error"],
)

ActionStatusType.inactive = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/inactive",
    definition="A pending or suspended action.",
    name="inactive",
    synonyms=["inactive action status", "inactive action"],
)

ActionStatusType.paused = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/paused",
    definition="A temporarily stopped action that can be resumed at a later point in time.",
    name="paused",
    synonyms=["paused action type", "paused action", "suspended"],
)

ActionStatusType.pending = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/pending",
    definition="An action which is awaiting execution.",
    name="pending",
    synonyms=["queued", "pending action type", "pending action"],
)

ActionStatusType.potential = ActionStatusType(
    id="https://openminds.om-i.org/instances/actionStatusType/potential",
    definition="A description of an action that is supported.",
    name="potential",
    preferred_ontology_identifier=IRI("https://schema.org/PotentialActionStatus"),
    synonyms=["potential action type", "potential action"],
)
