import json


class Driver:
    name: str = "File"
    description = "Store ip result in .json file"
    author = "@MsterHuj"

    data_file = "./config/data.json"
    file = None
    data = []

    def __init__(self):
        self.file = open(self.data_file, "w")
        pass

    def configure(self):
        self.data_file = input("Driver file : Enter file name with '.json' (default ./data.json): " or "./data.json")
        print("Driver file : setup success !")
        pass

    def save(self, data: list):
        pass
