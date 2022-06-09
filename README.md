# EmuGUI
What should I say? I didn't like the existing QEMU interfaces for Windows, so I made my own.

## System requirements
OS: Windows 8.1, Windows Server 2012 R2 or later (x64)

Python: 3.6 or newer

Processor: x64 Dual Core Processor with @2.6 GHz¹

RAM: 6 GB¹

HDD: 2 GB¹

¹ This is the absolute minimum, the required performance depends on the operating system system you want to run.

## Dependencies

- Python 3
- PyQt 6
- PySide 6
- QEMU

## Installation

1. Get QEMU at https://qemu.weilnetz.de/w64/ and install it
2. Get EmuGUI and extract it
3. Run main.exe in the EmuGUI directory.
4. Set the QEMU paths at the Settings/QEMU tab.
5. Create a new virtual machine and start it.

## Building on Windows

1. Install Python. You can get it from https://www.python.org/
2. Get QEMU at https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
8. After that is done, type: `python -m venv your-venv-name`. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
9. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
10. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
11. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PyQt6 PyQt6-tools PySide6`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile .\main.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Contributing

There are several ways to contribute, including:
- Programming (bugfixes, new features etc.)
- Testing (operating systems, the program itself etc.)
- Translation into foreign languages like German or French
- Documentation
