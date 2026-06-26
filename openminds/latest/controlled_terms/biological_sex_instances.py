# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.biological_sex import BiologicalSex


BiologicalSex.female = BiologicalSex(
    id="https://openminds.om-i.org/instances/biologicalSex/female",
    definition="Biological sex that produces egg cells (ova).",
    description="A female organism typically has the capacity to produce relatively large, usually immobile gametes (reproductive cells), called egg cells (or ova). In the process of fertilization, an egg cell (ovum) fuses with a smaller, usually mobile male gametes, called sperm cells (or spermatozoa).",
    name="female",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0104150"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/PATO_0000383"),
)

BiologicalSex.hermaphrodite = BiologicalSex(
    id="https://openminds.om-i.org/instances/biologicalSex/hermaphrodite",
    definition="Biological sex with both male and female reproductive organs.",
    description="A hermaphrodite is an animal or plant that can produce gametes (reproductive cells) of both, male and female sexes. In sexually dimorphic organisms, hermaphroditism may occur because of variations in the genetic code. The term *hermaphrodite* is considered to be misleading, stigmatizing, and scientifically specious in reference to humans. For this reason, in humans the term *intersex* is typically used.",
    name="hermaphrodite",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0104963"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/PATO_0001340"),
    synonyms=["intersex"],
)

BiologicalSex.male = BiologicalSex(
    id="https://openminds.om-i.org/instances/biologicalSex/male",
    definition="Biological sex that produces sperm cells (spermatozoa).",
    description="A male organism typically has the capacity to produce relatively small, usually mobile gametes (reproductive cells), called sperm cells (or spermatozoa). In the process of fertilization, these sperm cells fuse with a larger, usually immobile female gamete, called egg cell (or ovum).",
    name="male",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0106489"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/PATO_0000384"),
)

BiologicalSex.not_detectable = BiologicalSex(
    id="https://openminds.om-i.org/instances/biologicalSex/notDetectable",
    definition="Can be stated if the biological sex in visually not detectable at a specific point in time.",
    name="not detectable",
)
