def translateMainUK(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Головниє меню") # Main
    window.tabWidget.setTabText(1, "Налаштування") # Settings

    # Main tab
    window.pushButton_8.setText("Новий віртуальний комп’ютер") # New virtual machine
    window.pushButton_9.setText("Запустіть віртуальний комп’ютер") # Start virtual machine
    window.pushButton_10.setText("Редагувати високоякісний виртзальний комп’ютер") # Edit selected virtual machine
    window.pushButton_11.setText("Видалити високоякісний виртзальний комп’ютер") # Delete selected virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Загальний") # General
    window.tabWidget_2.setTabText(2, "Про EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Мова") # Language
    window.pushButton_15.setText("Застосувати") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "System default" or window.comboBox_4.itemText(i) == "Systemstandard":
            window.comboBox_4.setItemText(i, "System default") # System default
            break

        i += 1

        if window.comboBox_4.itemText(i) == "По умолчанию системы" or window.comboBox_4.itemText(i) == "Па змаўчанні сістэмы":
            window.comboBox_4.setItemText(i, "System default") # System default
            break

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "System default" or window.comboBox_5.itemText(i) == "Systemstandard":
            window.comboBox_5.setItemText(i, "System default") # System default
            break

        i += 1

        if window.comboBox_5.itemText(i) == "По умолчанию системы" or window.comboBox_5.itemText(i) == "Па змаўчанні сістэмы":
            window.comboBox_5.setItemText(i, "System default") # System default
            break

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

    window.pushButton.setText("Огляд") # Browse
    window.pushButton_2.setText("Огляд") # Browse
    window.pushButton_3.setText("Огляд") # Browse
    window.pushButton_4.setText("Огляд") # Browse
    window.pushButton_5.setText("Огляд") # Browse
    window.pushButton_7.setText("Огляд") # Browse
    window.pushButton_12.setText("Огляд") # Browse
    window.pushButton_16.setText("Огляд") # Browse
    window.pushButton_17.setText("Огляд") # Browse
    window.pushButton_18.setText("Огляд") # Browse
    window.pushButton_19.setText("Огляд") # Browse
    window.pushButton_13.setText("Огляд") # Browse
    window.pushButton_14.setText("Огляд") # Browse
    window.pushButton_6.setText("Застосувати") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Built on Python and PyQt technology, licensed under GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner made by Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI on social media (у English)") # EmuGUI on social media (in English)

def translateNewVmUK(window):
    # First page
    window.label.setText("Звати") # Name
    window.label_3.setText("Архітектура") # Architecture
    window.comboBox.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.pushButton_3.setText("Наступний >") # Next >
    window.pushButton_2.setText("Скасувати") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Машина") # Machine
    window.label_5.setText("Процесор") # CPU
    window.label_6.setText("RAM у MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_3.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_5.setText("< Попередній") # < Previous
    window.pushButton_4.setText("Наступний >") # Next >
    window.pushButton_6.setText("Скасувати") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_2.itemText(i) == "Пусть QEMU решает":
            window.comboBox_2.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_3.itemText(i) == "Пусть QEMU решает":
            window.comboBox_3.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Машина") # Machine
    window.label_8.setText("Процесор") # CPU
    window.label_7.setText("RAM у MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_5.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_7.setText("< Попередній") # < Previous
    window.pushButton_8.setText("Наступний >") # Next >
    window.pushButton_9.setText("Скасувати") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_4.itemText(i) == "Пусть QEMU решает":
            window.comboBox_4.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_5.itemText(i) == "Пусть QEMU решает":
            window.comboBox_5.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Машина") # Machine
    window.label_11.setText("Процесор") # CPU
    window.label_10.setText("RAM у MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_7.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_10.setText("< Попередній") # < Previous
    window.pushButton_11.setText("Наступний >") # Next >
    window.pushButton_12.setText("Скасувати") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_6.itemText(i) == "Пусть QEMU решает":
            window.comboBox_6.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_7.itemText(i) == "Пусть QEMU решает":
            window.comboBox_7.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Машина") # Machine
    window.label_30.setText("Процесор") # CPU
    window.label_29.setText("RAM у MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Please select a machine") # Please select a machine
    window.comboBox_15.setPlaceholderText("Please select a processor") # Please select a processor

    window.pushButton_33.setText("< Попередній") # < Previous
    window.pushButton_34.setText("Наступний >") # Next >
    window.pushButton_35.setText("Скасувати") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_14.itemText(i) == "Пусть QEMU решает":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_15.itemText(i) == "Пусть QEMU решает":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Машина") # Machine
    window.label_35.setText("RAM у MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Please select a machine") # Please select a machine

    window.pushButton_37.setText("< Попередній") # < Previous
    window.pushButton_38.setText("Наступний >") # Next >
    window.pushButton_39.setText("Скасувати") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_20.itemText(i) == "Пусть QEMU решает":
            window.comboBox_20.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Машина") # Machine
    window.label_36.setText("RAM у MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Please select a machine") # Please select a machine

    window.pushButton_41.setText("< Попередній") # < Previous
    window.pushButton_40.setText("Наступний >") # Next >
    window.pushButton_42.setText("Скасувати") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_21.itemText(i) == "Пусть QEMU решает":
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

        elif window.comboBox_18.itemText(i) == "Neue virtuelle Festplatte erstellen":
            window.comboBox_18.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Создать новый виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Existierende virtuelle Festplatte anfügen":
            window.comboBox_18.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Добавить существующий виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Keine virtuelle Festplatte anfügen":
            window.comboBox_18.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Не добавлять виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("VHD path") # VHD path
    window.label_14.setText("VHD Файл формат") # VHD file format
    window.label_15.setText("Maximum size") # Maximum size

    window.comboBox_8.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.pushButton_13.setText("Огляд") # Browse
    window.pushButton_16.setText("< Попередній") # < Previous
    window.pushButton_14.setText("Наступний >") # Next >
    window.pushButton_15.setText("Скасувати") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Мережа") # Network
    window.label_28.setText("Мишка") # Mouse

    window.comboBox_10.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.pushButton_18.setText("< Попередній") # < Previous
    window.pushButton_17.setText("Наступний >") # Next >
    window.pushButton_19.setText("Скасувати") # Cancel

    # Fifth page
    window.label_19.setText(
        "Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("External BIOS file") # External BIOS file

    window.pushButton_36.setText("Огляд") # Browse
    window.pushButton_25.setText("< Попередній") # < Previous
    window.pushButton_24.setText("Наступний >") # Next >
    window.pushButton_23.setText("Скасувати") # Cancel

    # Sixth page
    window.label_23.setText("Звукова карта") # Sound card
    window.label_33.setText("CPU cores") # CPU cores
    window.label_34.setText("Клавіатура") # Keyboard
    window.label_21.setText("Клавіатура layout") # Keyboard layout

    window.pushButton_28.setText("< Попередній") # < Previous
    window.pushButton_27.setText("Наступний >") # Next >
    window.pushButton_26.setText("Скасувати") # Cancel

    # Seventh page
    window.label_24.setText("Linux ядро") # Linux kernel
    window.label_25.setText("Linux initrd імідж") # Linux initrd image
    window.label_26.setText("Linux cmd args") # Linux cmd args

    window.pushButton.setText("Огляд") # Browse
    window.pushButton_32.setText("Огляд") # Browse
    window.pushButton_31.setText("< Попередній") # < Previous
    window.pushButton_30.setText("Наступний >") # Next >
    window.pushButton_29.setText("Скасувати") # Cancel

    # Eighth page
    window.label_2.setText("Additional arguments (if needed)") # Additional arguments (if needed)

    window.checkBox_2.setText("Я хочу установити Windows 2000\n(Знецінений)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Добавити USB пітримка") # Add USB support

    window.pushButton_22.setText("< Попередній") # < Previous
    window.pushButton_20.setText("Закінчити") # Finish
    window.pushButton_21.setText("Скасувати") # Cancel

def translateStartVmUK(window):
    window.label_4.setText("Дата і час") # Date & Time
    window.label_3.setText("Boot from") # Boot from
    
    window.label_5.setText("""
    Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Огляд") # Browse
    window.pushButton_2.setText("Огляд") # Browse
    window.pushButton_5.setText("Set to system") # Set to system
    window.pushButton_3.setText("Запустіть VM") # Start VM
    window.pushButton_4.setText("Скасувати") # Cancel

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox.itemText(i) == "Пусть QEMU решает":
            window.comboBox.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

def translateVmExistsUK(window):
    window.label.setText(
        "Вибачте, but a VM with this name already exists."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Please consider either deleting that VM or thinking of a new name."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsUK(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Вибачте, but the disk you want to create is already existant."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Do you want to keep (Залишити) or overwrite (Переписати) it?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Переписати") # Overwrite
    window.pushButton_2.setText("Залишити") # Keep

"""
def translateUpdateAvailableUK(window):
    window.label.setText(
        "An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.\n\nThe \"I want to download a pre-release from GitLab!\" button is only here temporarily as the stable repository hasn't been hosted on there yet at the time this pre-release version has been worked on."
    ) # An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.

    window.pushButton.setText("Так") # Yes
    window.pushButton_2.setText("Ні") # No

def translateNoUpdateAvailableUK(window):
    window.label.setText("You are already running the latest version of EmuGUI.") # You are already running the latest version of EmuGUI.
    window.label_2.setText("...or don't have an internet connection.") # ...or don't have an internet connection.

    window.pushButton.setText("OK") # OK
"""

def translateSettingsPendingUK(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("You didn't setup the QEMU paths.")
    window.label_2.setText("Please go to settings to do that and try again afterwards.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewUK(window):
    window.label.setText(
        "This VM is made with a version of EmuGUI that is too new. Please use a later version!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingUK(window, arch):
    window.label.setText(
        f"Вибачте, but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Налаштування/QEMU to solve this issue."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingUK(window):
    window.label.setText(
        "Вибачте, but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Налаштування/QEMU to solve this issue."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMUK(window):
    # Buttons on all tabs
    window.pushButton.setText("Скасувати") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Загальний") # General
    window.tabWidget.setTabText(1, "Машина") # Machine
    window.tabWidget.setTabText(2, "Virtual hard disks") # Virtual hard disks
    window.tabWidget.setTabText(3, "Периферійний") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Additional components") # Additional components

    # Translations for General tab
    window.label.setText("Звати") # Name
    window.label_2.setText("Архітектура") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("Процесор") # CPU
    window.label_18.setText("Машина") # Machine
    window.label_19.setText("RAM у MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_11.itemText(i) == "Пусть QEMU решает":
            window.comboBox_11.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_12.itemText(i) == "Пусть QEMU решает":
            window.comboBox_12.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("Процесор") # CPU
    window.label_22.setText("Машина") # Machine
    window.label_21.setText("RAM у MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_13.itemText(i) == "Пусть QEMU решает":
            window.comboBox_13.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_14.itemText(i) == "Пусть QEMU решает":
            window.comboBox_14.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("Процесор") # CPU
    window.label_25.setText("Машина") # Machine
    window.label_24.setText("RAM у MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_15.itemText(i) == "Пусть QEMU решает":
            window.comboBox_15.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_16.itemText(i) == "Пусть QEMU решает":
            window.comboBox_16.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("Процесор") # CPU
    window.label_28.setText("Машина") # Machine
    window.label_27.setText("RAM у MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_17.itemText(i) == "Пусть QEMU решает":
            window.comboBox_17.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        elif window.comboBox_18.itemText(i) == "Пусть QEMU решает":
            window.comboBox_18.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("VHD usage") # VHD usage
    window.label_4.setText("VHD path") # VHD path
    window.label_5.setText("VHD фаіл формат") # VHD file format
    window.label_6.setText("Maximum size") # Maximum size
    window.pushButton_3.setText("Огляд") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Neue virtuelle Festplatte erstellen":
            window.comboBox_2.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Создать новый виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Existierende virtuelle Festplatte anfügen":
            window.comboBox_2.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Добавить существующий виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Keine virtuelle Festplatte anfügen":
            window.comboBox_2.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Не добавлять виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Mouse type") # Mouse type
    window.label_8.setText("Keyboard type") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Location of external BIOS file (Leave empty to use the default BIOS)")
    window.label_12.setText("External BIOS file") # External BIOS file
    window.pushButton_4.setText("Огляд") # Browse

    # Translations for Linux tab
    window.label_13.setText("Linux ядро") # Linux kernel
    window.label_14.setText("Linux initrd імідж") # Linux initrd image
    window.label_15.setText("Linux cmd arguments") # Linux cmd arguments
    window.pushButton_5.setText("Огляд") # Browse
    window.pushButton_6.setText("Огляд") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Network adapter") # Network adapter
    window.label_16.setText("Sound card") # Sound card
    window.label_29.setText("Additional arguments (if necessary)") # Additional arguments (if necessary)
    window.label_30.setText("CPU cores") # CPU cores
    window.checkBox.setText("Добавити USB пітримка") # Add USB support