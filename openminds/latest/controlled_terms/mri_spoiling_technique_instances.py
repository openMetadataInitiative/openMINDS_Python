# this file was auto-generated!


from openminds.latest.controlled_terms.mri_spoiling_technique import MRISpoilingTechnique


MRISpoilingTechnique.combined_spoiling = MRISpoilingTechnique(
    id="https://openminds.om-i.org/instances/MRISpoilingTechnique/combinedSpoiling",
    definition="A spoiling technique that suppresses residual transverse magnetization by combining radiofrequency phase cycling with gradient-induced spatial dephasing.",
    description="Combined spoiling applies radiofrequency (RF) phase cycling together with spoiler gradients within the same pulse sequence. This dual approach disrupts transverse coherence both temporally and spatially. RF spoiling controls phase evolution across repetitions. Gradient spoiling further enforces dephasing within each repetition. The combination provides robust suppression of steady-state transverse magnetization in modern gradient-echo imaging.",
    name="combined spoiling",
    synonyms=["combined radiofrequency–gradient spoiling", "combined RF–gradient spoiling"],
)

MRISpoilingTechnique.gradient_spoiling = MRISpoilingTechnique(
    id="https://openminds.om-i.org/instances/MRISpoilingTechnique/gradientSpoiling",
    definition="A spoiling technique that suppresses residual transverse magnetization by applying additional gradient moments to induce spatial dephasing.",
    description="Gradient spoiling applies crusher or spoiler gradients after signal acquisition. These gradients introduce position-dependent phase shifts in transverse magnetization. The resulting spatial dephasing reduces coherent signal contributions in subsequent repetitions. The effectiveness depends on gradient strength and duration. Gradient spoiling is widely used in gradient-echo and spin-echo sequences to control unwanted coherence pathways.",
    name="gradient spoiling",
    synonyms=["gradient crusher spoiling", "gradient dephasing"],
)

MRISpoilingTechnique.radiofrequency_spoiling = MRISpoilingTechnique(
    id="https://openminds.om-i.org/instances/MRISpoilingTechnique/radiofrequencySpoiling",
    definition="A spoiling technique that suppresses residual transverse magnetization by applying controlled phase cycling to successive radiofrequency excitation pulses.",
    description="Radiofrequency (RF) spoiling introduces systematic phase increments between consecutive RF pulses to disrupt coherent transverse magnetization. This phase cycling prevents the formation of stable transverse steady states. The method enforces incoherence of residual magnetization across repetitions. Reconstruction relies on predictable phase behavior imposed by the RF scheme. RF spoiling is commonly used in spoiled gradient-echo sequences for T1-weighted imaging.",
    name="radiofrequency spoiling",
    synonyms=["RF phase spoiling", "RF spoiling"],
)
