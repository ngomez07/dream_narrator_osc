import time

from audio_stream import AudioStream
from audio_buffer import AudioBuffer
from voice_detector import VoiceDetector
from prompt_logic import generate_prompt
from osc_sender import OSCSender

from prompt_engine import PromptEngine

from config import (
    VOICE_THRESHOLD,
    MIN_VOICE_FRAMES,
    MIN_SILENCE_FRAMES
)


# --- Audio callback -------------------------------------------------

def audio_callback(indata, frames, time_info, status):
    buffer.update(indata)


# --- Main -----------------------------------------------------------

def main():
    global buffer

    # Audio + logic components
    buffer = AudioBuffer()
    audio = AudioStream(device=1)

    detector = VoiceDetector(
        threshold=VOICE_THRESHOLD,
        min_voice_frames=MIN_VOICE_FRAMES,
        min_silence_frames=MIN_SILENCE_FRAMES
    )

    osc = OSCSender(
        ip="172.16.0.120",  # usa tu IP real
        port=8000
    )

    prompt_engine = PromptEngine(mode="rules")

    # Start audio stream
    audio.start(audio_callback)
    print("Escuchando micrófono...")
    osc.send_prompt("Escuchando micrófono...")

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
                    prompt = prompt_engine.generate(voice_event)
                    print("🌀 Prompt:", prompt)
                    osc.send_prompt(prompt)

            time.sleep(0.05)

    except KeyboardInterrupt:
        audio.stop()
        print("Audio detenido.")


# --- Entry point ----------------------------------------------------

if __name__ == "__main__":
    main()
