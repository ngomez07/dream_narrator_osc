def generate_prompt(event):
    duration = event["duration"]
    energy = event["energy"]
    peak = event["peak"]

    # Qualifiers by duration
    if duration < 1.5:
        time_word = "fleeting"
    elif duration < 3.5:
        time_word = "lingering"
    else:
        time_word = "extended"

    # Qualifiers by energy
    if energy < 0.003:
        energy_word = "whispered"
    elif energy < 0.008:
        energy_word = "soft"
    else:
        energy_word = "intense"

    # Qualifiers by peak
    if peak < 0.01:
        texture_word = "blurred"
    elif peak < 0.02:
        texture_word = "fragmented"
    else:
        texture_word = "sharp"

    return f"{energy_word} {texture_word} dream {time_word}"
