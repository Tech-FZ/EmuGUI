import json
import os
import services.pathfinder as pf

def read_hw_plugin():
    exec_folder = pf.retrieveExecFolder()
    pluginContent = []
    pluginFiles = [f for f in os.listdir(f"{exec_folder}plugins/hw_additions") if os.path.isfile(os.path.join(f"{exec_folder}plugins/hw_additions", f))]

    for plugin in pluginFiles:
        with open(f"{exec_folder}plugins/hw_additions/{plugin}", "r+") as pluginFile:
            jsonplugin = json.load(pluginFile)
            pluginContent.append(jsonplugin)

    return pluginContent