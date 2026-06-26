# this file was auto-generated!


from openminds.latest.controlled_terms.spatial_encoding import SpatialEncoding


SpatialEncoding.one_dimensional_frequency_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalFrequencyEncoding",
    definition="A spatial encoding method in which position along a single dimension is represented by differences in signal frequency.",
    description="In one-dimensional frequency encoding, spatial location is mapped directly to frequency components of the detected signal. A spatially varying field or gradient establishes a linear relationship between position and frequency. Signals from different locations are separated through spectral analysis. Reconstruction is performed by converting frequency information into spatial coordinates. This method is widely used in line-scan imaging, spectroscopy, and single-axis readout systems.",
    name="one-dimensional frequency encoding",
    synonyms=["1D frequency encoding", "single-dimensional frequency encoding"],
)

SpatialEncoding.one_dimensional_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalPhaseEncoding",
    definition="A spatial encoding method in which position along a single dimension is represented by controlled phase shifts of the signal.",
    description="In one-dimensional phase encoding, spatial position is encoded through accumulated phase differences. A preparatory gradient or modulation step introduces position-dependent phase offsets. These phase shifts are sampled over repeated measurements. Spatial information is recovered through Fourier or phase-sensitive reconstruction. This method is commonly used when frequency-based encoding is impractical or insufficient.",
    name="one-dimensional phase encoding",
    synonyms=["1D phase encoding", "single-dimensional phase encoding"],
)

SpatialEncoding.three_dimensional_frequency_phase_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/three-dimensionalFrequency-phase-phaseEncoding",
    definition="A spatial encoding method in which position in three dimensions is represented using frequency encoding along one axis and phase encoding along two orthogonal axes.",
    description="In three-dimensional frequency-phase-phase encoding, spatial information is distributed across one frequency-encoded and two phase-encoded dimensions. A readout gradient provides frequency discrimination along one axis. Two independent phase-encoding steps encode the remaining spatial directions. Repeated acquisitions sample the three-dimensional encoding space. Reconstruction produces volumetric spatial representations from the combined frequency and phase data.",
    name="three-dimensional frequency-phase-phase encoding",
    synonyms=["3D frequency-phase-phase encoding", "three-dimensional frequency and dual-phase encoding"],
)

SpatialEncoding.two_dimensional_frequency_phase_encoding = SpatialEncoding(
    id="https://openminds.om-i.org/instances/spatialEncoding/two-dimensionalFrequency-phaseEncoding",
    definition="A spatial encoding method in which position in two dimensions is represented using frequency encoding along one axis and phase encoding along a second axis.",
    description="In two-dimensional frequency-phase encoding, one spatial direction is mapped to signal frequency and the other to signal phase. A readout gradient establishes frequency encoding, while stepped gradients impose phase encoding. Multiple acquisitions are combined to sample the two-dimensional encoding space. Reconstruction converts frequency and phase information into planar spatial coordinates. This approach is widely used in two-dimensional imaging and mapping applications.",
    name="two-dimensional frequency-phase encoding",
    synonyms=["2D frequency-phase encoding", "two-dimensional frequency and phase encoding"],
)
