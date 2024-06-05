# EmuGUI v2.0.0.5611 "Ioana Rosa" (based on v2.0.0.5610_rc4)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- April Fools! (from 2.0.0.5606_b2)
- Networking should now work on RISC-V and Alpha.
- Word wrapping is activated in the BIOS thing on the New VM dialog now.
- Thanks to imwez (Discord username), the Portuguese translation is now more complete.
- There are efforts in fixing the readme.
- The main UI file has been recreated.
- User0 is now responsible for the Debian packages. They will come out later than the portable binaries tho.
- Speaking about portable binaries, Windows executables will be built with Python 3.12 from now on.
- The additional argument for KVM is no longer mentioned in the readme because it is no longer necessary.
- The tab order in the first QEMU tab has been adjusted.
- Welcome to the team, PrelevatedInsider18204.
- The main window has been translated as far as possible.
- EmuGUI now has a Guilded server.
- If you wanna know: The VM dialogs are re-translated.
- The new banner has been introduced.
- The fact that EmuGUI on Linux now needs (lib)xcb-cursor0 is mentioned in the readme.
- On the Linux building section, you can now see the exact install commands for Git and binutils.
- Also on the Linux building section, you can now click directly on the installation section where you're told to install QEMU.
- On Linux, there are efforts to make EmuGUI accept spaces in file paths.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5610_rc4

- The redundant code has been removed from the main window.
- Some old/backup files have been deleted.
- Some old code has been removed from the Start VM dialog.
- Some old code has been removed from the New VM dialog.
- Some old code has been removed from the Edit VM dialog.
- Old translation code has been removed from the language files for: Belarusian, Czech.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.

# EmuGUI v2.0.0.5610_rc4 "Ioana Rosa" (based on v2.0.0.5609_rc3)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.
- April Fools! (from 2.0.0.5606_b2)
- Networking should now work on RISC-V and Alpha.
- Word wrapping is activated in the BIOS thing on the New VM dialog now.
- Thanks to imwez (Discord username), the Portuguese translation is now more complete.
- There are efforts in fixing the readme.
- The main UI file has been recreated.
- User0 is now responsible for the Debian packages. They will come out later than the portable binaries tho.
- Speaking about portable binaries, Windows executables will be built with Python 3.12 from now on.
- The additional argument for KVM is no longer mentioned in the readme because it is no longer necessary.
- The tab order in the first QEMU tab has been adjusted.
- Welcome to the team, PrelevatedInsider18204.
- The main window has been translated as far as possible.
- EmuGUI now has a Guilded server.
- If you wanna know: The VM dialogs are re-translated.
- The new banner has been introduced.
- The fact that EmuGUI on Linux now needs (lib)xcb-cursor0 is mentioned in the readme.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5609_rc3

- On the Linux building section, you can now see the exact install commands for Git and binutils.
- Also on the Linux building section, you can now click directly on the installation section where you're told to install QEMU.
- On Linux, there are efforts to make EmuGUI accept spaces in file paths.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.

# EmuGUI v2.0.0.5609_rc3 "Ioana Rosa" (based on v2.0.0.5608_rc2)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.
- April Fools! (from 2.0.0.5606_b2)
- Networking should now work on RISC-V and Alpha.
- Word wrapping is activated in the BIOS thing on the New VM dialog now.
- Thanks to imwez (Discord username), the Portuguese translation is now more complete.
- There are efforts in fixing the readme.
- The main UI file has been recreated.
- User0 is now responsible for the Debian packages. They will come out later than the portable binaries tho.
- Speaking about portable binaries, Windows executables will be built with Python 3.12 from now on.
- The additional argument for KVM is no longer mentioned in the readme because it is no longer necessary.
- The tab order in the first QEMU tab has been adjusted.
- Welcome to the team, PrelevatedInsider18204.
- The main window has been translated as far as possible.
- EmuGUI now has a Guilded server.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5608_rc2

- The new banner has been introduced.
- The fact that EmuGUI on Linux now needs (lib)xcb-cursor0 is mentioned in the readme.

### Edit VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | (Mostly) done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | In progress |
| Czech | Done |

### New VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | Done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | In progress |
| Czech | Done |

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5608_rc2 "Ioana Rosa" (based on v2.0.0.5607_rc1)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.
- April Fools! (from 2.0.0.5606_b2)
- Networking should now work on RISC-V and Alpha.
- Word wrapping is activated in the BIOS thing on the New VM dialog now.
- Thanks to imwez (Discord username), the Portuguese translation is now more complete.
- There are efforts in fixing the readme.
- The main UI file has been recreated.
- User0 is now responsible for the Debian packages. They will come out later than the portable binaries tho.
- Speaking about portable binaries, Windows executables will be built with Python 3.12 from now on.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5607_rc1

- The additional argument for KVM is no longer mentioned in the readme because it is no longer necessary.
- The tab order in the first QEMU tab has been adjusted.
- Welcome to the team, PrelevatedInsider18204.
- The main window has been translated as far as possible.
- EmuGUI now has a Guilded server.

### Edit VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | (Mostly) done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | In progress |
| Czech | Done |

### New VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | Done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | In progress |
| Czech | Done |

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5607_rc1 "Ioana Rosa" (based on v2.0.0.5606_b2)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.
- April Fools! (from 2.0.0.5606_b2)

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5606_b2

- Networking should now work on RISC-V and Alpha.
- Word wrapping is activated in the BIOS thing on the New VM dialog now.
- Thanks to imwez (Discord username), the Portuguese translation is now more complete.
- There are efforts in fixing the readme.
- The main UI file has been recreated.
- User0 is now responsible for the Debian packages. They will come out later than the portable binaries tho.
- Speaking about portable binaries, Windows executables will be built with Python 3.12 from now on.

### Edit VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | (Mostly) done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Done |

### New VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | Done |
| French | In progress |
| Italian | Done |
| Polish | Done |
| Portuguese | Done |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Done |

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5606_b2 "Ioana Rosa" (based on v2.0.0.5605_b1)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.
- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5605_b1

- This is solely a translation update, I guess.
- April Fools!

### Edit VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | (Mostly) done |
| French | In progress |
| Italian | Pending |
| Polish | Pending |
| Portuguese | Pending |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Pending |

### New VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | Done |
| French | In progress |
| Italian | Pending |
| Polish | Pending |
| Portuguese | Pending |
| Romanian | Pending |
| Russian | In progress |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Pending |

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5605_b1 "Ioana Rosa" (based on v2.0.0.5604_dev)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.
- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5603_dev

- The translations for RISC-V have been added.
- I'm working on bringing back the translation functionality on the Edit VM dialog.

### Edit VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | (Mostly) done |
| French | In progress |
| Italian | Pending |
| Polish | Pending |
| Portuguese | Pending |
| Romanian | Pending |
| Russian | Pending |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Pending |

### New VM dialog - Progress

| Language | Status |
| -------- | ------ |
| German | Done |
| Spanish | Done |
| French | In progress |
| Italian | Pending |
| Polish | Pending |
| Portuguese | Pending |
| Romanian | Pending |
| Russian | Pending |
| Ukrainian | Pending |
| Belarusian | Pending |
| Czech | Pending |

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5604_dev "Ioana Rosa" (based on v2.0.0.5603_dev)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.
- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5603_dev

- The readme had to be corrected again.
- Work on the RISC-V 32/64 plug-in has begun.
- The translation files had to be corrected.
- The New VM dialog is now ready to be translated again.
- RISC-V 32-bit support has been added. Sorry, but I have to make a second QEMU page starting with RISC-V 64-bit.
- RISC-V 64-bit support has been added. From now on, there are two QEMU tabs.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5603_dev "Ioana Rosa" (based on v2.0.0.5602_dev)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.
- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5602_dev

- The New and Edit VM dialogs are being optimised further.
- An issue in the New VM dialog which caused the VM creation to be incomplete has been fixed.
- The Start VM dialog has been adjusted.
- The SPARC64 plug-in has been corrected.
- An Alpha plug-in is in the making.
- The Alpha support is mostly there. However, VMs don't seem to run.
- As suggested by [levelad](https://github.com/levelad), an experimental option to run WHPX with `kernel-irqchip=off` has been added.
- The translation of the main window was updated.
- I'm working on bringing back translations for the New VM dialog. However, it will take a while until I can actually re-activate them.
- Some things on the New VM dialog had to be corrected.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.
- Due to the massive restructuring of the New and Edit VM dialogs, those will NOT be translated at this time, meaning they are English only. However, I'll be working on fixing that during development.

# EmuGUI v2.0.0.5602_dev "Ioana Rosa" (based on v2.0.0.5601_dev)

## WARNING

- You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.
- This is a pre-release, meaning it's still in development. Don't use this build for production. Evaluation is okay tho.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.
- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v2.0.0.5601_dev

- I'm doing my best to optimise EmuGUI by adapting the New VM dialog.
- For that, the plug-in reader has been prepared.
- The delcache scripts have been updated.
- However, due to translation issues, the New VM dialog is exclusively in English at this time.
- The Edit VM dialog is also to be shrunk in size.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.

# EmuGUI v2.0.0.5601_dev "Ioana Rosa" (based on v2.0.0.5600_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

## Changes compared to v1.2.3.5513 and v2.0.0.5600_dev

- The "Install on Linux" part of the readme has been corrected.
- I'm now working on what will become the MIPS and SPARC plug-ins.
- Some plug-ins have been separated.
- The generic plug-in is in the works.
- HAXM is now depreciated on EmuGUI.
- A copy of the New VM dialog has been edited.
- A copy of the Edit VM dialog has been edited.

## Known issues

- Unfortunately, you might have to run EmuGUI from the terminal on Linux.
- You will not be notified about any more updates for now as update.txt will not be updated.
- As for the TPM functionality, you must run `mkdir (insert-path-here)` and `swtpm socket --tpm2 --tpmstate dir=(insert-path-here) --ctrl type=unixio,path=(insert-path-here)/swtpm-sock --log level=20` in a terminal (You can leave the `--tpm2` argument away tho if you plan to use TPM 1.2 instead).
- The QCOW2 format is prone to not work for some Windows VMs.

# EmuGUI v2.0.0.5600_dev "Ioana Rosa" (based on v1.2.2.5512)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.2.2.5512

- As always, EmuGUI 2.0 receives another codename, in this case "Ioana Rosa".
- An architecture list in the main window and its usage made the number of used initialisation code shrink. The old code has been commented out.
- The same optimisation efforts have been applied to the code which changes the settings and the code which starts VMs.
- The old feature list has been updated.
- Even though the Additional Hardware Selection Plug-In System (AHSPIS) still has to be made, I started working on JSON plug-ins for x86, PowerPC and ARM machines which are planned to be included with EmuGUI anyway.
- The copyright in the license file has been updated.

## Foreported from v1.2.3.5513

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

# EmuGUI v1.2.3.5513 "Garuka Pula" (based on v1.2.2.5512)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.2.2.5512

- SPARC64 VMs didn't have network capabilities under any circumstances. This is now fixed.

# EmuGUI v1.2.2.5512 "Garuka Pula" (based on v1.2.1.5511)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.2.1.5511

- The Polish translation has been worked on by Calibrato.
- More VHD file endings are now natively supported by EmuGUI.

# EmuGUI v1.2.1.5511 "Garuka Pula" (based on v1.2.0.5510)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.2.0.5510

- I forgot to actually assign the second ISO stuff. Now I realised and fixed it.
- The translations are now more complete too.
- Also, the RTC checkbox enables and disables the time options in the start VM dialog.

# EmuGUI v1.2.0.5510 "Garuka Pula" (based on v1.2.0.5509_rc2)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.
- You can now start the VM without passing a specific time and date to it.
- The building process for Windows binaries with cx_Freeze is now documented in the readme.
- Now you can delete the cache with the delcache scripts for your OS.
- The Garuka Pula banner from lucien-rowan/Tech-FZ has been added.
- The musicpal machine can now be used for ARM machines.
- Some window names are now translated as well (at least technically).
- An effort in fixing the theme issue on Ubuntu 22.04 LTS has been made.

## Changes made compared to 1.2.0.5509_rc2

- The readme has been completed to fully support the cx_Freeze way of compiling.
- The readme contains the pyqtdarktheme module in its tutorials (for Linux only).
- Some unnecessary code has been removed.

# EmuGUI v1.2.0.5509_rc2 "Garuka Pula" (based on v1.2.0.5508_rc1)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.
- You can now start the VM without passing a specific time and date to it.
- The building process for Windows binaries with cx_Freeze is now documented in the readme.
- Now you can delete the cache with the delcache scripts for your OS.
- The Garuka Pula banner from lucien-rowan/Tech-FZ has been added.
- The musicpal machine can now be used for ARM machines.

# EmuGUI v1.2.0.5508_rc1 "Garuka Pula" (based on v1.2.0.5507_b2)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.
- You can now start the VM without passing a specific time and date to it.

## Changes made compared to 1.2.0.5507_b2

- The logging system is not as lazy as it was before.

# EmuGUI v1.2.0.5507_b2 "Garuka Pula" (based on v1.2.0.5506_b1)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.
- You can now start the VM without passing a specific time and date to it.

## Changes made compared to 1.2.0.5506_b1

- The edit VM dialog now received a logging system
- A dot has been removed in one of the logging messages for the new VM dialog.

# EmuGUI v1.2.0.5506_b1 "Garuka Pula" (based on v1.2.0.5505_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.

# EmuGUI v1.2.0.5505_dev "Garuka Pula" (based on v1.2.0.5504_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.5.5413

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.
- Translations have been updated.
- Thanks to Calibrato, we can now add the Polish translation.

## Foreported fixes from 1.1.5

- A bug which turned out to let EmuGUI utilise Portuguese when it should utilise Italian has been fixed. Thanks for reporting it, OSBetaEAC.

## Fixes for features coming with EmuGUI 1.2

- The EmuGUI folder issue is now fixed.
- As Windows 11 internally identifies itself as Windows 10, this has been circumvented by letting each (potential) Windows 11 identify itself by the build number instead.

# EmuGUI v1.2.0.5504_dev "Garuka Pula" (based on v1.2.0.5503_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.4.5411

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- The MAC address generator is now taking up a lot less lines of code.
- System information is now being retrieved.
- The readme has been updated.
- The messages in the main script have been updated.
- I'm now working on a logging system.
- An easteregg has been removed because it wasn't telling the truth anymore.

# EmuGUI v1.2.0.5503_dev "Garuka Pula" (based on v1.2.0.5502_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.4.5411

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.
- You can now choose the HDD controller.
- A few more errors have been added.
- The MAC address generator is now taking up a lot less lines of code.

# EmuGUI v1.2.0.5502_dev "Garuka Pula" (based on v1.2.0.5501_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.4.5411

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).
- There are now bash scripts to start EmuGUI with on Linux.
- The Open/Save dialogs for VHDs are now correctly separated.
- A bug regarding VHDs has been fixed.
- Some more errors are now implemented.

# EmuGUI v1.2.0.5501_dev "Garuka Pula" (based on v1.2.0.5500_dev)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.2.5410

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.
- The fix issued by rzglitch regarding ARM64 VMs has been applied here as well.
- The YouTube and Odysee channels of EmuGUI have been linked in the readme and in the main window under the About tab.
- The outdated feature list has been updated.
- You can now choose the CD controller (IDE, SCSI or Virtio).
- You can now add two CDs to your VMs (instead of one).

# EmuGUI v1.2.0.5500_dev "Garuka Pula" (based on v1.1.2.5410)

## WARNING

You now need the latest version of your Linux distribution or at least Windows 10 to get official support for this pre-release.

## Changes compared to v1.1.2.5410

- As for the last two feature updates, this one gets another codename: "Garuka Pula".
- The feature to import and export VMs has been added.
- The readme has been updated with the new system requirements.
- I think I might have fixed the issue with subprocess.run on Windows.
- An error dialog is now there.

# EmuGUI v1.1.5.5413 "Sara Angeline" (based on v1.1.4.5412)

## WARNING

Ubuntu 20.04 LTS and derivates will no longer receive new features on EmuGUI, now you need the latest (LTS) version of your Linux distribution for anything beyond the EmuGUI 1.1.x line. However, you will still receive bugfixes for the EmuGUI 1.1.x line.

## Changes compared to v1.1.4.5412

- A bug which turned out to let EmuGUI utilise Portuguese when it should utilise Italian has been fixed. Thanks for reporting it, OSBetaEAC.

# EmuGUI v1.1.4.5412 "Sara Angeline" (based on v1.1.3.5411)

## WARNING

Ubuntu 20.04 LTS and derivates will no longer receive new features on EmuGUI, now you need the latest (LTS) version of your Linux distribution for anything beyond the EmuGUI 1.1.x line. However, you will still receive bugfixes for the EmuGUI 1.1.x line.

## Changes compared to v1.1.3.5411

- A bug was fixed to address the issue in the Edit VM dialog regarding the creation of other VHDs for existing VMs.

# EmuGUI v1.1.3.5411 "Sara Angeline" (based on v1.1.2.5410)

## WARNING

Ubuntu 20.04 LTS and derivates will no longer receive new features on EmuGUI, now you need the latest (LTS) version of your Linux distribution for anything beyond the EmuGUI 1.1.x line. However, you will still receive bugfixes for the EmuGUI 1.1.x line.

## Changes compared to v1.1.2.5410

- rzglitch fixed a bug on the Edit VM dialog which swapped machine and CPU.

# EmuGUI v1.1.2.5410 "Sara Angeline" (based on v1.1.1.5409)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.1.1.5409

- The Tab order has been corrected in the Start VM and Edit VM UIs.
- The Boot from combobox in the Start VM UI is now a little wider.

# EmuGUI v1.1.1.5409 "Sara Angeline" (based on v1.1.0.5408)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.1.0.5408

- The Tab order has been corrected in the Main and New VM UIs.
- A critical bug which ruined edited VMs has been fixed.

# EmuGUI v1.1.0.5408 "Sara Angeline" (based on v1.1.0.5407_b2)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.2.5312

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Easter! A banner just for easter has been added.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.
- The edit VM dialogue for choosing a VHD has been stripped down to save some time for now.
- The program has been translated into Spanish. (Thanks, SuperVitu64)
- In the contributors file, you'll now be credited with what you did, not only that you did something.
- Portuguese support has been added (Thanks, PurpleVibe32 and Rafael Magalhães).
- The New and Start VM UIs have been polished.
- TPM functionality for emulated TPM devices is implemented (but you will need a terminal and the feature is for Linux only).
- Hardware acceleration is now easier to set up. You can choose between no acceleration, TCG, HAXM (unsupported, can't help you), WHPX (can't help you) and KVM.
- The German translation has been updated.
- The Czech translation has been added (Thanks, ParmanCZ).
- The Italian translation has been added (Thanks, Vichingo455).
- The Main UI has been enhanced a little so it looks better.
- The readme has been updated.
- The code has been cleaned up.
- The banner for Sara Angeline has been added.
- Two words have been translated into Romanian.

# EmuGUI v1.1.0.5407_b2 "Sara Angeline" (based on v1.1.0.5406_b1)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.2.5312

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Easter! A banner just for easter has been added.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.
- The edit VM dialogue for choosing a VHD has been stripped down to save some time for now.
- The program has been translated into Spanish. (Thanks, SuperVitu64)
- In the contributors file, you'll now be credited with what you did, not only that you did something.
- Portuguese support has been added (Thanks, PurpleVibe32 and Rafael Magalhães).
- The New and Start VM UIs have been polished.
- TPM functionality for emulated TPM devices is implemented (but you will need a terminal and the feature is for Linux only).
- Hardware acceleration is now easier to set up. You can choose between no acceleration, TCG, HAXM (unsupported, can't help you), WHPX (can't help you) and KVM.
- The German translation has been updated.
- The Czech translation has been added (Thanks, ParmanCZ).
- The Italian translation has been added (Thanks, Vichingo455).
- The Main UI has been enhanced a little so it looks better.
- The readme has been updated.
- The code has been cleaned up.

# EmuGUI v1.1.0.5406_b1 "Sara Angeline" (based on v1.1.0.5405_dev)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.2.5312

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Easter! A banner just for easter has been added.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.
- The edit VM dialogue for choosing a VHD has been stripped down to save some time for now.
- The program has been translated into Spanish. (Thanks, SuperVitu64)
- In the contributors file, you'll now be credited with what you did, not only that you did something.
- Portuguese support has been added (Thanks, PurpleVibe32 and Rafael Magalhães).
- The New and Start VM UIs have been polished.
- TPM functionality for emulated TPM devices is implemented (but you will need a terminal and the feature is for Linux only).
- Hardware acceleration is now easier to set up. You can choose between no acceleration, TCG, HAXM (unsupported, can't help you), WHPX (can't help you) and KVM.
- The German translation has been updated.
- The Czech translation has been added (Thanks, ParmanCZ).
- The Italian translation has been added (Thanks, Vichingo455).

# EmuGUI v1.1.0.5405_dev "Sara Angeline" (based on v1.1.0.5404_dev)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.2.5312

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Easter! A banner just for easter has been added.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.
- The edit VM dialogue for choosing a VHD has been stripped down to save some time for now.
- The program has been translated into Spanish. (Thanks, SuperVitu64)
- In the contributors file, you'll now be credited with what you did, not only that you did something.
- Portuguese support has been added (Thanks, PurpleVibe32).
- The New and Start VM UIs have been polished.
- TPM functionality for emulated TPM devices is implemented (but you will need a terminal and the feature is for Linux only).

# EmuGUI v1.1.0.5404_dev "Sara Angeline" (based on v1.1.0.5403_dev)

## WARNING

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.1.5311

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Eastern! A banner just for eastern has been added.
- For Python 3.10.11 on Windows, there was a bug which prevented EmuGUI from starting up, which is fixed by making a try-except clause for both the Python versions which still require the parent argument in the initialisation and those which crash because of it.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.
- The edit VM dialogue for choosing a VHD has been stripped down to save some time for now.
- The program has been translated into Spanish. (Thanks, SuperVitu64)
- In the contributors file, you'll now be credited with what you did, not only that you did something.

# EmuGUI v1.1.0.5403_dev "Sara Angeline" (based on v1.1.0.5402_dev)

## Changes compared to v1.0.1.5311

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Eastern! A banner just for eastern has been added.
- For Python 3.10.11 on Windows, there was a bug which prevented EmuGUI from starting up, which is fixed by making a try-except clause for both the Python versions which still require the parent argument in the initialisation and those which crash because of it.
- As I noticed the code would go confusing, I decided to use text files containing the strings for affected combo boxes instead. The code which was used before this update has been commented out for now so we can roll back if something is wrong.

# EmuGUI v1.1.0.5402_dev "Sara Angeline" (based on v1.1.0.5401_dev)

## Changes compared to v1.0.1.5311

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.
- The old feature list has been updated again.
- The requests list has been commented out.
- Happy Eastern! A banner just for eastern has been added.
- For Python 3.10.11 on Windows, there was a bug which prevented EmuGUI from starting up, which is fixed by making a try-except clause for both the Python versions which still require the parent argument in the initialisation and those which crash because of it.

# EmuGUI v1.1.0.5401_dev "Sara Angeline" (based on v1.1.0.5400_dev)

## Changes compared to v1.0.1.5311

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish, Czech, Russian, Belarusian and Romanian have been prepared.
- Thanks for translating EmuGUI into Russian and Belarusian, Danik2343.

# EmuGUI v1.1.0.5400_dev "Sara Angeline" (based on v1.0.1.5311)

## Changes compared to v1.0.1.5311

- New feature level, new codename. I decided to call it "Sara Angeline" based on what I want to add so far.
- Language files for French, Spanish and Romanian have been prepared.

# EmuGUI v1.0.2.5312 "Adèle Angela" (based on v1.0.1.5311)

## WARNING

Windows 8.1 and Windows Server 2012 R2 are no longer supported as an EmuGUI host as of 14th February, 2023. Even if you are still able to run EmuGUI, you will need at least Windows 10 or Server 2016 to get support.

Ubuntu 20.04 LTS and derivates will be no longer supported as EmuGUI hosts from 8th July, 2023. You would then need at least Ubuntu 22.04 LTS or one of its derivates.

## Changes compared to v1.0.1.5311

- A backport from the pre-release is now making compilation on later versions of Python possible.

# EmuGUI v1.0.1.5311 "Adèle Angela" (based on v1.0.0.5310)

## WARNING

Windows 8.1 and Windows Server 2012 R2 are no longer supported as an EmuGUI host as of 14th February, 2023. Even if you are still able to run EmuGUI, you will need at least Windows 10 or Server 2016 to get support.

## Changes compared to v1.0.0.5310

- A bug which didn't let you edit x86_64 VMs directly has been fixed.

# EmuGUI v1.0.0.5310 "Adèle Angela" (based on v1.0.0.5309_b3)

## WARNING

Windows 8.1 and Windows Server 2012 R2 are no longer supported as an EmuGUI host as of 14th February, 2023. Even if you are still able to run EmuGUI, you will need at least Windows 10 or Server 2016 to get support.

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.
- SPARC 64-bit support has been added and the functionality is ready for testing.
- In the development version 1.0.0.5305_dev, there has been a bug which didn't properly fill the text fields for the QEMU settings. That has been fixed in this development version.
- The readme was updated with the meaning of the "_b" ending.
- The translations have been worked on so the new features can be translated now.
- The text colourized logo has been made transparent.
- The default banner has been replaced with a new banner fitting the codename of EmuGUI 1.0.
- The contributors list has been updated so there you get credit for the banners you made.
- If one of your banners is being used, you'll also get credit in the About EmuGUI section.
- "main.py" has been renamed to "EmuGUI.py"
- You can now join a Discord server via Readme.
- The readme is fancier. Thanks, the-amazing-atharva.
- The commands and the documentation thing have been updated on the readme.
- Also, the-amazing-atharva added a Code of Conduct.
- The Windows binaries are updated to Python 3.10.10.
- The obsolete code which has been commented out has been removed.
- There are now social media links in the About EmuGUI section. However, please note that they are (mostly) in English.
- The .gitignore has been updated so it fits the new name of the Python script.
- The readme and the Windows 8.1 support dialog have been updated.
- I'm nice, so the about section will tell you if you use an outdated version of Windows.

# EmuGUI v1.0.0.5309_b3 "Adèle Angela" (based on v1.0.0.5308_b2)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.
- SPARC 64-bit support has been added and the functionality is ready for testing.
- In the development version 1.0.0.5305_dev, there has been a bug which didn't properly fill the text fields for the QEMU settings. That has been fixed in this development version.
- The readme was updated with the meaning of the "_b" ending.
- The translations have been worked on so the new features can be translated now.
- The text colourized logo has been made transparent.
- The default banner has been replaced with a new banner fitting the codename of EmuGUI 1.0.
- The contributors list has been updated so there you get credit for the banners you made.
- If one of your banners is being used, you'll also get credit in the About EmuGUI section.
- "main.py" has been renamed to "EmuGUI.py"
- You can now join a Discord server via Readme.
- The readme is fancier. Thanks, the-amazing-atharva.
- The commands and the documentation thing have been updated on the readme.
- Also, the-amazing-atharva added a Code of Conduct.
- The Windows binaries are updated to Python 3.10.10.
- The obsolete code which has been commented out has been removed.
- There are now social media links in the About EmuGUI section. However, please note that they are (mostly) in English.

# EmuGUI v1.0.0.5308_b2 "Adèle Angela"  (based on v1.0.0.5307_b1)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.
- SPARC 64-bit support has been added and the functionality is ready for testing.
- In the development version 1.0.0.5305_dev, there has been a bug which didn't properly fill the text fields for the QEMU settings. That has been fixed in this development version.
- The readme was updated with the meaning of the "_b" ending.
- The translations have been worked on so the new features can be translated now.
- The text colourized logo has been made transparent.
- The default banner has been replaced with a new banner fitting the codename of EmuGUI 1.0.
- The contributors list has been updated so there you get credit for the banners you made.
- If one of your banners is being used, you'll also get credit in the About EmuGUI section.
- "main.py" has been renamed to "EmuGUI.py"
- You can now join a Discord server via Readme.

# EmuGUI v1.0.0.5307_b1 "Adèle Angela"  (based on v1.0.0.5306_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.
- SPARC 64-bit support has been added and the functionality is ready for testing.
- In the development version 1.0.0.5305_dev, there has been a bug which didn't properly fill the text fields for the QEMU settings. That has been fixed in this development version.
- The readme was updated with the meaning of the "_b" ending.
- The translations have been worked on so the new features can be translated now.
- The text colourized logo has been made transparent.

# EmuGUI v1.0.0.5306_dev "Adèle Angela"  (based on v1.0.0.5305_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.
- SPARC 64-bit support has been added and the functionality is ready for testing.
- In the development version 1.0.0.5305_dev, there has been a bug which didn't properly fill the text fields for the QEMU settings. That has been fixed in this development version.

# EmuGUI v1.0.0.5305_dev "Adèle Angela"  (based on v1.0.0.5304_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.
- SPARC 32-bit support has been added and the functionality is ready for testing.
- The old feature list is updated so it fits the current circumstances.

# EmuGUI v1.0.0.5304_dev "Adèle Angela"  (based on v1.0.0.5303_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.
- You can now select different keyboard layouts.
- The version string has been moved to the About section and is also shown in the title of the main window.
- The main window now scales its content when resized.
- The codename will be shown in the About section as well.
- The license file has been updated with the copyright information.
- The readme has been updated so it fits the current circumstances.

# EmuGUI v1.0.0.5303_dev (based on v0.9.0.5302_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- The updater has been removed due to some unexpected complications.
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is now GitHub-only due to some unexpected complications.

# EmuGUI v0.9.0.5302_dev (based on v0.9.0.5301_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- Also, the update file will now be created in your user directory (instead of in the root).
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- This release is only put in place to ensure you can be directly redirected to GitLab as well. Please note that this is only a temporary action while we prepare to mirror the entirety of EmuGUI on GitLab.
- Also, the GitLab mirror has been added to the Readme.

# EmuGUI v0.9.0.5301_dev (based on v0.9.0.5300_dev)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- Also, the update file will now be created in your user directory (instead of in the root).
- The database now supports the keyboard layout selection, which hasn't been implemented as of yet.
- Also, this is the first release which is hosted on GitLab as well as Codeberg is not accessable in Belarus.

# EmuGUI v0.9.0.5300_dev (based on v0.8.0.5206)

## Changes compared to v0.8.0.5206

- The old feature list has been updated beforehand.
- Also, the update file will now be created in your user directory (instead of in the root).

# EmuGUI v0.8.0.5206 (based on v0.8.0.5205_dev)

## Changes compared to v0.7.6.5112

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- With a new dialog, editing VMs has been made more convenient than it was before.
- The edit VM dialog has been translated into the currently supported languages.
- "Переглядати" in Ukrainian has been changed to "Огляд" in the entire program.
- Same applies with "Назва", which is now "Звати".
- You can now choose a specific theme for EmuGUI. The number of themes included by default depends on your operating system.
- The requests module is now included into the default pip command of README.md.
- The Windows binaries will be made with Python 3.10.8 instead of 3.10.7.
- You can now create custom *.qss stylesheets. Just don't call it Windows, windowsvista, Fusion, Breeze or something else that one or another system might reserve for itself.
- The Ukrainian translation is another step further to completion.

# EmuGUI v0.8.0.5205_dev (based on v0.8.0.5204_dev)

## Changes compared to v0.7.6.5112

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- With a new dialog, editing VMs has been made more convenient than it was before.
- The edit VM dialog has been translated into the currently supported languages.
- "Переглядати" in Ukrainian has been changed to "Огляд" in the entire program.
- Same applies with "Назва", which is now "Звати".
- You can now choose a specific theme for EmuGUI. The number of themes included by default depends on your operating system.
- The requests module is now included into the default pip command of README.md.
- The Windows binaries will be made with Python 3.10.8 instead of 3.10.7.
- You can now create custom *.qss stylesheets. Just don't call it Windows, windowsvista, Fusion, Breeze or something else that one or another system might reserve for itself.

# EmuGUI v0.8.0.5204_dev (based on v0.8.0.5203_dev)

## Changes compared to v0.7.6.5112

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- With a new dialog, editing VMs has been made more convenient than it was before.
- The edit VM dialog has been translated into the currently supported languages.
- "Переглядати" in Ukrainian has been changed to "Огляд" in the entire program.
- Same applies with "Назва", which is now "Звати".
- You can now choose a specific theme for EmuGUI. The number of themes included by default depends on your operating system.

## Changes made within development of this feature level

- An issue which translated both buttons at the bottom of the edit VM dialog to "OK" has been corrected.

# EmuGUI v0.8.0.5203_dev (based on v0.8.0.5202_dev)

## Changes compared to v0.7.6.5112

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- With a new dialog, editing VMs has been made more convenient than it was before.
- The edit VM dialog has been translated into the currently supported languages.
- "Переглядати" in Ukrainian has been changed to "Огляд" in the entire program.
- Same applies with "Назва", which is now "Звати".

# EmuGUI v0.8.0.5202_dev (based on v0.8.0.5201_dev)

## Changes compared to v0.7.6.5112

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- With a new dialog, editing VMs has been made more convenient than it was before.

# EmuGUI v0.8.0.5201_dev (based on v0.8.0.5200_dev)

## Changes compared to v0.7.5.5111

- Support for the MIPS and MIPS64 big-endian architectures has been added.
- We began to work on a better dialog for editing existing virtual machines.
- The .gitignore file also experienced a change: The ./ suffix is no longer present - that's how the file works.
- The Icelake-Client x86/x64 CPU, which has been removed from QEMU 7.1, is depreciated on EmuGUI now. Please change the CPU on affected VMs as soon as possible. This measure is already present in 0.7.6.5112, but it had to be written into this version as well.
- The old editing VM dialog might have crashed if your installation didn't contain the EmuGUI.png icon. That is now fixed in both 0.7 and 0.8.

# EmuGUI v0.8.0.5200_dev (based on v0.7.5.5111)

## Changes compared to v0.7.5.5111

- Support for the MIPS and MIPS64 big-endian architectures has been added.

# EmuGUI v0.7.6.5112 (based on v0.7.5.5111)

## Changes compared to v0.7.5.5111

- The ./ prefix in .gitignore has been removed from every single line there.
- The Icelake-Client x86/x64 CPU, which has been removed from QEMU 7.1, is depreciated on EmuGUI now. Please change the CPU on affected VMs as soon as possible.
- The editing VM dialog might have crashed if your installation didn't contain the EmuGUI.png icon. That is now fixed.

# EmuGUI v0.7.5.5111 (based on v0.7.4.5110)

## Changes compared to 0.7.4.5110

- The Windows binaries are now compiled with Python 3.10.7 instead of Python 3.10.6.
- Obsolete code which was commented out is now completely removed.
- Some more words have been translated into Ukrainian.

# EmuGUI v0.7.4.5110 (based on v0.7.3.5109)

## Changes compared to 0.7.3.5109

- On some Linux configurations, the main branch was prone to crash. While the fix was exclusive to the Linux binaries in the previous two updates, the main code should also be fixed now.
- Also, some more phrases and words have been (partially) translated into Ukrainian.
- Obsolete code which is no longer in use within EmuGUI has been either commented out or removed as a whole.
- To make translating EmuGUI easier in the future, comments with the English translation have been added to all currently available ones.
- Also, something inside the German translation had to be corrected.

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
