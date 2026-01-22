from perceptual_mapper import map_perception


class PromptEngine:
    def __init__(self, mode="rules", language="en"):
        self.mode = mode
        self.language = language

        self.listening_words = {
            "en": ["listening", "waiting"],
            "es": ["escucha", "espera"]
        }

    def generate(self, event: dict) -> str:
        base_words = map_perception(event, self.language)

        # --- Force 6 words -----------------------------------------
        extras = self.listening_words.get(
            self.language, self.listening_words["en"]
        )

        while len(base_words) < 6:
            base_words.append(extras[len(base_words) % len(extras)])

        return " ".join(base_words[:6])
