"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateSpace(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommonCoordinateSpace"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate space.",
        ),
        Property(
            "authors",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space as authors.",
        ),
        Property(
            "custodians",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the common coordinate space.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v4.core.DOI", "openminds.v4.core.ISBN", "openminds.v4.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the common coordinate space.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_versions",
            "openminds.v4.sands.CommonCoordinateSpaceVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this common coordinate space.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the common coordinate space.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the common coordinate space registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the common coordinate space.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "used_species",
            "openminds.v4.controlled_terms.Species",
            "usedSpecies",
            required=True,
            description="no description available",
            instructions="Add the species that was used for the creation of this common coordinate space.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        authors=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_name=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifiers=None,
        short_name=None,
        used_species=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            authors=authors,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifiers=ontology_identifiers,
            short_name=short_name,
            used_species=used_species,
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


from . import common_coordinate_space_instances as _  # noqa: F401
