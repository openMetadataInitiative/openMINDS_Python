"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI
from datetime import date

from openminds.base import LinkedMetadata
from openminds.properties import Property


class LearningResource(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/publications/LearningResource"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "iri",
            IRI,
            "vocab:IRI",
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) to this creative work.",
        ),
        Property(
            "about",
            [
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipe",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.Dataset",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModel",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.Software",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebService",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaper",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlas",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpace",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "vocab:about",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all research product (versions) this learning resource are about. Note that the learning resource should supplement the usage of the research product (versions) with e.g., instructions on their usage or additional information.",
        ),
        Property(
            "abstract",
            str,
            "vocab:abstract",
            formatting="text/plain",
            multiline=True,
            description="no description available",
            instructions="Enter the abstract or a short description of the creative work.",
        ),
        Property(
            "author",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this creative work as authors.",
        ),
        Property(
            "cited_publication",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN"],
            "vocab:citedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all references this creative work cites.",
        ),
        Property(
            "copyright",
            "openminds.latest.core.Copyright",
            "vocab:copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this creative work.",
        ),
        Property(
            "creation_date",
            date,
            "vocab:creationDate",
            description="no description available",
            instructions="Enter the date on which this creative work was created, formatted as '2023-02-07'.",
        ),
        Property(
            "custodian",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this creative work (e.g., a corresponding author). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the creative work.",
        ),
        Property(
            "digital_identifier",
            "openminds.latest.core.DOI",
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this creative work.",
        ),
        Property(
            "editor",
            "openminds.latest.core.Person",
            "vocab:editor",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all persons that edited this creative work.",
        ),
        Property(
            "educational_level",
            "openminds.latest.controlled_terms.EducationalLevel",
            "vocab:educationalLevel",
            description="no description available",
            instructions="Add the educational level that best summarizes the prerequisite of this learning resource.",
        ),
        Property(
            "funding",
            "openminds.latest.core.Funding",
            "vocab:funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this creative work.",
        ),
        Property(
            "keyword",
            [
                "openminds.latest.controlled_terms.ActionStatusType",
                "openminds.latest.controlled_terms.AgeCategory",
                "openminds.latest.controlled_terms.AnalysisTechnique",
                "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
                "openminds.latest.controlled_terms.AnatomicalIdentificationType",
                "openminds.latest.controlled_terms.AnatomicalPlane",
                "openminds.latest.controlled_terms.AnnotationCriteriaType",
                "openminds.latest.controlled_terms.AnnotationType",
                "openminds.latest.controlled_terms.AtlasType",
                "openminds.latest.controlled_terms.AuditoryStimulusType",
                "openminds.latest.controlled_terms.BiologicalOrder",
                "openminds.latest.controlled_terms.BiologicalProcess",
                "openminds.latest.controlled_terms.BiologicalSex",
                "openminds.latest.controlled_terms.BreedingType",
                "openminds.latest.controlled_terms.CellCultureType",
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.ChemicalMixtureType",
                "openminds.latest.controlled_terms.Colormap",
                "openminds.latest.controlled_terms.ContributionType",
                "openminds.latest.controlled_terms.CranialWindowConstructionType",
                "openminds.latest.controlled_terms.CranialWindowReinforcementType",
                "openminds.latest.controlled_terms.CriteriaQualityType",
                "openminds.latest.controlled_terms.DataType",
                "openminds.latest.controlled_terms.DeviceType",
                "openminds.latest.controlled_terms.DifferenceMeasure",
                "openminds.latest.controlled_terms.Disease",
                "openminds.latest.controlled_terms.DiseaseModel",
                "openminds.latest.controlled_terms.EducationalLevel",
                "openminds.latest.controlled_terms.ElectricalStimulusType",
                "openminds.latest.controlled_terms.EthicsAssessment",
                "openminds.latest.controlled_terms.ExperimentalApproach",
                "openminds.latest.controlled_terms.FileBundleGrouping",
                "openminds.latest.controlled_terms.FileRepositoryType",
                "openminds.latest.controlled_terms.FileUsageRole",
                "openminds.latest.controlled_terms.GeneticStrainType",
                "openminds.latest.controlled_terms.GustatoryStimulusType",
                "openminds.latest.controlled_terms.Handedness",
                "openminds.latest.controlled_terms.Language",
                "openminds.latest.controlled_terms.Laterality",
                "openminds.latest.controlled_terms.LearningResourceType",
                "openminds.latest.controlled_terms.MeasuredQuantity",
                "openminds.latest.controlled_terms.MeasuredSignalType",
                "openminds.latest.controlled_terms.MetaDataModelType",
                "openminds.latest.controlled_terms.ModelAbstractionLevel",
                "openminds.latest.controlled_terms.ModelScope",
                "openminds.latest.controlled_terms.MolecularEntity",
                "openminds.latest.controlled_terms.OlfactoryStimulusType",
                "openminds.latest.controlled_terms.OperatingDevice",
                "openminds.latest.controlled_terms.OperatingSystem",
                "openminds.latest.controlled_terms.OpticalStimulusType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.PatchClampVariation",
                "openminds.latest.controlled_terms.PreparationType",
                "openminds.latest.controlled_terms.ProductAccessibility",
                "openminds.latest.controlled_terms.ProgrammingLanguage",
                "openminds.latest.controlled_terms.QualitativeOverlap",
                "openminds.latest.controlled_terms.SemanticDataType",
                "openminds.latest.controlled_terms.Service",
                "openminds.latest.controlled_terms.SetupType",
                "openminds.latest.controlled_terms.SoftwareApplicationCategory",
                "openminds.latest.controlled_terms.SoftwareFeature",
                "openminds.latest.controlled_terms.Species",
                "openminds.latest.controlled_terms.StimulationApproach",
                "openminds.latest.controlled_terms.StimulationTechnique",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.SubjectAttribute",
                "openminds.latest.controlled_terms.TactileStimulusType",
                "openminds.latest.controlled_terms.Technique",
                "openminds.latest.controlled_terms.TermSuggestion",
                "openminds.latest.controlled_terms.Terminology",
                "openminds.latest.controlled_terms.TissueSampleAttribute",
                "openminds.latest.controlled_terms.TissueSampleType",
                "openminds.latest.controlled_terms.TypeOfUncertainty",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.controlled_terms.UnitOfMeasurement",
                "openminds.latest.controlled_terms.VisualStimulusType",
            ],
            "vocab:keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of something or someone.",
            instructions="Add all relevant keywords to this creative work either by adding controlled terms or by suggesting new terms.",
        ),
        Property(
            "learning_outcome",
            str,
            "vocab:learningOutcome",
            formatting="text/markdown",
            multiline=True,
            description="no description available",
            instructions="Enter a description for the expected learning outcomes of this learning resource.",
        ),
        Property(
            "license",
            "openminds.latest.core.License",
            "vocab:license",
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this creative work.",
        ),
        Property(
            "modification_date",
            date,
            "vocab:modificationDate",
            description="no description available",
            instructions="Enter the date on which this creative work was last modfied, formatted as '2023-02-07'.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name (or title) of this creative work.",
        ),
        Property(
            "order",
            int,
            "vocab:order",
            description="no description available",
            instructions="Enter the order in which this resource should appear, relative to other resources with the same topic.",
        ),
        Property(
            "prerequisite",
            str,
            "vocab:prerequisite",
            formatting="text/markdown",
            multiline=True,
            description="no description available",
            instructions="Enter any knowledge, skills, or abilities that are required to be able to use this learning resource.",
        ),
        Property(
            "publication_date",
            date,
            "vocab:publicationDate",
            required=True,
            description="no description available",
            instructions="Enter the date on which this creative work was published, formatted as '2023-02-07'.",
        ),
        Property(
            "publisher",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "vocab:publisher",
            description="no description available",
            instructions="Add the party (private or commercial) that published this creative work.",
        ),
        Property(
            "required_time",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "vocab:requiredTime",
            description="no description available",
            instructions="Enter the time that is required to complete this learning resource.",
        ),
        Property(
            "topic",
            str,
            "vocab:topic",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the name or a short description of the aspect of the research product that is covered by this tutorial",
        ),
        Property(
            "type",
            "openminds.latest.controlled_terms.LearningResourceType",
            "vocab:type",
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this learning resource.",
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            formatting="text/plain",
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this creative work.",
        ),
    ]

    def __init__(
        self,
        id=None,
        iri=None,
        about=None,
        abstract=None,
        author=None,
        cited_publication=None,
        copyright=None,
        creation_date=None,
        custodian=None,
        digital_identifier=None,
        editor=None,
        educational_level=None,
        funding=None,
        keyword=None,
        learning_outcome=None,
        license=None,
        modification_date=None,
        name=None,
        order=None,
        prerequisite=None,
        publication_date=None,
        publisher=None,
        required_time=None,
        topic=None,
        type=None,
        version_identifier=None,
    ):
        return super().__init__(
            id=id,
            iri=iri,
            about=about,
            abstract=abstract,
            author=author,
            cited_publication=cited_publication,
            copyright=copyright,
            creation_date=creation_date,
            custodian=custodian,
            digital_identifier=digital_identifier,
            editor=editor,
            educational_level=educational_level,
            funding=funding,
            keyword=keyword,
            learning_outcome=learning_outcome,
            license=license,
            modification_date=modification_date,
            name=name,
            order=order,
            prerequisite=prerequisite,
            publication_date=publication_date,
            publisher=publisher,
            required_time=required_time,
            topic=topic,
            type=type,
            version_identifier=version_identifier,
        )