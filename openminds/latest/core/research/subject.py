"""
Structured information on a subject.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Subject(LinkedMetadata):
    """
    Structured information on a subject.
    """

    type_ = "https://openminds.ebrains.eu/core/Subject"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "biological_sex",
            "openminds.latest.controlled_terms.BiologicalSex",
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
            "openminds.latest.core.SubjectGroup",
            "isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add all subject groups of which this subject is a member.",
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
            "species",
            ["openminds.latest.controlled_terms.Species", "openminds.latest.core.Strain"],
            "species",
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species or strain (a sub-type of a genetic variant of species) of this specimen.",
        ),
        Property(
            "studied_states",
            "openminds.latest.core.SubjectState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this subject was studied.",
        ),
    ]

    def __init__(
        self,
        id=None,
        biological_sex=None,
        internal_identifier=None,
        is_part_of=None,
        lookup_label=None,
        species=None,
        studied_states=None,
    ):
        return super().__init__(
            id=id,
            biological_sex=biological_sex,
            internal_identifier=internal_identifier,
            is_part_of=is_part_of,
            lookup_label=lookup_label,
            species=species,
            studied_states=studied_states,
        )
