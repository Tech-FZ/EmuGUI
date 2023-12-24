from translations.systemdefaultset import *

def translateMainBE(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Галоўная") # Main
    window.tabWidget.setTabText(1, "Налады") # Settings

    # Main tab
    window.pushButton_8.setText("Стварыць віртуальную машыну") # New virtual machine
    window.pushButton_9.setText("Запусціць віртуальную машыну") # Start virtual machine
    window.pushButton_10.setText("Рэдагаваць абраную віртуальную машыну") # Edit selected virtual machine
    window.pushButton_11.setText("Выдаліць абраную віртуальную машыну") # Delete selected virtual machine
    window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    window.pushButton_23.setText("Import virtual machine") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Агульныя") # General
    window.tabWidget_2.setTabText(2, "Аб EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Мова") # Language
    window.pushButton_15.setText("Ужыць") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Па змаўчанні сістэмы", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Па змаўчанні сістэмы", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("Шлях да qemu-img") # qemu-img Path
    window.label_2.setText("Шлях да qemu-system-i386") # qemu-system-i386 Path
    window.label_3.setText("Шлях да qemu-system-x86_64") # qemu-system-x86_64 Path
    window.label_4.setText("Шлях да qemu-system-ppc") # qemu-system-ppc Path
    window.label_5.setText("Шлях да qemu-system-mips64el") # qemu-system-mips64el Path
    window.label_9.setText("Шлях да qemu-system-aarch64") # qemu-system-aarch64 Path
    window.label_11.setText("Шлях да qemu-system-arm") # qemu-system-arm Path
    window.label_16.setText("Шлях да qemu-system-ppc64") # qemu-system-ppc64 Path
    window.label_17.setText("Шлях да qemu-system-mipsel") # qemu-system-mipsel Path
    window.label_18.setText("Шлях да qemu-system-mips") # qemu-system-mips Path
    window.label_19.setText("Шлях да qemu-system-mips64") # qemu-system-mips64 Path
    window.label_12.setText("Шлях да qemu-system-sparc") # qemu-system-sparc Path
    window.label_13.setText("Шлях да qemu-system-sparc64") # qemu-system-sparc64 Path

    window.pushButton.setText("Агляд") # Browse
    window.pushButton_2.setText("Агляд") # Browse
    window.pushButton_3.setText("Агляд") # Browse
    window.pushButton_4.setText("Агляд") # Browse
    window.pushButton_5.setText("Агляд") # Browse
    window.pushButton_7.setText("Агляд") # Browse
    window.pushButton_12.setText("Агляд") # Browse
    window.pushButton_16.setText("Агляд") # Browse
    window.pushButton_17.setText("Агляд") # Browse
    window.pushButton_18.setText("Агляд") # Browse
    window.pushButton_19.setText("Агляд") # Browse
    window.pushButton_13.setText("Агляд") # Browse
    window.pushButton_14.setText("Агляд") # Browse
    window.pushButton_6.setText("Ужыць") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Сабрана на Python і тэхналогіі PyQt, ліцэнзавана пад GNU General Public License 3.0")

    window.label_10.setText(
        """
        ПАПЯРЭДЖАННЕ: Гэтая праграма пастаўляецца з АБСАЛЮТНА НІЯКІМІ ГАРАНТЫЯМІ ў адпаведнасці з дзеючым заканадаўствам.
        Падрабязнасці гл. у ліцэнзіі GNU GPL.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Банер зроблены Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI у сацыяльных сетках (на англійскай мове)") # EmuGUI on social media (in English)

def translateNewVmBE(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.label.setText("Назва") # Name
    window.label_3.setText("Архітэктура") # Architecture
    window.comboBox.setPlaceholderText("Калі ласка, абярыце архітэктуру") # Please choose an architecture

    window.pushButton_3.setText("Далей >") # Next >
    window.pushButton_2.setText("Адмена") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Машына") # Machine
    window.label_5.setText("Працэсар") # CPU
    window.label_6.setText("АЗП у MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine
    window.comboBox_3.setPlaceholderText("Калі ласка абярыце працэсар") # Please select a processor

    window.pushButton_5.setText("< Назад") # < Previous
    window.pushButton_4.setText("Далей >") # Next >
    window.pushButton_6.setText("Адмена") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Машына") # Machine
    window.label_8.setText("Працэсар") # CPU
    window.label_7.setText("АЗП у MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine
    window.comboBox_5.setPlaceholderText("Калі ласка абярыце працэсар") # Please select a processor

    window.pushButton_7.setText("< Назад") # < Previous
    window.pushButton_8.setText("Далей >") # Next >
    window.pushButton_9.setText("Адмена") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Машына") # Machine
    window.label_11.setText("Працэсар") # CPU
    window.label_10.setText("АЗП у MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine
    window.comboBox_7.setPlaceholderText("Калі ласка абярыце працэсар") # Please select a processor

    window.pushButton_10.setText("< Назад") # < Previous
    window.pushButton_11.setText("Далей >") # Next >
    window.pushButton_12.setText("Адмена") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Машына") # Machine
    window.label_30.setText("Працэсар") # CPU
    window.label_29.setText("АЗП у MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine
    window.comboBox_15.setPlaceholderText("Калі ласка абярыце працэсар") # Please select a processor

    window.pushButton_33.setText("< Назад") # < Previous
    window.pushButton_34.setText("Далей >") # Next >
    window.pushButton_35.setText("Адмена") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Машына") # Machine
    window.label_35.setText("АЗП у MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine

    window.pushButton_37.setText("< Назад") # < Previous
    window.pushButton_38.setText("Далей >") # Next >
    window.pushButton_39.setText("Адмена") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Машына") # Machine
    window.label_36.setText("АЗП у MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Калі ласка абярыце машыну") # Please select a machine

    window.pushButton_41.setText("< Назад") # < Previous
    window.pushButton_40.setText("Далей >") # Next >
    window.pushButton_42.setText("Адмена") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("Выкарыстанне VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Стварыць новы віртуальны жорсткі дыск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Дадаць існуючы віртуальны жорсткі дыск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Не дадаваць віртуальны жорсткі дыск") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("Шлях да VHD") # VHD path
    window.label_14.setText("Фармат файла VHD") # VHD file format
    window.label_15.setText("Максімальны памер") # Maximum size
    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Калі ласка, абярыце фармат файла)") # (Please select a file format)

    window.pushButton_13.setText("Агляд") # Browse
    window.pushButton_16.setText("< Назад") # < Previous
    window.pushButton_14.setText("Далей >") # Next >
    window.pushButton_15.setText("Адмена") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Сетка") # Network
    window.label_28.setText("Мыш") # Mouse

    window.comboBox_10.setPlaceholderText("(Калі ласка абярыце графічны адаптар)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Калі ласка абярыце сеткавы адаптар)") # (Please select a network adapter)

    window.pushButton_18.setText("< Назад") # < Previous
    window.pushButton_17.setText("Далей >") # Next >
    window.pushButton_19.setText("Адмена") # Cancel

    # Fifth page
    window.label_19.setText(
        "Размяшчэнне знешняга\nфайла BIOS (Пакіньце\nпустым, каб выкарыстоўваць\nBIOS па змаўчанні)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("Вонкавы файл BIOS") # External BIOS file

    window.pushButton_36.setText("Агляд") # Browse
    window.pushButton_25.setText("< Назад") # < Previous
    window.pushButton_24.setText("Далей >") # Next >
    window.pushButton_23.setText("Адмена") # Cancel

    # Sixth page
    window.label_23.setText("Гукавая карта") # Sound card
    window.label_33.setText("Ядра працэсара")# CPU cores
    window.label_34.setText("Клавіятура") # Keyboard
    window.label_21.setText("Раскладка клавіятуры") # Keyboard layout

    window.pushButton_28.setText("< Назад") # < Previous
    window.pushButton_27.setText("Далей >") # Next >
    window.pushButton_26.setText("Адмена") # Cancel

    # Seventh page
    window.label_24.setText("Ядро Linux") # Linux kernel
    window.label_25.setText("Выява initrd Linux") # Linux initrd image
    window.label_26.setText("Аргументы Linux cmd") # Linux cmd args

    window.pushButton.setText("Агляд") # Browse
    window.pushButton_32.setText("Агляд") # Browse
    window.pushButton_31.setText("< Назад") # < Previous
    window.pushButton_30.setText("Далей >") # Next >
    window.pushButton_29.setText("Адмена") # Cancel

    # Eighth page
    window.label_71.setText("Acceleration") # Acceleration
    window.label_70.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1
    
    window.pushButton_81.setText("< Назад") # < Previous
    window.pushButton_77.setText("Далей >") # Next >
    window.pushButton_80.setText("Адмена") # Cancel

    # Ninth page
    window.label_2.setText("Дадатковыя аргументы (пры неабходнасці)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Дадаць падтрымку USB") # Add USB support

    window.pushButton_22.setText("< Назад") # < Previous
    window.pushButton_20.setText("Finish") # Finish
    window.pushButton_21.setText("Адмена") # Cancel

def translateStartVmBE(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Дата і Час") # Date & Time
    window.label_3.setText("Загрузка з") # Boot from
    window.label_6.setText("TPM path (Linux only)") # TPM path (Linux only)
    window.label_7.setText("Create the TPM from the terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Заўвага: Калі ВМ не запускаецца на працягу пяці хвілін, то неабходна праверыць наладкі ВМ і QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Агляд") # Browse
    window.pushButton_2.setText("Агляд") # Browse
    window.pushButton_6.setText("Агляд") # Browse
    window.pushButton_5.setText("Усталяваць у сістэму") # Set to system
    window.pushButton_3.setText("Запусціць віртуальную машыну") # Start VM
    window.pushButton_4.setText("Адмена") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

def translateVmExistsBE(window):
    window.label.setText(
        "Выбачыце, але віртуальная машына з такім імем ужо існуе."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Калі ласка, падумайце аб тым, каб або выдаліць гэты VM, або прыдумаць новую назву."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsBE(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Выбачыце, але дыск, які вы жадаеце стварыць, ужо існуе."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Вы хочаце захаваць ці перазапісаць яго?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Перазапісаць") # Overwrite
    window.pushButton_2.setText("Захаваць") # Keep

def translateSettingsPendingBE(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Вы не наладзілі шляхі QEMU.")
    window.label_2.setText("Калі ласка, перайдзіце ў наладкі, каб зрабіць гэта, і паспрабуйце яшчэ раз.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewBE(window):
    window.label.setText(
        "Гэта віртуальная машына зроблена з версіяй EmuGUI, якая з'яўляецца занадта новай. Калі ласка, выкарыстоўвайце пазнейшую версію!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingBE(window, arch):
    window.label.setText(
        f"Выбачыце, але EmuGUI пакуль не наладжаны на выкарыстанне \"qemu-system-{arch}\".\nАднак гэты кампанент неабходзен для запуску дадзенай віртуальнай машыны.\nКалі ласка, перайдзіце ў Настройкі/QEMU, каб вырашыць гэтую праблему."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingBE(window):
    window.label.setText(
        "Выбачыце, але EmuGUI пакуль не наладжаны на выкарыстанне \"qemu-img\".\nАднак гэты кампанент неабходны для стварэння ці рэдагаванні віртуальных машын.\nКалі ласка, перайдзіце ў Настройкі/QEMU, каб вырашыць гэтую праблему."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMBE(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.pushButton.setText("Адмена") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Агульныя") # General
    window.tabWidget.setTabText(1, "Машына") # Machine
    window.tabWidget.setTabText(2, "Віртуальныя жорсткія дыскі") # Virtual hard disks
    window.tabWidget.setTabText(3, "Перыферыйныя прылады") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Дадатковыя кампаненты") # Additional components

    # Translations for General tab
    window.label.setText("Назва") # Name
    window.label_2.setText("Архітэктура") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("Працэсар") # CPU
    window.label_18.setText("Машына") # Machine
    window.label_19.setText("АЗП у MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("Працэсар") # CPU
    window.label_22.setText("Машына") # Machine
    window.label_21.setText("АЗП у MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("Працэсар") # CPU
    window.label_25.setText("Машына") # Machine
    window.label_24.setText("АЗП у MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("Працэсар") # CPU
    window.label_28.setText("Машына") # Machine
    window.label_27.setText("АЗП у MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("Выкарыстанне VHD") # VHD usage
    window.label_4.setText("Шлях да VHD") # VHD path
    window.label_5.setText("Фармат файла VHD") # VHD file format
    window.label_6.setText("Максімальны памер") # Maximum size
    window.pushButton_3.setText("Агляд") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Стварыць новы віртуальны жорсткі дыск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Дадаць існуючы віртуальны жорсткі дыск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Не дадаваць віртуальны жорсткі дыск") # Don't add a virtual hard drive
            break

        i += 1

    window.label_70.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Тып мышы") # Mouse type
    window.label_8.setText("Тып клавіятуры") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Размяшчэнне знешняга файла BIOS (Пакіньце пустым, каб выкарыстоўваць BIOS па змаўчанні)")
    window.label_12.setText("Вонкавы файл BIOS") # External BIOS file
    window.pushButton_4.setText("Агляд") # Browse

    # Translations for Linux tab
    window.label_13.setText("Ядро Linux") # Linux kernel
    window.label_14.setText("Выява initrd Linux") # Linux initrd image
    window.label_15.setText("Linux cmd arguments") # Linux cmd arguments
    window.pushButton_5.setText("Агляд") # Browse
    window.pushButton_6.setText("Агляд") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Network adapter") # Network adapter
    window.label_16.setText("Гукавая карта") # Sound card
    window.label_29.setText("Дадатковыя аргументы (пры неабходнасці)") # Additional arguments (if necessary)
    window.label_30.setText("Ядра працэсара") # CPU cores
    window.checkBox.setText("Дадаць падтрымку USB") # Add USB support
    window.label_36.setText("Acceleration") # Acceleration

def translateErrDialogBE(window, errcode):
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