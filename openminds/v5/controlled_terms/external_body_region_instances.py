# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.external_body_region import ExternalBodyRegion


ExternalBodyRegion.face = ExternalBodyRegion(
    id="https://openminds.om-i.org/instances/externalBodyRegion/face",
    definition="Is a subdivision of the head. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001456) ('is_a' and 'relationship')]",
    description="A subdivision of the head that has as parts the layers deep to the surface of the anterior surface, including the mouth, eyes, and nose (when present). In vertebrates, this includes the facial skeleton and structures superficial to the facial skeleton (cheeks, mouth, eyeballs, skin of face, etc). [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001456)]",
    name="face",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001456"),
)

ExternalBodyRegion.head = ExternalBodyRegion(
    id="https://openminds.om-i.org/instances/externalBodyRegion/head",
    definition="Is a subdivision of organism along the main body axis. Is part of the anterior region of the body and the craniocervical region. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000033) ('is_a' and 'relationship')]",
    description="The head is the anterior-most division of the body. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000033)]",
    name="head",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000033"),
    synonyms=["head (volume)"],
)

ExternalBodyRegion.neck = ExternalBodyRegion(
    id="https://openminds.om-i.org/instances/externalBodyRegion/neck",
    definition="Is a subdivision of organism connecting the head to the trunk. Is part of the anterior region of the body. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000974) ('is_a' and 'relationship')]",
    description="An organism subdivision that extends from the head to the pectoral girdle, encompassing the cervical vertebral column. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000974)]",
    name="neck",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000974"),
)
