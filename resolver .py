import struct
import random
import socket

def build_header():
    return struct.pack("!HHHHHH", random.randint(0, 65535), 0x0100, 1, 0,0,0)

def encode_name(domain):
    result = b""
    for part in domain.split("."):
        result += struct.pack("B", len(part)) + part.encode()
    return result + b"\x00"

