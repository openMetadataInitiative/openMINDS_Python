"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationTerminology(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ParcellationTerminology"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "defined_in",
            "openminds.v2.core.File",
            "definedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a file instance in which something is stored.",
            instructions="Add one or several files in which this parcellation terminology is stored in.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this parcellation terminology.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.v2.sands.BrainAtlasVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add one or several alternative versions to this parcellation terminology.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v2.sands.BrainAtlasVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the earlier version of this parcellation terminology.",
        ),
        Property(
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this parcellation terminology.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this parcellation terminology.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this parcellation terminology.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description of the novelties/peculiarities of this parcellation terminology.",
        ),
    ]

    def __init__(
        self,
        id=None,
        defined_in=None,
        full_name=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        ontology_identifier=None,
        short_name=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            defined_in=defined_in,
            full_name=full_name,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            ontology_identifier=ontology_identifier,
            short_name=short_name,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
