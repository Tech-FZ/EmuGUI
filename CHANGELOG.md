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
