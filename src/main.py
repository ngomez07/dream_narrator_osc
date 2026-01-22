import time

from audio_stream import AudioStream
from audio_buffer import AudioBuffer
from voice_detector import VoiceDetector

from prompt_engine import PromptEngine
from osc_sender import OSCSender
from dream_state import DreamState

from audio_features import extract_features  # 👈 NUEVO

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

    # --- Core components -------------------------------------------
    buffer = AudioBuffer()
    audio = AudioStream(device=1)

    detector = VoiceDetector(
        threshold=VOICE_THRESHOLD,
        min_voice_frames=MIN_VOICE_FRAMES,
        min_silence_frames=MIN_SILENCE_FRAMES
    )

    prompt_engine = PromptEngine(mode="rules")
    dream_state = DreamState()

    osc = OSCSender(
        ip="172.16.0.120",  # tu IP actual
        port=8000
    )

    # --- Start audio ------------------------------------------------
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

                if voice_event and "audio" in voice_event:
                    # --- NEW: audio feature extraction -----------------
                    features = extract_features(voice_event["audio"])
                    print("🎛 Features:", features)

                    # --- Prompt generation -----------------------------
                    prompt = prompt_engine.generate({
                        **voice_event,
                        **features
                    })

                    print("🌀 Prompt:", prompt)
                    osc.send_prompt(prompt)

            time.sleep(0.05)

    except KeyboardInterrupt:
        audio.stop()
        print("Audio detenido.")


# --- Entry point ----------------------------------------------------

if __name__ == "__main__":
    main()
