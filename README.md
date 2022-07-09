<<<<<<< HEAD
# EmuGUI
What should I say? I didn't like the existing QEMU interfaces for Windows, so I made my own.

## Mirrors

GitHub: https://github.com/Tech-FZ/EmuGUI

Codeberg: https://codeberg.org/lucien-rowan/EmuGUI

## We're Using GitHub Under Protest

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open issue](https://github.com/Tech-FZ/EmuGUI/issues/24) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please 
contact me at lucien-rowan#1916 on Discord so we can find a solution together.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)

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
- Python Magic

## Installation

1. Get QEMU at https://qemu.weilnetz.de/w64/ and install it
2. Get EmuGUI and extract it
3. Run main.exe in the EmuGUI directory.
4. Set the QEMU paths at the Settings/QEMU tab.
5. Create a new virtual machine and start it.

## Updating EmuGUI

1. Close out of EmuGUI before updating.
2. Open your internet browser of choice and go to the EmuGUI repository.
3. If the most recent version of EmuGUI is newer than the one you're currently running, download and extract the EmuGUI zip file.
4. If you have external BIOS files in the root directory of your old EmuGUI installation, copy these into the root directory of the new one.
5. Start the new EmuGUI installation. You might need to reinstall some virtual machines.

## Building on Windows (Python Venv)

1. Install Python. You can get it from https://www.python.org/
2. Get QEMU from https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git` or `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
8. After that is done, type: `python -m venv your-venv-name`. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
9. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
10. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
11. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PyQt6 PyQt6-tools PySide6 python-magic-bin`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile .\main.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Anaconda)

1. Install Anaconda. You can get it from here: https://www.anaconda.com/
2. Get QEMU from https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Install Qt. You can get it from here: https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5
6. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git` or `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
7. Open Visual Studio Code in that folder.
8. Open Anaconda Navigator and create a new virtual environment.
9. Open the venv in VS Code and try to run a Python script with it.
10. Within the VS Code terminal, type: `& pip install --upgrade pip PyInstaller PySide6 python-magic-bin PyQt6`
11. After this is done, run the main.py script.
12. To compile the program for users who don't have Python installed, type: `& PyInstaller --onefile .\main.py`
13. After that is finished, copy the code into the dist folder PyInstaller created.
14. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
15. If it works, have fun! If not, try to start again from number 9.

## Documentation

A documentation of EmuGUI can be found at: https://tech-fz.github.io/EmuGUI-doc/

## Contributing

There are several ways to contribute, including:
- Programming (bugfixes, new features etc.)
- Testing (operating systems, the program itself etc.)
- Translation into foreign languages like German or French
- Documentation
=======
# EmuGUI
What should I say? I didn't like the existing QEMU interfaces for Windows, so I made my own.

## New experimental mirror on Codeberg

This is an experimental mirror of EmuGUI which is also hosted on GitHub. If you still prefer the GitHub mirror, you can check here: https://github.com/Tech-FZ/EmuGUI

## We're Using GitHub Under Protest

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open issue](https://github.com/Tech-FZ/EmuGUI/issues/24) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please 
contact me at lucien-rowan#1916 on Discord so we can find a solution together.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)

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

## Updating EmuGUI

1. Close out of EmuGUI before updating.
2. Open your internet browser of choice and go to the EmuGUI repository.
3. If the most recent version of EmuGUI is newer than the one you're currently running, download and extract the EmuGUI zip file.
4. If you have external BIOS files in the root directory of your old EmuGUI installation, copy these into the root directory of the new one.
5. Start the new EmuGUI installation. You might need to reinstall some virtual machines.

## Building on Windows (Python Venv)

1. Install Python. You can get it from https://www.python.org/
2. Get QEMU from https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Open a terminal and type: `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
8. After that is done, type: `python -m venv your-venv-name`. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
9. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
10. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
11. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PyQt6 PyQt6-tools PySide6 python-magic-bin`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile .\main.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Anaconda)

1. Install Anaconda. You can get it from here: https://www.anaconda.com/
2. Get QEMU from https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Install Qt. You can get it from here: https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5
6. Open a terminal and type: `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
7. Open Visual Studio Code in that folder.
8. Open Anaconda Navigator and create a new virtual environment.
9. Open the venv in VS Code and try to run a Python script with it.
10. Within the VS Code terminal, type: `& pip install --upgrade pip PyInstaller PySide6 python-magic-bin PyQt6`
11. After this is done, run the main.py script.
12. To compile the program for users who don't have Python installed, type: `& PyInstaller --onefile .\main.py`
13. After that is finished, copy the code into the dist folder PyInstaller created.
14. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
15. If it works, have fun! If not, try to start again from number 9.

## Documentation

A documentation of EmuGUI can be found at: https://tech-fz.github.io/EmuGUI-doc/

## Contributing

There are several ways to contribute, including:
- Programming (bugfixes, new features etc.)
- Testing (operating systems, the program itself etc.)
- Translation into foreign languages like German or French
- Documentation
>>>>>>> b200ca3c0ce81a265284200b88555fe539b5d35b
