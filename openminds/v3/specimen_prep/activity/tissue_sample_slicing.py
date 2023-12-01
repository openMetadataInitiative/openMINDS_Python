"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleSlicing(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/specimenPrep/TissueSampleSlicing"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "device",
            "openminds.v3.specimen_prep.SlicingDeviceUsage",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the device used to slice the tissue sample.",
        ),
        Property(
            "input",
            [
                "openminds.v3.core.SubjectState",
                "openminds.v3.core.TissueSampleCollectionState",
                "openminds.v3.core.TissueSampleState",
            ],
            "input",
            description="Something or someone that is put into or participates in a process or machine.",
            instructions="Add the state of the specimen that was sliced during this activity.",
        ),
        Property(
            "outputs",
            ["openminds.v3.core.TissueSampleCollectionState", "openminds.v3.core.TissueSampleState"],
            "output",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Something or someone that comes out of, is delivered or produced by a process or machine.",
            instructions="Add the state of the tissue sample slice or collection of slices that resulted from this activity.",
        ),
        Property(
            "temperature",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "temperature",
            description="no description available",
            instructions="Enter the temperature at which the tissue sample was sliced during the activity.",
        ),
        Property(
            "tissue_bath_solution",
            "openminds.v3.chemicals.ChemicalMixture",
            "tissueBathSolution",
            description="no description available",
            instructions="Add the chemical mixture used as bath solution during this activity.",
        ),
    ]

    def __init__(self, id=None, device=None, input=None, outputs=None, temperature=None, tissue_bath_solution=None):
        return super().__init__(
            id=id,
            device=device,
            input=input,
            outputs=outputs,
            temperature=temperature,
            tissue_bath_solution=tissue_bath_solution,
        )
