import os
from dotenv import load_dotenv


class Config(object):
    __instance = None

    docker_mode: bool

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.docker_mode = os.environ.get("DOCKER_MODE", False)
        return cls.__instance

    def load(self):
        if not self.docker_mode:
            load_dotenv(".env")
