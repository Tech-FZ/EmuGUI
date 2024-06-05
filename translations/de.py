from translations.systemdefaultset import *

def translateMainDE(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Hauptmenü") # Main
    window.tabWidget.setTabText(1, "Einstellungen") # Settings

    # Main tab
    window.pushButton_8.setText("Neue virtuelle Maschine") # New virtual machine
    window.pushButton_9.setText("Virtuelle Maschine starten") # Start virtual machine
    window.pushButton_10.setText("Ausgewählte virtuelle Maschine bearbeiten") # Edit selected virtual machine
    window.pushButton_11.setText("Ausgewählte virtuelle Maschine löschen") # Delete selected virtual machine
    window.pushButton_22.setText("Ausgewählte virtuelle Maschine exportieren") # Export selected virtual machine
    window.pushButton_23.setText("Virtuelle Maschine importieren") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Allgemein") # General
    window.tabWidget_2.setTabText(3, "Über EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Sprache") # Language
    window.pushButton_15.setText("Übernehmen") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Systemstandard", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Systemstandard", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img-Pfad") # qemu-img Path
    window.label_2.setText("qemu-system-i386-Pfad") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64-Pfad") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc-Pfad") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el-Pfad") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64-Pfad") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm-Pfad") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64-Pfad") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel-Pfad") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips-Pfad") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64-Pfad") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc-Pfad") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64-Pfad") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("qemu-system-alpha-Pfad") # qemu-system-alpha Path
    window.lbl_riscv32.setText("qemu-system-riscv32-Pfad") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("qemu-system-riscv64-Pfad") # qemu-system-riscv64 Path

    window.pushButton.setText("Durchsuchen") # Browse
    window.pushButton_2.setText("Durchsuchen") # Browse
    window.pushButton_3.setText("Durchsuchen") # Browse
    window.pushButton_4.setText("Durchsuchen") # Browse
    window.pushButton_5.setText("Durchsuchen") # Browse
    window.pushButton_7.setText("Durchsuchen") # Browse
    window.pushButton_12.setText("Durchsuchen") # Browse
    window.pushButton_16.setText("Durchsuchen") # Browse
    window.pushButton_17.setText("Durchsuchen") # Browse
    window.pushButton_18.setText("Durchsuchen") # Browse
    window.pushButton_19.setText("Durchsuchen") # Browse
    window.pushButton_13.setText("Durchsuchen") # Browse
    window.pushButton_14.setText("Durchsuchen") # Browse
    window.btn_alpha.setText("Durchsuchen") # Browse
    window.btn_riscv32.setText("Durchsuchen") # Browse
    window.btn_riscv64.setText("Durchsuchen") # Browse
    window.pushButton_6.setText("Übernehmen") # Apply
    window.btn_apply_qemu2.setText("Übernehmen") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Basierend auf Python- und PyQt-Technologien, lizenziert unter GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNUNG: Das Programm kommt, sofern das Gesetz es zulässt, OHNE JEGLICHE GARANTIE. Bitte sehen Sie für Details die GNU GPL-Lizenz ein.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner stammt von Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI in sozialen Medien (auf Englisch)") # EmuGUI on social media (in English)

def translateNewVmDE(window):
    window.setWindowTitle("EmuGUI - Neue VM erstellen")

    # First page
    window.lbl_vmname.setText("Name") # Name
    window.lbl_arch.setText("Architektur") # Architecture
    window.cb_arch.setPlaceholderText("Bitte wählen Sie eine Architektur") # Please choose an architecture

    window.btn_next1.setText("Weiter >") # Next >
    window.btn_cancel1.setText("Abbrechen") # Cancel

    # Second page
    window.lbl_machine.setText("Maschine") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM in MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Bitte wählen Sie einen Prozessor") # Please select a processor

    window.pb_prev2.setText("< Zurück") # < Previous
    window.pb_next2.setText("Weiter >") # Next >
    window.pb_cancel2.setText("Abbrechen") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("VHD-Nutzung") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Neue virtuelle Festplatte erstellen") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Existierende virtuelle Festplatte anfügen") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Keine virtuelle Festplatte anfügen") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("VHD-Pfad") # VHD path
    window.lbl_vhdF.setText("VHD-Dateiformat") # VHD file format
    window.lbl_maxsize.setText("Maximale Größe") # Maximum size
    window.lbl_hddC.setText("HDD-Controller") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Bitte wählen Sie ein Dateiformat)") # (Please select a file format)

    window.btn_vhdP.setText("Durchsuchen") # Browse
    window.btn_prev3.setText("< Zurück") # < Previous
    window.btn_next3.setText("Weiter >") # Next >
    window.btn_cancel3.setText("Abbrechen") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Netzwerk") # Network
    window.lbl_mouse.setText("Maus") # Mouse

    window.cb_vga.setPlaceholderText("(Bitte wählen Sie einen Grafikadapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Bitte wählen Sie einen Netzwerkadapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Zurück") # < Previous
    window.btn_next4.setText("Weiter >") # Next >
    window.btn_cancel4.setText("Abbrechen") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Ort der externen BIOS-Datei\n(Leerlassen für\nStandard-BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Externe BIOS-Datei") # External BIOS file

    window.btn_biosF.setText("Durchsuchen") # Browse
    window.btn_prev5.setText("< Zurück") # < Previous
    window.btn_next5.setText("Weiter >") # Next >
    window.btn_cancel5.setText("Abbrechen") # Cancel

    # Sixth page
    window.lbl_sound.setText("Soundkarte") # Sound card
    window.lbl_cores.setText("CPU-Kerne")# CPU cores
    window.lbl_kbd.setText("Tastatur") # Keyboard
    window.lbl_kbdlayout.setText("Tastaturlayout") # Keyboard layout

    window.btn_prev6.setText("< Zurück") # < Previous
    window.btn_next6.setText("Weiter >") # Next >
    window.btn_cancel6.setText("Abbrechen") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Linux-Kernel") # Linux kernel
    window.lbl_initrd.setText("Linux initrd-Image") # Linux initrd image
    window.lbl_cmd.setText("Linux-CMD-Argumente") # Linux cmd args

    window.btn_kernel.setText("Durchsuchen") # Browse
    window.btn_initrd.setText("Durchsuchen") # Browse
    window.btn_prev7.setText("< Zurück") # < Previous
    window.btn_next7.setText("Weiter >") # Next >
    window.btn_cancel7.setText("Abbrechen") # Cancel

    # Eighth page
    window.lbl_accel.setText("Beschleunigung") # Acceleration
    window.lbl_cdc1.setText("CD-Controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD-Controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Zurück") # < Previous
    window.btn_next8.setText("Weiter >") # Next >
    window.btn_cancel8.setText("Abbrechen") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Zusätzliche Argumente (falls nötig)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("USB-Support hinzufügen") # Add USB support

    window.btn_prev9.setText("< Zurück") # < Previous
    window.btn_finish.setText("Abschließen") # Finish
    window.btn_cancel9.setText("Abbrechen") # Cancel

def translateStartVmDE(window, vmname):
    window.setWindowTitle(f"EmuGUI - {vmname} starten")
    window.label_4.setText("Datum & Zeit") # Date & Time
    window.label_3.setText("Booten von") # Boot from
    window.label_6.setText("TPM-Pfad (nur für Linux)") # TPM path (Linux only)
    window.label_7.setText("Bitte erstellen Sie das TPM vom Terminal aus!") # Create the TPM from the terminal!
    
    window.label_5.setText("""
    Notiz: Sollte die VM innerhalb fünf Minuten nicht starten, sollten Sie die Einstellungen von VM und QEMU überprüfen.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Durchsuchen") # Browse
    window.pushButton_2.setText("Durchsuchen") # Browse
    window.pushButton_6.setText("Durchsuchen") # Browse
    window.pushButton_5.setText("Auf Systemzeit setzen") # Set to system
    window.pushButton_3.setText("VM starten") # Start VM
    window.pushButton_4.setText("Abbrechen") # Cancel
    window.checkBox.setText("RTC-Option nutzen") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

def translateVmExistsDE(window):
    window.label.setText(
        "Tut mir leid, jedoch trägt bereits eine andere VM diesen Namen."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Bitte löschen Sie die entsprechende VM oder geben Sie dieser einen neuen Namen."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsDE(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Es tut mir leid, aber die Platte, die Sie erstellen wollen, existiert bereits."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Wollen Sie dieses behalten oder überschreiben?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Überschreiben") # Overwrite
    window.pushButton_2.setText("Behalten") # Keep

def translateSettingsPendingDE(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Sie haben die QEMU-Pfade noch nicht eingestellt.")
    window.label_2.setText("Bitte gehen Sie in die Einstellungen, um dies zu beheben und versuchen Sie es danach nochmal.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewDE(window):
    window.label.setText(
        "Diese VM wurde mit einer zu neuen Version von EmuGUI erstellt. Bitte verwenden Sie eine neuere Version!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingDE(window, arch):
    window.label.setText(
        f"Tut mir leid, aber EmuGUI wurde noch nicht für die Nutzung von \"qemu-system-{arch}\" konfiguriert.\nDiese Komponente wird jedoch benötigt, um diese virtuelle Maschine zu starten.\nBitte gehen Sie zu Einstellungen/QEMU, um das Problem zu lösen."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingDE(window):
    window.label.setText(
        "Tut mir leid, aber EmuGUI wurde noch nicht für die Nutzung von \"qemu-img\" konfiguriert.\nDiese Komponente wird jedoch benötigt, um virtuelle Maschinen zu erstellen oder zu bearbeiten.\nBitte gehen Sie zu Einstellungen/QEMU, um das Problem zu lösen."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMDE(window, vmname):
    window.setWindowTitle(f"EmuGUI - {vmname} bearbeiten")

    # Buttons on all tabs
    window.btn_cancel.setText("Abbrechen") # Cancel
    window.btn_ok.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Allgemein") # General
    window.tabWidget.setTabText(1, "Maschine") # Machine
    window.tabWidget.setTabText(2, "Virtuelle Festplatten") # Virtual hard disks
    window.tabWidget.setTabText(3, "Peripherie") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Zusätzliche Komponenten") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Name") # Name
    window.lbl_arch.setText("Architektur") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("Maschine") # Machine
    window.lbl_ram.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("VHD-Nutzung") # VHD usage
    window.lbl_vhdp.setText("VHD-Pfad") # VHD path
    window.lbl_vhdf.setText("VHD-Dateiformat") # VHD file format
    window.lbl_maxsize.setText("Maximale Größe") # Maximum size
    window.btn_vhdp.setText("Durchsuchen") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Neue virtuelle Festplatte erstellen") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Existierende virtuelle Festplatte anfügen") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Keine virtuelle Festplatte anfügen") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("CD-Controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD-Controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("HDD-Controller") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Maustyp") # Mouse type
    window.lbl_kbdtype.setText("Tastaturtyp") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Pfad der externen BIOS-Datei (Leerlassen für Standard-BIOS)")
    window.lbl_biosf.setText("Externe BIOS-Datei") # External BIOS file
    window.btn_biosf.setText("Durchsuchen") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Linux-Kernel") # Linux kernel
    window.lbl_initrd.setText("Linux-initrd-Image") # Linux initrd image
    window.lbl_cmd.setText("Linux-CMD-Argumente") # Linux cmd arguments
    window.btn_kernel.setText("Durchsuchen") # Browse
    window.btn_initrd.setText("Durchsuchen") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Netzwerkadapter") # Network adapter
    window.lbl_sound.setText("Soundkarte") # Sound card
    window.lbl_addargs.setText("Zusätzliche Argumente (falls nötig)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("CPU-Kerne") # CPU cores
    window.chb_usb.setText("USB-Support hinzufügen") # Add USB support
    window.lbl_accel.setText("Beschleunigung") # Acceleration

def translateErrDialogDE(window, errcode):
    window.setWindowTitle(f"EmuGUI - Fehler")

    if errcode.startswith("C"):
        window.label.setText("Innerhalb von EmuGUI ist ein kritischer Fehler aufgetreten, weshalb das Programm geschlossen werden muss.") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("Innerhalb von EmuGUI ist ein Fehler aufgetreten.") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI muss Sie warnen.") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI muss Ihnen etwas sagen.") # EmuGUI has something to say.

    window.label_2.setText("Fehlercode: " + errcode) # Error Code:

    window.label_3.setText(
        "Sollte dieser Fehler mehrmals auftreten, kontaktieren Sie Ihren Administrator und/oder suchen Sie über dem EmuGUI-Discord-Server oder auf der GitHub-Repository nach Rat."
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("OK") # OK