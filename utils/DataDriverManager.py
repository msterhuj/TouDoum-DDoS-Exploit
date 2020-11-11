import importlib
import re
from glob import glob
from columnar import columnar

function_require_plugin = [
    "__init__",
    "scan",
    "attack"
]
var_require_plugin = [
    "name",
    "description",
    "author",
    "protocol"
]


class PluginManager:
    plugins: list = []
    plugin_list_for_load = []

    # @arg plugin_list : list of plugin to load
    def __init__(self, plugin_list: str = "-"):
        self.plugin_list_for_load = plugin_list.split(',')
        self.load()

    # Load and initialise all plugin in plugins directory
    # Skip Plugin file named 'Example.py'
    def load(self):
        for plugin_file in glob("./plugins/*.py"):
            if "ExamplePlugin.py" not in plugin_file:
                plugin_file = plugin_file.replace("\\", "/")  # avoid windows directory cheat
                plugin_name = re.sub("\./plugins/|\.py", "", plugin_file)
                module = importlib.import_module("plugins." + plugin_name, ".")

                obj = module.Plugin()
                obj_content = dir(obj)

                # load all plugin of plugin given
                if self.plugin_list_for_load[0] == "-" or obj.name in self.plugin_list_for_load:
                    # check if plugin contain all default function for run
                    if len(set(obj_content) & set(function_require_plugin)) == 3:
                        # check if plugin information is set
                        if len(set(obj_content) & set(var_require_plugin)) == 4:
                            self.plugins.append(obj)
                        else:
                            print("Error the '" + plugin_name +
                                  "' plugin does not contain the required information to be correctly loaded")
                    else:
                        print("Error the '" + plugin_name +
                              "' plugin does not contain the required functions to be correctly loaded")

    def reload(self, plugin_list: str = "-"):
        self.plugins = []
        self.plugin_list_for_load = plugin_list.split(',')
        self.load()

    def plugin_loaded(self):
        return len(self.plugins)

    def print_plugins_list(self):
        col_headers = ['name', 'author', 'description']

        col_data = []

        for plugin in self.plugins:
            col_data.append([
                plugin.name,
                plugin.author,
                plugin.description
            ])

        print(columnar(col_data, col_headers, no_borders=True))
