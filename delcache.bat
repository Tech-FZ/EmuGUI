@echo off

if exist dialogExecution\__pycache__\ (
    del dialogExecution\__pycache__\*.* /q
    rd dialogExecution\__pycache__\ 
)

if exist errors\__pycache__\ (
    del errors\__pycache__\*.* /q
    rd errors\__pycache__\ 
)

if exist platformSpecific\__pycache__\ (
    del platformSpecific\__pycache__\*.* /q
    rd platformSpecific\__pycache__\ 
)

if exist translations\__pycache__\ (
    del translations\__pycache__\*.* /q
    rd translations\__pycache__\ 
)

if exist uiScripts\__pycache__\ (
    del uiScripts\__pycache__\*.* /q
    rd uiScripts\__pycache__\ 
)

if exist plugins\pluginmgr\__pycache__\ (
    del plugins\pluginmgr\__pycache__\*.* /q
    rd plugins\pluginmgr\__pycache__\ 
)