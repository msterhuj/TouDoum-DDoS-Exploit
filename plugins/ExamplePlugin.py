class Plugin:

    name = ""         # give a name to plugin
    description = ""  # describe what do this plugin
    author = ""       # your name here
    protocol = ""     # "TCP" "UDP" or "TCP|UDP"

    def __init__(self):
        pass

    def scan(self):
        pass

    def attack(self):
        pass