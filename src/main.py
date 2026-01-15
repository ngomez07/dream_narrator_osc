import time
from audio_stream import AudioStream
from audio_buffer import AudioBuffer
from voice_detector import VoiceDetector
from config import VOICE_THRESHOLD, MIN_VOICE_FRAMES, MIN_SILENCE_FRAMES

detector = VoiceDetector(
    threshold=VOICE_THRESHOLD,
    min_voice_frames=MIN_VOICE_FRAMES,
    min_silence_frames=MIN_SILENCE_FRAMES)

def audio_callback(indata, frames, time_info, status):
    buffer.update(indata)

def main():
    global buffer

    buffer = AudioBuffer()
    audio = AudioStream(device=1)
    detector = VoiceDetector()

    audio.start(audio_callback)

    print("Escuchando micrófono...")

    try:
        while True:
            level = buffer.level
            event = detector.process(level)

            if event == "start":
                print("🎤 VOICE START")
            elif event == "end":
                print("🛑 VOICE END")

            time.sleep(0.05)

    except KeyboardInterrupt:
        audio.stop()

if __name__ == "__main__":
    main()

