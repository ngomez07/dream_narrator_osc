"# Dream Narrator OSC" 

src/
├── main.py                 # Orquestador general
├── audio_stream.py         # Captura de audio en tiempo real
├── speech_to_text.py       # STT streaming (ES / EN)
├── semantic_synth.py       # OpenAI: 6 palabras
├── prompt_logic.py         # Timer + cambio a "monito"
├── osc_sender.py           # OSC → TouchDesigner
└── config.py               # API keys, IPs, puertos

Prompt fijo → "a small monkey listening attentively"
