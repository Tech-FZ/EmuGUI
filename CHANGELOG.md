# EmuGUI v0.7.4.5110 (based on v0.7.3.5109)

## Changes compared to 0.7.3.5109

- On some Linux configurations, the main branch was prone to crash. While the fix was exclusive to the Linux binaries in the previous two updates, the main code should also be fixed now.
- Also, some more phrases and words have been (partially) translated into Ukrainian.
- Obsolete code which is no longer in use within EmuGUI has been either commented out or removed as a whole.

# EmuGUI v0.7.3.5109 (based on v0.7.2.5108)

## Changes compared to 0.7.2.5108

- I removed the OS support tables from OLD_FEATURES.md.
- In the main code, there was a bug which caused some Linux configurations to crash. This has been fixed with a try-catch block although an additional platform check must now be performed in the imports.
- Never has been translated into Ukrainian.

# EmuGUI v0.7.2.5108 (based on v0.7.1.5107)

## Changes compared to 0.7.1.5107

- I forgot to update OLD_FEATURES.md with 0.7.0.5106 - now I did it.
- And when we are already there, the TESTED.md file inside the doc folder has been depreciated in favour of the EmuGUI wiki on the stable repository on Codeberg.
- Also, I translated the "Start VM" button into Ukrainian as well.

# EmuGUI v0.7.1.5107 (based on v0.7.0.5106)

## Changes compared to 0.7.0.5106

- Worked on the Ukrainian translation again

# EmuGUI v0.7.0.5106 ("The comfort update", based on v0.7.0.5105_rc1)

## Changes compared to 0.6.7

- A fixed versioning scheme is on README.md.
- Fixed a spelling mistake on doc/OLD_FEATURES.md.
- The combo boxes can now be translated for the most part.
- Changed documentation to EmuGUI wiki.
- Added a basic contribution guide.
- Good news: You will now tell EmuGUI if and how to handle VHDs beforehand (instead of after selecting it).
- The formatting issues on README.md have been fixed.
- Also, "Let QEMU decide" has been translated into German in the entire program.
- I also made a small easteregg. Let's see if you can find it.

# EmuGUI v0.7.0.5105_rc1 (based on v0.7.0.5104_dev)

- The versioning scheme has been updated again.
- The combobox on the VHD usage has been translated into German.
- I also corrected the upper-/lowercase where the VHD mode should be added. (isEnabled instead of isenabled)

# EmuGUI v0.7.0.5104_dev (based on v0.7.0.5103_dev)

- Changed documentation to EmuGUI wiki.
- Added a basic contribution guide.
- Good news: You will now tell EmuGUI if and how to handle VHDs beforehand (instead of after selecting it).

# EmuGUI v0.7.0.5103_dev (based on v0.7.0.5102_dev)

- Removed the old component dependency code which was commented out in the previous build.
- Fixing a VHD problem which prevents you from booting VMs without a hard drive.

# EmuGUI v0.7.0.5102_dev (based on v0.7.0.5101_dev)

- Worrying that you have to install too much? No longer necessary, because you no longer need everything from QEMU to use EmuGUI.

# EmuGUI v0.7.0.5101_dev (based on v0.7.0.5100_dev)

- The formatting issues on README.md have been fixed.
- Also, "Let QEMU decide" has been translated into German in the entire program.

# EmuGUI v0.7.0.5100_dev (based on v0.6.6)

- A fixed versioning scheme is on README.md.
- Fixed a spelling mistake on doc/OLD_FEATURES.md.
- The combo boxes in the settings can now be translated.

# EmuGUI v0.6.7 (based on v0.6.6)

- You can now boot virtual machines without VHDs (backported from v0.7.0.5103)

# EmuGUI v0.6.6

- Some formatting issues have been corrected.
- The update checker has been prepared for future development of feature updates.
- The pre-release mirror has been added to README.md.
- Translated the VHD exists dialog into German.

# EmuGUI v0.6.5

- The Windows 2000 checkbox is now depreciated and is going to be removed in a future update.
- TESTED.md has been updated as such.
- A new file, OLD_FEATURES.md, has been added.

# EmuGUI v0.6.4

- Reduced the number of required restarts by putting the incorporate code into a seperate except clause for every language block.

# EmuGUI v0.6.3

- Added a restart dialog for general settings

# EmuGUI v0.6.2

- Floppy & CD code for Linux has been added, what I forgot with the 0.5 lineup.
- Altered the floppy code so QEMU doesn't complain anymore.
- At least you can use EmuGUI normally now, except you can't change the language too often in a single session.

# EmuGUI v0.6.1

- A spacing mistake has been fixed.
- The editing VM dialog had a bug which sometimes didn't apply the actual architecture of the VM.
- I tried to fix a language bug but it failed. For now, if the editing VM dialog doesn't open, restart EmuGUI.

# EmuGUI v0.6

- A dialog for VMs which are created with a version of EmuGUI too new has been added.
- The most of EmuGUI is now translated into English, German, and also, English with parts of Ukrainian is supported
- Added a section for Windows users who can't install Qt via pip.
- Also, a note about the update checker has been added to README.md.
- To make translating a bit easier, "About" has been changed to "About EmuGUI"
- PowerPC 64-bit and MIPSel 32-bit architectures have been added.
- Thanks to BasDeGamer for fixing the spelling mistake on README.md. Credits to him or her go to CONTRIBUTORS.md.
- Also, I fear that I violated an Ukrainian grammar rule in the main menu tab (hopefully fixed).

# EmuGUI v0.5.2

- The updater also closes now when clicking "Yes".

# EmuGUI v0.5.1

- Windows 8.1 and Windows Server 2012 R2 users are now notified about end of support for EmuGUI.
- README.md has been updated as such.

# EmuGUI v0.5

- Updated TESTED.md
- Updated README.md
- An update checker has been added
- ARM-based VMs can now run with standard VGA
- You can now select between several USB controllers.
- This script can now be run on Linux.
- Installation and building instructions for Linux have been added to README.md.
- If you start a virtual machine, there is now a message at the bottom of the window which could be helpful when debugging.
- There is now a window which warns you if your VM uses the depreciated USB checkbox.
- The icon is now present on the windows as well.

# EmuGUI v0.4.2

- Added compiling instructions for Anaconda to README.md
- Resolved an issue which caused some virtual machines to be impossible to create

# EmuGUI v0.4.1

- Fixed an issue which caused USB input devices on ARM machines not to be accepted because USB support was being initialized too late.
- To do that, I had to specify an USB 1.1 controller in the VM bootcode.
- Also, to make it easier, USB support is enabled automatically if you decide to use an USB device.
- With that, a network issue has been caused on ARM emulator instances. That has been fixed by adding the virtio-net-device.
- Updated TESTED.md

# EmuGUI v0.4

- Updated TESTED.md
- Commented the code
- Fixed a raw issue
- Added USB support
- The USB Tablet checkbox is now depreciated and will be removed in a future update.
- Added USB keyboard support
- Added experimental ARM support
- Added python-magic instructions to README.md

# EmuGUI v0.3

- Updated TESTED.md
- Added extended mouse support (experimental)
- Added support for aarch64 virtual machines
- Added support for multiple cores
- Added some legal stuff

# EmuGUI v0.2.3

- Updated TESTED.md
- (Hopefully) fixed the Linux-specific argument issue by...
- ...adding an option to let QEMU decide where to boot from
- ...correcting "initrid" to "initrd" in the start VM code
- Corrected a grammar issue in README.md
- Corrected a spelling mistake of "initrd" in the VM creation/editing dialog
- Corrected an issue which caused the VHD exists dialog to appear when you selected the Linux kernel and initrd files

# EmuGUI v0.2.2

- (Hopefully) fixed a bug that caused additional arguments to be saved in the external BIOS variables as well
- With that, Windows NT 4.0 MIPS should also work again.

# EmuGUI v0.2.1

- Updated TESTED.md
- Fixed an issue causing some "Previous" buttons in the VM creation/editing dialog to no longer work
- Added update documentation to README.md.

# EmuGUI v0.2

- Updated README.md so terminal commands are formatted like such
- Updated TESTED.md
- Added Doumentation info in README.md
- Removed Reset button from the QEMU settings
- Removed Browse button from the BIOS location part of VM creating/editing feature
- Removed quotes from BIOS location addition line in starting VM
- Added experimental sound card support
- Added experimental Linux parameter support (kernel, intrid, cmd arguments)
- Windows binaries now use Python 3.9.13 instead of Python 3.9.12
- In the PowerPC machines there is some compatibility stuff now.

# EmuGUI v0.1

- added TESTED.md
- added building instructions for Windows
- fixed the VM creation/editing bug

# EmuGUI v0.0.1

- Capabilities to run i386, x86_64, mips64el and ppc operating systems via QEMU
- Added documentation
