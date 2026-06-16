
from scapy.all import IP, ICMP, Raw, send, sniff


def modify_icmp_packet(packet):
    try:
        # Đảm bảo packet có cả IP và ICMP
        if not packet.haslayer(IP):
            return

        if not packet.haslayer(ICMP):
            return

        ip_layer = packet[IP]
        icmp_layer = packet[ICMP]

        print("\n===== ORIGINAL ICMP PACKET =====")
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

        # Tạo packet mới
        new_payload = b"This is a modified ICMP packet."

        new_packet = (
            IP(src=ip_layer.dst, dst=ip_layer.src)
            / ICMP(
                type=icmp_layer.type,
                code=icmp_layer.code,
                id=icmp_layer.id,
                seq=icmp_layer.seq
            )
            / Raw(load=new_payload)
        )

        print("\n===== MODIFIED ICMP PACKET =====")
        print(f"Source IP      : {new_packet[IP].src}")
        print(f"Destination IP : {new_packet[IP].dst}")
        print(f"Payload        : {new_payload}")

        print("=" * 50)

        send(new_packet, verbose=False)

    except Exception as e:
        print("ERROR:", e)


def main():
    print("Listening for ICMP packets...")
    sniff(
        filter="icmp",
        prn=modify_icmp_packet,
        store=False
    )


if __name__ == "__main__":
    main()