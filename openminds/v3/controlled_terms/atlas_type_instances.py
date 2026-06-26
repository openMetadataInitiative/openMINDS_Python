# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.atlas_type import AtlasType


AtlasType.deterministic_atlas = AtlasType(
    id="https://openminds.ebrains.eu/instances/atlasType/deterministicAtlas",
    definition="A 'deterministic atlas' is an anatomical or anatomopathological atlases based on a definite composite of a single specimen.",
    name="deterministic atlas",
)

AtlasType.parcellation_scheme = AtlasType(
    id="https://openminds.ebrains.eu/instances/atlasType/parcellationScheme",
    definition="A 'parcellation scheme' is a set of parcels occupying a part or all of an anatomical entity that has been delineated or annotated using a common approach or set of criteria.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0108526"),
    name="parcellation scheme",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_144019"),
    synonyms=["partition scheme"],
)

AtlasType.probabilistic_atlas = AtlasType(
    id="https://openminds.ebrains.eu/instances/atlasType/probabilisticAtlas",
    definition="A 'probabilistic atlas' is an anatomical or anatomopathological atlases based on statistically-weighted composites of many specimens.",
    name="probabilistic atlas",
    synonyms=["probability map"],
)
