import json
import os

def read_hw_plugin():
    pluginContent = []
    pluginFiles = [f for f in os.listdir("./plugins/hw_additions") if os.path.isfile(os.path.join("./plugins/hw_additions", f))]

    for plugin in pluginFiles:
        with open(f"./plugins/hw_additions/{plugin}", "r+") as pluginFile:
            jsonplugin = json.load(pluginFile)
            pluginContent.append(jsonplugin)

    return pluginContent