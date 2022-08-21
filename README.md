# EmuGUI
What should I say? I didn't like the existing QEMU interfaces for Windows, so I made my own.

## Important note about update check

EmuGUI automatically checks for updates by default. No personal data is being shared while doing so. If you don't want this, you can disable it in settings.

## Mirrors

GitHub: https://github.com/Tech-FZ/EmuGUI

Codeberg: https://codeberg.org/lucien-rowan/EmuGUI

Pre-releases: https://codeberg.org/lucien-rowan/EmuGUI-PreRelease

## Versioning

Last update: 21st August, 2022 with 0.7.0.5100_dev

### Version number

Starting with 0.7, the versioning scheme looks like this:

Major: increments with every first feature update in a year

Minor: becomes 0 when major increments, else it increments with every feature update within a year

Micro: becomes 0 with every feature update, else increments by 1 with every bugfix update

Nano: is the build number

If "_dev" is added, it's a pre-release not meant for production.

### Version code

For the update checker, a version code is being used instead of the number. Here's how it increments:

| Update type | Next version code |
| ----------- | ----------------- |
| Preview update | current version code + 1 |
| Bugfix/minor update | current version code + 1|
| Feature update | current version code rounded up to the next hundred (e. g. 4237 becomes 4300) |

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
OS: Windows 8.1², Windows Server 2012 R2² or later (x64); Ubuntu 20.04, Debian 10, openSUSE Leap 15.3, openSUSE Tumbleweed, Fedora 35, RHEL 7, Arch Linux or distributions based on those (x64)

Python: 3.6 or newer

Processor: x64 Dual Core Processor with @2.6 GHz¹

RAM: 6 GB¹

HDD: 2 GB¹

¹ This is the absolute minimum, the required performance depends on the operating system you want to run.

² We try to continue host support on Windows 8.1 and Windows Server 2012 R2 until at least 14th February, 2023.

## Dependencies

- Python 3
- PyQt 6
- PySide 6
- QEMU
- Python Magic
- requests

## Installation (Windows)

1. Get QEMU at https://qemu.weilnetz.de/w64/ and install it
2. Get EmuGUI and extract it
3. Run main.exe in the EmuGUI directory.
4. Set the QEMU paths at the Settings/QEMU tab.
5. Create a new virtual machine and start it.

## Installation (Linux)

1. Open your terminal and type in one of the commands to update your system, depending on your distro:
- Arch: `sudo pacman -Syu`
- Debian/Ubuntu: `sudo apt-get update && sudo apt-get upgrade`
- Fedora/RHEL 8: `sudo dnf upgrade --refresh` or `sudo dnf update`
- Gentoo: `sudo emaint -a sync && sudo emerge --ask --verbose --update --deep --newuse @world`
- RHEL 7: `sudo yum update`
- SUSE and openSUSE Leap: `sudo zypper patch && sudo zypper up`
- openSUSE Tumbleweed: `sudo zypper patch && sudo zypper dup`

2. Open your terminal and type in one of the commands to install QEMU, depending on your distribution:
- Arch: `sudo pacman -S qemu`
- Debian/Ubuntu: `sudo apt-get install qemu`
- Fedora: `sudo dnf install @virtualization`
- Gentoo: `sudo emerge --ask app-emulation/qemu`
- RHEL: `sudo yum install qemu-kvm`
- (open-)SUSE: `sudo zypper install qemu`

3. Get EmuGUI from this website and extract it.
4. Run main in the EmuGUI directory (if it fails from file manager, open a terminal inside the directory and type `./main`).
5. Set the QEMU paths at the Settings/QEMU tab (either `/usr/bin/qemu-system-*` or just `qemu-system-*`).
6. Create a new virtual machine and start it.

Another tip: If you want a machine to run with KVM (`-enable-kvm` in the additional arguments), you must open a terminal inside the directory and type: `sudo ./main`.

## Updating EmuGUI

1. Close out of EmuGUI before updating.
2. Open your internet browser of choice and go to the EmuGUI repository.
3. If the most recent version of EmuGUI is newer than the one you're currently running, download and extract the EmuGUI zip file.
4. If you have external BIOS files in the root directory of your old EmuGUI installation, copy these into the root directory of the new one.
5. Start the new EmuGUI installation. You might need to reinstall some virtual machines.

## Building on Windows (Python Venv, Qt installed via Python)

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
13. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile --icon .\EmuGUI.ico .\main.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Python Venv, Qt installed via official installer)

1. Install Python. You can get it from https://www.python.org/
2. Get QEMU from https://qemu.weilnetz.de/w64/ and install it
3. Install Git. You can get it from https://git-scm.com/downloads
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Install Qt from the following site (you need a Qt account for that): https://www.qt.io/download-open-source?__hstc=152220518.4df0e407aa37c96fa5547ca135b274e3.1659787309440.1659787309440.1659787309440.1&__hssc=152220518.1.1659787309441&__hsfp=1951994995&hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5
6. You only need the Qt Creator.
7. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git` or `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
8. Open Visual Studio Code in that folder.
9. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
10. After that is done, type: `python -m venv your-venv-name`. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
11. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
12. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
13. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PySide6 python-magic-bin`
14. After this is done, run the main.py script.
15. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile --icon .\EmuGUI.ico .\main.py`
16. After that is finished, copy the code into the dist folder PyInstaller created.
17. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
18. If it works, have fun! If not, try to start again from number 9.

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
12. To compile the program for users who don't have Python installed, type: `& PyInstaller --onefile --icon .\EmuGUI.ico .\main.py`
13. After that is finished, copy the code into the dist folder PyInstaller created.
14. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
15. If it works, have fun! If not, try to start again from number 9.

## Building on Linux

1. Install Python 3. You can either compile the source code or get it from your distribution's repositories.
2. Install QEMU using one of the commands listed on Installation (Linux).
3. Install Git using the install command of your distribution.
4. Install Visual Studio Code. You can get it from https://code.visualstudio.com/download
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git` or `git clone https://codeberg.org/lucien-rowan/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python3 -m pip install --upgrade pip PyInstaller PyQt6 PyQt6-tools PySide6 python-magic`. You can try getting a VENV working but I personally have problems with using Python virtual environments on Linux.
8. After this is done, run the main.py script.
9. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile main.py` (for those who can get a VENV to work) or `python3 -m PyInstaller --onefile main.py`
10. After that is finished, copy the code into the dist folder PyInstaller created.
11. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
12. If it works, have fun! If not, try to start again from number 7.

## Documentation

A documentation of EmuGUI can be found at: https://tech-fz.github.io/EmuGUI-doc/

## Contributing

There are several ways to contribute, including:
- Programming (bugfixes, new features etc.)
- Testing (operating systems, the program itself etc.)
- Translation into foreign languages like German or French
- Documentation
