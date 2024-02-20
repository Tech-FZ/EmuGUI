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
    window.tabWidget_2.setTabText(2, "О EmuGUI") # About EmuGUI

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
    window.pushButton_6.setText("Применить") # Apply

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
    window.lbl_vmname.setText("Name") # Name
    window.lbl_arch.setText("Architecture") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Next >") # Next >
    window.btn_cancel1.setText("Cancel") # Cancel

    # Second page
    window.lbl_machine.setText("Machine") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM in MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Previous") # < Previous
    window.pb_next2.setText("Next >") # Next >
    window.pb_cancel2.setText("Cancel") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("VHD usage") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Create a new virtual hard drive") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Add an existing virtual hard drive") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Don't add a virtual hard drive") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("VHD path") # VHD path
    window.lbl_vhdF.setText("VHD file format") # VHD file format
    window.lbl_maxsize.setText("Maximum size") # Maximum size
    window.lbl_hddC.setText("HDD controller") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Browse") # Browse
    window.btn_prev3.setText("< Previous") # < Previous
    window.btn_next3.setText("Next >") # Next >
    window.btn_cancel3.setText("Cancel") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Network") # Network
    window.lbl_mouse.setText("Mouse") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Previous") # < Previous
    window.btn_next4.setText("Next >") # Next >
    window.btn_cancel4.setText("Cancel") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("External BIOS file") # External BIOS file

    window.btn_biosF.setText("Browse") # Browse
    window.btn_prev5.setText("< Previous") # < Previous
    window.btn_next5.setText("Next >") # Next >
    window.btn_cancel5.setText("Cancel") # Cancel

    # Sixth page
    window.lbl_sound.setText("Sound card") # Sound card
    window.lbl_cores.setText("CPU cores")# CPU cores
    window.lbl_kbd.setText("Keyboard") # Keyboard
    window.lbl_kbdlayout.setText("Keyboard layout") # Keyboard layout

    window.btn_prev6.setText("< Previous") # < Previous
    window.btn_next6.setText("Next >") # Next >
    window.btn_cancel6.setText("Cancel") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Linux kernel") # Linux kernel
    window.lbl_initrd.setText("Linux initrd image") # Linux initrd image
    window.lbl_cmd.setText("Linux cmd args") # Linux cmd args

    window.btn_kernel.setText("Browse") # Browse
    window.btn_initrd.setText("Browse") # Browse
    window.btn_prev7.setText("< Previous") # < Previous
    window.btn_next7.setText("Next >") # Next >
    window.btn_cancel7.setText("Cancel") # Cancel

    # Eighth page
    window.lbl_accel.setText("Acceleration") # Acceleration
    window.lbl_cdc1.setText("CD controller 1") # CD controller 1
    window.lbl_cdc2.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Previous") # < Previous
    window.btn_next8.setText("Next >") # Next >
    window.btn_cancel8.setText("Cancel") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Additional arguments (if needed)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Add USB support") # Add USB support

    window.btn_prev9.setText("< Previous") # < Previous
    window.btn_finish.setText("Finish") # Finish
    window.btn_cancel9.setText("Cancel") # Cancel

def translateNewVmRUOld(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.label.setText("Название") # Name
    window.label_3.setText("Архитектура") # Architecture
    window.comboBox.setPlaceholderText("Пожалуйста, выберите архитектуру") # Please choose an architecture

    window.pushButton_3.setText("Дальше >") # Next >
    window.pushButton_2.setText("Отмена") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Машина") # Machine
    window.label_5.setText("Процессор") # CPU
    window.label_6.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine
    window.comboBox_3.setPlaceholderText("Пожалуйста выберите процессор") # Please select a processor

    window.pushButton_5.setText("< Назад") # < Previous
    window.pushButton_4.setText("Дальше >") # Next >
    window.pushButton_6.setText("Отмена") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Машина") # Machine
    window.label_8.setText("Процессор") # CPU
    window.label_7.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine
    window.comboBox_5.setPlaceholderText("Пожалуйста выберите процессор") # Please select a processor

    window.pushButton_7.setText("< Назад") # < Previous
    window.pushButton_8.setText("Дальше >") # Next >
    window.pushButton_9.setText("Отмена") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Машина") # Machine
    window.label_11.setText("Процессор") # CPU
    window.label_10.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine
    window.comboBox_7.setPlaceholderText("Пожалуйста выберите процессор") # Please select a processor

    window.pushButton_10.setText("< Назад") # < Previous
    window.pushButton_11.setText("Дальше >") # Next >
    window.pushButton_12.setText("Отмена") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Машина") # Machine
    window.label_30.setText("Процессор") # CPU
    window.label_29.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine
    window.comboBox_15.setPlaceholderText("Пожалуйста выберите процессор") # Please select a processor

    window.pushButton_33.setText("< Назад") # < Previous
    window.pushButton_34.setText("Дальше >") # Next >
    window.pushButton_35.setText("Отмена") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Машина") # Machine
    window.label_35.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine

    window.pushButton_37.setText("< Назад") # < Previous
    window.pushButton_38.setText("Дальше >") # Next >
    window.pushButton_39.setText("Отмена") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Машина") # Machine
    window.label_36.setText("ОЗУ в MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Пожалуйста выберите машину") # Please select a machine

    window.pushButton_41.setText("< Назад") # < Previous
    window.pushButton_40.setText("Дальше >") # Next >
    window.pushButton_42.setText("Отмена") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("Использование VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Создать новый виртуальный жесткий диск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Добавить существующий виртуальный жесткий диск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Не добавлять виртуальный жесткий диск") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("Путь к VHD") # VHD path
    window.label_14.setText("Формат файла VHD") # VHD file format
    window.label_15.setText("Максимальный размер") # Maximum size
    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Пожалуйста, выберите формат файла)") # (Please select a file format)

    window.pushButton_13.setText("Обзор") # Browse
    window.pushButton_16.setText("< Назад") # < Previous
    window.pushButton_14.setText("Дальше >") # Next >
    window.pushButton_15.setText("Отмена") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Сеть") # Network
    window.label_28.setText("Мышь") # Mouse

    window.comboBox_10.setPlaceholderText("(Пожалуйста выберите графический адаптер)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Пожалуйста выберите сетевой адаптер)") # (Please select a network adapter)

    window.pushButton_18.setText("< Назад") # < Previous
    window.pushButton_17.setText("Дальше >") # Next >
    window.pushButton_19.setText("Отмена") # Cancel

    # Fifth page
    window.label_19.setText(
        "Расположение внешнего\nфайла BIOS\n(Оставьте пустым, чтобы\nиспользовать BIOS по умолчанию)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("Внешний файл BIOS") # External BIOS file

    window.pushButton_36.setText("Обзор") # Browse
    window.pushButton_25.setText("< Назад") # < Previous
    window.pushButton_24.setText("Дальше >") # Next >
    window.pushButton_23.setText("Отмена") # Cancel

    # Sixth page
    window.label_23.setText("Звуковая карта") # Sound card
    window.label_33.setText("Ядра процессора")# CPU cores
    window.label_34.setText("Клавиатура") # Keyboard
    window.label_21.setText("Раскладка клавиатуры") # Keyboard layout

    window.pushButton_28.setText("< Назад") # < Previous
    window.pushButton_27.setText("Дальше >") # Next >
    window.pushButton_26.setText("Отмена") # Cancel

    # Seventh page
    window.label_24.setText("Ядро Linux") # Linux kernel
    window.label_25.setText("Образ initrd Linux") # Linux initrd image
    window.label_26.setText("Аргументы Linux cmd") # Linux cmd args

    window.pushButton.setText("Обзор") # Browse
    window.pushButton_32.setText("Обзор") # Browse
    window.pushButton_31.setText("< Назад") # < Previous
    window.pushButton_30.setText("Дальше >") # Next >
    window.pushButton_29.setText("Отмена") # Cancel

    # Eighth page
    window.label_71.setText("Acceleration") # Acceleration
    window.label_70.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1
    
    window.pushButton_81.setText("< Назад") # < Previous
    window.pushButton_77.setText("Дальше >") # Next >
    window.pushButton_80.setText("Отмена") # Cancel

    # Ninth page
    window.label_2.setText("Дополнительные аргументы (при необходимости)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Добавить поддержку USB") # Add USB support

    window.pushButton_22.setText("< Назад") # < Previous
    window.pushButton_20.setText("Finish") # Finish
    window.pushButton_21.setText("Отмена") # Cancel

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
    window.pushButton.setText("Отмена") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Общие") # General
    window.tabWidget.setTabText(1, "Машина") # Machine
    window.tabWidget.setTabText(2, "Виртуальные жесткие диски") # Virtual hard disks
    window.tabWidget.setTabText(3, "Периферийные устройства") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Дополнительные компоненты") # Additional components

    # Translations for General tab
    window.label.setText("Название") # Name
    window.label_2.setText("Архитектура") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("Процессор") # CPU
    window.label_18.setText("Машина") # Machine
    window.label_19.setText("ОЗУ в MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("Процессор") # CPU
    window.label_22.setText("Машина") # Machine
    window.label_21.setText("ОЗУ в MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("Процессор") # CPU
    window.label_25.setText("Машина") # Machine
    window.label_24.setText("ОЗУ в MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("Процессор") # CPU
    window.label_28.setText("Машина") # Machine
    window.label_27.setText("ОЗУ в MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("Использование VHD") # VHD usage
    window.label_4.setText("Путь к VHD") # VHD path
    window.label_5.setText("Формат файла VHD") # VHD file format
    window.label_6.setText("Максимальный размер") # Maximum size
    window.pushButton_3.setText("Обзор") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Создать новый виртуальный жесткий диск") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Добавить существующий виртуальный жесткий диск") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Не добавлять виртуальный жесткий диск") # Don't add a virtual hard drive
            break

        i += 1

    window.label_37.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Пусть QEMU решает") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Тип мыши") # Mouse type
    window.label_8.setText("Тип клавиатуры") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Расположение внешнего файла BIOS (Оставьте пустым, чтобы использовать BIOS по умолчанию)")
    window.label_12.setText("Внешний файл BIOS") # External BIOS file
    window.pushButton_4.setText("Обзор") # Browse

    # Translations for Linux tab
    window.label_13.setText("Ядро Linux") # Linux kernel
    window.label_14.setText("Образ initrd Linux") # Linux initrd image
    window.label_15.setText("Аргументы Linux cmd") # Linux cmd arguments
    window.pushButton_5.setText("Обзор") # Browse
    window.pushButton_6.setText("Обзор") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Сеть") # Network adapter
    window.label_16.setText("Звуковая карта") # Sound card
    window.label_29.setText("Дополнительные аргументы (при необходимости)") # Additional arguments (if necessary)
    window.label_30.setText("Ядра процессора") # CPU cores
    window.checkBox.setText("Add USB support") # Add USB support
    window.label_36.setText("Acceleration") # Acceleration

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