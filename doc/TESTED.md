# Compatible guests list

Such a program needs tests in its lifetime. That's why I make this compatibility list. Feel free to grab your old installation disc and test it out.

## Microsoft operating systems

| Operating system                           | Architecture | Working   | Notes                                                                          |
| ------------------------------------------ | ------------ | --------- | ------------------------------------------------------------------------------ |
| Windows 95 C                               | i386         | Yes       |                                                                                |
| Windows NT 4.0 Workstation Service Pack 1  | MIPS64el     | Yes       | Needs external BIOS                                                            |
| Windows NT 4.0 Workstation Service Pack 1  | i386         | Yes       | Use only 256 colors and 800x600 pixels or else there are mouse problems        |
| Windows NT 4.0 Workstation Service Pack 6a | i386         | Yes       | Use only 256 colors and 800x600 pixels or else there are mouse problems        |
| Windows 98 Second Edition                  | i386         | Partially | Prepare to boot Safe Mode with VBox; don't add sound card to installed systems |
| Windows 2000 Professional Service Pack 4   | i386         | No        |                                                                                |
| Windows XP Home Edition Service Pack 3     | i386         | Yes       |                                                                                |
| Windows Vista Ultimate Service Pack 2      | i386         | Yes       | Aero not available despite drivers being available                             |
| Windows 7 Ultimate Service Pack 1          | x86_64       | Yes       | No VGA drivers, no Aero                                                        |

## Mac operating systems

| Operating system                          | Architecture | Working   | Notes                                                                          |
| ----------------------------------------- | ------------ | --------- | ------------------------------------------------------------------------------ |
| Mac OS X 10.5.6 Snow Leopard              | PowerPC      | No        | To be honest, the installer suggested something I haven't tried yet.           |

## Linux operating systems

### Ubuntu-based distributions

| Operating system                          | Architecture | Working   | Notes                                                                            |
| ----------------------------------------- | ------------ | --------- | -------------------------------------------------------------------------------- |
| Ubuntu Desktop 12.04 LTS                  | PowerPC      | Partially | Severe mouse issues, never ever use any GUI on this distribution at anytime      |

### SUSE-based distributions

| Operating system                          | Architecture | Working   | Notes                                                                            |
| ----------------------------------------- | ------------ | --------- | -------------------------------------------------------------------------------- |
| openSUSE Leap 15.4                        | Aarch64      | No        | Installation is impossible                                                       |
| openSUSE Tumbleweed                       | Aarch64      | Partially | For networking, please take the preinstalled Xfce image. Terminal only.          |
