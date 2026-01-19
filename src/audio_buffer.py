import numpy as np
import time

class AudioBuffer:
    def __init__(self):
        self.level = 0.0
        self.reset_event()

    def reset_event(self):
        self.active = False
        self.start_time = None
        self.levels = []

    def start(self):
        self.active = True
        self.start_time = time.time()
        self.levels = []

    def update(self, indata):
        # RMS simple
        rms = float(np.sqrt(np.mean(indata**2)))
        self.level = rms

        if self.active:
            self.levels.append(rms)

    def end(self):
        if not self.active:
            return None

        duration = time.time() - self.start_time
        energy = sum(self.levels) / len(self.levels) if self.levels else 0
        peak = max(self.levels) if self.levels else 0

        event = {
            "duration": round(duration, 2),
            "energy": round(energy, 6),
            "peak": round(peak, 6)
        }

        self.reset_event()
        return event
