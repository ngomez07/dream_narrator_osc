import time
import numpy as np
from audio_stream import AudioStream

def audio_callback(indata, frames, time_info, status):
    volume = np.linalg.norm(indata)
    print(f"Audio level: {volume:.3f}")

def main():
    audio = AudioStream()
    audio.start(audio_callback)

    print("Micrófono activo. Ctrl+C para salir")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        audio.stop()
        print("Audio detenido")

if __name__ == "__main__":
    main()
