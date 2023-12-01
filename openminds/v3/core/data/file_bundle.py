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
    schema_version = "v3.0"

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
            "openminds.v3.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="If the files within this bundle are organised and formatted according to a formal data structure, add the content type of this file bundle. Leave blank if no formal data structure has been applied to the files within this bundle.",
        ),
        Property(
            "grouped_by",
            [
                "openminds.v3.computation.LocalFile",
                "openminds.v3.controlled_terms.AnalysisTechnique",
                "openminds.v3.controlled_terms.AuditoryStimulusType",
                "openminds.v3.controlled_terms.BiologicalOrder",
                "openminds.v3.controlled_terms.BiologicalSex",
                "openminds.v3.controlled_terms.BreedingType",
                "openminds.v3.controlled_terms.CellCultureType",
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Disease",
                "openminds.v3.controlled_terms.DiseaseModel",
                "openminds.v3.controlled_terms.ElectricalStimulusType",
                "openminds.v3.controlled_terms.GeneticStrainType",
                "openminds.v3.controlled_terms.GustatoryStimulusType",
                "openminds.v3.controlled_terms.Handedness",
                "openminds.v3.controlled_terms.MolecularEntity",
                "openminds.v3.controlled_terms.OlfactoryStimulusType",
                "openminds.v3.controlled_terms.OpticalStimulusType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.OrganismSystem",
                "openminds.v3.controlled_terms.Species",
                "openminds.v3.controlled_terms.StimulationApproach",
                "openminds.v3.controlled_terms.StimulationTechnique",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.TactileStimulusType",
                "openminds.v3.controlled_terms.Technique",
                "openminds.v3.controlled_terms.TermSuggestion",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.controlled_terms.VisualStimulusType",
                "openminds.v3.core.BehavioralProtocol",
                "openminds.v3.core.File",
                "openminds.v3.core.FileBundle",
                "openminds.v3.core.Subject",
                "openminds.v3.core.SubjectGroup",
                "openminds.v3.core.SubjectGroupState",
                "openminds.v3.core.SubjectState",
                "openminds.v3.core.TissueSample",
                "openminds.v3.core.TissueSampleCollection",
                "openminds.v3.core.TissueSampleCollectionState",
                "openminds.v3.core.TissueSampleState",
                "openminds.v3.sands.CommonCoordinateSpace",
                "openminds.v3.sands.CommonCoordinateSpaceVersion",
                "openminds.v3.sands.CustomAnatomicalEntity",
                "openminds.v3.sands.CustomCoordinateSpace",
                "openminds.v3.sands.ParcellationEntity",
                "openminds.v3.sands.ParcellationEntityVersion",
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
            "openminds.v3.controlled_terms.FileBundleGrouping",
            "groupingType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all grouping types that were used to define this file bundle. Note that the grouping types define the possible schema type of the instances stated under 'groupedBy'.",
        ),
        Property(
            "hash",
            "openminds.v3.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file bundle.",
        ),
        Property(
            "is_part_of",
            ["openminds.v3.core.FileBundle", "openminds.v3.core.FileRepository"],
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
            "openminds.v3.core.QuantitativeValue",
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
