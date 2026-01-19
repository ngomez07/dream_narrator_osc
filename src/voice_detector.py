class VoiceDetector:
    def __init__(
        self,
        threshold=0.001,
        min_voice_frames=5,
        min_silence_frames=10
    ):
        self.threshold = threshold
        self.min_voice_frames = min_voice_frames
        self.min_silence_frames = min_silence_frames

        self.voice_frames = 0
        self.silence_frames = 0
        self.in_voice = False

    def process(self, level):
        if level > self.threshold:
            self.voice_frames += 1
            self.silence_frames = 0
        else:
            self.silence_frames += 1
            self.voice_frames = 0

        if not self.in_voice and self.voice_frames >= self.min_voice_frames:
            self.in_voice = True
            return "start"

        if self.in_voice and self.silence_frames >= self.min_silence_frames:
            self.in_voice = False
            return "end"

        return None
    
def reset(self):
    self.voice_frames = 0
    self.silence_frames = 0
    self.in_voice = False