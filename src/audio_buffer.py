import numpy as np
import time

class AudioBuffer:
    def __init__(self, samplerate=16000, window_seconds=5):
        self.samplerate = samplerate
        self.window_seconds = window_seconds
        self.max_samples = samplerate * window_seconds
        self.buffer = np.zeros((0,), dtype=np.float32)
        self.last_emit_time = time.time()

    def add_audio(self, audio_chunk):
        """
        audio_chunk: numpy array (frames, channels)
        """
        audio_chunk = audio_chunk.flatten()
        self.buffer = np.concatenate((self.buffer, audio_chunk))

        # Mantener tamaño máximo
        if len(self.buffer) > self.max_samples:
            self.buffer = self.buffer[-self.max_samples:]

    def should_emit(self):
        return (time.time() - self.last_emit_time) >= self.window_seconds

    def get_window(self):
        self.last_emit_time = time.time()
        return np.copy(self.buffer)
