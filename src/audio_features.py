import numpy as np


def extract_features(audio: np.ndarray) -> dict:
    """
    audio: numpy array shape (N, 1) or (N,)
    """

    if audio is None or len(audio) == 0:
        return {}

    # Flatten in case it's (N, 1)
    signal = audio.flatten()

    # --- Basic features --------------------------------------------
    peak = float(np.max(np.abs(signal)))
    rms = float(np.sqrt(np.mean(signal ** 2)))
    variance = float(np.var(signal))
    dynamic_range = float(np.max(signal) - np.min(signal))

    return {
        "peak_audio": round(peak, 6),
        "rms_audio": round(rms, 6),
        "variance": round(variance, 8),
        "dynamic_range": round(dynamic_range, 6)
    }
