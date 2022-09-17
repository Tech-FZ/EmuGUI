# Old features of EmuGUI

As features come, they also have to go! That's for every program. EmuGUI heavily relies on QEMU and therefore, has to fit the emulator. Here you can see what is depreciated/removed and EmuGUI's depreciation policy.

## Features of EmuGUI

### Depreciation policy of features

EmuGUI's depreciation policy for built-in features is as follows: When one feature gets depreciated, e.g. because a better solution has been made or it simply doesn't do its job anymore, it will be removed after ten other feature levels. The first feature level (the second/minor number of EmuGUI's version string) to depreciate a feature doesn't count, for example, if version 0.4 depreciates the USB Tablet checkbox, the counting begins at 0.5 (0.5 = 1; 0.6 = 2; ... 0.14 = 10) and it would not be removed until 0.15.x. That way, you hopefully have got enough time to migrate your VMs before it's completely removed (although you could even change it when it's removed already, I guess).

### Features to be removed

| Feature | State | Depreciated/Removed since | Minimum number of feature levels left | Reason for depreciation |
| ------- | ----- | ------------------------- | ------------------------------------- | ----------------------- |
| USB Tablet checkbox | Depreciated | 0.4 | 7 | A combobox with more possibilities has been created |
| Windows 2000 checkbox | Depreciated | 0.6.5 | 9 | Rather prevents you from installing the OS in question than helping you |
| doc/TESTED.md compatibility list | Depreciated | 0.7.2.5108 | 10 | It's not very productive to use two versions of the same file. Please visit the EmuGUI wiki on the stable repository on Codeberg instead. |
| Icelake-Client x86 CPU | Depreciated | 0.7.6.5112 | 10 | This CPU has been removed from QEMU 7.1 already, although EmuGUI is going to keep it for compatibility reasons (for now). Please change the CPU as soon as possible. |

## Supported host operating systems

### Host depreciation policy

This is only for orientation and may not apply because of technical problems. Generally, an operating system is supported until its End of Life or until one of EmuGUI's dependencies is no longer going to run on there. Also, this does NOT apply as soon as EmuGUI's development is stopped completely.