"""
Structured information on an anatomical entity.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnatomicalEntity(LinkedMetadata):
    """
    Structured information on an anatomical entity.
    """

    type_ = "https://openminds.ebrains.eu/sands/AnatomicalEntity"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "has_parent",
            "openminds.v1.sands.AnatomicalEntity",
            "hasParent",
            description="Reference to a parent object or legal person.",
            instructions="Add another anatomical entity representing the anatomical parent structure of this anatomical entity.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this anatomical entity based on anatomical location or characteristics.",
        ),
        Property(
            "ontology_identifier",
            str,
            "ontologyIdentifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the ontological term matching this anatomical entity.",
        ),
        Property(
            "other_anatomical_relations",
            "openminds.v1.sands.AnatomicalEntityRelation",
            "otherAnatomicalRelation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a related anatomical structure.",
            instructions="Add one or several relations of this anatomical entity to other anatomical entities that are used elsewhere to describe (roughly) the same anatomical location.",
        ),
    ]

    def __init__(self, id=None, has_parent=None, name=None, ontology_identifier=None, other_anatomical_relations=None):
        return super().__init__(
            id=id,
            has_parent=has_parent,
            name=name,
            ontology_identifier=ontology_identifier,
            other_anatomical_relations=other_anatomical_relations,
        )
