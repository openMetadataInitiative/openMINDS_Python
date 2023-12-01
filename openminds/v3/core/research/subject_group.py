"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubjectGroup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/SubjectGroup"
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
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen set that may help you to find this instance more easily.",
        ),
        Property(
            "number_of_subjects",
            int,
            "numberOfSubjects",
            description="no description available",
            instructions="Enter the number of subjects that belong to this subject group.",
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
            "openminds.v3.core.SubjectGroupState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this subject group was studied.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        biological_sexes=None,
        internal_identifier=None,
        lookup_label=None,
        number_of_subjects=None,
        species=None,
        studied_states=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            biological_sexes=biological_sexes,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            number_of_subjects=number_of_subjects,
            species=species,
            studied_states=studied_states,
        )
