#!/bin/bash

source $HOME/EmuGUIVenv/emugui_venv/bin/activate
$HOME/EmuGUIVenv/emugui_venv/bin/python -m pip install --upgrade pip PySide6 python-magic requests python-dateutil psutil
$HOME/EmuGUIVenv/emugui_venv/bin/python ./emugui.py