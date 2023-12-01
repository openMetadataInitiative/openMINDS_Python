"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationEntityVersion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ParcellationEntityVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this parcellation entity version.",
        ),
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this parcellation entity version.",
        ),
        Property(
            "alternate_names",
            str,
            "alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any alternate names, including any alternative abbreviations, for this parcellation entity version.",
        ),
        Property(
            "corrected_name",
            str,
            "correctedName",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the refined or corrected name of this parcellation entity version.",
        ),
        Property(
            "has_annotations",
            "openminds.v3.sands.AtlasAnnotation",
            "hasAnnotation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all atlas annotations which define this parcellation entity version.",
        ),
        Property(
            "has_parents",
            ["openminds.v3.sands.ParcellationEntity", "openminds.v3.sands.ParcellationEntityVersion"],
            "hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a parent object or legal person.",
            instructions="Add all anatomical parent structures (or version of the structures) for this parcellation entity as defined within corresponding brain atlas version.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this parcellation entity version that may help you to find this instance more easily.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this parcellation entity version.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity version.",
        ),
        Property(
            "relation_assessments",
            ["openminds.v3.sands.QualitativeRelationAssessment", "openminds.v3.sands.QuantitativeRelationAssessment"],
            "relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all relations (qualitative or quantitative) of this parcellation entity version to other anatomical entities.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this parcellation entity version.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
            formatting="text/markdown",
            multiline=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this parcellation entity version in comparison to its preceding versions. If this parcellation entity version is the first version, leave blank.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        additional_remarks=None,
        alternate_names=None,
        corrected_name=None,
        has_annotations=None,
        has_parents=None,
        lookup_label=None,
        name=None,
        ontology_identifiers=None,
        relation_assessments=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            additional_remarks=additional_remarks,
            alternate_names=alternate_names,
            corrected_name=corrected_name,
            has_annotations=has_annotations,
            has_parents=has_parents,
            lookup_label=lookup_label,
            name=name,
            ontology_identifiers=ontology_identifiers,
            relation_assessments=relation_assessments,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
