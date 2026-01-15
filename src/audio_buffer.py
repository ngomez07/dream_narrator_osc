import numpy as np

class AudioBuffer:
    def __init__(self):
        self.level = 0.0

    def update(self, indata):
        # RMS simple
        self.level = float(np.sqrt(np.mean(indata**2)))
