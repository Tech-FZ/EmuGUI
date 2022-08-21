def translateMainEN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Main")
    window.tabWidget.setTabText(1, "Settings")

    # Main tab
    window.pushButton_8.setText("New virtual machine")
    window.pushButton_9.setText("Start virtual machine")
    window.pushButton_10.setText("Edit selected virtual machine")
    window.pushButton_11.setText("Delete selected virtual machine")

    # Settings tabs
    window.tabWidget_2.setTabText(0, "General")
    window.tabWidget_2.setTabText(3, "About EmuGUI")

    # General tab
    window.label_15.setText("Language")
    window.pushButton_15.setText("Apply")

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "System default" or window.comboBox_4.itemText(i) == "Systemstandard":
            window.comboBox_4.setItemText(i, "System default")
            break

        i += 1

    # QEMU tab
    window.label.setText("qemu-img Path")
    window.label_2.setText("qemu-system-i386 Path")
    window.label_3.setText("qemu-system-x86_64 Path")
    window.label_4.setText("qemu-system-ppc Path")
    window.label_5.setText("qemu-system-mips64el Path")
    window.label_9.setText("qemu-system-aarch64 Path")
    window.label_11.setText("qemu-system-arm Path")
    window.label_16.setText("qemu-system-ppc64 Path")
    window.label_17.setText("qemu-system-mipsel Path")

    window.pushButton.setText("Browse")
    window.pushButton_2.setText("Browse")
    window.pushButton_3.setText("Browse")
    window.pushButton_4.setText("Browse")
    window.pushButton_5.setText("Browse")
    window.pushButton_7.setText("Browse")
    window.pushButton_12.setText("Browse")
    window.pushButton_16.setText("Browse")
    window.pushButton_17.setText("Browse")
    window.pushButton_6.setText("Apply")

    # Update tab
    window.label_12.setText("Update mirror")
    window.label_13.setText("Update notify frequency")
    window.label_14.setText("Update channel")

    window.pushButton_13.setText("Check for updates")
    window.pushButton_14.setText("Apply")

    # Combo box for update frequencies
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Everytime I run this program":
            window.comboBox_2.setItemText(i, "Everytime I run this program")
            break

        elif window.comboBox_2.itemText(i) == "Jedes Mal, wenn ich dieses Programm ausführe":
            window.comboBox_2.setItemText(i, "Everytime I run this program")
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Never" or window.comboBox_2.itemText(i) == "Nie":
            window.comboBox_2.setItemText(i, "Never")
            break

        i += 1

    # About tab
    window.label_7.setText("Built on Python and PyQt technology, licensed under GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
        )

def translateNewVmEN(window):
    # First page
    window.label.setText("Name")
    window.label_3.setText("Architecture")
    window.comboBox.setPlaceholderText("Please choose an architecture")

    window.pushButton_3.setText("Next >")
    window.pushButton_2.setText("Cancel")

    # Second page (i386/x64 machines)
    window.label_4.setText("Machine")
    window.label_5.setText("CPU")
    window.label_6.setText("RAM in MB")

    window.comboBox_2.setPlaceholderText("Please select a machine")
    window.comboBox_3.setPlaceholderText("Please select a processor")

    window.pushButton_5.setText("< Previous")
    window.pushButton_4.setText("Next >")
    window.pushButton_6.setText("Cancel")

    # Second page (PowerPC machines)
    window.label_9.setText("Machine")
    window.label_8.setText("CPU")
    window.label_7.setText("RAM in MB")

    window.comboBox_4.setPlaceholderText("Please select a machine")
    window.comboBox_5.setPlaceholderText("Please select a processor")

    window.pushButton_7.setText("< Previous")
    window.pushButton_8.setText("Next >")
    window.pushButton_9.setText("Cancel")

    # Second page (MIPSel machines)
    window.label_12.setText("Machine")
    window.label_11.setText("CPU")
    window.label_10.setText("RAM in MB")

    window.comboBox_6.setPlaceholderText("Please select a machine")
    window.comboBox_7.setPlaceholderText("Please select a processor")

    window.pushButton_10.setText("< Previous")
    window.pushButton_11.setText("Next >")
    window.pushButton_12.setText("Cancel")

    # Second page (ARM machines)
    window.label_31.setText("Machine")
    window.label_30.setText("CPU")
    window.label_29.setText("RAM in MB")

    window.comboBox_14.setPlaceholderText("Please select a machine")
    window.comboBox_15.setPlaceholderText("Please select a processor")

    window.pushButton_33.setText("< Previous")
    window.pushButton_34.setText("Next >")
    window.pushButton_35.setText("Cancel")

    # Third page
    window.label_13.setText("VHD path")
    window.label_14.setText("VHD file format")
    window.label_15.setText("Maximum size")

    window.comboBox_8.setPlaceholderText("(Please select a file format)")

    window.pushButton_13.setText("Browse")
    window.pushButton_16.setText("< Previous")
    window.pushButton_14.setText("Next >")
    window.pushButton_15.setText("Cancel")

    # Fourth page
    window.label_16.setText("VGA")
    window.label_17.setText("Network")
    window.label_28.setText("Mouse")

    window.comboBox_10.setPlaceholderText("(Please select a graphics adapter)")
    window.comboBox_11.setPlaceholderText("(Please select a network adapter)")

    window.pushButton_18.setText("< Previous")
    window.pushButton_17.setText("Next >")
    window.pushButton_19.setText("Cancel")

    # Fifth page
    window.label_19.setText("Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)")
    window.label_32.setText("External BIOS file")

    window.pushButton_36.setText("Browse")
    window.pushButton_25.setText("< Previous")
    window.pushButton_24.setText("Next >")
    window.pushButton_23.setText("Cancel")

    # Sixth page
    window.label_23.setText("Sound card")
    window.label_33.setText("CPU cores")
    window.label_34.setText("Keyboard")

    window.pushButton_28.setText("< Previous")
    window.pushButton_27.setText("Next >")
    window.pushButton_26.setText("Cancel")

    # Seventh page
    window.label_24.setText("Linux kernel")
    window.label_25.setText("Linux initrd image")
    window.label_26.setText("Linux cmd args")

    window.pushButton.setText("Browse")
    window.pushButton_32.setText("Browse")
    window.pushButton_31.setText("< Previous")
    window.pushButton_30.setText("Next >")
    window.pushButton_29.setText("Cancel")

    # Eighth page
    window.label_2.setText("Additional arguments (if needed)")

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)")
    window.checkBox_3.setText("Add USB support")

    window.pushButton_22.setText("< Previous")
    window.pushButton_20.setText("Finish")
    window.pushButton_21.setText("Cancel")

def translateStartVmEN(window):
    window.label_4.setText("Date & Time")
    window.label_3.setText("Boot from")

    window.label_5.setText("""
    Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.
    """)

    window.pushButton.setText("Browse")
    window.pushButton_2.setText("Browse")
    window.pushButton_5.setText("Set to system")
    window.pushButton_3.setText("Start VM")
    window.pushButton_4.setText("Cancel")

def translateVmExistsEN(window):
    window.label.setText("Sorry, but a VM with this name already exists.")
    window.label_2.setText("Please consider either deleting that VM or thinking of a new name.")

    window.pushButton.setText("OK")

def translateVhdExistsEN(window):
    window.label.setText("Sorry, but the disk you want to create is already existant.")
    window.label_2.setText("Do you want to keep or overwrite it?")

    window.pushButton.setText("Overwrite")
    window.pushButton_2.setText("Keep")

def translateUpdateAvailableEN(window):
    window.label.setText(
        "An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror."
        )

    window.pushButton.setText("Yes")
    window.pushButton_2.setText("No")

def translateNoUpdateAvailableEN(window):
    window.label.setText("You are already running the latest version of EmuGUI.")
    window.label_2.setText("...or don't have an internet connection.")

    window.pushButton.setText("OK")

def translateSettingsPendingEN(window):
    window.label.setText("You didn't setup the QEMU paths.")
    window.label_2.setText("Please go to settings to do that and try again afterwards.")

    window.pushButton.setText("OK")

def translateVmTooNewEN(window):
    window.label.setText("This VM is made with a version of EmuGUI that is too new. Please use a later version!")

    window.pushButton.setText("OK")