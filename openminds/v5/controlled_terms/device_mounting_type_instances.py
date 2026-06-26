# this file was auto-generated!


from openminds.v5.controlled_terms.device_mounting_type import DeviceMountingType


DeviceMountingType.conformable_mounting = DeviceMountingType(
    id="https://openminds.om-i.org/instances/deviceMountingType/conformableMounting",
    definition="A mounting configuration in which the device or its mounting interface deforms to conform to the surface geometry of the host structure.",
    name="conformable mounting",
)

DeviceMountingType.form_stable_mounting = DeviceMountingType(
    id="https://openminds.om-i.org/instances/deviceMountingType/form-stableMounting",
    definition="A mounting configuration in which the device retains a fixed geometry and does not conform to the surface shape of the host structure.",
    name="form-stable mounting",
)

DeviceMountingType.integrated_mounting = DeviceMountingType(
    id="https://openminds.om-i.org/instances/deviceMountingType/integratedMounting",
    definition="A mounting configuration in which the device is structurally incorporated into a larger system or enclosure and not intended for routine removal.",
    name="integrated mounting",
    synonyms=["built-in mounting"],
)
