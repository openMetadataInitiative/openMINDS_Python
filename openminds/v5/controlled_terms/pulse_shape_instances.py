# this file was auto-generated!


from openminds.v5.controlled_terms.pulse_shape import PulseShape


PulseShape.fermi_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/FermiPulse",
    definition="A pulse whose amplitude envelope follows a Fermi (logistic) function.",
    description="A Fermi pulse exhibits a smooth transition between low and high amplitude regions. Its shape is defined by a logistic function with adjustable slope parameters. The envelope allows controlled edge steepness. The pulse provides reduced spectral ringing compared to abrupt transitions. It is used in applications requiring smooth but bounded excitation profiles.",
    name="Fermi pulse",
    synonyms=["Fermi-shaped pulse"],
)

PulseShape.gaussian__hanning_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/Gaussian-HanningPulse",
    definition="A composite pulse formed by applying a Hanning window to a Gaussian pulse envelope.",
    description="A Gaussian-Hanning pulse combines a Gaussian envelope with a Hanning apodization window. The additional windowing further smooths temporal boundaries. This reduces spectral leakage beyond that of a simple Gaussian pulse. The pulse maintains symmetry about its center. It is used in applications requiring controlled spectral characteristics.",
    name="Gaussian-Hanning pulse",
    synonyms=["Hanning-windowed Gaussian pulse"],
)

PulseShape.gaussian_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/GaussianPulse",
    definition="A pulse whose amplitude envelope follows a Gaussian function over time.",
    description="A Gaussian pulse exhibits a smooth, symmetric amplitude profile. Its spectral distribution is also Gaussian. The smooth temporal transitions reduce spectral sidelobes. It is commonly used in RF excitation and optical systems. The pulse shape is fully defined by its standard deviation or width parameter.",
    name="Gaussian pulse",
    synonyms=["Gaussian-shaped pulse"],
)

PulseShape.rectangular_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/rectangularPulse",
    definition="A pulse with constant amplitude over its duration and abrupt onset and offset transitions.",
    description="A rectangular pulse maintains a uniform amplitude for a defined time interval. The rise and fall times are ideally instantaneous. Its frequency spectrum follows a sinc distribution. This shape is widely used in stimulation and RF excitation as a hard pulse. It represents the simplest temporal pulse form.",
    name="rectangular pulse",
)

PulseShape.sinc__gaussian_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sinc-GaussianPulse",
    definition="A composite pulse formed by modulating a sinc pulse with a Gaussian envelope.",
    description="A sinc-Gaussian pulse multiplies a sinc waveform by a Gaussian window. The Gaussian envelope reduces sidelobes in the frequency domain. This modification improves spectral selectivity compared to a truncated sinc pulse. The resulting waveform retains the central lobe characteristics of the sinc function. It is commonly used where reduced spectral leakage is required.",
    name="sinc-Gaussian pulse",
    synonyms=["Gaussian-windowed sinc pulse"],
)

PulseShape.sinc__hanning_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sinc-HanningPulse",
    definition="A composite pulse formed by modulating a sinc pulse with a Hanning window.",
    description="A sinc-Hanning pulse applies a Hanning window to a sinc waveform. The window smooths the pulse edges and suppresses spectral sidelobes. This reduces ringing artifacts compared to a simple truncated sinc. The central excitation profile remains governed by the sinc component. The pulse is used in applications requiring improved spectral control.",
    name="sinc-Hanning pulse",
    synonyms=["Hanning-windowed sinc pulse"],
)

PulseShape.sinc_pulse = PulseShape(
    id="https://openminds.om-i.org/instances/pulseShape/sincPulse",
    definition="A pulse whose amplitude envelope follows a sinc function in time.",
    description="A sinc pulse is defined by the mathematical sinc function. It produces a rectangular frequency-domain profile under ideal conditions. The pulse typically includes truncation in practical implementations. It is widely used in selective excitation applications. Its bandwidth is determined by the temporal scaling of the function.",
    name="sinc pulse",
    synonyms=["sinc-shaped pulse"],
)
