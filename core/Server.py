import iptools
import os
from flask import Flask


class Server:
    app = Flask("TouDoum !")

    ip_list = []

    ip_range_list: iptools.IpRangeList
    current_ip: str

    def __init__(self, ip_range_list, host="0.0.0.0", port="80"):
        #  self.ip_range_list = iptools.IpRangeList(ip_range_list).__iter__()
        self.app.run(host=os.environ.get("SERVER_LISTEN"), port=os.environ.get("SERVER_PORT"))

    app.route("/api/")
    def next_ip(self):
        try:
            self.current_ip = iptools.next(self.ip_range_list)
            return str(self.current_ip)
        except StopIteration:
            return 0
