import sounddevice as sd

class AudioStream:
    def __init__(self, samplerate=16000, channels=1, blocksize=1024):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize
        self.stream = None

    def start(self, callback):
        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            blocksize=self.blocksize,
            callback=callback
        )
        self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
