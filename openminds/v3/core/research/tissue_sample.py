"""
Structured information on a tissue sample.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSample(LinkedMetadata):
    """
    Structured information on a tissue sample.
    """

    type_ = "https://openminds.ebrains.eu/core/TissueSample"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
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
            instructions="Add all anatomical entities that describe the anatomical location of this tissue sample.",
        ),
        Property(
            "biological_sex",
            "openminds.v3.controlled_terms.BiologicalSex",
            "biologicalSex",
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of this specimen.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this specimen that is used within the corresponding data files to identify this specimen.",
        ),
        Property(
            "is_part_of",
            "openminds.v3.core.TissueSampleCollection",
            "isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add all tissue sample collections this tissue sample is part of.",
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
            instructions="Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample originates from.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen that may help you to find this instance more easily.",
        ),
        Property(
            "origin",
            [
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
            ],
            "origin",
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin of this tissue sample.",
        ),
        Property(
            "species",
            ["openminds.v3.controlled_terms.Species", "openminds.v3.core.Strain"],
            "species",
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species or strain (a sub-type of a genetic variant of species) of this specimen.",
        ),
        Property(
            "studied_states",
            "openminds.v3.core.TissueSampleState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample was studied.",
        ),
        Property(
            "type",
            "openminds.v3.controlled_terms.TissueSampleType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this tissue sample.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_locations=None,
        biological_sex=None,
        internal_identifier=None,
        is_part_of=None,
        lateralities=None,
        lookup_label=None,
        origin=None,
        species=None,
        studied_states=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            anatomical_locations=anatomical_locations,
            biological_sex=biological_sex,
            internal_identifier=internal_identifier,
            is_part_of=is_part_of,
            lateralities=lateralities,
            lookup_label=lookup_label,
            origin=origin,
            species=species,
            studied_states=studied_states,
            type=type,
        )
