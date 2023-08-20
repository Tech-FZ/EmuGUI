#!/bin/bash

mkdir $HOME/EmuGUIVenv
python3 -m venv $HOME/EmuGUIVenv/emugui_venv
source $HOME/EmuGUIVenv/emugui_venv/bin/activate
$HOME/EmuGUIVenv/emugui_venv/bin/python -m pip install --upgrade pip PySide6 python-magic requests python-dateutil psutil
echo You can now run EmuGUI with "emugui_run_linux.sh"