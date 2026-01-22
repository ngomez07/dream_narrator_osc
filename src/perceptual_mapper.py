def map_perception(event: dict, language="en") -> list:
    """
    Devuelve una lista de palabras perceptuales (mínimo 4)
    """

    words = []

    # --- Dictionaries ---------------------------------------------
    vocab = {
        "en": {
            "time": ["fleeting", "lingering", "endless"],
            "energy": ["whispered", "soft", "violent"],
            "texture": ["smooth", "fragmented", "chaotic"],
            "core": "dream"
        },
        "es": {
            "time": ["fugaz", "persistente", "interminable"],
            "energy": ["susurrado", "suave", "violento"],
            "texture": ["suave", "fragmentado", "caótico"],
            "core": "sueño"
        }
    }

    v = vocab.get(language, vocab["en"])

    # --- Time ------------------------------------------------------
    duration = event.get("duration", 0)
    if duration < 1.5:
        words.append(v["time"][0])
    elif duration < 3.5:
        words.append(v["time"][1])
    else:
        words.append(v["time"][2])

    # --- Energy ----------------------------------------------------
    energy = event.get("energy", 0)
    if energy < 0.002:
        words.append(v["energy"][0])
    elif energy < 0.006:
        words.append(v["energy"][1])
    else:
        words.append(v["energy"][2])

    # --- Texture ---------------------------------------------------
    variance = event.get("variance", 0)
    if variance < 0.000002:
        words.append(v["texture"][0])
    elif variance < 0.00001:
        words.append(v["texture"][1])
    else:
        words.append(v["texture"][2])

    # --- Core concept ----------------------------------------------
    words.append(v["core"])

    return words
