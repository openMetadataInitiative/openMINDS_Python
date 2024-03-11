"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DifferenceMeasure(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/DifferenceMeasure"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
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
            description="Longer statement or account giving the characteristics of someone or something.",
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
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
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
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


DifferenceMeasure.chi_squared_statistic = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/chiSquaredStatistic",
    definition="Test statistic resulting from a chi-squared test.",
    name="chi-squared statistic",
    synonyms=["χ2-statistic"],
)
DifferenceMeasure.kolmogorov_smirnov_statistic = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/kolmogorovSmirnovStatistic",
    definition="Quantification of a distance between the empirical distribution function of the sample and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.",
    name="Kolmogorov-Smirnov statistic",
    synonyms=["KS-statistic"],
)
DifferenceMeasure.kullback_leibler_divergence = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/kullbackLeiblerDivergence",
    definition="A measure of how one probability distribution is different from a second, reference probability distribution.",
    name="Kullback-Leibler divergence",
    synonyms=["KL divergence"],
)
DifferenceMeasure.mean_squared_error = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/meanSquaredError",
    definition="The mean squared difference between two series of values.",
    name="mean squared error",
)
DifferenceMeasure.t_statistic = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/t_statistic",
    definition="The ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error.",
    name="t-statistic",
)
DifferenceMeasure.z_score = DifferenceMeasure(
    id="https://openminds.ebrains.eu/instances/differenceMeasure/z_score",
    definition="The number of standard deviations by which an observed value is above or below the mean value.",
    name="z-score",
)
