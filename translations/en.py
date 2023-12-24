from translations.systemdefaultset import *

def translateMainEN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Main") # Main
    window.tabWidget.setTabText(1, "Settings") # Settings

    # Main tab
    window.pushButton_8.setText("New virtual machine") # New virtual machine
    window.pushButton_9.setText("Start virtual machine") # Start virtual machine
    window.pushButton_10.setText("Edit selected virtual machine") # Edit selected virtual machine
    window.pushButton_11.setText("Delete selected virtual machine") # Delete selected virtual machine
    window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    window.pushButton_23.setText("Import virtual machine") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "General") # General
    window.tabWidget_2.setTabText(2, "About EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Language") # Language
    window.pushButton_15.setText("Apply") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("System default", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("System default", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img Path") # qemu-img Path
    window.label_2.setText("qemu-system-i386 Path") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64 Path") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc Path") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el Path") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64 Path") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm Path") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64 Path") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel Path") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips Path") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64 Path") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc Path") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64 Path") # qemu-system-sparc64 Path

    window.pushButton.setText("Browse") # Browse
    window.pushButton_2.setText("Browse") # Browse
    window.pushButton_3.setText("Browse") # Browse
    window.pushButton_4.setText("Browse") # Browse
    window.pushButton_5.setText("Browse") # Browse
    window.pushButton_7.setText("Browse") # Browse
    window.pushButton_12.setText("Browse") # Browse
    window.pushButton_16.setText("Browse") # Browse
    window.pushButton_17.setText("Browse") # Browse
    window.pushButton_18.setText("Browse") # Browse
    window.pushButton_19.setText("Browse") # Browse
    window.pushButton_13.setText("Browse") # Browse
    window.pushButton_14.setText("Browse") # Browse
    window.pushButton_6.setText("Apply") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Built on Python and PyQt technology, licensed under GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner made by Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI on social media (in English)") # EmuGUI on social media (in English)

def translateNewVmEN(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.label.setText("Name") # Name
    window.label_3.setText("Architecture") # Architecture
    window.comboBox.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.pushButton_3.setText("Next >") # Next >
    window.pushButton_2.setText("Cancel") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Machine") # Machine
    window.label_5.setText("CPU") # CPU
    window.label_6.setText("RAM in MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_3.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_5.setText("< Previous") # < Previous
    window.pushButton_4.setText("Next >") # Next >
    window.pushButton_6.setText("Cancel") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Machine") # Machine
    window.label_8.setText("CPU") # CPU
    window.label_7.setText("RAM in MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_5.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_7.setText("< Previous") # < Previous
    window.pushButton_8.setText("Next >") # Next >
    window.pushButton_9.setText("Cancel") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Machine") # Machine
    window.label_11.setText("CPU") # CPU
    window.label_10.setText("RAM in MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_7.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_10.setText("< Previous") # < Previous
    window.pushButton_11.setText("Next >") # Next >
    window.pushButton_12.setText("Cancel") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Machine") # Machine
    window.label_30.setText("CPU") # CPU
    window.label_29.setText("RAM in MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_15.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_33.setText("< Previous") # < Previous
    window.pushButton_34.setText("Next >") # Next >
    window.pushButton_35.setText("Cancel") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Machine") # Machine
    window.label_35.setText("RAM in MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Please select a machine") # Please select a machine

    window.pushButton_37.setText("< Previous") # < Previous
    window.pushButton_38.setText("Next >") # Next >
    window.pushButton_39.setText("Cancel") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Machine") # Machine
    window.label_36.setText("RAM in MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Please select a machine") # Please select a machine

    window.pushButton_41.setText("< Previous") # < Previous
    window.pushButton_40.setText("Next >") # Next >
    window.pushButton_42.setText("Cancel") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("VHD usage") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("VHD path") # VHD path
    window.label_14.setText("VHD file format") # VHD file format
    window.label_15.setText("Maximum size") # Maximum size
    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.pushButton_13.setText("Browse") # Browse
    window.pushButton_16.setText("< Previous") # < Previous
    window.pushButton_14.setText("Next >") # Next >
    window.pushButton_15.setText("Cancel") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Network") # Network
    window.label_28.setText("Mouse") # Mouse

    window.comboBox_10.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.pushButton_18.setText("< Previous") # < Previous
    window.pushButton_17.setText("Next >") # Next >
    window.pushButton_19.setText("Cancel") # Cancel

    # Fifth page
    window.label_19.setText(
        "Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("External BIOS file") # External BIOS file

    window.pushButton_36.setText("Browse") # Browse
    window.pushButton_25.setText("< Previous") # < Previous
    window.pushButton_24.setText("Next >") # Next >
    window.pushButton_23.setText("Cancel") # Cancel

    # Sixth page
    window.label_23.setText("Sound card") # Sound card
    window.label_33.setText("CPU cores")# CPU cores
    window.label_34.setText("Keyboard") # Keyboard
    window.label_21.setText("Keyboard layout") # Keyboard layout

    window.pushButton_28.setText("< Previous") # < Previous
    window.pushButton_27.setText("Next >") # Next >
    window.pushButton_26.setText("Cancel") # Cancel

    # Seventh page
    window.label_24.setText("Linux kernel") # Linux kernel
    window.label_25.setText("Linux initrd image") # Linux initrd image
    window.label_26.setText("Linux cmd args") # Linux cmd args

    window.pushButton.setText("Browse") # Browse
    window.pushButton_32.setText("Browse") # Browse
    window.pushButton_31.setText("< Previous") # < Previous
    window.pushButton_30.setText("Next >") # Next >
    window.pushButton_29.setText("Cancel") # Cancel

    # Eighth page
    window.label_71.setText("Acceleration") # Acceleration
    window.label_70.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    window.pushButton_81.setText("< Previous") # < Previous
    window.pushButton_77.setText("Next >") # Next >
    window.pushButton_80.setText("Cancel") # Cancel

    # Ninth page
    window.label_2.setText("Additional arguments (if needed)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Add USB support") # Add USB support

    window.pushButton_22.setText("< Previous") # < Previous
    window.pushButton_20.setText("Finish") # Finish
    window.pushButton_21.setText("Cancel") # Cancel

def translateStartVmEN(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Date & Time") # Date & Time
    window.label_3.setText("Boot from") # Boot from
    window.label_6.setText("TPM path (Linux only)") # TPM path (Linux only)
    window.label_7.setText("Create the TPM from the terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Browse") # Browse
    window.pushButton_2.setText("Browse") # Browse
    window.pushButton_6.setText("Browse") # Browse
    window.pushButton_5.setText("Set to system") # Set to system
    window.pushButton_3.setText("Start VM") # Start VM
    window.pushButton_4.setText("Cancel") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

def translateVmExistsEN(window):
    window.label.setText(
        "Sorry, but a VM with this name already exists."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Please consider either deleting that VM or thinking of a new name."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsEN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Sorry, but the disk you want to create is already existant."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Do you want to keep or overwrite it?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Overwrite") # Overwrite
    window.pushButton_2.setText("Keep") # Keep

def translateSettingsPendingEN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("You didn't setup the QEMU paths.")
    window.label_2.setText("Please go to settings to do that and try again afterwards.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewEN(window):
    window.label.setText(
        "This VM is made with a version of EmuGUI that is too new. Please use a later version!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingEN(window, arch):
    window.label.setText(
        f"Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingEN(window):
    window.label.setText(
        "Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMEN(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.pushButton.setText("Cancel") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "General") # General
    window.tabWidget.setTabText(1, "Machine") # Machine
    window.tabWidget.setTabText(2, "Virtual hard disks") # Virtual hard disks
    window.tabWidget.setTabText(3, "Peripherals") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Additional components") # Additional components

    # Translations for General tab
    window.label.setText("Name") # Name
    window.label_2.setText("Architecture") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("CPU") # CPU
    window.label_18.setText("Machine") # Machine
    window.label_19.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("CPU") # CPU
    window.label_22.setText("Machine") # Machine
    window.label_21.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("CPU") # CPU
    window.label_25.setText("Machine") # Machine
    window.label_24.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("CPU") # CPU
    window.label_28.setText("Machine") # Machine
    window.label_27.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("VHD usage") # VHD usage
    window.label_4.setText("VHD path") # VHD path
    window.label_5.setText("VHD file format") # VHD file format
    window.label_6.setText("Maximum size") # Maximum size
    window.pushButton_3.setText("Browse") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        i += 1

    window.label_37.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Mouse type") # Mouse type
    window.label_8.setText("Keyboard type") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Location of external BIOS file (Leave empty to use the default BIOS)")
    window.label_12.setText("External BIOS file") # External BIOS file
    window.pushButton_4.setText("Browse") # Browse

    # Translations for Linux tab
    window.label_13.setText("Linux kernel") # Linux kernel
    window.label_14.setText("Linux initrd image") # Linux initrd image
    window.label_15.setText("Linux cmd arguments") # Linux cmd arguments
    window.pushButton_5.setText("Browse") # Browse
    window.pushButton_6.setText("Browse") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Network adapter") # Network adapter
    window.label_16.setText("Sound card") # Sound card
    window.label_29.setText("Additional arguments (if necessary)") # Additional arguments (if necessary)
    window.label_30.setText("CPU cores") # CPU cores
    window.checkBox.setText("Add USB support") # Add USB support
    window.label_36.setText("Acceleration") # Acceleration

def translateErrDialogEN(window, errcode):
    window.setWindowTitle(f"EmuGUI - Error")
    
    if errcode.startswith("C"):
        window.label.setText("EmuGUI encountered a critical error and needs to be closed.") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI encountered an error.") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI has to warn you.") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI has something to say.") # EmuGUI has something to say.

    window.label_2.setText("Error Code: " + errcode) # Error Code:

    window.label_3.setText(
        "If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository."
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("OK") # OK