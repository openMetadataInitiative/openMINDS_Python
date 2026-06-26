# this file was auto-generated!


from openminds.v4.controlled_terms.ethics_assessment import EthicsAssessment


EthicsAssessment.eu_compliant = EthicsAssessment(
    id="https://openminds.om-i.org/instances/ethicsAssessment/EUCompliant",
    definition="Data are ethically approved in compliance with EU law. No additional ethics assessment was made by the data sharing initiative.",
    description="Data are ethically approved in compliance with EU law. No additional ethics assessment was made by the data sharing initiative. This is typically true for all, human post-mortem data, human cross-subject statistics, non-primate vertebrate animals as well as cephalopods.",
    name="EU compliant",
)

EthicsAssessment.eu_compliantplus = EthicsAssessment(
    id="https://openminds.om-i.org/instances/ethicsAssessment/EUCompliant+",
    definition="Data are ethically approved in compliance with EU law and an additional assessment was made by the data sharing initiative.",
    description="Data are ethically approved in compliance with EU law and an additional assessment was made by the data sharing initiative. This is typically true for all living human single-subject data as well as all non-human primate data.",
    name="EU compliant +",
)

EthicsAssessment.not_required = EthicsAssessment(
    id="https://openminds.om-i.org/instances/ethicsAssessment/notRequired",
    definition="An ethics assessment is 'not required' when no ethics approval was needed to conduct the study.",
    description="An ethics assessment is 'not required' when no ethics approval was needed to conduct the study. This is typically true for all simulated and invertebrate data (except cephalopods).",
    name="not required",
)

EthicsAssessment.us_compliant = EthicsAssessment(
    id="https://openminds.om-i.org/instances/ethicsAssessment/USCompliant",
    definition="Data are ethically approved in compliance with the laws of the United States of America. No additional ethics assessment was made by the data sharing initiative.",
    name="US compliant",
)
