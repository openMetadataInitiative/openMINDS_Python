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

    type_ = "https://openminds.om-i.org/types/ParcellationEntity"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this parcellation entity.",
        ),
        Property(
            "alternate_names",
            str,
            "alternateName",
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
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter the definition for this parcellation entity.",
        ),
        Property(
            "has_parents",
            "openminds.latest.sands.ParcellationEntity",
            "hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a parent object or legal person.",
            instructions="Add all anatomical parent structures for this parcellation entity as defined within the corresponding brain atlas.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter a lookup label for this parcellation entity that may help you to find this instance more easily.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the parcellation entity.",
            instructions="Enter the name of this parcellation entity.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the parcellation entity registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity.",
        ),
        Property(
            "related_interspecies_anatomy",
            [
                "openminds.latest.controlled_terms.AnatomicalCavity",
                "openminds.latest.controlled_terms.ExternalBodyRegion",
                "openminds.latest.controlled_terms.MuscularStructure",
                "openminds.latest.controlled_terms.NervousSystemStructure",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganSystemStructure",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.SkeletalStructure",
                "openminds.latest.controlled_terms.TissueStructure",
                "openminds.latest.controlled_terms.VascularStructure",
            ],
            "relatedInterspeciesAnatomy",
            description="no description available",
            instructions="Add the corresponding cross-species anatomical entity from the UBERON-derived terminologies that represents the generic anatomical concept underlying the atlas parcellation entity.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        alternate_names=None,
        definition=None,
        has_parents=None,
        lookup_label=None,
        name=None,
        ontology_identifiers=None,
        related_interspecies_anatomy=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            alternate_names=alternate_names,
            definition=definition,
            has_parents=has_parents,
            lookup_label=lookup_label,
            name=name,
            ontology_identifiers=ontology_identifiers,
            related_interspecies_anatomy=related_interspecies_anatomy,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
        case_sensitive: bool = True,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default), "contains"
                (the name-like property contains the given string), or "within"
                (the given string contains the name-like property).
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
            case_sensitive (bool, optional): Whether the search should be case-sensitive. Defaults to True.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    value = getattr(instance, prop_name, None)
                    if value is not None:
                        keys.append(value)
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]

        def normalize(s):
            return s if case_sensitive else s.casefold()

        if match == "equals":
            if case_sensitive:
                matches = cls._instance_lookup.get(name, [])
            else:
                matches = []
                for key, instances in cls._instance_lookup.items():
                    if key.casefold() == name.casefold():
                        matches.extend(instances)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(name) in normalize(key):
                    matches.extend(instances)
        elif match == "within":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(key) in normalize(name):
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals', 'contains', or 'within'")
        if not matches:
            return None
        elif all:
            return list(dict.fromkeys(matches))
        else:
            return matches[0]


from . import parcellation_entity_instances as _  # noqa: F401
