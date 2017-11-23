import os
import importlib


class PluginRadio():
    def __init__(self):
        self.folder = 'plugins'
        self.list = self.get_list()
        self.plugins = []

    def get_list(self):
        list_plug = os.listdir(self.folder)
        plugins = []
        for plugin in list_plug:
            if '.py' in plugin and '__' not in plugin:
                plugins.append(self.folder + '.' + plugin.replace('.py', ''))
        return plugins

    def load_plugins(self):
        for plugin in self.list:
            self.plugins.append(self.load_plugin(plugin))

    def load_plugin(self, plugin):
        return importlib.import_module(plugin, '.')
