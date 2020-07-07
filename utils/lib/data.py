import jsonpickle as json


def load(filename: str):
    try:
        with open(filename, 'r') as file:
            d = file.read().replace("\n", "")
            return json.decode(d)
    except FileNotFoundError:
        return Data(filename)


class Data:
    def __init__(self, filename: str):
        self.filename = filename
        self.memcached = []
        self.dns = []
        self.ntp = []

    def add_dns(self, ip: str):
        if ip not in self.dns:
            self.dns.append(ip)

    def add_ntp(self, ip: str):
        if ip not in self.ntp:
            self.ntp.append(ip)

    def add_memcached(self, ip: str):
        if ip not in self.memcached:
            self.memcached.append(ip)

    def get_all(self):
        return [self.memcached, self.dns, self.dns]

    def save(self):
        with open(self.filename, 'w+') as file:
            file.write(json.encode(self))
            file.close()
