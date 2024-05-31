# EmuGUI
What should I say? I didn't like the existing QEMU interfaces for Windows, so I made my own.

## Mirrors

| Release | Link |
|---------|------|
| Stable  | [Link](https://github.com/Tech-FZ/EmuGUI) |
| Pre-releases | [Link](https://github.com/Tech-FZ/EmuGUI-PreRelease) |


## Versioning

Last update: 28th January, 2023 with 1.0.0.5307_b1

### Version number

Starting with 0.7, the versioning scheme looks like this:
| Feature | Content |
|--------|--------|
| Major | increments with every first feature update in a year |
| Minor | becomes 0 when major increments, else it increments with every feature update within a year |
| Micro | becomes 0 with every feature update, else increments by 1 with every bugfix update |
| Nano | is the build number |

If `_dev` is added, it's a pre-release not meant for production.

If `_b1` and a number are added, the EmuGUI version is in a state where minor features can still be added, but it starts to focus on stability. Generally, you shouldn't use it for production as it's still a pre-release.

If `_rc` and a number are added, the release is meant to be focused solely on stability and completeness, but still not for productive use.

### Version code

For the update checker, a version code is being used instead of the number. Here's how it increments:

| Update type | Next version code |
| ----------- | ----------------- |
| Preview update | current version code + 1 |
| Bugfix/minor update | current version code + 1 |
| Feature update | current version code rounded up to the next hundred (e. g. 4237 becomes 4300) |

## System requirements
| Component | Requirement |
|-------|--------|
| OS | Windows 10, Windows Server 2016 or later (x64); The latest (LTS) version of your Linux distribution (x64) |
| Python | 3.6 or newer |
| Processor | x64 Dual Core Processor with @2.6 GHz¹ |
| RAM | 6 GB¹ |
| HDD | 2 GB¹ |

*¹ This is the absolute minimum, the required performance depends on the operating system you want to run.*

## Dependencies

- Python 3
- PyQt 6
- PySide 6
- QEMU
- Python Magic
- requests

## Installation (Windows)

1. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
2. Get EmuGUI and extract it
3. Run emugui.exe in the EmuGUI directory.
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

3. Starting with EmuGUI 2.0, you also need to install (lib)xcb-cursor0 in order for this to work.
    - Arch: `sudo pacman -S libxcb-cursor`
    - Debian/Ubuntu: `sudo apt install libxcb-cursor-dev`
    - Fedora: `sudo dnf install libxcb-cursor`
    - Gentoo: `sudo emerge -av x11-libs/libxcb-cursor`
    - RHEL: `sudo yum install libxcb-cursor`
    - (open-)SUSE: `sudo zypper in libxcb-cursor`

4. Get EmuGUI from this website and extract it.
5. Run emugui in the EmuGUI directory (if it fails from file manager, open a terminal inside the directory and type `./emugui`).
6. Set the QEMU paths at the Settings/QEMU tab (either `/usr/bin/qemu-system-*` or just `qemu-system-*`).
7. Create a new virtual machine and start it.

**Another tip:** If you want a machine to run with KVM, you must open a terminal inside the directory and type: `sudo ./emugui`.

## Updating EmuGUI

1. Close out of EmuGUI before updating.
2. Open your internet browser of choice and go to the EmuGUI repository.
3. If the most recent version of EmuGUI is newer than the one you're currently running, download and extract the EmuGUI zip file.
4. If you have external BIOS files in the root directory of your old EmuGUI installation, copy these into the root directory of the new one.
5. Start the new EmuGUI installation. You might need to reinstall some virtual machines.

## Build Contents
- [Building on Windows (Python Venv, Qt installed via Python, with PyInstaller)](#building-on-windows-python-venv-qt-installed-via-python-with-pyinstaller)
- [Building on Windows (Python Venv, Qt installed via Python, with cx_Freeze)](#building-on-windows-python-venv-qt-installed-via-python-with-cx_freeze)
- [Building on Windows (Python Venv, Qt installed via official installer, with PyInstaller)](#building-on-windows-python-venv-qt-installed-via-official-installer-with-pyinstaller)
- [Building on Windows (Python Venv, Qt installed via official installer, with cx_Freeze)](#building-on-windows-python-venv-qt-installed-via-official-installer-with-cx_freeze)
- [Building on Windows (Anaconda, with PyInstaller)](#building-on-windows-anaconda-with-pyinstaller)
- [Building on Windows (Anaconda, with cx_Freeze)](#building-on-windows-anaconda-with-cx_Freeze)
- [Building on Linux (Python Venv, Qt installed via Python)](#building-on-linux-python-venv-qt-installed-via-python)
- [Building on Linux (Python Venv, Qt installed via official installer)](#building-on-linux-python-venv-qt-installed-via-official-installer)
- [Building on Linux (Anaconda)](#building-on-linux-anaconda)

## Building on Windows (Python Venv, Qt installed via Python, with PyInstaller)

1. Install Python. You can get it [here](https://www.python.org/)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
8. After that is done, type: `python -m venv your-venv-name` OUTSIDE of the code folder. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances.
9. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
10. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
11. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PyQt6 PyQt6-tools PySide6 python-magic-bin requests python-dateutil psutil`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile --icon .\EmuGUI.ico .\emugui.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Python Venv, Qt installed via Python, with cx_Freeze)

1. Install Python. You can get it [here](https://www.python.org/)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
6. Open Visual Studio Code in that folder.
7. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
8. After that is done, type: `python -m venv your-venv-name` OUTSIDE of the code folder. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances.
9. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
10. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
11. Within the terminal VS Code just opened, type: `pip install --upgrade pip cx_Freeze PyQt6 PyQt6-tools PySide6 python-magic-bin requests python-dateutil psutil`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `cxfreeze -c emugui.py --target-dir dist --icon EmuGUI.ico`
14. After that is finished, copy the code into the dist folder cx_Freeze created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Python Venv, Qt installed via official installer, with PyInstaller)

1. Install Python. You can get it [here](https://www.python.org)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Install Qt from the following [site](https://www.qt.io/download-open-source?__hstc=152220518.4df0e407aa37c96fa5547ca135b274e3.1659787309440.1659787309440.1659787309440.1&__hssc=152220518.1.1659787309441&__hsfp=1951994995&hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5) (you need a Qt account for that) 
6. You only need the Qt Creator.
7. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
8. Open Visual Studio Code in that folder.
9. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
10. After that is done, type: `python -m venv your-venv-name`. OUTSIDE of the code folder. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances.
11. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
12. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
13. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PySide6 python-magic-bin requests python-dateutil psutil`
14. After this is done, run the main.py script.
15. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile --icon .\EmuGUI.ico .\emugui.py`
16. After that is finished, copy the code into the dist folder PyInstaller created.
17. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
18. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Python Venv, Qt installed via official installer, with cx_Freeze)

1. Install Python. You can get it [here](https://www.python.org)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Install Qt from the following [site](https://www.qt.io/download-open-source?__hstc=152220518.4df0e407aa37c96fa5547ca135b274e3.1659787309440.1659787309440.1659787309440.1&__hssc=152220518.1.1659787309441&__hsfp=1951994995&hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5) (you need a Qt account for that) 
6. You only need the Qt Creator.
7. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
8. Open Visual Studio Code in that folder.
9. Open a terminal WITHIN VS Code and type: `python -m pip install --upgrade pip venv`
10. After that is done, type: `python -m venv your-venv-name`. OUTSIDE of the code folder. You can call it whatever you want, but don't forget that it is NOT allowed to get into the EmuGUI repository under any circumstances.
11. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
12. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
13. Within the terminal VS Code just opened, type: `pip install --upgrade pip cx_Freeze PySide6 python-magic-bin requests python-dateutil psutil`
14. After this is done, run the main.py script.
15. To compile the program for users who don't have Python installed, type: `cxfreeze -c emugui.py --target-dir dist --icon EmuGUI.ico`
16. After that is finished, copy the code into the dist folder cx_Freeze created.
17. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
18. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Anaconda, with PyInstaller)

1. Install Anaconda. You can get it from [here](https://www.anaconda.com/)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it from [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it from [here](https://code.visualstudio.com/download)
5. Install Qt. You can get it from [here](https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5)
6. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
7. Open Visual Studio Code in that folder.
8. Open Anaconda Navigator and create a new virtual environment.
9. Open the venv in VS Code and try to run a Python script with it.
10. Within the VS Code terminal, type: `& pip install --upgrade pip PyInstaller PySide6 python-magic-bin PyQt6 requests python-dateutil psutil`
11. After this is done, run the main.py script.
12. To compile the program for users who don't have Python installed, type: `& PyInstaller --onefile --icon .\EmuGUI.ico .\emugui.py`
13. After that is finished, copy the code into the dist folder PyInstaller created.
14. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
15. If it works, have fun! If not, try to start again from number 9.

## Building on Windows (Anaconda, with cx_Freeze)

1. Install Anaconda. You can get it from [here](https://www.anaconda.com/)
2. Get [QEMU](https://qemu.weilnetz.de/w64/) and install it
3. Install Git. You can get it from [here](https://git-scm.com/downloads)
4. Install Visual Studio Code. You can get it from [here](https://code.visualstudio.com/download)
5. Install Qt. You can get it from [here](https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5)
6. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
7. Open Visual Studio Code in that folder.
8. Open Anaconda Navigator and create a new virtual environment.
9. Open the venv in VS Code and try to run a Python script with it.
10. Within the VS Code terminal, type: `& pip install --upgrade pip cx_Freeze PySide6 python-magic-bin PyQt6 requests python-dateutil psutil`
11. After this is done, run the main.py script.
12. To compile the program for users who don't have Python installed, type: `& cxfreeze -c emugui.py --target-dir dist --icon EmuGUI.ico`
13. After that is finished, copy the code into the dist folder cx_Freeze created.
14. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
15. If it works, have fun! If not, try to start again from number 9.

## Building on Linux (Python Venv, Qt installed via Python)

1. Install Python 3. You can either compile the source code or get it from your distribution's repositories.
2. Install QEMU using one of the commands listed on [Installation (Linux)](#installation-linux).
3. Install Git and binutils using the install command of your distribution.
    - Arch: `sudo pacman -S git binutils`
    - Debian/Ubuntu: `sudo apt install git binutils`
    - Fedora: `sudo dnf install git binutils`
    - Gentoo: `sudo emerge -ask dev-vcs/git` for Git, `sudo emerge --ask --oneshot sys-devel/binutils` for binutils
    - RHEL: `sudo yum install git binutils`
    - (open-)SUSE: `sudo zypper in git binutils`

4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
6. As you already have the terminal open, install (lib)xcb-cursor0. Commands for that can be found on [Installation (Linux)](#installation-linux).
7. Open Visual Studio Code in that folder.
8. Open a terminal WITHIN VS Code and type: `python3 -m pip install --upgrade pip venv`
9. After that is done, type: `python3 -m venv your-venv-name`. OUTSIDE of the code folder. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
10. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
11. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
12. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PySide6 python-magic requests python-dateutil psutil pyqtdarktheme`
13. After this is done, run the main.py script.
14. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile emugui.py` (for those who can get a VENV to work) or `python3 -m PyInstaller --onefile emugui.py`
15. After that is finished, copy the code into the dist folder PyInstaller created.
16. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
17. If it works, have fun! If not, try to start again from number 7.

## Building on Linux (Python Venv, Qt installed via official installer)

1. Install Python 3. You can either compile the source code or get it from your distribution's repositories.
2. Install QEMU using one of the commands listed on [Installation (Linux)](#installation-linux).
3. Install Git and binutils using the install command of your distribution.
    - Arch: `sudo pacman -S git binutils`
    - Debian/Ubuntu: `sudo apt install git binutils`
    - Fedora: `sudo dnf install git binutils`
    - Gentoo: `sudo emerge -ask dev-vcs/git` for Git, `sudo emerge --ask --oneshot sys-devel/binutils` for binutils
    - RHEL: `sudo yum install git binutils`
    - (open-)SUSE: `sudo zypper in git binutils`

4. Install Visual Studio Code. You can get it [here](https://code.visualstudio.com/download)
5. Install Qt from the following [site](https://www.qt.io/download-open-source?__hstc=152220518.4df0e407aa37c96fa5547ca135b274e3.1659787309440.1659787309440.1659787309440.1&__hssc=152220518.1.1659787309441&__hsfp=1951994995&hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5) (you need a Qt account for that) 
6. You only need the Qt Creator.
7. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
8. As you already have the terminal open, install (lib)xcb-cursor0. Commands for that can be found on [Installation (Linux)](#installation-linux).
9. Open Visual Studio Code in that folder.
10. Open a terminal WITHIN VS Code and type: `python3 -m pip install --upgrade pip venv`
11. After that is done, type: `python3 -m venv your-venv-name`. OUTSIDE of the code folder. That's why Git is only going to be used to clone the code, but not to commit - that's to be done manually.
12. Wait until VS Code notices your venv and select it. You might need to restart the editor for it to recognize your virtual environment after it has been created.
13. With your virtual environment selected, try to run a Python script. If it throws an error, that's okay. We just need to activate the venv anyway.
14. Within the terminal VS Code just opened, type: `pip install --upgrade pip PyInstaller PySide6 python-magic requests python-dateutil psutil pyqtdarktheme`
15. After this is done, run the main.py script.
16. To compile the program for users who don't have Python installed, type: `PyInstaller --onefile .\emugui.py`
17. After that is finished, copy the code into the dist folder PyInstaller created.
18. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
19. If it works, have fun! If not, try to start again from number 9.

## Building on Linux (Anaconda)

1. Install Anaconda. You can get it from [here](https://www.anaconda.com/)
2. Install QEMU using one of the commands listed on [Installation (Linux)](#installation-linux).
3. Install Git and binutils using the install command of your distribution.
    - Arch: `sudo pacman -S git binutils`
    - Debian/Ubuntu: `sudo apt install git binutils`
    - Fedora: `sudo dnf install git binutils`
    - Gentoo: `sudo emerge -ask dev-vcs/git` for Git, `sudo emerge --ask --oneshot sys-devel/binutils` for binutils
    - RHEL: `sudo yum install git binutils`
    - (open-)SUSE: `sudo zypper in git binutils`

4. Install Visual Studio Code. You can get it from [here](https://code.visualstudio.com/download)
5. Install Qt. You can get it from [here](https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5)
6. Open a terminal and type: `git clone https://github.com/Tech-FZ/EmuGUI.git`
7. As you already have the terminal open, install (lib)xcb-cursor0. Commands for that can be found on [Installation (Linux)](#installation-linux).
8. Open Visual Studio Code in that folder.
9. Open Anaconda Navigator and create a new virtual environment.
10. Open the venv in VS Code and try to run a Python script with it.
11. Within the VS Code terminal, type: `& pip install --upgrade pip PyInstaller PySide6 python-magic PyQt6 requests python-dateutil psutil pyqtdarktheme`
12. After this is done, run the main.py script.
13. To compile the program for users who don't have Python installed, type: `& PyInstaller --onefile .\emugui.py`
14. After that is finished, copy the code into the dist folder PyInstaller created.
15. Run the executable in the dist folder. If your antivirus puts it into quarantine, don't worry as this should be a false positive and restore it.
16. If it works, have fun! If not, try to start again from number 9.

## Documentation

A documentation of EmuGUI can be found [here](https://github.com/Tech-FZ/EmuGUI/wiki)

## EmuGUI on Social Media

<a href="https://discord.gg/rTGpYCwF89">
  <img src="https://play-lh.googleusercontent.com/0oO5sAneb9lJP6l8c6DH4aj6f85qNpplQVHmPmbbBxAukDnlO7DarDW0b-kEIHa8SQ=s48-rw" alt="Discord Icon">
</a>

<a href="https://www.youtube.com/@EmuGUI-vr2xd">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/70px-YouTube_full-color_icon_%282017%29.svg.png" alt="YouTube Icon">
</a>

<a href="https://odysee.com/@EmuGUI:0">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFggUmAjv5TiQcgCt7BW-PKJpyrFvnAQBwYGX2lhU&s" alt="Odysee Icon" height="70px">
</a>

<a href="https://www.guilded.gg/i/pBAY6BAk">
  <img src="https://www.guilded.gg/asset/Logos/logomark/Color/Guilded_Logomark_Color.png?ver=3" alt="Guilded Icon" height="70px">
</a>

<!-- Discord: https://discord.gg/rTGpYCwF89 -->

## Contributing

There are several ways to contribute, including:
- Programming (bugfixes, new features etc.)
- Testing (operating systems, the program itself etc.)
- Translation into foreign languages like German or French
- Documentation

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

