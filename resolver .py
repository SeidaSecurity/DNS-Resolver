import struct
import random
import socket

def build_header():
    #Build a DNS query header, "! for big-endian, H for unsigned short (2 bytes)", random ID, flags set to 0x0100 for a recursive query, QDCOUNT=1, ANCOUNT=0, NSCOUNT=0, ARCOUNT=0
    return struct.pack("!HHHHHH", random.randint(0, 65535), 0x0100, 1, 0,0,0)

def encode_name(domain):
    #store domain name in byte format, each label prefixed with its length, and terminated with a null byte
    result = b""
    for part in domain.split("."):
        result += struct.pack("B", len(part)) + part.encode()
    return result + b"\x00"

def send_query(packet, server="8.8.8.8"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    sock.sendto(packet, (server,53))
    response, _ = sock.recvfrom(1024)
    sock.close()
    return response

if __name__ == "__main__":
    question = encode_name("www.example.com") + struct.pack("!HH", 1, 1)  # QTYPE=A, QCLASS=IN
    packet = build_header() + question
    response = send_query(packet)
    print(f"Got {len(response)} bytes in response:")
    print(response.hex(" "))