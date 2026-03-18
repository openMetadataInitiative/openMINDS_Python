"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SpatialEncoding(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SpatialEncoding"
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
            description="Longer statement or account giving the characteristics of the spatial encoding.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the spatial encoding.",
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


SpatialEncoding.one_dimensional_frequency_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalFrequencyEncoding",
    definition="A spatial encoding method in which position along a single dimension is represented by differences in signal frequency.",
    description="In one-dimensional frequency encoding, spatial location is mapped directly to frequency components of the detected signal. A spatially varying field or gradient establishes a linear relationship between position and frequency. Signals from different locations are separated through spectral analysis. Reconstruction is performed by converting frequency information into spatial coordinates. This method is widely used in line-scan imaging, spectroscopy, and single-axis readout systems.",
    name="one-dimensional frequency encoding",
    synonyms=["1D frequency encoding", "single-dimensional frequency encoding"],
)
SpatialEncoding.one_dimensional_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalPhaseEncoding",
    definition="A spatial encoding method in which position along a single dimension is represented by controlled phase shifts of the signal.",
    description="In one-dimensional phase encoding, spatial position is encoded through accumulated phase differences. A preparatory gradient or modulation step introduces position-dependent phase offsets. These phase shifts are sampled over repeated measurements. Spatial information is recovered through Fourier or phase-sensitive reconstruction. This method is commonly used when frequency-based encoding is impractical or insufficient.",
    name="one-dimensional phase encoding",
    synonyms=["1D phase encoding", "single-dimensional phase encoding"],
)
SpatialEncoding.three_dimensional_frequency_phase_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/three-dimensionalFrequency-phase-phaseEncoding",
    definition="A spatial encoding method in which position in three dimensions is represented using frequency encoding along one axis and phase encoding along two orthogonal axes.",
    description="In three-dimensional frequency-phase-phase encoding, spatial information is distributed across one frequency-encoded and two phase-encoded dimensions. A readout gradient provides frequency discrimination along one axis. Two independent phase-encoding steps encode the remaining spatial directions. Repeated acquisitions sample the three-dimensional encoding space. Reconstruction produces volumetric spatial representations from the combined frequency and phase data.",
    name="three-dimensional frequency-phase-phase encoding",
    synonyms=["3D frequency-phase-phase encoding", "three-dimensional frequency and dual-phase encoding"],
)
SpatialEncoding.two_dimensional_frequency_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/two-dimensionalFrequency-phaseEncoding",
    definition="A spatial encoding method in which position in two dimensions is represented using frequency encoding along one axis and phase encoding along a second axis.",
    description="In two-dimensional frequency-phase encoding, one spatial direction is mapped to signal frequency and the other to signal phase. A readout gradient establishes frequency encoding, while stepped gradients impose phase encoding. Multiple acquisitions are combined to sample the two-dimensional encoding space. Reconstruction converts frequency and phase information into planar spatial coordinates. This approach is widely used in two-dimensional imaging and mapping applications.",
    name="two-dimensional frequency-phase encoding",
    synonyms=["2D frequency-phase encoding", "two-dimensional frequency and phase encoding"],
)
