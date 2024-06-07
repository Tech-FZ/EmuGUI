from translations.systemdefaultset import *

def translateMainRU(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Главная") # Main
    window.tabWidget.setTabText(1, "Настройки") # Settings

    # Main tab
    window.pushButton_8.setText("Создать виртуальную машину") # New virtual machine
    window.pushButton_9.setText("Запустить виртуальную машину") # Start virtual machine
    window.pushButton_10.setText("Редактировать выбранную виртуальную машину") # Edit selected virtual machine
    window.pushButton_11.setText("Удалить выбранную виртуальную машину") # Delete selected virtual machine
    window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    window.pushButton_23.setText("Import virtual machine") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Общие") # General
    window.tabWidget_2.setTabText(3, "О EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Язык") # Language
    window.pushButton_15.setText("Применить") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("По умолчанию системы", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("По умолчанию системы", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("Путь к qemu-img") # qemu-img Path
    window.label_2.setText("Путь к qemu-system-i386") # qemu-system-i386 Path
    window.label_3.setText("Путь к qemu-system-x86_64") # qemu-system-x86_64 Path
    window.label_4.setText("Путь к qemu-system-ppc") # qemu-system-ppc Path
    window.label_5.setText("Путь к qemu-system-mips64el") # qemu-system-mips64el Path
    window.label_9.setText("Путь к qemu-system-aarch64") # qemu-system-aarch64 Path
    window.label_11.setText("Путь к qemu-system-arm") # qemu-system-arm Path
    window.label_16.setText("Путь к qemu-system-ppc64") # qemu-system-ppc64 Path
    window.label_17.setText("Путь к qemu-system-mipsel") # qemu-system-mipsel Path
    window.label_18.setText("Путь к qemu-system-mips") # qemu-system-mips Path
    window.label_19.setText("Путь к qemu-system-mips64") # qemu-system-mips64 Path
    window.label_12.setText("Путь к qemu-system-sparc") # qemu-system-sparc Path
    window.label_13.setText("Путь к qemu-system-sparc64") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("Путь к qemu-system-alpha") # qemu-system-alpha Path
    window.lbl_riscv32.setText("Путь к qemu-system-riscv32") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("Путь к qemu-system-riscv64") # qemu-system-riscv64 Path

    window.pushButton.setText("Обзор") # Browse
    window.pushButton_2.setText("Обзор") # Browse
    window.pushButton_3.setText("Обзор") # Browse
    window.pushButton_4.setText("Обзор") # Browse
    window.pushButton_5.setText("Обзор") # Browse
    window.pushButton_7.setText("Обзор") # Browse
    window.pushButton_12.setText("Обзор") # Browse
    window.pushButton_16.setText("Обзор") # Browse
    window.pushButton_17.setText("Обзор") # Browse
    window.pushButton_18.setText("Обзор") # Browse
    window.pushButton_19.setText("Обзор") # Browse
    window.pushButton_13.setText("Обзор") # Browse
    window.pushButton_14.setText("Обзор") # Browse
    window.btn_alpha.setText("Обзор") # Browse
    window.btn_riscv32.setText("Обзор") # Browse
    window.btn_riscv64.setText("Обзор") # Browse
    window.pushButton_6.setText("Применить") # Apply
    window.btn_apply_qemu2.setText("Применить") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Собрано на Python и технологии PyQt, лицензировано под GNU General Public License 3.0")

    window.label_10.setText(
        """
        ПРЕДУПРЕЖДЕНИЕ: Эта программа поставляется с АБСОЛЮТНО НИКАКИМИ ГАРАНТИЯМИ в соответствии с действующим законодательством.
        Подробности см. в лицензии GNU GPL.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Баннер сделан Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI в социальных сетях (на английском языке)") # EmuGUI on social media (in English)

def translateNewVmRU(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.lbl_vmname.setText("Название") # Name
    window.lbl_arch.setText("Архитектура") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Дальше >") # Next >
    window.btn_cancel1.setText("Отмена") # Cancel

    # Second page
    window.lbl_machine.setText("Машина") # Machine
    window.lbl_cpu.setText("Процессор") # CPU
    window.lbl_ram.setText("ОЗУ в MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Назад") # < Previous
    window.pb_next2.setText("Дальше >") # Next >
    window.pb_cancel2.setText("Отмена") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Использование VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Создать новый виртуальный жесткий диск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Добавить существующий виртуальный жесткий диск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Не добавлять виртуальный жесткий диск") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Путь к VHD") # VHD path
    window.lbl_vhdF.setText("Формат файла VHD") # VHD file format
    window.lbl_maxsize.setText("Максимальный размер") # Maximum size
    window.lbl_hddC.setText("HDD controller") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Обзор") # Browse
    window.btn_prev3.setText("< Назад") # < Previous
    window.btn_next3.setText("Дальше >") # Next >
    window.btn_cancel3.setText("Отмена") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Сеть") # Network
    window.lbl_mouse.setText("Мышь") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Назад") # < Previous
    window.btn_next4.setText("Дальше >") # Next >
    window.btn_cancel4.setText("Отмена") # Cancel

    # Fifth page
    window.lbl_biosLoc.setWordWrap(True)
    window.lbl_biosLoc.setText(
        "Расположение внешнего файла BIOS (Оставьте пустым, чтобы использовать BIOS по умолчанию)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Внешний файл BIOS") # External BIOS file

    window.btn_biosF.setText("Обзор") # Browse
    window.btn_prev5.setText("< Назад") # < Previous
    window.btn_next5.setText("Дальше >") # Next >
    window.btn_cancel5.setText("Отмена") # Cancel

    # Sixth page
    window.lbl_sound.setText("Звуковая карта") # Sound card
    window.lbl_cores.setText("Ядра процессора")# CPU cores
    window.lbl_kbd.setText("Клавиатура") # Keyboard
    window.lbl_kbdlayout.setText("Раскладка клавиатуры") # Keyboard layout

    window.btn_prev6.setText("< Назад") # < Previous
    window.btn_next6.setText("Дальше >") # Next >
    window.btn_cancel6.setText("Отмена") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Ядро Linux") # Linux kernel
    window.lbl_initrd.setText("Образ initrd Linux") # Linux initrd image
    window.lbl_cmd.setText("Аргументы Linux cmd") # Linux cmd args

    window.btn_kernel.setText("Обзор") # Browse
    window.btn_initrd.setText("Обзор") # Browse
    window.btn_prev7.setText("< Назад") # < Previous
    window.btn_next7.setText("Дальше >") # Next >
    window.btn_cancel7.setText("Отмена") # Cancel

    # Eighth page
    window.lbl_accel.setText("Acceleration") # Acceleration
    window.lbl_cdc1.setText("CD controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Назад") # < Previous
    window.btn_next8.setText("Дальше >") # Next >
    window.btn_cancel8.setText("Отмена") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Дополнительные аргументы (при необходимости)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Добавить поддержку USB") # Add USB support

    window.btn_prev9.setText("< Назад") # < Previous
    window.btn_finish.setText("Finish") # Finish
    window.btn_cancel9.setText("Отмена") # Cancel

def translateStartVmRU(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Дата и Время") # Date & Time
    window.label_3.setText("Загрузка из") # Boot from
    window.label_6.setText("TPM path (Linux only)") # TPM path (Linux only)
    window.label_7.setText("Create the TPM from the terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Примечание: Если ВМ не запускается в течение пяти минут, то необходимо проверить настройки ВМ и QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Обзор") # Browse
    window.pushButton_2.setText("Обзор") # Browse
    window.pushButton_6.setText("Обзор") # Browse
    window.pushButton_5.setText("Установить в систему") # Set to system
    window.pushButton_3.setText("Запустить ВМ") # Start VM
    window.pushButton_4.setText("Отмена") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

def translateVmExistsRU(window):
    window.label.setText(
        "Извините, но виртуальная машина с таким именем уже существует."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Пожалуйста, подумайте о том, чтобы либо удалить этот VM, либо придумать новое название."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsRU(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Извините, но диск, который вы хотите создать, уже существует."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Вы хотите сохранить или перезаписать его?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Перезаписать") # Overwrite
    window.pushButton_2.setText("Сохранить") # Keep

def translateSettingsPendingRU(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Вы не настроили пути QEMU.")
    window.label_2.setText("Пожалуйста, перейдите в настройки, чтобы сделать это, и повторите попытку после этого.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewRU(window):
    window.label.setText(
        "Этот виртуальная машина сделана с версией EmuGUI, которая является слишком новой. Пожалуйста, используйте более позднюю версию!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingRU(window, arch):
    window.label.setText(
        f"Извините, но EmuGUI пока не настроен на использование \"qemu-system-{arch}\".\nОднако этот компонент необходим для запуска данной виртуальной\nмашины. Пожалуйста, перейдите в Настройки/QEMU, чтобы решить эту проблему."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingRU(window):
    window.label.setText(
        "Извините, но EmuGUI пока не настроен на использование \"qemu-img\".\nОднако этот компонент необходим для создания или редактирования виртуальных\nмашин. Пожалуйста, перейдите в Настройки/QEMU, чтобы решить эту проблему."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMRU(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("Отмена") # Cancel
    window.btn_ok.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Общие") # General
    window.tabWidget.setTabText(1, "Машина") # Machine
    window.tabWidget.setTabText(2, "Virtual hard disks") # Virtual hard disks
    window.tabWidget.setTabText(3, "Peripherals") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Additional components") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Название") # Name
    window.lbl_arch.setText("Архитектура") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("Процессор") # CPU
    window.lbl_machine.setText("Машина") # Machine
    window.lbl_ram.setText("ОЗУ в MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Использование VHD") # VHD usage
    window.lbl_vhdp.setText("Путь к VHD") # VHD path
    window.lbl_vhdf.setText("Формат файла VHD") # VHD file format
    window.lbl_maxsize.setText("Максимальный размер") # Maximum size
    window.btn_vhdp.setText("Обзор") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Создать новый виртуальный жесткий диск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Добавить существующий виртуальный жесткий диск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Не добавлять виртуальный жесткий диск") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("CD controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("HDD controller") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Мышь") # Mouse type
    window.lbl_kbdtype.setText("Клавиатура") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Расположение внешнего файла BIOS (Оставьте пустым, чтобы использовать BIOS по умолчанию)")
    window.lbl_biosf.setText("Внешний файл BIOS") # External BIOS file
    window.btn_biosf.setText("Обзор") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Ядро Linux") # Linux kernel
    window.lbl_initrd.setText("Образ initrd Linux") # Linux initrd image
    window.lbl_cmd.setText("Аргументы Linux cmd") # Linux cmd arguments
    window.btn_kernel.setText("Обзор") # Browse
    window.btn_initrd.setText("Обзор") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Сеть") # Network adapter
    window.lbl_sound.setText("Звуковая карта") # Sound card
    window.lbl_addargs.setText("Дополнительные аргументы (при необходимости)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Ядра процессора") # CPU cores
    window.chb_usb.setText("Добавить поддержку USB") # Add USB support
    window.lbl_accel.setText("Acceleration") # Acceleration

def translateErrDialogRU(window, errcode):
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