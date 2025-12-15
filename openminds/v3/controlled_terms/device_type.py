"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DeviceType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/DeviceType"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

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
            description="Longer statement or account giving the characteristics of the device type.",
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
            description="Word or phrase that constitutes the distinctive designation of the device type.",
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
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


DeviceType.c_tscanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/CTscanner",
    definition="A 'CT scanner' is an x-ray machine that creates and combines serial two-dimensional x-ray images (sections) with the aid of a computer to generate cross-sectional views and/or three-dimensional images of internal body structures (e.g., bones, blood vessels or soft tissues).",
    name="CT scanner",
    synonyms=["CAT scanner", "computed axial tomography scanner", "computed tomography scanner"],
)
DeviceType.closed_bore_mri_scanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/closedBoreMRIScanner",
    definition="'Closed-bore MRI scanners' are high-field scanners which feature a magnet surrounding the patient creating a capsule-like space (standard or wide) where the patient lies on.",
    name="closed-bore MRI scanner",
    synonyms=[
        "closed-bore magnetic resonance imaging scanner",
        "closed magnetic resonance imaging scanner",
        "closed MRI scanner",
    ],
)
DeviceType.electronic_amplifier = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/electronicAmplifier",
    definition="An 'electronic amplifier' is a device that increases the power (voltage or current) of a time-varying signal.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0100567"),
    name="electronic amplifier",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/nlx_27076"),
    synonyms=["amp", "amplifier"],
)
DeviceType.microscope = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/microscope",
    definition="A 'microscope' is an instrument used to obtain a magnified image of small objects and reveal details of structures not otherwise distinguishable.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106921"),
    name="microscope",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_2106"),
)
DeviceType.microtome = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/microtome",
    definition="A 'microtome' is a mechanical instrument with a steel, glass or diamond blade used to cut (typically) biological specimens into very thin segments for further treatment and ultimately microscopic or histologic examination.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106925"),
    name="microtome",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/OBI_0400168"),
)
DeviceType.mr_iscanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIscanner",
    definition="An 'MRI scanner' is a machine that uses strong magnetic fields, magnetic field gradients, and radio waves to generate static or time-resolved three-dimensional images of the anatomy and physiological processes of the body.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106463"),
    name="MRI scanner",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_2100"),
    synonyms=["magnetic resonance imaging scanner"],
)
DeviceType.mri_body_coil = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIBodyCoil",
    definition="Type of volume coil optimized for uniform radiofrequency transmission and/or reception across large anatomical regions, typically encompassing the torso or entire body.",
    description="Body coils are integrated volume coils typically built into the bore of an MRI scanner to provide homogeneous B1 field distribution across extensive anatomical areas. They are often used as transmit or transmit/receive coils for imaging the torso and whole body, and frequently serve as the system's default transmit coil when combined with local receive arrays. Their large geometry ensures consistent excitation and reception, enabling high-quality imaging across diverse body regions and supporting calibration or reference functions in multi-coil setups.",
    name="MRI body coil",
    synonyms=["body coil", "body MRI coil", "whole-body coil"],
)
DeviceType.mri_extremity_coil = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIExtremityCoil",
    definition="Type of volume coil optimized for imaging peripheral anatomical regions such as the arms, legs, wrists, ankles, or knees; in rare cases, extremity coils may adopt a surface-coil design when full enclosure of the anatomy is impractical.",
    description="Extremity coils are specialized radiofrequency volume coils designed to provide high signal-to-noise ratio and uniform excitation when imaging smaller body parts like the limbs. They typically use cylindrical or contoured geometries that enclose the target region but can also appear as surface-coil variants for joints or areas where full coverage is not feasible. Extremity coils are widely used in musculoskeletal and vascular MRI, offering focused, high-resolution imaging of localized peripheral structures.",
    name="MRI extremity coil",
    synonyms=["knee/ankle/wrist coil", "limb coil", "peripheral coil"],
)
DeviceType.mri_head_coil = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIHeadCoil",
    definition="Type of volume coil optimized for radiofrequency transmission and/or reception over the head and brain, providing homogeneous B1 field coverage within the cranial region.",
    description="Head coils are dedicated radiofrequency (RF) volume coils designed to image the brain and cranial structures. They typically use birdcage or quadrature configurations to achieve uniform excitation and reception across the entire head. Head coils can operate as transmit/receive or receive-only systems depending on the scanner design. High-channel phased-array head coils are increasingly common, improving signal-to-noise ratio (SNR) and parallel-imaging capabilities. In some advanced configurations, open or partial head coils are employed for interventional or functional MRI studies, where full enclosure is not required.",
    name="MRI head coil",
    synonyms=["brain coil", "cranial coil", "head MRI coil"],
)
DeviceType.mri_multi_coil_array = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIMulti-coilArray",
    definition="Type of radiofrequency coil composed of multiple coordinated elements optimized for transmit and/or receive operation over an extended field of view; phased-array coils are a specialized subclass focused on parallel signal reception.",
    description="Multi-coil arrays consist of several individual RF elements that work together to improve signal quality, coverage, and control of the B₁ field. Depending on their configuration, they may operate as transmit, receive, or transmit-receive systems, enabling techniques such as RF shimming, parallel transmission, and parallel imaging. These arrays can be designed with volume-type geometries that enclose the anatomy or surface-type arrangements that conform to the body's contour. Phased-array coils represent a subset of multi-coil arrays specialized for independent receive channels used in parallel acquisition.",
    name="MRI multi-coil array",
    synonyms=["MRI array coil", "MRI multicoil array", "multi-channel coil", "phased-array coil"],
)
DeviceType.mri_surface_coil = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRISurfaceCoil",
    definition="Type of radiofrequency coil optimized for localized signal reception from tissue near the coil surface, providing high sensitivity over a small field of view.",
    description="Surface coils are small radiofrequency coils placed directly adjacent to the region of interest to capture strong signals from nearby tissues with high spatial resolution. Their sensitivity decreases rapidly with distance, making them ideal for imaging superficial structures such as the spine, joints, or breast. Surface coils are typically receive-only and operate in combination with a separate transmit coil, often the body coil. They can also serve as building blocks in multi-coil or phased-array configurations, extending coverage while maintaining local sensitivity.",
    name="MRI surface coil",
    synonyms=["local coil", "surface MRI coil"],
)
DeviceType.mri_volume_coil = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/MRIVolumeCoil",
    definition="Type of radiofrequency coil optimized for uniform transmit and/or receive coverage across a defined enclosed volume of anatomy.",
    description="Volume coils are radiofrequency coils that fully or partially enclose the anatomy to produce a homogeneous B₁ field within a specified region, such as the head, torso, or extremities. They are used for both transmission and reception of MR signals and are commonly built in birdcage or quadrature configurations. Volume coils provide uniform excitation and reception, making them suitable for general-purpose imaging or as transmit coils in combination with local receive arrays. Their subtypes include body, head, and extremity coils, which differ mainly by size and anatomical coverage.",
    name="MRI volume coil",
    synonyms=["volume MRI coil", "volumetric coil"],
)
DeviceType.open_bore_mri_scanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/openBoreMRIScanner",
    definition="'Open-bore MRI scanners' are low-field scanners which have a magnetic top and bottom, but are otherwise open, increasing patient's comfort and unobstructed view of the scanning area.",
    name="open-bore MRI scanner",
    synonyms=[
        "open-bore magnetic resonance imaging scanner",
        "open magnetic resonance imaging scanner",
        "open MRI scanner",
    ],
)
DeviceType.standard_bore_mri_scanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/standardBoreMRIScanner",
    definition="A 'standard-bore MRI scanner' is a closed high-field scanner which features a magnet surrounding the patient creating a capsule-like space where the patient lies on.",
    name="standard-bore MRI scanner",
    synonyms=[
        "standard-bore magnetic resonance imaging scanner",
        "standard-bore closed magnetic resonance imaging scanner",
        "standard-bore closed MRI scanner",
    ],
)
DeviceType.vibrating_microtome = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/vibratingMicrotome",
    definition="A 'vibrating microtome' is an mechanical instrument with a vibrating steel blade used to cut (typically) biological specimens into thin segments for further treatment and ultimately microscopic or histologic examination.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0780522"),
    name="vibrating microtome",
    synonyms=["vibratome"],
)
DeviceType.wide_bore_mri_scanner = DeviceType(
    id="https://openminds.ebrains.eu/instances/deviceType/wideBoreMRIScanner",
    definition="A 'wide-bore MRI scanner' is a closed high-field scanner which features a widened bore compared to the standard-bore MRI scanner.",
    name="wide-bore MRI scanner",
    synonyms=[
        "wide-bore magnetic resonance imaging scanner",
        "wide-bore closed magnetic resonance imaging scanner",
        "wide-bore closed MRI scanner",
    ],
)
