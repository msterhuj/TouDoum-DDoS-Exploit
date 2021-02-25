import random
import socket
import struct


# credit : https://stackoverflow.com/a/51970598
class SendDNSPkt:
    def __init__(self, url: str, server_ip: str, timeout: int, port=53):
        self.url = url
        self.server_ip = server_ip
        self.port = port
        self.timeout = timeout

    def send_pkt(self):
        pkt = self._build_packet()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)
        sock.sendto(bytes(pkt), (self.server_ip, self.port))
        data, addr = sock.recvfrom(1024)
        sock.close()
        return data

    def _build_packet(self):
        randint = random.randint(0, 65535)
        packet = struct.pack(">H", randint)  # Query Ids (Just 1 for now)
        packet += struct.pack(">H", 0x0100)  # Flags
        packet += struct.pack(">H", 1)  # Questions
        packet += struct.pack(">H", 0)  # Answers
        packet += struct.pack(">H", 0)  # Authorities
        packet += struct.pack(">H", 0)  # Additional
        split_url = self.url.split(".")
        for part in split_url:
            packet += struct.pack("B", len(part))
            for s in part:
                packet += struct.pack('c', s.encode())
        packet += struct.pack("B", 0)  # End of String
        packet += struct.pack(">H", 1)  # Query Type
        packet += struct.pack(">H", 1)  # Query Class
        return packet


class Plugin:
    name = "DNS"
    description = "scan and use dns vulnerable server for amp attack"
    author = "@Msterhuj"
    protocol = "UDP"

    def __init__(self):
        pass

    def scan(self, ip: str, timeout: int, domain_name="www.google.com"):
        # replace 8.8.8.8 with your server IP!
        s = SendDNSPkt(domain_name, ip, timeout)
        status = False
        for _ in range(5):  # udp is unreliable.Packet loss may occur
            try:
                s.send_pkt()
                status = True
                break
            except KeyboardInterrupt:
                print("User request Ctrl + C Quitting.")
                exit(-1)
            except:
                pass
        return status

    def attack(self):
        pass
