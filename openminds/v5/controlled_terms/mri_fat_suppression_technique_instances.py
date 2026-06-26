# this file was auto-generated!


from openminds.v5.controlled_terms.mri_fat_suppression_technique import MRIFatSuppressionTechnique


MRIFatSuppressionTechnique.chemical_shift_selective_suppression = MRIFatSuppressionTechnique(
    id="https://openminds.om-i.org/instances/MRIFatSuppressionTechnique/chemicalShiftSelectiveSuppression",
    definition="A classical frequency-selective fat saturation technique that suppresses fat signal by applying a narrowband radiofrequency pulse tuned to the fat resonance frequency prior to image acquisition.",
    description="Chemical shift selective suppression, short CHESS, exploits the chemical shift difference between water and fat to selectively target fat protons. A spectrally selective RF pulse is applied at the fat resonance frequency, followed by a spoiler gradient to eliminate transverse magnetization. This preparation reduces fat signal intensity during subsequent imaging readout. The method is fast and straightforward to implement within most pulse sequences. However, it is sensitive to B₀ and B₁ field inhomogeneities, which can lead to incomplete or uneven fat suppression.",
    name="chemical shift selective suppression",
    synonyms=["chemical shift selective saturation", "CHESS"],
)

MRIFatSuppressionTechnique.dixon_water_fat_separation_technique = MRIFatSuppressionTechnique(
    id="https://openminds.om-i.org/instances/MRIFatSuppressionTechnique/DixonWater-fatSeparationTechnique",
    definition="A water-fat separation technique that acquires images at different echo times to mathematically decompose water and fat signals based on their phase differences.",
    description="The Dixon water-fat separation technique exploits the phase shift between water and fat signals that occurs at specific echo times due to their chemical shift difference. Images are acquired at in-phase and out-of-phase echo times, allowing computational separation of water and fat components. Multi-echo implementations improve robustness by modeling field inhomogeneities and signal complexity. The technique provides uniform fat suppression even in regions with magnetic field variation. Modern implementations form the basis of many contemporary clinical fat-water imaging protocols.",
    name="Dixon water-fat separation technique",
    synonyms=["Dixon method", "Dixon technique"],
)
