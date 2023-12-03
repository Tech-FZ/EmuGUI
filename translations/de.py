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
    window.tabWidget_2.setTabText(2, "Über EmuGUI") # About EmuGUI

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
    window.pushButton_6.setText("Übernehmen") # Apply

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
    window.label.setText("Name") # Name
    window.label_3.setText("Architektur") # Architecture
    window.comboBox.setPlaceholderText("Bitte wählen Sie eine Architektur") # Please choose an architecture

    window.pushButton_3.setText("Weiter >") # Next >
    window.pushButton_2.setText("Abbrechen") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Maschine") # Machine
    window.label_5.setText("CPU") # CPU
    window.label_6.setText("RAM in MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine
    window.comboBox_3.setPlaceholderText("Bitte wählen Sie einen Prozessor") # Please select a processor

    window.pushButton_5.setText("< Zurück") # < Previous
    window.pushButton_4.setText("Weiter >") # Next >
    window.pushButton_6.setText("Abbrechen") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Maschine") # Machine
    window.label_8.setText("CPU") # CPU
    window.label_7.setText("RAM in MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine
    window.comboBox_5.setPlaceholderText("Bitte wählen Sie einen Prozessor") # Please select a processor

    window.pushButton_7.setText("< Zurück") # < Previous
    window.pushButton_8.setText("Weiter >") # Next >
    window.pushButton_9.setText("Abbrechen") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Maschine") # Machine
    window.label_11.setText("CPU") # CPU
    window.label_10.setText("RAM in MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine
    window.comboBox_7.setPlaceholderText("Bitte wählen Sie einen Prozessor") # Please select a processor

    window.pushButton_10.setText("< Zurück") # < Previous
    window.pushButton_11.setText("Weiter >") # Next >
    window.pushButton_12.setText("Abbrechen") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Maschine") # Machine
    window.label_30.setText("CPU") # CPU
    window.label_29.setText("RAM in MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine
    window.comboBox_15.setPlaceholderText("Bitte wählen Sie einen Prozessor") # Please select a processor

    window.pushButton_33.setText("< Zurück") # < Previous
    window.pushButton_34.setText("Weiter >") # Next >
    window.pushButton_35.setText("Abbrechen") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Maschine") # Machine
    window.label_35.setText("RAM in MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine

    window.pushButton_37.setText("< Zurück") # < Previous
    window.pushButton_38.setText("Weiter >") # Next >
    window.pushButton_39.setText("Abbrechen") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Maschine") # Machine
    window.label_36.setText("RAM in MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Bitte wählen Sie eine Maschine") # Please select a machine

    window.pushButton_41.setText("< Zurück") # < Previous
    window.pushButton_40.setText("Weiter >") # Next >
    window.pushButton_42.setText("Abbrechen") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("VHD-Nutzung") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Neue virtuelle Festplatte erstellen") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Existierende virtuelle Festplatte anfügen") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Keine virtuelle Festplatte anfügen") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("VHD-Ort") # VHD path
    window.label_14.setText("VHD-Dateiformat") # VHD file format
    window.label_15.setText("Maximale Größe") # Maximum size
    window.label_73.setText("HDD-Controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Bitte wählen Sie ein Dateiformat)") # (Please select a file format)

    window.pushButton_13.setText("Durchsuchen") # Browse
    window.pushButton_16.setText("< Zurück") # < Previous
    window.pushButton_14.setText("Weiter >") # Next >
    window.pushButton_15.setText("Abbrechen") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Netzwerk") # Network
    window.label_28.setText("Maus") # Mouse
    window.label_21.setText("Tastaturlayout") # Keyboard layout

    window.comboBox_10.setPlaceholderText("(Bitte wählen Sie einen Grafikadapter)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Bitte wählen Sie einen Netzwerkadapter)") # (Please select a network adapter)

    window.pushButton_18.setText("< Zurück") # < Previous
    window.pushButton_17.setText("Weiter >") # Next >
    window.pushButton_19.setText("Abbrechen") # Cancel

    # Fifth page
    window.label_19.setText(
        "Ort der externen\nBIOS-Datei (Lassen\nSie dies leer, um das\nStandard-BIOS zu\nnutzen.)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("Externe BIOS-Datei") # External BIOS file

    window.pushButton_36.setText("Durchsuchen") # Browse
    window.pushButton_25.setText("< Zurück") # < Previous
    window.pushButton_24.setText("Weiter >") # Next >
    window.pushButton_23.setText("Abbrechen") # Cancel

    # Sixth page
    window.label_23.setText("Soundkarte") # Sound card
    window.label_33.setText("CPU-Kerne") # CPU cores
    window.label_34.setText("Tastatur") # Keyboard

    window.pushButton_28.setText("< Zurück") # < Previous
    window.pushButton_27.setText("Weiter >") # Next >
    window.pushButton_26.setText("Abbrechen") # Cancel

    # Seventh page
    window.label_24.setText("Linux-Kernel") # Linux kernel
    window.label_25.setText("Linux-initrd-Image") # Linux initrd image
    window.label_26.setText("Linux-CMD-Argumente") # Linux cmd args

    window.pushButton.setText("Durchsuchen") # Browse
    window.pushButton_32.setText("Durchsuchen") # Browse
    window.pushButton_31.setText("< Zurück") # < Previous
    window.pushButton_30.setText("Weiter >") # Next >
    window.pushButton_29.setText("Abbrechen") # Cancel

    # Eighth page
    window.label_71.setText("Beschleunigung") # Acceleration
    window.label_70.setText("CD-Controller 1") # CD controller 1
    window.label_72.setText("CD-Controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1
    
    window.pushButton_81.setText("< Zurück") # < Previous
    window.pushButton_77.setText("Weiter >") # Next >
    window.pushButton_80.setText("Abbrechen") # Cancel

    # Ninth page
    window.label_2.setText("Zusätzliche Argumente (sofern nötig)") # Additional arguments (if needed)

    window.checkBox_2.setText("Ich will Windows 2000 installieren\n(überholt)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("USB-Support hinzufügen") # Add USB support

    window.pushButton_22.setText("< Zurück") # < Previous
    window.pushButton_20.setText("Abschließen") # Finish
    window.pushButton_21.setText("Abbrechen") # Cancel

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
    window.pushButton_5.setText("Auf Systemzeit setzen") # Set to system
    window.pushButton_3.setText("VM starten") # Start VM
    window.pushButton_4.setText("Abbrechen") # Cancel

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
    window.pushButton.setText("Abbrechen") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Allgemein") # General
    window.tabWidget.setTabText(1, "Maschine") # Machine
    window.tabWidget.setTabText(2, "Virtuelle Festplatten") # Virtual hard disks
    window.tabWidget.setTabText(3, "Peripherie") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Zusätzliche Komponenten") # Additional components

    # Translations for General tab
    window.label.setText("Name") # Name
    window.label_2.setText("Architektur") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("CPU") # CPU
    window.label_18.setText("Maschine") # Machine
    window.label_19.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("CPU") # CPU
    window.label_22.setText("Maschine") # Machine
    window.label_21.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("CPU") # CPU
    window.label_25.setText("Maschine") # Machine
    window.label_24.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("CPU") # CPU
    window.label_28.setText("Maschine") # Machine
    window.label_27.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("VHD-Nutzung") # VHD usage
    window.label_4.setText("VHD-Pfad") # VHD path
    window.label_5.setText("VHD-Dateiformat") # VHD file format
    window.label_6.setText("Maximale Größe") # Maximum size
    window.pushButton_3.setText("Durchsuchen") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Neue virtuelle Festplatte erstellen") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Existierende virtuelle Festplatte anfügen") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Keine virtuelle Festplatte anfügen") # Don't add a virtual hard drive
            break
        
        i += 1

    window.label_37.setText("CD-Controller 1") # CD controller 1
    window.label_72.setText("CD-Controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("HDD-Controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "QEMU überlassen") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Maustyp") # Mouse type
    window.label_8.setText("Tastaturtyp") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Ort der externen BIOS-Datei (Leerlassen für Standard-BIOS)")
    window.label_12.setText("Externe BIOS-Datei") # External BIOS file
    window.pushButton_4.setText("Durchsuchen") # Browse

    # Translations for Linux tab
    window.label_13.setText("Linux-Kernel") # Linux kernel
    window.label_14.setText("Linux-initrd-Image") # Linux initrd image
    window.label_15.setText("Linux-CMD-Argumente") # Linux cmd arguments
    window.pushButton_5.setText("Durchsuchen") # Browse
    window.pushButton_6.setText("Durchsuchen") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Netzwerkadapter") # Network adapter
    window.label_16.setText("Soundkarte") # Sound card
    window.label_29.setText("Zusätzliche Argumente (falls nötig)") # Additional arguments (if necessary)
    window.label_30.setText("CPU-Kerne") # CPU cores
    window.checkBox.setText("USB-Support hinzufügen") # Add USB support
    window.label_36.setText("Beschleunigung") # Acceleration

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