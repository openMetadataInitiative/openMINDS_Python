# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.publication_status import PublicationStatus


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
