# from scapy.all import *

# def packet_callback(packet):
#     if packet.haslayer(ICMP):
#         icmp_packet = packet[ICMP]
#         print("ICMP Packet Information:")
#         print(f"Source IP: {icmp_packet.src}")
#         print(f"Destination IP: {icmp_packet.dst}")
#         print(f"Type: {icmp_packet.type}")
#         print(f"Code: {icmp_packet.code}")
#         print(f"ID: {icmp_packet.id}")
#         print(f"Sequence: {icmp_packet.seq}")
#         print(f"Load: {icmp_packet.load}")
#         print("=" * 30)

# def main():
#     sniff(prn=packet_callback, filter="icmp", store=0)

# if __name__ == '__main__':
#     main() 
from scapy.all import IP, ICMP, Raw, sniff


def packet_callback(packet):
    try:
        if not packet.haslayer(IP):
            return

        if not packet.haslayer(ICMP):
            return

        ip_layer = packet[IP]
        icmp_layer = packet[ICMP]

        print("\nICMP Packet Information:")
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Type           : {icmp_layer.type}")
        print(f"Code           : {icmp_layer.code}")
        print(f"ID             : {icmp_layer.id}")
        print(f"Sequence       : {icmp_layer.seq}")

        if packet.haslayer(Raw):
            print(f"Payload        : {packet[Raw].load}")
        else:
            print("Payload        : None")

        print("=" * 30)

    except Exception as e:
        print("Error:", e)


def main():
    print("Listening for ICMP packets...")
    sniff(
        filter="icmp",
        prn=packet_callback,
        store=False
    )


if __name__ == "__main__":
    main()