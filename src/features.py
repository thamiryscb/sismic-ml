import numpy as np
from scipy.signal import hilbert
from scipy.ndimage import uniform_filter1d

def normalize_seismic_traces(data):

    data = np.asarray(data, dtype=np.float32)

    scale = np.percentile(
        np.abs(data),
        99.5,
        axis=2,
        keepdims=True
    ).astype(np.float32)

    # Evitar divisão por zero
    scale = np.where(scale > 0, scale, 1.0)

    normalized_data = data / scale

    return normalized_data.astype(np.float32)

def extract_seismic_attributes(
    seismic_data,
    dt_ms,
    window_ms=40,
    normalize=False
):

    if dt_ms <= 0:
        raise ValueError("Intervalo de amostragem inválido.")

    # Amplitude original
    amplitude = np.array(
        seismic_data,
        dtype=np.float32,
        copy=True
    )

    # Normalização somente quando solicitada
    if normalize:
        amplitude = normalize_seismic_traces(amplitude)

    if not np.isfinite(amplitude).all():
        raise ValueError("Traços com valores inválidos.")

    # Sinal analítico
    analytical_signal = hilbert(amplitude, axis=2)

    # Envelope — metodologia original
    attribute_envelope = np.abs(analytical_signal)

    # Fase instantânea — metodologia original
    attribute_phase = np.arctan2(
        np.imag(analytical_signal),
        np.real(analytical_signal)
    )

    del analytical_signal

    # Frequência instantânea
    phase_unwrapped = np.unwrap(
        attribute_phase,
        axis=2
    )

    attribute_frequency = np.gradient(
        phase_unwrapped,
        dt_ms / 1000,
        axis=2
    ) / (2 * np.pi)

    del phase_unwrapped

    # Janela temporal para RMS e variância
    window = max(3, round(window_ms / dt_ms))

    if window % 2 == 0:
        window += 1

    local_mean = uniform_filter1d(
        amplitude,
        size=window,
        axis=2
    )

    local_mean_square = uniform_filter1d(
        amplitude**2,
        size=window,
        axis=2
    )

    # Amplitude RMS
    attribute_rms = np.sqrt(
        np.maximum(local_mean_square, 0)
    )

    # Variância local
    attribute_variance = np.maximum(
        local_mean_square - local_mean**2,
        0
    )

    features_list = {
        "Amplitude": amplitude,
        "Envelope": attribute_envelope,
        "Fase": attribute_phase,
        "Frequência": attribute_frequency,
        "RMS": attribute_rms,
        "Variância": attribute_variance
    }

    return features_list


def create_feature_matrix(
    features_list,
    selected_features=None
):

    if selected_features is None:
        selected_features = list(features_list.keys())

    columns = []

    for name in selected_features:

        if name == "Seno da fase":
            values = np.sin(features_list["Fase"])

        elif name == "Cosseno da fase":
            values = np.cos(features_list["Fase"])

        else:
            values = features_list[name]

        columns.append(values)

    # Empilhamento dos atributos — metodologia original
    voxel_features = np.stack(columns, axis=-1)

    X = voxel_features.reshape(
        -1, len(selected_features)
    )

    return X.astype(np.float32, copy=False)