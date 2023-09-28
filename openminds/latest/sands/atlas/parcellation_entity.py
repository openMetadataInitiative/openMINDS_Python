"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationEntity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ParcellationEntity"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "abbreviation",
            str,
            "vocab:abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this parcellation entity.",
        ),
        Property(
            "alternate_name",
            str,
            "vocab:alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any alternate names, including any alternative abbreviations, for this parcellation entity.",
        ),
        Property(
            "definition",
            str,
            "vocab:definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter the definition for this parcellation entity.",
        ),
        Property(
            "has_parent",
            "openminds.latest.sands.ParcellationEntity",
            "vocab:hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a parent object or legal person.",
            instructions="Add all anatomical parent structures for this parcellation entity as defined within the corrsponding brain atlas.",
        ),
        Property(
            "has_version",
            "openminds.latest.sands.ParcellationEntityVersion",
            "vocab:hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to variants of an original.",
            instructions="Add all versions of this parcellation entity.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this parcellation entity that may help you to find this instance more easily.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this parcellation entity.",
        ),
        Property(
            "ontology_identifier",
            str,
            "vocab:ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity.",
        ),
        Property(
            "related_uberon_term",
            ["openminds.latest.controlled_terms.Organ", "openminds.latest.controlled_terms.UBERONParcellation"],
            "vocab:relatedUBERONTerm",
            description="no description available",
            instructions="Add the related anatomical entity as defined by the UBERON ontology.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        alternate_name=None,
        definition=None,
        has_parent=None,
        has_version=None,
        lookup_label=None,
        name=None,
        ontology_identifier=None,
        related_uberon_term=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            alternate_name=alternate_name,
            definition=definition,
            has_parent=has_parent,
            has_version=has_version,
            lookup_label=lookup_label,
            name=name,
            ontology_identifier=ontology_identifier,
            related_uberon_term=related_uberon_term,
        )
