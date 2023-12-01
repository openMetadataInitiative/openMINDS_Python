"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileBundle(LinkedMetadata):
    """
    Structured information on a bundle of file instances.
    """

    type_ = "https://openminds.ebrains.eu/core/FileBundle"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "content_description",
            str,
            "contentDescription",
            formatting="text/plain",
            multiline=True,
            description="no description available",
            instructions="Enter a short content description for this file bundle.",
        ),
        Property(
            "format",
            "openminds.latest.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="If the files within this bundle are organised and formatted according to a formal data structure, add the content type of this file bundle. Leave blank if no formal data structure has been applied to the files within this bundle.",
        ),
        Property(
            "grouped_by",
            [
                "openminds.latest.computation.LocalFile",
                "openminds.latest.controlled_terms.AnalysisTechnique",
                "openminds.latest.controlled_terms.AuditoryStimulusType",
                "openminds.latest.controlled_terms.BiologicalOrder",
                "openminds.latest.controlled_terms.BiologicalSex",
                "openminds.latest.controlled_terms.BreedingType",
                "openminds.latest.controlled_terms.CellCultureType",
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.Disease",
                "openminds.latest.controlled_terms.DiseaseModel",
                "openminds.latest.controlled_terms.ElectricalStimulusType",
                "openminds.latest.controlled_terms.GeneticStrainType",
                "openminds.latest.controlled_terms.GustatoryStimulusType",
                "openminds.latest.controlled_terms.Handedness",
                "openminds.latest.controlled_terms.MolecularEntity",
                "openminds.latest.controlled_terms.OlfactoryStimulusType",
                "openminds.latest.controlled_terms.OpticalStimulusType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.Species",
                "openminds.latest.controlled_terms.StimulationApproach",
                "openminds.latest.controlled_terms.StimulationTechnique",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.TactileStimulusType",
                "openminds.latest.controlled_terms.Technique",
                "openminds.latest.controlled_terms.TermSuggestion",
                "openminds.latest.controlled_terms.TissueSampleType",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.controlled_terms.VisualStimulusType",
                "openminds.latest.core.BehavioralProtocol",
                "openminds.latest.core.File",
                "openminds.latest.core.FileBundle",
                "openminds.latest.core.Subject",
                "openminds.latest.core.SubjectGroup",
                "openminds.latest.core.SubjectGroupState",
                "openminds.latest.core.SubjectState",
                "openminds.latest.core.TissueSample",
                "openminds.latest.core.TissueSampleCollection",
                "openminds.latest.core.TissueSampleCollectionState",
                "openminds.latest.core.TissueSampleState",
                "openminds.latest.sands.CommonCoordinateSpace",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
                "openminds.latest.sands.CustomAnatomicalEntity",
                "openminds.latest.sands.CustomCoordinateSpace",
                "openminds.latest.sands.ParcellationEntity",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "groupedBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the aspect used to group something.",
            instructions="Add all entities that defined which files were grouped into this file bundle. Note that the schema types of the instances stated here, need to match the ones stated under 'groupingType'.",
        ),
        Property(
            "grouping_types",
            "openminds.latest.controlled_terms.FileBundleGrouping",
            "groupingType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all grouping types that were used to define this file bundle. Note that the grouping types define the possible schema type of the instances stated under 'groupedBy'.",
        ),
        Property(
            "hash",
            "openminds.latest.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file bundle.",
        ),
        Property(
            "is_part_of",
            ["openminds.latest.core.FileBundle", "openminds.latest.core.FileRepository"],
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the file bundle or file repository this file bundle is part of.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this file bundle.",
        ),
        Property(
            "storage_size",
            "openminds.latest.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size of this file bundle.",
        ),
    ]

    def __init__(
        self,
        id=None,
        content_description=None,
        format=None,
        grouped_by=None,
        grouping_types=None,
        hash=None,
        is_part_of=None,
        name=None,
        storage_size=None,
    ):
        return super().__init__(
            id=id,
            content_description=content_description,
            format=format,
            grouped_by=grouped_by,
            grouping_types=grouping_types,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            storage_size=storage_size,
        )
