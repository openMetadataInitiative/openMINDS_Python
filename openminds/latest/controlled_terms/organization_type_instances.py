# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.organization_type import OrganizationType


OrganizationType.legal_entity = OrganizationType(
    id="https://openminds.om-i.org/instances/organizationType/legalEntity",
    definition="An organization classified as a type of legal entity recognized within a specific legal system.",
    name="legal entity",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q10541491"),
)

OrganizationType.organizational_unit = OrganizationType(
    id="https://openminds.om-i.org/instances/organizationType/organizationalUnit",
    definition="A distinct unit within a larger organization.",
    name="organizational unit",
)
