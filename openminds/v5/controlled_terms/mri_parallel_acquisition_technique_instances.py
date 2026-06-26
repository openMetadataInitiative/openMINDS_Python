# this file was auto-generated!


from openminds.v5.controlled_terms.mri_parallel_acquisition_technique import MRIParallelAcquisitionTechnique


MRIParallelAcquisitionTechnique.generalized_autocalibrating_partially_parallel_acquisition = MRIParallelAcquisitionTechnique(
    id="https://openminds.om-i.org/instances/MRIParallelAcquisitionTechnique/generalizedAutocalibratingPartiallyParallelAcquisition",
    definition="A parallel MRI reconstruction technique that accelerates imaging by undersampling k-space and reconstructing missing data using calibration-derived interpolation kernels in k-space.",
    description="A generalized autocalibrating partially parallel acquisition, short GRAPPA, acquires undersampled k-space data along with additional autocalibration lines. The method determines reconstruction weights directly from acquired calibration data without requiring explicit coil sensitivity maps. Missing k-space lines are synthesized by linear combinations of neighboring acquired data across multiple coils. Reconstruction occurs in k-space prior to final Fourier transformation. The technique is robust to coil sensitivity estimation errors and widely implemented in clinical MRI systems.",
    name="generalized autocalibrating partially parallel acquisition",
    synonyms=["GRAPPA"],
)

MRIParallelAcquisitionTechnique.sensitivity_encoding = MRIParallelAcquisitionTechnique(
    id="https://openminds.om-i.org/instances/MRIParallelAcquisitionTechnique/sensitivityEncoding",
    definition="A parallel MRI reconstruction technique that accelerates imaging by undersampling k-space and using coil sensitivity profiles to reconstruct full-resolution images in the image domain.",
    description="Sensitivity encoding, short SENSE, reduces acquisition time by undersampling phase-encoding steps during data acquisition. The method relies on prior estimation of spatial sensitivity maps for each coil element in a multi-array coil system. Aliased images resulting from undersampling are mathematically unfolded using these sensitivity profiles. Reconstruction is performed in the image domain after Fourier transformation. The technique directly links achievable acceleration to coil geometry and signal-to-noise characteristics.",
    name="sensitivity encoding",
    synonyms=["SENSE"],
)
