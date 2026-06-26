# this file was auto-generated!


from openminds.v5.controlled_terms.signal_directionality import SignalDirectionality


SignalDirectionality.signal_receiving = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-receiving",
    definition="A signal directionality mode in which a device detects and acquires incoming signals from an external source or medium.",
    description="In signal-receiving mode, the device operates as a passive or semi-passive sensor of external signals. It converts physical signal energy into measurable electrical or digital representations. Sensitivity and noise characteristics determine reception performance. Received signals are commonly amplified, filtered, and digitized for analysis. This mode is used in monitoring, imaging, and data acquisition systems.",
    name="signal-receiving",
    synonyms=["receiving", "receive-only"],
)

SignalDirectionality.signal_transceiving = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-transceiving",
    definition="A signal directionality mode in which a device both emits and detects signals within the same system or operational context.",
    description="In signal-transceiving mode, the device integrates transmitting and receiving functions. It alternates between emission and detection or performs both simultaneously depending on system design. Switching and isolation mechanisms are used to prevent self-interference. Operational timing is coordinated to manage bidirectional signal flow. This mode is common in imaging, communication, and active sensing technologies.",
    name="signal-transceiving",
    synonyms=["transceiving", "transmit–receive", "transmitting–receiving"],
)

SignalDirectionality.signal_transmitting = SignalDirectionality(
    id="https://openminds.om-i.org/instances/signalDirectionality/signal-transmitting",
    definition="A signal directionality mode in which a device generates and emits signals toward an external system, medium, or target.",
    description="In signal-transmitting mode, the device functions as an active source of signal energy or information. It produces controlled waveforms or data streams for delivery to another system or environment. The emitted signal may be electromagnetic, electrical, acoustic, or optical in nature. Transmission parameters such as power, timing, and modulation are typically configurable. This mode is used in applications including stimulation, communication, and active sensing.",
    name="signal-transmitting",
    synonyms=["transmitting", "transmit-only"],
)
