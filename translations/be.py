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
    window.tabWidget_2.setTabText(3, "Аб EmuGUI") # About EmuGUI

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
    window.lbl_alpha.setText("Шлях да qemu-system-alpha") # qemu-system-alpha Path
    window.lbl_riscv32.setText("Шлях да qemu-system-riscv32") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("Шлях да qemu-system-riscv64") # qemu-system-riscv64 Path

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
    window.btn_alpha.setText("Агляд") # Browse
    window.btn_riscv32.setText("Агляд") # Browse
    window.btn_riscv64.setText("Агляд") # Browse
    window.pushButton_6.setText("Ужыць") # Apply
    window.btn_apply_qemu2.setText("Ужыць") # Apply

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
    window.lbl_vmname.setText("Назва") # Name
    window.lbl_arch.setText("Архітэктура") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Далей >") # Next >
    window.btn_cancel1.setText("Адмена") # Cancel

    # Second page
    window.lbl_machine.setText("Машына") # Machine
    window.lbl_cpu.setText("Працэсар") # CPU
    window.lbl_ram.setText("АЗП у MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Назад") # < Previous
    window.pb_next2.setText("Далей >") # Next >
    window.pb_cancel2.setText("Адмена") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Выкарыстанне VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Стварыць новы віртуальны жорсткі дыск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Дадаць існуючы віртуальны жорсткі дыск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Не дадаваць віртуальны жорсткі дыск") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Шлях да VHD") # VHD path
    window.lbl_vhdF.setText("Фармат файла VHD") # VHD file format
    window.lbl_maxsize.setText("Максімальны памер") # Maximum size
    window.lbl_hddC.setText("HDD controller") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Агляд") # Browse
    window.btn_prev3.setText("< Назад") # < Previous
    window.btn_next3.setText("Далей >") # Next >
    window.btn_cancel3.setText("Адмена") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Сетка") # Network
    window.lbl_mouse.setText("Мыш") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Назад") # < Previous
    window.btn_next4.setText("Далей >") # Next >
    window.btn_cancel4.setText("Адмена") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Размяшчэнне знешняга файла BIOS (Пакіньце пустым, каб выкарыстоўваць BIOS па змаўчанні)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Вонкавы файл BIOS") # External BIOS file

    window.btn_biosF.setText("Агляд") # Browse
    window.btn_prev5.setText("< Назад") # < Previous
    window.btn_next5.setText("Далей >") # Next >
    window.btn_cancel5.setText("Адмена") # Cancel

    # Sixth page
    window.lbl_sound.setText("Гукавая карта") # Sound card
    window.lbl_cores.setText("Ядра працэсара")# CPU cores
    window.lbl_kbd.setText("Клавіятура") # Keyboard
    window.lbl_kbdlayout.setText("Раскладка клавіятуры") # Keyboard layout

    window.btn_prev6.setText("< Назад") # < Previous
    window.btn_next6.setText("Далей >") # Next >
    window.btn_cancel6.setText("Адмена") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Ядро Linux") # Linux kernel
    window.lbl_initrd.setText("Выява initrd Linux") # Linux initrd image
    window.lbl_cmd.setText("Аргументы Linux cmd") # Linux cmd args

    window.btn_kernel.setText("Агляд") # Browse
    window.btn_initrd.setText("Агляд") # Browse
    window.btn_prev7.setText("< Назад") # < Previous
    window.btn_next7.setText("Далей >") # Next >
    window.btn_cancel7.setText("Адмена") # Cancel

    # Eighth page
    window.lbl_accel.setText("Acceleration") # Acceleration
    window.lbl_cdc1.setText("CD controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Назад") # < Previous
    window.btn_next8.setText("Далей >") # Next >
    window.btn_cancel8.setText("Адмена") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Дадатковыя аргументы (пры неабходнасці)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Дадаць падтрымку USB") # Add USB support

    window.btn_prev9.setText("< Назад") # < Previous
    window.btn_finish.setText("Finish") # Finish
    window.btn_cancel9.setText("Адмена") # Cancel

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
    window.btn_cancel.setText("Адмена") # Cancel
    window.btn_ok.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Агульныя") # General
    window.tabWidget.setTabText(1, "Машына") # Machine
    window.tabWidget.setTabText(2, "Віртуальныя жорсткія дыскі") # Virtual hard disks
    window.tabWidget.setTabText(3, "Перыферыйныя прылады") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Дадатковыя кампаненты") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Назва") # Name
    window.lbl_arch.setText("Архітэктура") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("Працэсар") # CPU
    window.lbl_machine.setText("Машына") # Machine
    window.lbl_ram.setText("АЗП у MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Выкарыстанне VHD") # VHD usage
    window.lbl_vhdp.setText("Шлях да VHD") # VHD path
    window.lbl_vhdf.setText("Фармат файла VHD") # VHD file format
    window.lbl_maxsize.setText("Максімальны памер") # Maximum size
    window.btn_vhdp.setText("Агляд") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Стварыць новы віртуальны жорсткі дыск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Дадаць існуючы віртуальны жорсткі дыск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Не дадаваць віртуальны жорсткі дыск") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("CD controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("HDD controller") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Няхай QEMU вырашае") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Тып мышы") # Mouse type
    window.lbl_kbdtype.setText("Тып клавіятуры") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Размяшчэнне знешняга файла BIOS (Пакіньце пустым, каб выкарыстоўваць BIOS па змаўчанні)")
    window.lbl_biosf.setText("Вонкавы файл BIOS") # External BIOS file
    window.btn_biosf.setText("Агляд") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Ядро Linux") # Linux kernel
    window.lbl_initrd.setText("Выява initrd Linux") # Linux initrd image
    window.lbl_cmd.setText("Аргументы Linux cmd") # Linux cmd arguments
    window.btn_kernel.setText("Агляд") # Browse
    window.btn_initrd.setText("Агляд") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Сетка") # Network adapter
    window.lbl_sound.setText("Гукавая карта") # Sound card
    window.lbl_addargs.setText("Дадатковыя аргументы (пры неабходнасці)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Ядра працэсара") # CPU cores
    window.chb_usb.setText("Дадаць падтрымку USB") # Add USB support
    window.lbl_accel.setText("Acceleration") # Acceleration

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