class DreamState:
    def __init__(self):
        self.last_narrative = None

    def update(self, narrative):
        self.last_narrative = narrative

    def clear(self):
        self.last_narrative = None