"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleCollection(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/core/TissueSampleCollection"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering this specimen set.",
        ),
        Property(
            "anatomical_location",
            [
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all anatomical entities that describe the anatomical location of this tissue sample collection.",
        ),
        Property(
            "biological_sex",
            "openminds.v3_0.controlled_terms.BiologicalSex",
            "vocab:biologicalSex",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of all specimen in this set.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.",
        ),
        Property(
            "laterality",
            "openminds.v3_0.controlled_terms.Laterality",
            "vocab:laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample collection originates from.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen set that may help you to find this instance more easily.",
        ),
        Property(
            "number_of_tissue_samples",
            int,
            "vocab:numberOfTissueSamples",
            description="no description available",
            instructions="Enter the number of tissue samples that belong to this tissue sample collection.",
        ),
        Property(
            "origin",
            [
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
            ],
            "vocab:origin",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin of all tissue samples in this collection.",
        ),
        Property(
            "species",
            ["openminds.v3_0.controlled_terms.Species", "openminds.v3_0.core.Strain"],
            "vocab:species",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.",
        ),
        Property(
            "studied_state",
            "openminds.v3_0.core.TissueSampleCollectionState",
            "vocab:studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample collection was studied.",
        ),
        Property(
            "type",
            "openminds.v3_0.controlled_terms.TissueSampleType",
            "vocab:type",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of all tissue samples in this collection.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        anatomical_location=None,
        biological_sex=None,
        internal_identifier=None,
        laterality=None,
        lookup_label=None,
        number_of_tissue_samples=None,
        origin=None,
        species=None,
        studied_state=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            anatomical_location=anatomical_location,
            biological_sex=biological_sex,
            internal_identifier=internal_identifier,
            laterality=laterality,
            lookup_label=lookup_label,
            number_of_tissue_samples=number_of_tissue_samples,
            origin=origin,
            species=species,
            studied_state=studied_state,
            type=type,
        )
