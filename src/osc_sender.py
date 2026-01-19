from pythonosc.udp_client import SimpleUDPClient

class OSCSender:
    def __init__(self, ip="192.168.44.234", port=8000):
        self.client = SimpleUDPClient(ip, port)

    def send_prompt(self, prompt: str):
        self.client.send_message("/prompt", prompt)
