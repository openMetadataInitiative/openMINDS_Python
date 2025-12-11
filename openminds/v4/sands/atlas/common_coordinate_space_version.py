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

    type_ = "https://openminds.om-i.org/types/CommonCoordinateSpaceVersion"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
            "openminds.v4.controlled_terms.ProductAccessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the common coordinate space version.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "anatomical_axes_orientation",
            "openminds.v4.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this common coordinate space version.",
        ),
        Property(
            "authors",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space version as authors. Note that these authors will overwrite the author list provided for the overarching common coordinate space.",
        ),
        Property(
            "axes_origins",
            "openminds.v4.core.QuantitativeValue",
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
            "openminds.v4.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "custodians",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.",
        ),
        Property(
            "default_images",
            "openminds.v4.core.File",
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
            ["openminds.v4.core.DOI", "openminds.v4.core.ISBN", "openminds.v4.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "full_documentation",
            [
                "openminds.v4.core.DOI",
                "openminds.v4.core.File",
                "openminds.v4.core.ISBN",
                "openminds.v4.core.WebResource",
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
            "openminds.v4.core.Funding",
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
            "openminds.v4.sands.CommonCoordinateSpaceVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all common coordinate space versions that can be used alternatively to this common coordinate space version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v4.sands.CommonCoordinateSpaceVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the common coordinate space version preceding this common coordinate space version.",
        ),
        Property(
            "keywords",
            [
                "openminds.v4.controlled_terms.ActionStatusType",
                "openminds.v4.controlled_terms.AgeCategory",
                "openminds.v4.controlled_terms.AnalysisTechnique",
                "openminds.v4.controlled_terms.AnatomicalAxesOrientation",
                "openminds.v4.controlled_terms.AnatomicalIdentificationType",
                "openminds.v4.controlled_terms.AnatomicalPlane",
                "openminds.v4.controlled_terms.AnnotationCriteriaType",
                "openminds.v4.controlled_terms.AnnotationType",
                "openminds.v4.controlled_terms.AtlasType",
                "openminds.v4.controlled_terms.AuditoryStimulusType",
                "openminds.v4.controlled_terms.BiologicalOrder",
                "openminds.v4.controlled_terms.BiologicalProcess",
                "openminds.v4.controlled_terms.BiologicalSex",
                "openminds.v4.controlled_terms.BreedingType",
                "openminds.v4.controlled_terms.CellCultureType",
                "openminds.v4.controlled_terms.CellType",
                "openminds.v4.controlled_terms.ChemicalMixtureType",
                "openminds.v4.controlled_terms.Colormap",
                "openminds.v4.controlled_terms.ContributionType",
                "openminds.v4.controlled_terms.CranialWindowConstructionType",
                "openminds.v4.controlled_terms.CranialWindowReinforcementType",
                "openminds.v4.controlled_terms.CriteriaQualityType",
                "openminds.v4.controlled_terms.DataType",
                "openminds.v4.controlled_terms.DeviceType",
                "openminds.v4.controlled_terms.DifferenceMeasure",
                "openminds.v4.controlled_terms.Disease",
                "openminds.v4.controlled_terms.DiseaseModel",
                "openminds.v4.controlled_terms.EducationalLevel",
                "openminds.v4.controlled_terms.ElectricalStimulusType",
                "openminds.v4.controlled_terms.EthicsAssessment",
                "openminds.v4.controlled_terms.ExperimentalApproach",
                "openminds.v4.controlled_terms.FileBundleGrouping",
                "openminds.v4.controlled_terms.FileRepositoryType",
                "openminds.v4.controlled_terms.FileUsageRole",
                "openminds.v4.controlled_terms.GeneticStrainType",
                "openminds.v4.controlled_terms.GustatoryStimulusType",
                "openminds.v4.controlled_terms.Handedness",
                "openminds.v4.controlled_terms.Language",
                "openminds.v4.controlled_terms.Laterality",
                "openminds.v4.controlled_terms.LearningResourceType",
                "openminds.v4.controlled_terms.MRIPulseSequence",
                "openminds.v4.controlled_terms.MRIWeighting",
                "openminds.v4.controlled_terms.MeasuredQuantity",
                "openminds.v4.controlled_terms.MeasuredSignalType",
                "openminds.v4.controlled_terms.MetaDataModelType",
                "openminds.v4.controlled_terms.ModelAbstractionLevel",
                "openminds.v4.controlled_terms.ModelScope",
                "openminds.v4.controlled_terms.MolecularEntity",
                "openminds.v4.controlled_terms.OlfactoryStimulusType",
                "openminds.v4.controlled_terms.OperatingDevice",
                "openminds.v4.controlled_terms.OperatingSystem",
                "openminds.v4.controlled_terms.OpticalStimulusType",
                "openminds.v4.controlled_terms.Organ",
                "openminds.v4.controlled_terms.OrganismSubstance",
                "openminds.v4.controlled_terms.OrganismSystem",
                "openminds.v4.controlled_terms.PatchClampVariation",
                "openminds.v4.controlled_terms.PreparationType",
                "openminds.v4.controlled_terms.ProductAccessibility",
                "openminds.v4.controlled_terms.ProgrammingLanguage",
                "openminds.v4.controlled_terms.QualitativeOverlap",
                "openminds.v4.controlled_terms.SemanticDataType",
                "openminds.v4.controlled_terms.Service",
                "openminds.v4.controlled_terms.SetupType",
                "openminds.v4.controlled_terms.SoftwareApplicationCategory",
                "openminds.v4.controlled_terms.SoftwareFeature",
                "openminds.v4.controlled_terms.Species",
                "openminds.v4.controlled_terms.StimulationApproach",
                "openminds.v4.controlled_terms.StimulationTechnique",
                "openminds.v4.controlled_terms.SubcellularEntity",
                "openminds.v4.controlled_terms.SubjectAttribute",
                "openminds.v4.controlled_terms.TactileStimulusType",
                "openminds.v4.controlled_terms.Technique",
                "openminds.v4.controlled_terms.TermSuggestion",
                "openminds.v4.controlled_terms.Terminology",
                "openminds.v4.controlled_terms.TissueSampleAttribute",
                "openminds.v4.controlled_terms.TissueSampleType",
                "openminds.v4.controlled_terms.TypeOfUncertainty",
                "openminds.v4.controlled_terms.UBERONParcellation",
                "openminds.v4.controlled_terms.UnitOfMeasurement",
                "openminds.v4.controlled_terms.VisualStimulusType",
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
            "openminds.v4.core.License",
            "license",
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this common coordinate space version.",
        ),
        Property(
            "native_unit",
            "openminds.v4.controlled_terms.UnitOfMeasurement",
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
            "openminds.v4.core.Contribution",
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
                "openminds.v4.core.DOI",
                "openminds.v4.core.HANDLE",
                "openminds.v4.core.ISBN",
                "openminds.v4.core.ISSN",
                "openminds.v4.publications.Book",
                "openminds.v4.publications.Chapter",
                "openminds.v4.publications.ScholarlyArticle",
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
            "openminds.v4.core.FileRepository",
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
                "openminds.v4.core.Subject",
                "openminds.v4.core.SubjectGroup",
                "openminds.v4.core.TissueSample",
                "openminds.v4.core.TissueSampleCollection",
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
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


CommonCoordinateSpaceVersion.amb_ccf_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v1",
    abbreviation="AMB CCF",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/PIR"},
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Lein E, Hawrylycz M, Ao N, et al.; 'Genome-wide atlas of gene expression in the adult mouse brain.'; Nature; Jan 2007; 445(7124):168–176. [doi: 10.1038/nature05453](https://doi.org/10.1038/nature05453)",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    short_name="Allen Mouse Brain CCF",
    version_identifier="v1",
    version_innovation="The first version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv1) is a 3D reconstruction of one brain hemisphere at 200µm resolution.",
)
CommonCoordinateSpaceVersion.amb_ccf_v2 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v2",
    abbreviation="AMB CCF",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/PIR"},
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Oh S, Harris J, Ng L, et al.; 'A mesoscale connectome of the mouse brain.'; Nature; Apr 2014; 508(7495):207–214. [doi: 10.1038/nature13186](https://doi.org/10.1038/nature13186)",
    is_new_version_of={"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v1"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    short_name="Allen Mouse Brain CCF",
    version_identifier="v2",
    version_innovation="The second version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv2) is a 3D reconstruction of a whole brain at 100µm resolution.",
)
CommonCoordinateSpaceVersion.amb_ccf_v3 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3",
    abbreviation="AMB CCF",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/PIR"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
    ],
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Wang Q, Ding S-L, Li Y, et al.; 'The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas.'; Cell; May 2020; 181(4):936-953.e20. [doi: 10.1016/j.cell.2020.04.007](https://doi.org/10.1016/j.cell.2020.04.007)",
    is_alternative_version_of=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3-RAS"}
    ],
    is_new_version_of={"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v2"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    release_date="2015-05-01",
    short_name="Allen Mouse Brain CCF",
    version_identifier="v3",
    version_innovation="The third version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv3) is a 3D reconstruction of a whole brain at 10µm resolution.",
)
CommonCoordinateSpaceVersion.amb_ccf_v3_ras = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3-RAS",
    abbreviation="AMB CCF",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 0.0},
    ],
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Wang Q, Ding S-L, Li Y, et al.; 'The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas.'; Cell; May 2020; 181(4):936-953.e20. [doi: 10.1016/j.cell.2020.04.007](https://doi.org/10.1016/j.cell.2020.04.007)",
    is_alternative_version_of=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3"}
    ],
    is_new_version_of={"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v2"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    release_date="2015-05-01",
    short_name="Allen Mouse Brain CCF",
    version_identifier="v3-RAS",
    version_innovation="The third version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv3-RAS) is a 3D reconstruction of a whole brain at 10µm resolution. This alternative CCFv3 version was transformed to RAS axes orientation.",
)
CommonCoordinateSpaceVersion.big_brain_2015 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/BigBrain_2015",
    abbreviation="BigBrain",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 3338.5795590551184},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 3500.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 2776.899244094488},
    ],
    custodians=[
        {"@id": "https://openminds.om-i.org/instances/person/evansAlanC"},
        {"@id": "https://openminds.om-i.org/instances/person/amuntsKatrin"},
    ],
    full_name="BigBrain Whole-Brain Model",
    homepage=IRI("https://bigbrainproject.org/"),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    release_date="2013-06-21",
    short_name="BigBrain Model",
    version_identifier="2015",
    version_innovation="The 'BigBrain Whole-Brain Model' (2015) is an ultrahigh-resolution three-dimensional (3D) model of a brain from a male human subject, deceased at the age of 65 years, at nearly cellular resolution of 20 micrometers. The model is based on a full 3D reconstruction from digital scans of 7404 histological coronal sections, which were stained for cell bodies.",
)
CommonCoordinateSpaceVersion.fs_lr_164k = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsLR_164k",
    abbreviation="fsLR",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="fsLR Surface Space",
    version_identifier="164k",
    version_innovation="This fsLR Surface Space version has about 163842 (164k) vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fs_lr_32k = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsLR_32k",
    abbreviation="fsLR",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="fsLR Surface Space",
    version_identifier="32k",
    version_innovation="This fsLR Surface Space version has about 32492 (32k) vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fsaverage_3 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_3",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="FsAverage Surface Space",
    version_identifier="3",
    version_innovation="This FsAverage Surface Space version has about 1k vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fsaverage_4 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_4",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="FsAverage Surface Space",
    version_identifier="4",
    version_innovation="This FsAverage Surface Space version has about 3k vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fsaverage_5 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_5",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="FsAverage Surface Space",
    version_identifier="5",
    version_innovation="This FsAverage Surface Space version has about 10k vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fsaverage_6 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_6",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="FsAverage Surface Space",
    version_identifier="6",
    version_innovation="This FsAverage Surface Space version has about 41k vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.fsaverage_7 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_7",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    short_name="FsAverage Surface Space",
    version_identifier="7",
    version_innovation="This FsAverage Surface Space version has about 164k vertices per hemisphere.",
)
CommonCoordinateSpaceVersion.marmoset_nmt_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1",
    abbreviation="MarmosetNMT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/LPI"},
    description="The Nencki-Monash (NM) template v1.0 (2020) represents a computational morphological average of selected gender-balanced young adult brains of the Common Marmoset monkey (Callithrix jacchus), derived from 3D reconstructions based on Nissl-stained serial sections.",
    full_documentation={"@id": "https://www.marmosetbrain.org/nencki_monash_template/"},
    full_name="The Marmoset Nencki-Monash Template in Stereotaxic Coordinates",
    homepage=IRI("https://www.marmosetbrain.org/nencki_monash_template"),
    how_to_cite="Majka, P., Bednarek, S., Chan, J. M., Jermakow, N., Liu, C., Saworska, G., Worthy, K. H., Silva, A. C., Wójcik, D. K., & Rosa, M. G. P. (2021). Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas. NeuroImage, 226, 117625. https://doi.org/10.1016/j.neuroimage.2020.117625.",
    license={"@id": "https://openminds.om-i.org/instances/licenses/CC-BY-4.0"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    related_publications=[{"@id": "https://doi.org/10.1016/j.neuroimage.2020.117625"}],
    release_date="2021-02-01",
    short_name="Marmoset Nencki-Monash Template",
    version_identifier="v1",
    version_innovation="This is the first version of average histology.",
)
CommonCoordinateSpaceVersion.mebrain_stemplate_v1_0 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MEBRAINStemplate_v1.0",
    abbreviation="MEBRAINStemplate",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 108.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 128.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 70.0},
    ],
    full_name="MEBRAINS population-based monkey brain template",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    short_name="MEBRAINS brain template",
    version_identifier="v1.0",
    version_innovation="The first version of the 'MEBRAINS population-based monkey brain template' (v1.0) is a population average brain of T1- and T2-weighted MRI scans from 10 macaque brains. In addition, 9 CT scans of the same monkeys (one missing) are registered to the T1 modality and co-registered to the population average.",
)
CommonCoordinateSpaceVersion.mni__colin27_1998 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-Colin27_1998",
    abbreviation="MNI-Colin27",
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 75.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 111.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 67.0},
    ],
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    is_alternative_version_of=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-Colin27_2008"}
    ],
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="1998-06-01",
    short_name="MNI Colin27 Average Brain",
    version_identifier="1998",
)
CommonCoordinateSpaceVersion.mni__colin27_2008 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-Colin27_2008",
    abbreviation="MNI-Colin27",
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    is_alternative_version_of=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNIColin27_1998"}
    ],
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2006-08-01",
    short_name="MNI Colin27 Average Brain",
    version_identifier="2008",
)
CommonCoordinateSpaceVersion.mni_icbm152_linear_2001_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_linear-2001-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152lin"),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2001 linear symmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009a_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-asym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009a nonlinear asymmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009a_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009a nonlinear symmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009b_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-asym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009b nonlinear asymmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009b_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009b nonlinear symmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009c_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-asym",
    abbreviation="ICBM152",
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 96.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 132.0},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 78.0},
    ],
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009c nonlinear asymmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009c_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009c nonlinear symmetric",
)
CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_6_g_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-6G-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear"),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="nonlinear 6th generation symmetric",
)
CommonCoordinateSpaceVersion.p__marmoset_bsc_cor_t_v2012__interaural_lsa = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/P-MarmosetBSC-corT_v2012-Interaural-LSA",
    abbreviation="P-MarmosetBSC-corT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/LSA"},
    description="This coordinate space of the coronal plates from Paxinos et al. 'Marmoset Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the marmoset brain could not be determined from the information provided in the atlas publication. This coordinate space has LSA orientation (X, Y, Z axes are oriented towards left, superior and anterior, respectively). This was obtained by combining information provided in the pdf version of the 1st edition: (1) 'In the common marmoset, the horizontal zero plane is defined as the plane passing thorough the lower margin of the orbit and the center of the external auditory meatus (Figure B). The anteroposterior zero plane is defined as the plane perpendicular to the horizontal zero plane which passes the centers of the external auditory meati. The left-right zero plane is the midsagittal plane [...].' (quoted from chapter 'Introduction', subsection 'Histology', page IX). (2) Based on Figure C (chapter 'Introduction', subsection 'Histology', page X), the fiducial marks were made on the right hemisphere of the marmoset brain. These are visible in some of the photographic plates (e.g., Figure 187a) identifying the left hemisphere as delineated one. Thus, the coordinate system is oriented towards the left since the marmoset's left hemisphere has been used to draw the atlas. A pdf version of the atlas can be accessed from https://r.marmosetbrain.org/Atlas+Small.pdf or https://www.researchgate.net/publication/335871101_PDF_of_The_Marmoset_Brain_in_Stereotaxic_Coordinates.",
    full_documentation={"@id": "https://openminds.om-i.org/instances/ISBN/978-0-12-415818-4"},
    full_name="Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates",
    homepage=IRI("http://www.neura.edu.au/research/themes/paxinos-group"),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2011-10-11",
    short_name="Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)",
    version_identifier="v2012 (Interaural, LSA)",
    version_innovation="This is the first version of this stereotaxic coordinate system.",
)
CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__bregma_lia = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-LIA",
    abbreviation="PW-RBSC-corT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/paidAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/LIA"},
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses Bregma as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the left, inferior, anterior (positive mediolateral values describe the rat's left hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.om-i.org/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Bregma, LIA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)
CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__bregma_ria = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-RIA",
    abbreviation="PW-RBSC-corT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/paidAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RIA"},
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses Bregma as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the right, anterior, inferior (positive mediolateral values describe the rat's right hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.om-i.org/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Bregma, RIA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)
CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__interaural_lsa = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-LSA",
    abbreviation="PW-RBSC-corT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/paidAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/LSA"},
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the left, superior, anterior (positive mediolateral values describe the rat's left hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.om-i.org/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Interaural, LSA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)
CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__interaural_rsa = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-RSA",
    abbreviation="PW-RBSC-corT",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/paidAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RSA"},
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the right, superior, anterior (positive mediolateral values describe the rat's right hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.om-i.org/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Interaural, RSA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)
CommonCoordinateSpaceVersion.swanson_srb_v1992 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/SwansonSRB_v1992",
    abbreviation="SwansonSRB",
    accessibility={"@id": "https://openminds.om-i.org/instances/productAccessibility/freeAccess"},
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RIA"},
    axes_origins=[
        {
            "@type": "https://openminds.om-i.org/types/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
            "value": 0,
        },
        {
            "@type": "https://openminds.om-i.org/types/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
            "value": 12,
        },
        {
            "@type": "https://openminds.om-i.org/types/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
            "value": 8.11,
        },
    ],
    description="The coordinate space of Swanson’s ‘Brain Maps: Structure of the Rat Brain’ uses Bregma as its origin. The coordinates stated under ‘axesOrigin’ are the coordinates of the origin in the physical coordinate system of the rat brain. The coordinates, AP = 8.11 mm, DV = 12 mm and ML = 0 mm, were obtained by combining the information provided in the physical book and the pdf version of the 3rd edition of Brain Maps: (1) 'In the physical coordinate system, the z axis begins (= 0) at the rostral tip of the olfactory bulb, the y axis begins along an imaginary line that corresponds approximately to a surface that the extracted brain is lying upon, and the x axis begins at the midline.' (quoted from chapter [‘B. Coordinate Systems: Stereotaxic Surgery and Databases’ of the 3rd edition of Brain Maps (pdf version from Swanson’s homepage)](http://larrywswanson.com/wp-content/uploads/2015/03/2-Atlas-prep-BrainMaps3-20041.pdf)). (2) 'The rostrocaudal coordinate is given in parentheses after the corresponding physical coordinates, and the other two (dorsoventral and mediolateral) can be obtained with the transparent overlay provided in Appendix B.' (quoted from chapter ‘D. How to Use this Atlas’ of the 3rd edition of Brain Maps, p. 15; ISBN: 0-126-10582-0). Based on Figure 4 from chapter [‘A. Histology and Map Production’ of the 3rd edition of Brain Maps (pdf version from Swanson’s homepage)](http://larrywswanson.com/wp-content/uploads/2015/03/2-Atlas-prep-BrainMaps3-20041.pdf)), the coordinate system is oriented towards the right since the rat’s right hemisphere has been used to draw the atlas. Thus, giving Swanson’s coordinate system RIA orientation (X, Y, Z axes are oriented towards right, inferior and anterior, respectively). Note: More detailed descriptions were provided in the 3rd edition of the atlas (digital and book combined) compared to the 1st edition, but both describe the exact same coordinate system.",
    full_documentation={"@id": "https://larrywswanson.com/?page_id=164"},
    full_name="Swanson's Stereotactic Brain of the Sprague Dawley Rat",
    how_to_cite="Swanson, L.W. (1992) 'Coordinate Systems' Brain maps: structure of the rat brain, 1st edition.",
    license={"@id": "https://openminds.om-i.org/instances/licenses/CC-BY-NC-4.0"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/millimeter"},
    release_date="1992-12-24",
    short_name="Swanson's Stereotactic Rat Brain",
    version_identifier="v1992",
    version_innovation="This is the first version of this common coordinate space.",
)
CommonCoordinateSpaceVersion.whssd_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/WHSSD_v1",
    abbreviation="WHSSD",
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/ALS"},
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    release_date="2014-07-16",
    short_name="WHS of the SD Rat Brain",
    version_identifier="v1",
)
CommonCoordinateSpaceVersion.whssd_v1_01 = CommonCoordinateSpaceVersion(
    id="https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/WHSSD_v1.01",
    abbreviation="WHSSD",
    anatomical_axes_orientation={"@id": "https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS"},
    axes_origins=[
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 243.9999936},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 622.9999808},
        {"@type": "https://openminds.om-i.org/types/QuantitativeValue", "value": 247.9999936},
    ],
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    is_new_version_of={"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/WHSSD_v1"},
    native_unit={"@id": "https://openminds.om-i.org/instances/unitOfMeasurement/micrometer"},
    release_date="2014-07-16",
    short_name="WHS of the SD Rat Brain",
    version_identifier="v1.01",
)
