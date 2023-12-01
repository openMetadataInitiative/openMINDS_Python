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

    type_ = "https://openminds.ebrains.eu/core/TissueSampleCollection"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering this specimen set.",
        ),
        Property(
            "anatomical_locations",
            [
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.sands.CustomAnatomicalEntity",
                "openminds.v3.sands.ParcellationEntity",
                "openminds.v3.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all anatomical entities that describe the anatomical location of this tissue sample collection.",
        ),
        Property(
            "biological_sexes",
            "openminds.v3.controlled_terms.BiologicalSex",
            "biologicalSex",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of all specimen in this set.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.",
        ),
        Property(
            "lateralities",
            "openminds.v3.controlled_terms.Laterality",
            "laterality",
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
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen set that may help you to find this instance more easily.",
        ),
        Property(
            "number_of_tissue_samples",
            int,
            "numberOfTissueSamples",
            description="no description available",
            instructions="Enter the number of tissue samples that belong to this tissue sample collection.",
        ),
        Property(
            "origins",
            [
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
            ],
            "origin",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin of all tissue samples in this collection.",
        ),
        Property(
            "species",
            ["openminds.v3.controlled_terms.Species", "openminds.v3.core.Strain"],
            "species",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.",
        ),
        Property(
            "studied_states",
            "openminds.v3.core.TissueSampleCollectionState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample collection was studied.",
        ),
        Property(
            "types",
            "openminds.v3.controlled_terms.TissueSampleType",
            "type",
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
        anatomical_locations=None,
        biological_sexes=None,
        internal_identifier=None,
        lateralities=None,
        lookup_label=None,
        number_of_tissue_samples=None,
        origins=None,
        species=None,
        studied_states=None,
        types=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            anatomical_locations=anatomical_locations,
            biological_sexes=biological_sexes,
            internal_identifier=internal_identifier,
            lateralities=lateralities,
            lookup_label=lookup_label,
            number_of_tissue_samples=number_of_tissue_samples,
            origins=origins,
            species=species,
            studied_states=studied_states,
            types=types,
        )
