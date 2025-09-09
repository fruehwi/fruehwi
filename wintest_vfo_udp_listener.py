import socket

UDP_IP = "127.0.0.1"  # Listen on localhost
UDP_PORT = 12050      # Default Win-Test UDP port
OUTPUT_FILE = "vfo_frequency.txt"

def extract_frequency(message):
    # Adjust this parser for your Win-Test UDP message format
    # Example expected message: "FREQ:14074.0 MODE:FT8"
    if "FREQ:" in message:
        try:
            freq = message.split("FREQ:")[1].split()[0]
            return freq
        except Exception:
            return None
    return None

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode("utf-8", errors="ignore")
        freq = extract_frequency(message)
        if freq:
            with open(OUTPUT_FILE, "w") as f:
                f.write(freq)
            print(f"Frequency written: {freq}")

if __name__ == "__main__":
    main()