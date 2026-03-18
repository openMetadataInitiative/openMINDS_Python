"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PulseShape(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/PulseShape"
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
            description="Longer statement or account giving the characteristics of the pulse shape.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the pulse shape.",
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


PulseShape.fermi_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/FermiPulse",
    definition="A pulse whose amplitude envelope follows a Fermi (logistic) function.",
    description="A Fermi pulse exhibits a smooth transition between low and high amplitude regions. Its shape is defined by a logistic function with adjustable slope parameters. The envelope allows controlled edge steepness. The pulse provides reduced spectral ringing compared to abrupt transitions. It is used in applications requiring smooth but bounded excitation profiles.",
    name="Fermi pulse",
    synonyms=["Fermi-shaped pulse"],
)
PulseShape.gaussian__hanning_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/Gaussian-HanningPulse",
    definition="A composite pulse formed by applying a Hanning window to a Gaussian pulse envelope.",
    description="A Gaussian-Hanning pulse combines a Gaussian envelope with a Hanning apodization window. The additional windowing further smooths temporal boundaries. This reduces spectral leakage beyond that of a simple Gaussian pulse. The pulse maintains symmetry about its center. It is used in applications requiring controlled spectral characteristics.",
    name="Gaussian-Hanning pulse",
    synonyms=["Hanning-windowed Gaussian pulse"],
)
PulseShape.gaussian_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/GaussianPulse",
    definition="A pulse whose amplitude envelope follows a Gaussian function over time.",
    description="A Gaussian pulse exhibits a smooth, symmetric amplitude profile. Its spectral distribution is also Gaussian. The smooth temporal transitions reduce spectral sidelobes. It is commonly used in RF excitation and optical systems. The pulse shape is fully defined by its standard deviation or width parameter.",
    name="Gaussian pulse",
    synonyms=["Gaussian-shaped pulse"],
)
PulseShape.rectangular_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/rectangularPulse",
    definition="A pulse with constant amplitude over its duration and abrupt onset and offset transitions.",
    description="A rectangular pulse maintains a uniform amplitude for a defined time interval. The rise and fall times are ideally instantaneous. Its frequency spectrum follows a sinc distribution. This shape is widely used in stimulation and RF excitation as a hard pulse. It represents the simplest temporal pulse form.",
    name="rectangular pulse",
)
PulseShape.sinc__gaussian_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sinc-GaussianPulse",
    definition="A composite pulse formed by modulating a sinc pulse with a Gaussian envelope.",
    description="A sinc-Gaussian pulse multiplies a sinc waveform by a Gaussian window. The Gaussian envelope reduces sidelobes in the frequency domain. This modification improves spectral selectivity compared to a truncated sinc pulse. The resulting waveform retains the central lobe characteristics of the sinc function. It is commonly used where reduced spectral leakage is required.",
    name="sinc-Gaussian pulse",
    synonyms=["Gaussian-windowed sinc pulse"],
)
PulseShape.sinc__hanning_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sinc-HanningPulse",
    definition="A composite pulse formed by modulating a sinc pulse with a Hanning window.",
    description="A sinc-Hanning pulse applies a Hanning window to a sinc waveform. The window smooths the pulse edges and suppresses spectral sidelobes. This reduces ringing artifacts compared to a simple truncated sinc. The central excitation profile remains governed by the sinc component. The pulse is used in applications requiring improved spectral control.",
    name="sinc-Hanning pulse",
    synonyms=["Hanning-windowed sinc pulse"],
)
PulseShape.sinc_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sincPulse",
    definition="A pulse whose amplitude envelope follows a sinc function in time.",
    description="A sinc pulse is defined by the mathematical sinc function. It produces a rectangular frequency-domain profile under ideal conditions. The pulse typically includes truncation in practical implementations. It is widely used in selective excitation applications. Its bandwidth is determined by the temporal scaling of the function.",
    name="sinc pulse",
    synonyms=["sinc-shaped pulse"],
)
