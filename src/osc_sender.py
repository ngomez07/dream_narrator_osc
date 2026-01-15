from pythonosc.udp_client import SimpleUDPClient

class OSCSender:
    def __init__(self, ip="127.0.0.1", port=8000):
        self.client = SimpleUDPClient(ip, port)

    def send_prompt(self, prompt: str):
        self.client.send_message("/prompt", prompt)
