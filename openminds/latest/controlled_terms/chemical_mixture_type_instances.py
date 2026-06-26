# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.chemical_mixture_type import ChemicalMixtureType


ChemicalMixtureType.alloy = ChemicalMixtureType(
    id="https://openminds.om-i.org/instances/chemicalMixtureType/alloy",
    definition="A mixture of chemical elements of which at least one is a metal, the atoms are joined by metallic bonding and retains all properties of a metal. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Alloy)]",
    name="alloy",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/CHEBI_142648"),
)

ChemicalMixtureType.colloid = ChemicalMixtureType(
    id="https://openminds.om-i.org/instances/chemicalMixtureType/colloid",
    definition="A 'colloid' is a heterogeneous mixture in which one substance consisting of microscopically dispersed insoluble particles is suspended throughout another substance. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Colloid)]",
    description="A colloid is a mixture where very small particles of one substance are evenly distributed throughout another substance. They appear very similar to solutions, but the particles are suspended in the solvent rather than fully dissolved. The difference between a colloid and a suspension is that the particles will not settle to the bottom over a period of time, they will stay suspended or float.",
    name="colloid",
)

ChemicalMixtureType.solution = ChemicalMixtureType(
    id="https://openminds.om-i.org/instances/chemicalMixtureType/solution",
    definition="A 'solution' is a special type of homogeneous mixture where at least one substance, called solute, is fully dissolved in another substance, known as a solvent. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Solution_(chemistry))",
    description="A solution is a homogeneous mixture of two or more substances. The particles of solute in a solution cannot be seen by the naked eye. A solution does not cause beams of light to scatter. A solution is stable; solutes will not precipitate unless added in excess of the mixture's solubility, at which point the excess would remain in its solid phase, referred to as hypersaturation. The solute from a solution cannot be separated by filtration (or mechanically). It is composed of only one phase. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Solution_(chemistry))",
    name="solution",
)

ChemicalMixtureType.suspension = ChemicalMixtureType(
    id="https://openminds.om-i.org/instances/chemicalMixtureType/suspension",
    definition="A 'suspension' is a heterogeneous mixture of a fluid that contains solid particles sufficiently large for sedimentation and may even be visible to the naked eye. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Suspension_(chemistry))]",
    description="A suspension is a heterogeneous mixture in which the solute particles do not dissolve, but get suspended throughout the bulk of the solvent, left floating around freely in the medium. Solute particles are usually larger than one micrometer, and will eventually settle, although the mixture is only classified as a suspension when and while the particles have not settled out. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Suspension_(chemistry))]",
    name="suspension",
)
