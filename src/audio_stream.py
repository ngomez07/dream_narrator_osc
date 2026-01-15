import sounddevice as sd

class AudioStream:
    def __init__(self, samplerate=16000, channels=1, blocksize=1024, device=None):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize
        self.device = device
        self.stream = None

    def start(self, callback):
        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            blocksize=self.blocksize,
            device=self.device,
            callback=callback
        )
        self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
