import struct
import random
import socket

def build_header():
    return struct.pack("!HHHHHH", random.randint(0, 65535), 0x0100, 1, 0,0,0)

print(build_header().hex(" "))
print(len(build_header()))