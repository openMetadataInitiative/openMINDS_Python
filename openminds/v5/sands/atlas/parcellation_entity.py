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
    schema_version = "v5.0"

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
            "openminds.v5.sands.ParcellationEntity",
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
                "openminds.v5.controlled_terms.AnatomicalCavity",
                "openminds.v5.controlled_terms.ExternalBodyRegion",
                "openminds.v5.controlled_terms.MuscularStructure",
                "openminds.v5.controlled_terms.NervousSystemStructure",
                "openminds.v5.controlled_terms.Organ",
                "openminds.v5.controlled_terms.OrganSystemStructure",
                "openminds.v5.controlled_terms.OrganismSubstance",
                "openminds.v5.controlled_terms.OrganismSystem",
                "openminds.v5.controlled_terms.SkeletalStructure",
                "openminds.v5.controlled_terms.TissueStructure",
                "openminds.v5.controlled_terms.VascularStructure",
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
        ignore_accents: bool = False,
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
            ignore_accents (bool, optional): Whether to ignore accents (acute, grave, circumflex) and
                other diacritical marks (cedilla, tilde, ring, etc.) when matching. Also treat
                special letters (ß, œ, æ, ø, ł, etc.) as their closest plain-letter equivalents
                (e.g. "ß" as "ss"). Defaults to False.
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

        def remove_accents(s):
            import unicodedata

            special = str.maketrans(
                {
                    "Ł": "L",
                    "ł": "l",
                    "Ø": "O",
                    "ø": "o",
                    "Đ": "D",
                    "đ": "d",
                    "Ð": "D",
                    "ð": "d",
                    "Þ": "Th",
                    "þ": "th",
                    "Æ": "AE",
                    "æ": "ae",
                    "Œ": "OE",
                    "œ": "oe",
                    "ß": "ss",
                    "ẞ": "SS",
                    "Ə": "E",
                    "ə": "e",
                    "ı": "i",
                }
            )
            nfd_form = unicodedata.normalize("NFD", s)
            stripped = "".join(c for c in nfd_form if not unicodedata.combining(c))
            return stripped.translate(special)

        def normalize(s):
            if not case_sensitive:
                s = s.casefold()
            if ignore_accents:
                s = remove_accents(s)
            return s

        if match == "equals":
            if case_sensitive and not ignore_accents:
                matches = cls._instance_lookup.get(name, [])
            else:
                matches = []
                for key, instances in cls._instance_lookup.items():
                    if normalize(key) == normalize(name):
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
