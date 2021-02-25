import socket


class Plugin:
    name = "Memcache"
    description = "scan and use memcache vulnerable server for amp attack"
    author = "@Msterhuj"
    protocol = "UDP"

    def __init__(self):
        pass

    def scan(self, ip: str, timeout: int):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(timeout)
        try:
            client.sendto(bytes("\x00\x00\x00\x00\x00\x01\x00\x00\x73\x74\x61\x74\x73\x0d\x0a", encoding='utf8'),
                          (ip, 11211))
            data = client.recvfrom(4096)
            length = len(data[0])
            return length > 200
        except KeyboardInterrupt:
            print("User request Ctrl + C Quitting.")
            exit(-1)
        except:
            return False
        finally:
            client.close()

    def attack(self):
        pass
