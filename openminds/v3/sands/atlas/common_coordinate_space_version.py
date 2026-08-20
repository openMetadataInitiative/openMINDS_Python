"""
<description not available>
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateSpaceVersion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate space version.",
        ),
        Property(
            "accessibility",
            "openminds.v3.controlled_terms.ProductAccessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the common coordinate space version.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "anatomical_axes_orientation",
            "openminds.v3.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this common coordinate space version.",
        ),
        Property(
            "authors",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization", "openminds.v3.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space version as authors. Note that these authors will overwrite the author list provided for the overarching common coordinate space.",
        ),
        Property(
            "axes_origins",
            "openminds.v3.core.QuantitativeValue",
            "axesOrigin",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.",
            instructions="Enter the origin (central point where all axes intersect) of this common coordinate space version for two-dimensional spaces as [x, y] or for three-dimensional space as [x, y, z].",
        ),
        Property(
            "copyright",
            "openminds.v3.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "custodians",
            ["openminds.v3.core.Consortium", "openminds.v3.core.Organization", "openminds.v3.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.",
        ),
        Property(
            "default_images",
            "openminds.v3.core.File",
            "defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add all image files used as visual representation of this common coordinate space version.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the common coordinate space version.",
            instructions="Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v3.core.DOI", "openminds.v3.core.ISBN", "openminds.v3.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "full_documentation",
            [
                "openminds.v3.core.DOI",
                "openminds.v3.core.File",
                "openminds.v3.core.ISBN",
                "openminds.v3.core.WebResource",
            ],
            "fullDocumentation",
            required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the publication or file that acts as the full documentation of this research product version.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            description="Whole, non-abbreviated name of the common coordinate space version.",
            instructions="Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.",
        ),
        Property(
            "funding",
            "openminds.v3.core.Funding",
            "funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the common coordinate space version.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.v3.sands.CommonCoordinateSpaceVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all common coordinate space versions that can be used alternatively to this common coordinate space version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v3.sands.CommonCoordinateSpaceVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the common coordinate space version preceding this common coordinate space version.",
        ),
        Property(
            "keywords",
            [
                "openminds.v3.controlled_terms.ActionStatusType",
                "openminds.v3.controlled_terms.AgeCategory",
                "openminds.v3.controlled_terms.AnalysisTechnique",
                "openminds.v3.controlled_terms.AnatomicalAxesOrientation",
                "openminds.v3.controlled_terms.AnatomicalIdentificationType",
                "openminds.v3.controlled_terms.AnatomicalPlane",
                "openminds.v3.controlled_terms.AnnotationCriteriaType",
                "openminds.v3.controlled_terms.AnnotationType",
                "openminds.v3.controlled_terms.AtlasType",
                "openminds.v3.controlled_terms.AuditoryStimulusType",
                "openminds.v3.controlled_terms.BiologicalOrder",
                "openminds.v3.controlled_terms.BiologicalProcess",
                "openminds.v3.controlled_terms.BiologicalSex",
                "openminds.v3.controlled_terms.BreedingType",
                "openminds.v3.controlled_terms.CellCultureType",
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.ChemicalMixtureType",
                "openminds.v3.controlled_terms.Colormap",
                "openminds.v3.controlled_terms.ContributionType",
                "openminds.v3.controlled_terms.CranialWindowConstructionType",
                "openminds.v3.controlled_terms.CranialWindowReinforcementType",
                "openminds.v3.controlled_terms.CriteriaQualityType",
                "openminds.v3.controlled_terms.DataType",
                "openminds.v3.controlled_terms.DeviceType",
                "openminds.v3.controlled_terms.DifferenceMeasure",
                "openminds.v3.controlled_terms.Disease",
                "openminds.v3.controlled_terms.DiseaseModel",
                "openminds.v3.controlled_terms.EducationalLevel",
                "openminds.v3.controlled_terms.ElectricalStimulusType",
                "openminds.v3.controlled_terms.EthicsAssessment",
                "openminds.v3.controlled_terms.ExperimentalApproach",
                "openminds.v3.controlled_terms.FileBundleGrouping",
                "openminds.v3.controlled_terms.FileRepositoryType",
                "openminds.v3.controlled_terms.FileUsageRole",
                "openminds.v3.controlled_terms.GeneticStrainType",
                "openminds.v3.controlled_terms.GustatoryStimulusType",
                "openminds.v3.controlled_terms.Handedness",
                "openminds.v3.controlled_terms.Language",
                "openminds.v3.controlled_terms.Laterality",
                "openminds.v3.controlled_terms.LearningResourceType",
                "openminds.v3.controlled_terms.MRIPulseSequence",
                "openminds.v3.controlled_terms.MRIWeighting",
                "openminds.v3.controlled_terms.MeasuredQuantity",
                "openminds.v3.controlled_terms.MeasuredSignalType",
                "openminds.v3.controlled_terms.MetaDataModelType",
                "openminds.v3.controlled_terms.ModelAbstractionLevel",
                "openminds.v3.controlled_terms.ModelScope",
                "openminds.v3.controlled_terms.MolecularEntity",
                "openminds.v3.controlled_terms.OlfactoryStimulusType",
                "openminds.v3.controlled_terms.OperatingDevice",
                "openminds.v3.controlled_terms.OperatingSystem",
                "openminds.v3.controlled_terms.OpticalStimulusType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.OrganismSystem",
                "openminds.v3.controlled_terms.PatchClampVariation",
                "openminds.v3.controlled_terms.PreparationType",
                "openminds.v3.controlled_terms.ProductAccessibility",
                "openminds.v3.controlled_terms.ProgrammingLanguage",
                "openminds.v3.controlled_terms.QualitativeOverlap",
                "openminds.v3.controlled_terms.SemanticDataType",
                "openminds.v3.controlled_terms.Service",
                "openminds.v3.controlled_terms.SetupType",
                "openminds.v3.controlled_terms.SoftwareApplicationCategory",
                "openminds.v3.controlled_terms.SoftwareFeature",
                "openminds.v3.controlled_terms.Species",
                "openminds.v3.controlled_terms.StimulationApproach",
                "openminds.v3.controlled_terms.StimulationTechnique",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.SubjectAttribute",
                "openminds.v3.controlled_terms.TactileStimulusType",
                "openminds.v3.controlled_terms.Technique",
                "openminds.v3.controlled_terms.TermSuggestion",
                "openminds.v3.controlled_terms.Terminology",
                "openminds.v3.controlled_terms.TissueSampleAttribute",
                "openminds.v3.controlled_terms.TissueSampleType",
                "openminds.v3.controlled_terms.TypeOfUncertainty",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.controlled_terms.UnitOfMeasurement",
                "openminds.v3.controlled_terms.VisualStimulusType",
            ],
            "keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of the common coordinate space version.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.",
        ),
        Property(
            "license",
            "openminds.v3.core.License",
            "license",
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this common coordinate space version.",
        ),
        Property(
            "native_unit",
            "openminds.v3.controlled_terms.UnitOfMeasurement",
            "nativeUnit",
            required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this common coordinate space version.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the common coordinate space version registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space version.",
        ),
        Property(
            "other_contributions",
            "openminds.v3.core.Contribution",
            "otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.",
        ),
        Property(
            "related_publications",
            [
                "openminds.v3.core.DOI",
                "openminds.v3.core.HANDLE",
                "openminds.v3.core.ISBN",
                "openminds.v3.core.ISSN",
                "openminds.v3.publications.Book",
                "openminds.v3.publications.Chapter",
                "openminds.v3.publications.ScholarlyArticle",
            ],
            "relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).",
        ),
        Property(
            "release_date",
            date,
            "releaseDate",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.",
        ),
        Property(
            "repository",
            "openminds.v3.core.FileRepository",
            "repository",
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the common coordinate space version.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "support_channels",
            str,
            "supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which a user can receive support for handling this research product version.",
        ),
        Property(
            "used_specimens",
            [
                "openminds.v3.core.Subject",
                "openminds.v3.core.SubjectGroup",
                "openminds.v3.core.TissueSample",
                "openminds.v3.core.TissueSampleCollection",
            ],
            "usedSpecimen",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the specimen that was used for the creation of this common coordinate space version.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        accessibility=None,
        anatomical_axes_orientation=None,
        authors=None,
        axes_origins=None,
        copyright=None,
        custodians=None,
        default_images=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        keywords=None,
        license=None,
        native_unit=None,
        ontology_identifiers=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        used_specimens=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            accessibility=accessibility,
            anatomical_axes_orientation=anatomical_axes_orientation,
            authors=authors,
            axes_origins=axes_origins,
            copyright=copyright,
            custodians=custodians,
            default_images=default_images,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            keywords=keywords,
            license=license,
            native_unit=native_unit,
            ontology_identifiers=ontology_identifiers,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
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


from . import common_coordinate_space_version_instances as _  # noqa: F401
