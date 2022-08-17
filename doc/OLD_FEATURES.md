# Old features of EmuGUI

As features come, they also have to go! That's for every program. EmuGUI heavily relies on QEMU and therefore, has to fit the emulator. Here you can see what is depreciated/removed and EmuGUI's depreciation policy.

## Features of EmuGUI

### Depreciation policy of features

EmuGUI's depreciation policy for built-in features is as follows: When one feature gets depreciated, e.g. because a better solution has been made or it simply doesn't do its job anymore, it will be removed after ten other feature levels. The first feature level (the second/minor number of EmuGUI's version string) to depreciate a feature doesn't count, for example, if version 0.4 depreciates the USB Tablet checkbox, the counting begins at 0.5 (0.5 = 1; 0.6 = 2; ... 0.14 = 10) and it would not be removed until 0.15.x. That way, you hopefully have got enough time to migrate your VMs before it's completely removed (although you could even change it when it's removed already, I guess).

### Features to be removed

| Feature | State | Depreciated/Removed since | Minimum number of feature levels left | Reason for depreciation |
| ------- | ----- | ------------------------- | ------------------------------------- | ----------------------- |
| USB Tablet checkbox | Depreciated | 0.4 | 8 | A combobox with more possibilities has been created |
| Windows 2000 checkbox | Depreciated | 0.6.5 | 10 | Rather prevents you from installing the OS in question then helping you |

## Supported host operating systems

### Host depreciation policy

This is only for orientation and may not apply because of technical problems. Generally, an operating system is supported until its End of Life or until one of EmuGUI's dependencies is no longer going to run on there. Also, this does NOT apply as soon as EmuGUI's development is stopped completely.

#### Windows

Microsoft normally supports Windows versions until five to ten years and while doing so, releases security updates every month. As such, I try to support a version of Windows one month after the end of its general Extended Support (ESU doesn't count). However, it might not be possible for some reason (which is the case on Windows Server 2012).

| Operating system | Estimated end of EmuGUI's host support |
| ---------------- | -------------------------------------- |
| Windows 8.1 and Server 2012 R2 | 14th February, 2023 |
| Windows 10 Enterprise LTSB 2015, Windows 10, Version 1507 and 1511 | 11th November, 2025 |
| Windows 10 Enterprise LTSB 2016, Windows 10, Version 1607-1803, Windows Server 2016, Windows Server, Version 1803 | 16th February, 2027 |
| Windows 10 Enterprise LTSC 2019, Windows 10, Version 1809-21H1, Windows Server 2019, Windows Server, Version 1809-20H2 | 6th February, 2029 |
| Windows 10 Enterprise LTSC 2021, Windows 10, Version 21H2 and later, Windows Server 2022, Windows 11, Version 21H2 | 17th February, 2032 |

#### Linux

On Linux, this does get more complicated as there are so many distributions out there which are abandoned faster. Generally, EmuGUI support ends if a distro goes End of Life.

| Operating system | Estimated end of EmuGUI's host support |
| ---------------- | -------------------------------------- |
| Fedora 35 | 31st November, 2022 |
| Debian 11 | 31st July, 2024 |
| Ubuntu 20.04 | 31st April, 2025 |
| Ubuntu 22.04 | 31st April, 2027 |