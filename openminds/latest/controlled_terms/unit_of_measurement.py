"""
Structured information on the unit of measurement.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class UnitOfMeasurement(LinkedMetadata):
    """
    Structured information on the unit of measurement.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/UnitOfMeasurement"
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


UnitOfMeasurement.ampere = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/ampere",
    definition="An electric current unit which is equal to the constant current which, if maintained in two straight parallel conductors of infinite length, of negligible circular cross-section, and placed 1 m apart in vacuum, would produce between these conductors a force equal to 2 x 10^[-7] newton per meter of length.",
    name="ampere",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000011",
    synonyms=["A"],
)
UnitOfMeasurement.arcdegree = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/arcdegree",
    definition="An arcdegree is a measurement of a plane angle in which one full rotation is 360 degrees.",
    name="arcdegree",
    synonyms=["arc degree", "degree", "degree of arc", "°"],
)
UnitOfMeasurement.bit = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/bit",
    name="bit",
)
UnitOfMeasurement.byte = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/byte",
    name="byte",
)
UnitOfMeasurement.centimeter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/centimeter",
    name="centimeter",
)
UnitOfMeasurement.core_hour = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/coreHour",
    definition="Usage of a computer processor core for one hour",
    name="core-hour",
)
UnitOfMeasurement.day = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/day",
    name="day",
)
UnitOfMeasurement.degree_celsius = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/degreeCelsius",
    definition="The 'degree Celsius' is a unit of temperature on the Celsius scale where the freezing point of water is at 0 °C and the boiling point of water is at 100 °C under standard atmospheric pressure.",
    name="degree Celsius",
    synonyms=["Celsius", "degree", "°C"],
)
UnitOfMeasurement.degree_fahrenheit = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/degreeFahrenheit",
    definition="The 'degree Fahrenheit' is a unit of temperature on the Fahrenheit scale where the freezing point of water is at 32 °F and the boiling point of water is at 212 °F under standard atmospheric pressure.",
    name="degree Fahrenheit",
    synonyms=["degree", "Fahrenheit", "°F"],
)
UnitOfMeasurement.degree_rankine = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/degreeRankine",
    definition="The 'degree Rankine' is a unit of temperature on the Rankine scale where the freezing point of water is at 491.67 °R and the boiling point of water is at 671.64102 °R under standard atmospheric pressure.",
    name="degree Rankine",
    synonyms=["degree", "Rankine", "°R", "°Ra"],
)
UnitOfMeasurement.embryonic_day = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/embryonicDay",
    definition="'Embryonic day' is a specific unit to measure the developmental stage of an embryo, starting with fertilization (1st embryonic day).",
    name="embryonic day",
)
UnitOfMeasurement.gigabyte = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/gigabyte",
    name="gigabyte",
)
UnitOfMeasurement.gigaohm = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/gigaohm",
    name="gigaohm",
    synonyms=["GΩ"],
)
UnitOfMeasurement.gram = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/gram",
    name="gram",
)
UnitOfMeasurement.hertz = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/hertz",
    definition="Unit of frequency equivalent to one event per second",
    name="hertz",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000106",
    synonyms=["Hz", "cycles per second", "events per second"],
)
UnitOfMeasurement.hour = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/hour",
    name="hour",
)
UnitOfMeasurement.kilobyte = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/kilobyte",
    name="kilobyte",
)
UnitOfMeasurement.kilogram = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/kilogram",
    name="kilogram",
)
UnitOfMeasurement.liter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/liter",
    name="liter",
)
UnitOfMeasurement.megabyte = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/megabyte",
    name="megabyte",
)
UnitOfMeasurement.megaohm = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/megaohm",
    name="megaohm",
    synonyms=["MΩ"],
)
UnitOfMeasurement.meter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/meter",
    name="meter",
)
UnitOfMeasurement.microampere = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/microampere",
    definition="An electric current unit current which is equal to one millionth of an ampere or 10^[-6] A.",
    name="microampere",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000038",
    synonyms=["µA"],
)
UnitOfMeasurement.microgram_per_milliliter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/microgramPerMilliliter",
    name="microgram per milliliter",
    synonyms=["ug/ml", "µg/ml"],
)
UnitOfMeasurement.micrometer = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/micrometer",
    name="micrometer",
)
UnitOfMeasurement.micromolar = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/micromolar",
    definition="Micromolar is a decimal fraction of molar concentration describing the amount of substance (measured in micromole) in one liter solution.",
    name="micromolar",
    synonyms=["uM", "µM", "µmol*m⁻³", "µmol/l", "µmol/m³"],
)
UnitOfMeasurement.milligram_per_kilogram_body_weight = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/milligramPerKilogramBodyWeight",
    definition="A milligram of a substance per kilogram of the body weight of the subject taking the substance.",
    name="milligram per kilogram body weight",
    synonyms=["mg/kg"],
)
UnitOfMeasurement.milligram_per_milliliter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/milligramPerMilliliter",
    name="milligram per milliliter",
    synonyms=["mg/ml"],
)
UnitOfMeasurement.milliliter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/milliliter",
    name="milliliter",
)
UnitOfMeasurement.millimeter = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/millimeter",
    name="millimeter",
)
UnitOfMeasurement.millimolar = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/millimolar",
    definition="Millimolar is a decimal fraction of molar concentration that describes a solution as millimole per one liter of a solution.",
    name="millimolar",
    synonyms=["10^-3 mol/L", "mM", "mol/m^3"],
)
UnitOfMeasurement.millisecond = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/millisecond",
    name="millisecond",
)
UnitOfMeasurement.millisiemens = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/millisiemens",
    definition="An electrical conduction unit which is equal to one thousandth of a siemen or 10^[-3] siemens.",
    name="millisiemens",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0010002",
    synonyms=["mS"],
)
UnitOfMeasurement.millivolt = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/millivolt",
    definition="An electric potential difference unit which is equal to one thousandth of a volt or 10^[-3] V.",
    name="millivolt",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000247",
    synonyms=["mV"],
)
UnitOfMeasurement.minute = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/minute",
    name="minute",
)
UnitOfMeasurement.molar = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/molar",
    definition="Molar is a measure of concentration that describes a solution as moles of solute per one liter of a solution.",
    name="molar",
    synonyms=["10^3 mol/m^3", "M", "mol/L"],
)
UnitOfMeasurement.month = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/month",
    name="month",
)
UnitOfMeasurement.nanoampere = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/nanoampere",
    definition="An electric current unit current which is equal to one thousand millionth of an ampere or 10^[-9] A.",
    name="nanoampere",
    synonyms=["nA"],
)
UnitOfMeasurement.nanomolar = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/nanomolar",
    definition="Nanomolar is a decimal fraction of molar concentration describing the amount of substance (measured in nanomole) in one liter solution.",
    name="nanomolar",
    synonyms=["nM", "nmol*m⁻³", "nmol/l", "nmol/m³"],
)
UnitOfMeasurement.ohm = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/ohm",
    definition="The SI derived unit of electrical resistance, named after German physicist Georg Ohm, equal to 1 V/A",
    name="ohm",
    synonyms=["Ω"],
)
UnitOfMeasurement.percentage = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/percentage",
    definition="A 'percentage' (from Latin per centum 'by a hundred') is a quantity expressed as a fraction of 100 (amount of something in each hundred).",
    name="percent",
    synonyms=["%", "pc", "pct", "percent"],
)
UnitOfMeasurement.picoampere = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/picoampere",
    definition="An electric current unit current which is equal to one trillionth of an ampere or 10^[-12] A.",
    name="picoampere",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0010054",
    synonyms=["pA"],
)
UnitOfMeasurement.radian = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/radian",
    definition="A 'radian' is the SI unit for measuring angles. One 'radian' defines the arc of a circle with the same length as the radius of that circle.",
    name="radian",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000123",
    synonyms=["rad"],
)
UnitOfMeasurement.second = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/second",
    name="second",
)
UnitOfMeasurement.siemens = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/siemens",
    definition="An electrical conduction unit which is equal to A/V.",
    name="siemens",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0000264",
    synonyms=["S"],
)
UnitOfMeasurement.terabyte = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/terabyte",
    name="terabyte",
)
UnitOfMeasurement.volt = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/volt",
    definition="An electric potential difference unit which is equal to the work per unit charge. One volt is the potential difference required to move one coulomb of charge between two points in a circuit while using one joule of energy.",
    name="volt",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/UO_0010054",
    synonyms=["V"],
)
UnitOfMeasurement.volume_per_volume_percentage = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/volumePerVolumePercentage",
    definition="Percentage of volume of one liquid dissolved in another liquid, where the volume of both liquids have the same unit",
    name="volume per volume percentage",
    synonyms=["% v/v", "percent v/v", "v/v %", "v/v percent", "volume percent"],
)
UnitOfMeasurement.wafer_hour = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/waferHour",
    definition="Usage of one wafer of a wafer-scale computing system for one hour",
    description="An example of such a wafer-scale system would be BrainScaleS-1",
    name="wafer-hour",
)
UnitOfMeasurement.week = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/week",
    name="week",
)
UnitOfMeasurement.weight_per_volume_percentage = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/weightPerVolumePercentage",
    definition="Percentage of weight or mass of a dissolved, solid substance in a total volume of a solution. As per definition, the volume of a liquid is expressed in milliliter (ml) and the mass of a solute in grams (g)",
    name="weight per volume percentage",
    synonyms=["% w/v", "mass/volume percent", "percent w/v", "w/v %", "w/v percent"],
)
UnitOfMeasurement.weight_per_weight_percentage = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/weightPerWeightPercentage",
    definition="The percentage of a particular substance within a mixture, as measured by weight or mass and expressed in the same unit",
    name="weight per weight percentage",
    synonyms=["% w/w", "mass percent", "percent w/w", "w/w %", "w/w percent", "weight percent"],
)
UnitOfMeasurement.year = UnitOfMeasurement(
    id="https://openminds.ebrains.eu/instances/unitOfMeasurement/year",
    name="year",
)
