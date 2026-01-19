import time
from audio_stream import AudioStream
from audio_buffer import AudioBuffer
from voice_detector import VoiceDetector
from config import VOICE_THRESHOLD, MIN_VOICE_FRAMES, MIN_SILENCE_FRAMES
from prompt_logic import generate_prompt
from osc_sender import OSCSender

osc = OSCSender(
    ip="192.168.44.234",  # tu IP actual
    port=8000
)

def audio_callback(indata, frames, time_info, status):
    buffer.update(indata)

def main():
    global buffer

    buffer = AudioBuffer()

    audio = AudioStream(device=1)

    detector = VoiceDetector(
        threshold=VOICE_THRESHOLD,
        min_voice_frames=MIN_VOICE_FRAMES,
        min_silence_frames=MIN_SILENCE_FRAMES
    )

    audio.start(audio_callback)

    print("Escuchando micrófono...")

    try:
        while True:
            level = buffer.level
            event = detector.process(level)

            if event == "start":
                print("🎤 VOICE START")
                buffer.start()

            elif event == "end":
                print("🔴 VOICE END")
                voice_event = buffer.end()
                print("📦 Evento:", voice_event)

                if voice_event:
                    prompt = generate_prompt(voice_event)
                    print("🌀 Prompt:", prompt)
                    osc.send_prompt(prompt)

            time.sleep(0.05)

    except KeyboardInterrupt:
        audio.stop()

if __name__ == "__main__":
    main()
