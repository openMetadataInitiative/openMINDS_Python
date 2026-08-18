"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BrainAtlas(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlas"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this brain atlas.",
        ),
        Property(
            "authors",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization", "openminds.v3.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this brain atlas as authors.",
        ),
        Property(
            "custodians",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization", "openminds.v3.core.Person"],
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
            description="Longer statement or account giving the characteristics of the brain atlas.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v3.core.DOI", "openminds.v3.core.ISBN", "openminds.v3.core.RRID"],
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
            description="Whole, non-abbreviated name of the brain atlas.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_terminology",
            "openminds.v3.sands.ParcellationTerminology",
            "hasTerminology",
            required=True,
            description="no description available",
            instructions="Enter the parcellation terminology of this brain atlas.",
        ),
        Property(
            "has_versions",
            "openminds.v3.sands.BrainAtlasVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add versions of this brain atlas.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the brain atlas.",
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
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify the brain atlas registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) to the related ontological term matching this brain atlas.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the brain atlas.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "used_species",
            "openminds.v3.controlled_terms.Species",
            "usedSpecies",
            description="no description available",
            instructions="Add the species that was used for the creation of this brain atlas.",
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
        has_terminology=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifier=None,
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
            has_terminology=has_terminology,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifier=ontology_identifier,
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


from . import brain_atlas_instances as _  # noqa: F401
