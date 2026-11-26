import numpy as np
import segyio


def load_segy_manual_2d_final(filepath):

    with segyio.open(
        str(filepath), "r", ignore_geometry=True
    ) as segyfile:

        n_traces = segyfile.tracecount
        n_samples = len(segyfile.samples)

        # Leitura sequencial dos traços sísmicos
        all_traces = np.empty(
            (n_traces, n_samples),
            dtype=np.float32
        )

        for i, trace in enumerate(segyfile.trace):
            all_traces[i] = trace

        # Preservar a estrutura do notebook original
        n_inlines = n_traces
        n_crosslines = 1

        data = all_traces.reshape(
            n_inlines, n_crosslines, n_samples
        )

        # Índices dos traços
        inlines_idx = np.arange(n_inlines)
        crosslines_idx = np.arange(n_crosslines)

        # Amostras temporais
        times = np.array(segyfile.samples, copy=True)

    return data, inlines_idx, crosslines_idx, times