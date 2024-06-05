from translations.systemdefaultset import *

def translateMainCZ(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Hlavní") # Main
    window.tabWidget.setTabText(1, "Nastavení") # Settings

    # Main tab
    window.pushButton_8.setText("Nový virtuální počítač") # New virtual machine
    window.pushButton_9.setText("Spustit virtuální počítač") # Start virtual machine
    window.pushButton_10.setText("Upravit vybraný virtuální počítač") # Edit selected virtual machine
    window.pushButton_11.setText("Odstranit vybraný virtuální počítač") # Delete selected virtual machine
    window.pushButton_22.setText("Exportovat zvolený virtuální PC") # Export selected virtual machine
    window.pushButton_23.setText("Importovat virtuální PC") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Obecné") # General
    window.tabWidget_2.setTabText(3, "O EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Jazyk") # Language
    window.pushButton_15.setText("Aplikovat") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Výchozí nastavení systému", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Výchozí nastavení systému", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("Cesta qemu-img") # qemu-img Path
    window.label_2.setText("Cesta qemu-system-i386") # qemu-system-i386 Path
    window.label_3.setText("Cesta qemu-system-x86_64") # qemu-system-x86_64 Path
    window.label_4.setText("Cesta qemu-system-ppc") # qemu-system-ppc Path
    window.label_5.setText("Cesta qemu-system-mips64el") # qemu-system-mips64el Path
    window.label_9.setText("Cesta qemu-system-aarch64") # qemu-system-aarch64 Path
    window.label_11.setText("Cesta qemu-system-arm") # qemu-system-arm Path
    window.label_16.setText("Cesta qemu-system-ppc64") # qemu-system-ppc64 Path
    window.label_17.setText("Cesta qemu-system-mipsel") # qemu-system-mipsel Path
    window.label_18.setText("Cesta qemu-system-mips") # qemu-system-mips Path
    window.label_19.setText("Cesta qemu-system-mips64") # qemu-system-mips64 Path
    window.label_12.setText("Cesta qemu-system-sparc") # qemu-system-sparc Path
    window.label_13.setText("Cesta qemu-system-sparc64") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("Cesta qemu-system-alpha") # qemu-system-alpha Path
    window.lbl_riscv32.setText("Cesta qemu-system-riscv32") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("Cesta qemu-system-riscv64") # qemu-system-riscv64 Path

    window.pushButton.setText("Hledat") # Browse
    window.pushButton_2.setText("Hledat") # Browse
    window.pushButton_3.setText("Hledat") # Browse
    window.pushButton_4.setText("Hledat") # Browse
    window.pushButton_5.setText("Hledat") # Browse
    window.pushButton_7.setText("Hledat") # Browse
    window.pushButton_12.setText("Hledat") # Browse
    window.pushButton_16.setText("Hledat") # Browse
    window.pushButton_17.setText("Hledat") # Browse
    window.pushButton_18.setText("Hledat") # Browse
    window.pushButton_19.setText("Hledat") # Browse
    window.pushButton_13.setText("Hledat") # Browse
    window.pushButton_14.setText("Hledat") # Browse
    window.btn_alpha.setText("Hledat") # Browse
    window.btn_riscv32.setText("Hledat") # Browse
    window.btn_riscv64.setText("Hledat") # Browse
    window.pushButton_6.setText("Aplikovat") # Apply
    window.btn_apply_qemu2.setText("Aplikovat") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Postaveno na technologii Python a PyQt, licencováno pod GNU General Public License 3.0")

    window.label_10.setText(
        """
        VAROVÁNÍ: Na tento program se NEVZTAHUJE ABSOLUTNĚ ŽÁDNÁ ZÁRUKA podle platných zákonů. Podrobnosti naleznete v licenci GNU GPL.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner udělal Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI na sociálních médiích (in English)") # EmuGUI on social media (in English)

def translateNewVmCZ(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.lbl_vmname.setText("Název") # Name
    window.lbl_arch.setText("Architektura") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Další >") # Next >
    window.btn_cancel1.setText("Zrušit") # Cancel

    # Second page
    window.lbl_machine.setText("Stroj") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM v MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Předchozí") # < Previous
    window.pb_next2.setText("Další >") # Next >
    window.pb_cancel2.setText("Zrušit") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Využití VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Vytvořte nový virtuální pevný disk") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Přidejte existující virtuální pevný disk") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Nepřidávejte virtuální pevný disk") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Cesta VHD") # VHD path
    window.lbl_vhdF.setText("Formát souboru VHD") # VHD file format
    window.lbl_maxsize.setText("Maximální velikost") # Maximum size
    window.lbl_hddC.setText("Ovladač HDD") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Hledat") # Browse
    window.btn_prev3.setText("< Předchozí") # < Previous
    window.btn_next3.setText("Další >") # Next >
    window.btn_cancel3.setText("Zrušit") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Síť") # Network
    window.lbl_mouse.setText("Myš") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Předchozí") # < Previous
    window.btn_next4.setText("Další >") # Next >
    window.btn_cancel4.setText("Zrušit") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Umístění externího souboru BIOS (Chcete-li použít výchozí BIOS, ponechte prázdné)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Externí Soubor BIOS") # External BIOS file

    window.btn_biosF.setText("Hledat") # Browse
    window.btn_prev5.setText("< Předchozí") # < Previous
    window.btn_next5.setText("Další >") # Next >
    window.btn_cancel5.setText("Zrušit") # Cancel

    # Sixth page
    window.lbl_sound.setText("Zvuková Karta") # Sound card
    window.lbl_cores.setText("Jádra CPU")# CPU cores
    window.lbl_kbd.setText("Klávesnice") # Keyboard
    window.lbl_kbdlayout.setText("Rozložení klávesnice") # Keyboard layout

    window.btn_prev6.setText("< Předchozí") # < Previous
    window.btn_next6.setText("Další >") # Next >
    window.btn_cancel6.setText("Zrušit") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Linuxové jádro") # Linux kernel
    window.lbl_initrd.setText("Obraz initrd pro Linux") # Linux initrd image
    window.lbl_cmd.setText("Linux cmd args") # Linux cmd args

    window.btn_kernel.setText("Hledat") # Browse
    window.btn_initrd.setText("Hledat") # Browse
    window.btn_prev7.setText("< Předchozí") # < Previous
    window.btn_next7.setText("Další >") # Next >
    window.btn_cancel7.setText("Zrušit") # Cancel

    # Eighth page
    window.lbl_accel.setText("Akcelerace") # Acceleration
    window.lbl_cdc1.setText("Ovladač CD 1") # CD controller 1
    window.lbl_cdc2.setText("Ovladač CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Předchozí") # < Previous
    window.btn_next8.setText("Další >") # Next >
    window.btn_cancel8.setText("Zrušit") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Další argumenty (pokud jsou potřeba)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Pridat podporu USB") # Add USB support

    window.btn_prev9.setText("< Předchozí") # < Previous
    window.btn_finish.setText("Dokončit") # Finish
    window.btn_cancel9.setText("Zrušit") # Cancel

def translateStartVmCZ(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Datum a čas") # Date & Time
    window.label_3.setText("Spustit z") # Boot from
    window.label_6.setText("TPM path (Linux only)") # TPM path (Linux only)
    window.label_7.setText("Create the TPM from the terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Poznámka: Pokud se virtuální počítač nespustí do pěti minut, měli byste zkontrolovat nastavení virtuálního počítače a QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Hledat") # Browse
    window.pushButton_2.setText("Hledat") # Browse
    window.pushButton_6.setText("Hledat") # Browse
    window.pushButton_5.setText("Nastavit do systém") # Set to system
    window.pushButton_3.setText("Spustit virtuální počítač") # Start VM
    window.pushButton_4.setText("Zrušit") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

def translateVmExistsCZ(window):
    window.label.setText(
        "Je nám líto, ale virtuální počítač s tímto názvem již existuje."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Zvažte prosím smazání tohoto virtuálního počítače nebo přemýšlení o novém názvu."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsCZ(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Je nám líto, ale disk, který chcete vytvořit, již existuje."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Chcete jej zachovat nebo přepsat?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Přepsat") # Overwrite
    window.pushButton_2.setText("Nechat") # Keep

def translateSettingsPendingCZ(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Nenastavili jste cesty QEMU.")
    window.label_2.setText("Chcete-li to provést, přejděte do nastavení a zkuste to znovu.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewCZ(window):
    window.label.setText(
        "Tento VM je vytvořen s verzí EmuGUI, která je příliš nová. Použijte prosím novější verzi!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingCZ(window, arch):
    window.label.setText(
        f"Omlouváme se, ale EmuGUI ještě není nakonfigurováno pro použití \"qemu-system-{arch}\".\nTato komponenta je však nezbytná pro spuštění tohoto virtuálního stroje.\nChcete-li tento problém vyřešit, přejděte do Nastavení/QEMU."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingCZ(window):
    window.label.setText(
        "Omlouváme se, ale EmuGUI ještě není nakonfigurováno pro použití \"qemu-img\".\nTato komponenta je však nezbytná k vytvoření nebo úpravě virtuálních strojů.\nChcete-li tento problém vyřešit, přejděte do Nastavení/QEMU."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMCZ(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("Zrušit") # Cancel
    window.btn_ok.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Obecné") # General
    window.tabWidget.setTabText(1, "Stroj") # Machine
    window.tabWidget.setTabText(2, "Virtuální Pevné disky") # Virtual hard disks
    window.tabWidget.setTabText(3, "Periférie") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Další komponenty") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Název") # Name
    window.lbl_arch.setText("Architektura") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("Stroj") # Machine
    window.lbl_ram.setText("RAM v MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Využití VHD") # VHD usage
    window.lbl_vhdp.setText("Cesta VHD") # VHD path
    window.lbl_vhdf.setText("Formát souboru VHD") # VHD file format
    window.lbl_maxsize.setText("Maximální velikost") # Maximum size
    window.btn_vhdp.setText("Hledat") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Vytvořte nový virtuální pevný disk") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Přidejte existující virtuální pevný disk") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Nepřidávejte virtuální pevný disk") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("Ovladač CD 1") # CD controller 1
    window.lbl_cdc2.setText("Ovladač CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("Ovladač HDD") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Ať rozhodne QEMU") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Typ myši") # Mouse type
    window.lbl_kbdtype.setText("Typ klávesnice") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Umístění externího souboru BIOS (Chcete-li použít výchozí BIOS, ponechte prázdné)")
    window.lbl_biosf.setText("Externí Soubor BIOS") # External BIOS file
    window.btn_biosf.setText("Hledat") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Linuxové jádro") # Linux kernel
    window.lbl_initrd.setText("Obraz initrd pro Linux") # Linux initrd image
    window.lbl_cmd.setText("Linux cmd args") # Linux cmd arguments
    window.btn_kernel.setText("Hledat") # Browse
    window.btn_initrd.setText("Hledat") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Síť") # Network adapter
    window.lbl_sound.setText("Zvuková Karta") # Sound card
    window.lbl_addargs.setText("Další argumenty (pokud jsou potřeba)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Jádra CPU") # CPU cores
    window.chb_usb.setText("Pridat podporu USB") # Add USB support
    window.lbl_accel.setText("Akcelerace") # Acceleration

def translateErrDialogCZ(window, errcode):
    window.setWindowTitle(f"EmuGUI - Chybu")

    if errcode.startswith("C"):
        window.label.setText("EmuGUI narazil na kritickou chybu a musí být uzavřen.") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI narazil na chybu.") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI vás musí varovat.") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI musí něco sdělit.") # EmuGUI has something to say.

    window.label_2.setText("Kód chyby: " + errcode) # Error Code:

    window.label_3.setText(
        "Pokud se tato chyba stane vícekrát, kontaktujte vašeho administrátora a/nebo se zeptejte se o pomoc v EmuGUI Discord serveru nebo na repozitáři GitHub."
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("OK") # OK