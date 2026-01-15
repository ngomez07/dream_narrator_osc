import time
from audio_stream import AudioStream
from audio_buffer import AudioBuffer

def main():
    buffer = AudioBuffer(window_seconds=5)
    audio = AudioStream()

    def audio_callback(indata, frames, time_info, status):
        buffer.add_audio(indata)

    audio.start(audio_callback)

    print("Grabando audio en ventanas de 5 segundos...")
    try:
        while True:
            time.sleep(0.1)
            if buffer.should_emit():
                window = buffer.get_window()
                print(f"Ventana lista: {len(window)} muestras")
    except KeyboardInterrupt:
        audio.stop()
        print("Audio detenido")

if __name__ == "__main__":
    main()
