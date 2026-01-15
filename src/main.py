import time
from osc_sender import OSCSender
from config import OSC_IP, OSC_PORT

def main():
    osc = OSCSender(ip=OSC_IP, port=OSC_PORT)

    print("Enviando prompts OSC cada 5 segundos...")
    while True:
        osc.send_prompt("test dream prompt from python")
        time.sleep(5)

if __name__ == "__main__":
    main()
