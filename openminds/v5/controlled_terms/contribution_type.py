"""
Structured information on the type of contribution a person or organization performed.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContributionType(LinkedMetadata):
    """
    Structured information on the type of contribution a person or organization performed.
    """

    type_ = "https://openminds.om-i.org/types/ContributionType"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the contribution type.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the contribution type.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "other_cross_references",
            str,
            "otherCrossReference",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.",
        ),
        Property(
            "other_ontology_identifiers",
            str,
            "otherOntologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.",
        ),
        Property(
            "preferred_cross_reference",
            IRI,
            "preferredCrossReference",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        name=None,
        other_cross_references=None,
        other_ontology_identifiers=None,
        preferred_cross_reference=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            name=name,
            other_cross_references=other_cross_references,
            other_ontology_identifiers=other_ontology_identifiers,
            preferred_cross_reference=preferred_cross_reference,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


ContributionType.acquisition = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/acquisition",
    definition="A contribution type of a role-bearing entity realized by acquiring or obtaining an existing target entity or resources required for its use.",
    name="acquisition",
)
ContributionType.administration = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/administration",
    definition="A contribution type of a role-bearing entity realized by administrating organizational, operational, or procedural aspects related to a target entity.",
    name="administration",
)
ContributionType.authoring = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/authoring",
    definition="A contribution type of a role-bearing entity realized by creating textual, visual, or other expressive intellectual content about or for a target entity.",
    name="authoring",
)
ContributionType.collection = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/collection",
    definition="A contribution type of a role-bearing entity realized by gathering or aggregating instances or information forming a target entity.",
    name="collection",
)
ContributionType.communication = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/communication",
    definition="A contribution type of a role-bearing entity realized by communicating information about a target entity to relevant audiences.",
    name="communication",
)
ContributionType.coordination = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/coordination",
    definition="A contribution type of a role-bearing entity realized by coordinating activities, participants, or processes related to a target entity.",
    name="coordination",
)
ContributionType.creation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/creation",
    definition="A contribution type of a role-bearing entity realized by producing or bringing a target entity into existence.",
    name="creation",
)
ContributionType.curation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/curation",
    definition="A contribution type of a role-bearing entity realized by organizing, annotating, or improving the quality and usability of a target entity.",
    name="curation",
)
ContributionType.custodianship = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/custodianship",
    definition="A contribution type of a role-bearing entity realized by assuming responsibility for the long-term stewardship and oversight of a target entity.",
    name="custodianship",
)
ContributionType.deployment = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/deployment",
    definition="A contribution type of a role-bearing entity realized by installing or releasing a target entity into an operational or accessible environment.",
    name="deployment",
)
ContributionType.design = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/design",
    definition="A contribution type of a role-bearing entity realized by specifying the structure, methodology, or architecture of a target entity.",
    name="design",
)
ContributionType.development = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/development",
    definition="A contribution type of a role-bearing entity realized by creating, implementing, or extending physical or digital technological components of a target entity.",
    name="development",
)
ContributionType.dissemination = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/dissemination",
    definition="A contribution type of a role-bearing entity realized by distributing or publishing a target entity to make it accessible to relevant professional or specialist communities.",
    name="dissemination",
)
ContributionType.education = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/education",
    definition="A contribution type of a role-bearing entity realized by transferring knowledge about a target entity to enable learning about its nature, context, principles, or applications.",
    name="education",
)
ContributionType.hosting = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/hosting",
    definition="A contribution type of a role-bearing entity realized by providing and maintaining an environment, infrastructure, or resources that enable a target entity to exist, operate, or take place.",
    name="hosting",
)
ContributionType.human_medical_care = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/humanMedicalCare",
    definition="A contribution type of a role-bearing entity realized by providing medical diagnosis, treatment, or health management for a human.",
    name="human medical care",
)
ContributionType.husbandry = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/husbandry",
    definition="A contribution type of a role-bearing entity realized by managing the day-to-day care, growth, reproduction, or environmental conditions of living organisms.",
    name="husbandry",
)
ContributionType.implementation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/implementation",
    definition="A contribution type of a role-bearing entity realized by putting a specified design, plan, method, or specification into effect through or within a target entity.",
    name="implementation",
)
ContributionType.inspection = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/inspection",
    definition="A contribution type of a role-bearing entity realized by examining a target entity through observation or review to assess its condition, compliance, conformity, or quality.",
    name="inspection",
)
ContributionType.integration = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/integration",
    definition="A contribution type of a role-bearing entity realized by incorporating another living or non-living thing into a target entity so that it becomes part of and functions within a coherent whole.",
    name="integration",
)
ContributionType.liaison = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/liaison",
    definition="A contribution type of a role-bearing entity realized by serving as a point of contact or intermediary regarding a target entity.",
    name="liaison",
)
ContributionType.maintenance = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/maintenance",
    definition="A contribution type of a role-bearing entity realized by sustaining, updating, or repairing a target entity to ensure its continued functionality and quality.",
    name="maintenance",
)
ContributionType.manufacturing = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/manufacturing",
    definition="A contribution type of a role-bearing entity realized by producing physical target entities, typically in a repeatable or systematic manner, for distribution, use, or sale.",
    name="manufacturing",
)
ContributionType.operation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/operation",
    definition="A contribution type of a role-bearing entity realized by controlling, operating, or running a target entity in an active environment.",
    name="operation",
)
ContributionType.operational_storage = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/operationalStorage",
    definition="A contribution type of a role-bearing entity realized by maintaining a target entity in a storage system or environment to support its active access or use.",
    name="operational storage",
)
ContributionType.outreach = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/outreach",
    definition="A contribution type of a role-bearing entity realized by engaging with broader or non-specialist audiences to raise awareness, understanding, or adoption of a target entity.",
    name="outreach",
)
ContributionType.ownership = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/ownership",
    definition="A contribution type of a role-bearing entity realized by holding legal ownership rights and responsibilities for a target entity.",
    name="ownership",
)
ContributionType.packaging = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/packaging",
    definition="A contribution type of a role-bearing entity realized by preparing a target entity for distribution, installation, or deployment.",
    name="packaging",
)
ContributionType.preservation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/preservation",
    definition="A contribution type of a role-bearing entity realized by maintaining or protecting a target entity over time to ensure its continued existence, integrity, or availability.",
    name="preservation",
)
ContributionType.processing = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/processing",
    definition="A contribution type of a role-bearing entity realized by transforming, analyzing, or manipulating the state or content of a target entity.",
    name="processing",
)
ContributionType.provision = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/provision",
    definition="A contribution type of a role-bearing entity realized by making a target entity or its functionality available for use.",
    name="provision",
)
ContributionType.review = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/review",
    definition="A contribution type of a role-bearing entity realized by critically assessing a target entity through expert judgment to evaluate its quality, validity, or suitability.",
    name="review",
)
ContributionType.scientific_writing = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/scientificWriting",
    definition="A contribution type of a role-bearing entity realized by producing textual content that reports, analyzes, or interprets scientific investigations or knowledge about a target entity.",
    name="scientific writing",
)
ContributionType.standardization = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/standardization",
    definition="A contribution type of a role-bearing entity realized by aligning a target entity with shared specifications or conventions applied across multiple entities.",
    name="standardization",
)
ContributionType.support = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/support",
    definition="A contribution type of a role-bearing entity realized by assisting users or systems in the effective use or functioning of a target entity.",
    name="support",
)
ContributionType.surgical_performance = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/surgicalPerformance",
    definition="A contribution type of a role-bearing entity realized by performing surgical procedures on a living organism.",
    name="surgical performance",
)
ContributionType.technical_writing = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/technicalWriting",
    definition="A contribution type of a role-bearing entity realized by producing structured explanatory or instructional textual content describing the design, structure, operation, or use of a target entity.",
    name="technical writing",
)
ContributionType.testing = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/testing",
    definition="A contribution type of a role-bearing entity realized by executing defined procedures or experiments to evaluate the behavior, functionality, or performance of a target entity.",
    name="testing",
)
ContributionType.training = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/training",
    definition="A contribution type of a role-bearing entity realized by instructing or conditioning a target entity to acquire practical skills, behaviors, or operational knowledge.",
    name="training",
)
ContributionType.validation = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/validation",
    definition="A contribution type of a role-bearing entity realized by confirming, based on evidence or evaluation results, that a target entity fulfills specified requirements or intended purposes.",
    name="validation",
)
ContributionType.versioning = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/versioning",
    definition="A contribution type of a role-bearing entity realized by managing and tracking changes or designated versions of a target entity over time.",
    name="versioning",
)
ContributionType.veterinary_care = ContributionType(
    id="https://openminds.om-i.org/instances/contributionType/veterinaryCare",
    definition="A contribution type of a role-bearing entity realized by providing veterinary diagnosis, treatment, or health management for an animal.",
    name="veterinary care",
)
