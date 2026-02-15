"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PublicationStatus(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/PublicationStatus"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

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
            description="Longer statement or account giving the characteristics of the publication status.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the publication status.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
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
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
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


PublicationStatus.disposed = PublicationStatus(
    id="https://openminds.om-i.org/instances/publicationStatus/disposed",
    definition="A publication status indicating the work has been removed from active retention or management (e.g., after a retention period, superseded, or otherwise deaccessioned) and is no longer available, without implying wrongdoing or defects in the work.",
    name="disposed",
)
PublicationStatus.embargoed = PublicationStatus(
    id="https://openminds.om-i.org/instances/publicationStatus/embargoed",
    definition="A publication status indicating the work exists but cannot be publicly published, reported on, or made openly available until a specified embargo end date set by the embargoing party.",
    description="The status of a work that is subjected to an embargo, which means that the work cannot be published, or in the case of a press release that it cannot be reported on, until a particular date known as the embargo date. For open-access journal articles, an embargoed article is one in which availability of the open-access version of the article is delayed by the publisher for a substantial embargo period, typically of six or twelve months, after subscription-access availability of the published work. [[Publishing Status Ontology (PSO)](http://purl.org/spar/pso): [Peroni, S., Shotton, D., Vitali, F. (2012)](https://doi.org/10.1145/2362499.2362502)]",
    name="embargoed",
    preferred_ontology_identifier=IRI("http://purl.org/spar/pso/embargoed"),
)
PublicationStatus.published = PublicationStatus(
    id="https://openminds.om-i.org/instances/publicationStatus/published",
    definition="A publication status indicating the work has been formally released to the public by the responsible publisher or issuing entity and is accessible in its official published form.",
    description="The status of material (for example a document or a dataset) that has been published, i.e. made available for people to access, read or use, either freely or for a purchase price or an access fee. [[Publishing Status Ontology (PSO)](http://purl.org/spar/pso): [Peroni, S., Shotton, D., Vitali, F. (2012)](https://doi.org/10.1145/2362499.2362502)]",
    name="published",
    preferred_ontology_identifier=IRI("http://purl.org/spar/pso/published"),
    synonyms=["released"],
)
PublicationStatus.retracted = PublicationStatus(
    id="https://openminds.om-i.org/instances/publicationStatus/retracted",
    definition="A publication status indicating the work was previously published but has been formally withdrawn from the public record by the publisher or issuing authority, typically accompanied by a retraction notice.",
    description="The status of a publication that has been subsequently retracted by the publisher, for example because it was subsequently found to contain erroneous or fraudulent information. [[Publishing Status Ontology (PSO)](http://purl.org/spar/pso): [Peroni, S., Shotton, D., Vitali, F. (2012)](https://doi.org/10.1145/2362499.2362502)]",
    name="retracted",
    preferred_ontology_identifier=IRI("http://purl.org/spar/pso/retracted-from-publication"),
    synonyms=["retracted from publication"],
)
PublicationStatus.under_review = PublicationStatus(
    id="https://openminds.om-i.org/instances/publicationStatus/underReview",
    definition="A publication status indicating the work has been submitted for evaluation and is currently being assessed by an editor, reviewers, or an approval body, with no publication decision or public release yet.",
    description="The status of a document that has been received from the author(s) by an editor or a publisher for potential publication, and then has been sent to independent reviewers for their comments as to its suitability for publication, prior to receipt of such reviews. [[Publishing Status Ontology (PSO)](http://purl.org/spar/pso): [Peroni, S., Shotton, D., Vitali, F. (2012)](https://doi.org/10.1145/2362499.2362502)]",
    name="under review",
    preferred_ontology_identifier=IRI("http://purl.org/spar/pso/under-review"),
)
