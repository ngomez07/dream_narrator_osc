class PromptEngine:
    def __init__(self, mode="rules"):
        self.mode = mode

    def generate(self, voice_event):
        if self.mode == "rules":
            return self._rules_prompt(voice_event)

        # Placeholder para futuros modos
        return "abstract silent presence"

    def _rules_prompt(self, event):
        from prompt_logic import generate_prompt

        prompt = generate_prompt(event)

        # Garantizar máximo 6 palabras
        words = prompt.split()
        return " ".join(words[:6])
