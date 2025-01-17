from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"\n[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        
        # Check for TCP layer and print relevant details
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP | Src Port: {tcp_layer.sport} | Dst Port: {tcp_layer.dport}")
        
        # Check for UDP layer and print relevant details
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print(f"Protocol: UDP | Src Port: {udp_layer.sport} | Dst Port: {udp_layer.dport}")
        
        # Check for Raw layer (payload) and print a snippet of it
        if packet.haslayer(Raw):
            raw_layer = packet[Raw]
            payload = raw_layer.load
            print(f"Payload: {payload[:50]}...")  # Print first 50 bytes of payload
        else:
            print("No payload data")

# Sniff packets on the network interface
sniff(filter="ip", prn=packet_callback, store=0)
