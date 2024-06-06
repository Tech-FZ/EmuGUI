from translations.systemdefaultset import *

def translateMainPL(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Główne") # Main
    window.tabWidget.setTabText(1, "Ustawienia") # Settings

    # Main tab
    window.pushButton_8.setText("Nowa maszyna wirtualna") # New virtual machine
    window.pushButton_9.setText("Włącz maszynę wirtualną") # Start virtual machine
    window.pushButton_10.setText("Edytuj wybraną maszynę wirtualną") # Edit selected virtual machine
    window.pushButton_11.setText("Usuń wybraną maszynę wirtualną") # Delete selected virtual machine
    window.pushButton_22.setText("Exportuj wybraną maszyne wirtualną") # Export selected virtual machine
    window.pushButton_23.setText("Importuj maszynę wirtualną") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Generalne") # General
    window.tabWidget_2.setTabText(3, "O EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Język") # Language
    window.pushButton_15.setText("Zastosuj") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Systemowe domyślne", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Systemowe domyślne", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img Droga") # qemu-img Path
    window.label_2.setText("qemu-system-i386 Droga") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64 Droga") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc Droga") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el Droga") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64 Droga") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm Droga") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64 Droga") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel Droga") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips Droga") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64 Droga") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc Droga") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64 Droga") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("qemu-system-alpha Droga") # qemu-system-alpha Path
    window.lbl_riscv32.setText("qemu-system-riscv32 Droga") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("qemu-system-riscv64 Droga") # qemu-system-riscv64 Path

    window.pushButton.setText("Przeglądaj") # Browse
    window.pushButton_2.setText("Przeglądaj") # Browse
    window.pushButton_3.setText("Przeglądaj") # Browse
    window.pushButton_4.setText("Przeglądaj") # Browse
    window.pushButton_5.setText("Przeglądaj") # Browse
    window.pushButton_7.setText("Przeglądaj") # Browse
    window.pushButton_12.setText("Przeglądaj") # Browse
    window.pushButton_16.setText("Przeglądaj") # Browse
    window.pushButton_17.setText("Przeglądaj") # Browse
    window.pushButton_18.setText("Przeglądaj") # Browse
    window.pushButton_19.setText("Przeglądaj") # Browse
    window.pushButton_13.setText("Przeglądaj") # Browse
    window.pushButton_14.setText("Przeglądaj") # Browse
    window.btn_alpha.setText("Przeglądaj") # Browse
    window.btn_riscv32.setText("Przeglądaj") # Browse
    window.btn_riscv64.setText("Przeglądaj") # Browse
    window.pushButton_6.setText("Zastosuj") # Apply
    window.btn_apply_qemu2.setText("Zastosuj") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Zbudowane na Pythonie i technologii PyQt, licensowane pod GNU Generalna Publiczna Licencja 3.0")

    window.label_10.setText(
        """
        UWAGA: Ten program NIE PRZYCHODZI Z GWARANCJĄ pod obowiązującym prawem. Proszę sprawdzić licęcię GNU GPL dla więcej informacji.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Baner stworzony przez Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI na social media (po angielsku)") # EmuGUI on social media (in English)

def translateNewVmPL(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.lbl_vmname.setText("Nazwa") # Name
    window.lbl_arch.setText("Architektura") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Następne >") # Next >
    window.btn_cancel1.setText("Anuluj") # Cancel

    # Second page
    window.lbl_machine.setText("Maszyna") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM w MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Poprzednie") # < Previous
    window.pb_next2.setText("Następne >") # Next >
    window.pb_cancel2.setText("Anuluj") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Użycie VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Stwórz nowy wirtualny dysk twardy") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Dodaj istniejący wirtualny dysk twardy") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Nie dodawaj wirtualnego dysku twardego") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Ścieżka VHD") # VHD path
    window.lbl_vhdF.setText("Format pliku VHD") # VHD file format
    window.lbl_maxsize.setText("Maksymalny rozmiar") # Maximum size
    window.lbl_hddC.setText("Kontroler HDD") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Przeglądaj") # Browse
    window.btn_prev3.setText("< Poprzednie") # < Previous
    window.btn_next3.setText("Następne >") # Next >
    window.btn_cancel3.setText("Anuluj") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Sieć") # Network
    window.lbl_mouse.setText("Myszka") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Poprzednie") # < Previous
    window.btn_next4.setText("Następne >") # Next >
    window.btn_cancel4.setText("Anuluj") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Lokacja zewnętrznego pliku BIOS (Zostaw puste aby użyć domyślny BIOS)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Zewnętrzny plik BIOS") # External BIOS file

    window.btn_biosF.setText("Przeglądaj") # Browse
    window.btn_prev5.setText("< Poprzednie") # < Previous
    window.btn_next5.setText("Następne >") # Next >
    window.btn_cancel5.setText("Anuluj") # Cancel

    # Sixth page
    window.lbl_sound.setText("Karta dźwiękowa") # Sound card
    window.lbl_cores.setText("Rdzenie procesora")# CPU cores
    window.lbl_kbd.setText("Klawiatura") # Keyboard
    window.lbl_kbdlayout.setText("Układ klawiatury") # Keyboard layout

    window.btn_prev6.setText("< Poprzednie") # < Previous
    window.btn_next6.setText("Następne >") # Next >
    window.btn_cancel6.setText("Anuluj") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Jądro linux") # Linux kernel
    window.lbl_initrd.setText("Zdjęcie initrd linux") # Linux initrd image
    window.lbl_cmd.setText("Argumenty komend linux") # Linux cmd args

    window.btn_kernel.setText("Przeglądaj") # Browse
    window.btn_initrd.setText("Przeglądaj") # Browse
    window.btn_prev7.setText("< Poprzednie") # < Previous
    window.btn_next7.setText("Następne >") # Next >
    window.btn_cancel7.setText("Anuluj") # Cancel

    # Eighth page
    window.lbl_accel.setText("Akceleracja") # Acceleration
    window.lbl_cdc1.setText("Kontroler CD 1") # CD controller 1
    window.lbl_cdc2.setText("Kontroler CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Poprzednie") # < Previous
    window.btn_next8.setText("Następne >") # Next >
    window.btn_cancel8.setText("Anuluj") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Dodatkowe argumenty (jeżeli potrzebne)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Dodaj wsparcie USB") # Add USB support

    window.btn_prev9.setText("< Poprzednie") # < Previous
    window.btn_finish.setText("Zakończ") # Finish
    window.btn_cancel9.setText("Anuluj") # Cancel

def translateStartVmPL(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Data i Czas") # Date & Time
    window.label_3.setText("Uruchom z") # Boot from
    window.label_6.setText("Droga TPM (Tylko Linux)") # TPM path (Linux only)
    window.label_7.setText("Stwórz TPM z terminału!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Notatka: Jeżeli maszyna wirtualna nie włącza się w ciągu pięciu minut, powinno się sprawdzić ustawienia maszyny wirtualnej i QEMU
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Przeglądaj") # Browse
    window.pushButton_2.setText("Przeglądaj") # Browse
    window.pushButton_6.setText("Przeglądaj") # Browse
    window.pushButton_5.setText("Ustaw na system") # Set to system
    window.pushButton_3.setText("Włącz maszyne wirtualną") # Start VM
    window.pushButton_4.setText("Anuluj") # Cancel
    window.checkBox.setText("Użyj funkcji RTC") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

def translateVmExistsPL(window):
    window.label.setText(
        "Przepraszamy, ale maszyna wirtualna z tą nazwą już istnieje."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Prosimy rozważać usuwanie tej maszyny wirtualnej lub wymyślanie nowej nazwy."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("Okej") # OK

def translateVhdExistsPL(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Przepraszamy, ale dysk który chcesz stworzyć już istnieje."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Czy chcesz to zostawić czy nadpisać?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Nadpisz") # Overwrite
    window.pushButton_2.setText("Zostaw") # Keep

def translateSettingsPendingPL(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Ścieżki QEMU nie zostały ustawione.")
    window.label_2.setText("Prosimy iść do ustawień i następnie spróbować ponownie.")

    window.pushButton.setText("Okej") # OK

def translateVmTooNewPL(window):
    window.label.setText(
        "Ta maszyna wirtualna została stworzona z wersją EmuGUI która jest za nowa. Prosimy korzystać z innej wersji!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("Okej") # OK

def translateQemuSysMissingPL(window, arch):
    window.label.setText(
        f"Przepraszamy, ale EmuGUI nie jest skonfigurowane na użycie “qemu-system-{arch}”\nw tym momencie. Ten komponent jednak jest potrzebny na włączenie\ntej maszyny wirtualnej. Prosze iść do Ustawień/QEMU\naby rozwiązać ten problem."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("Okej") # OK

def translateQemuImgMissingPL(window):
    window.label.setText(
        "Przepraszamy, ale EmuGUI nie jest skonfigurowane na użycie “qemu-img”\nw tym momencie. Ten komponent jednak jest potrzebny aby tworzyć lub\nedytować maszyny wirtualne. Prosze iść do Ustawień/QEMU\naby rozwiązać ten problem."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("Okej") # OK

def translateEditVMPL(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("Anuluj") # Cancel
    window.btn_ok.setText("Okej") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Generalne") # General
    window.tabWidget.setTabText(1, "Maszyna") # Machine
    window.tabWidget.setTabText(2, "Wirtualne dyski twarde") # Virtual hard disks
    window.tabWidget.setTabText(3, "Peryferja") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Adycjonalne komponenty") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Nazwa") # Name
    window.lbl_arch.setText("Architektura") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("Maszyna") # Machine
    window.lbl_ram.setText("RAM w MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Użycie VHD") # VHD usage
    window.lbl_vhdp.setText("Ścieżka VHD") # VHD path
    window.lbl_vhdf.setText("Format pliku VHD") # VHD file format
    window.lbl_maxsize.setText("Maksymalny rozmiar") # Maximum size
    window.btn_vhdp.setText("Przeglądaj") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Stwórz nowy wirtualny dysk twardy") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Dodaj istniejący wirtualny dysk twardy") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Nie dodawaj wirtualnego dysku twardego") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("Kontroler CD 1") # CD controller 1
    window.lbl_cdc2.setText("Kontroler CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("Kontroler HDD") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Daj QEMU zdecydować") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Typ myszki") # Mouse type
    window.lbl_kbdtype.setText("Typ klawiatury") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Lokacja zewnętrznego pliku BIOS (Zostaw puste aby użyć domyślny BIOS)")
    window.lbl_biosf.setText("Zewnętrzny plik BIOS") # External BIOS file
    window.btn_biosf.setText("Przeglądaj") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Jądro linux") # Linux kernel
    window.lbl_initrd.setText("Zdjęcie initrd linux") # Linux initrd image
    window.lbl_cmd.setText("Argumenty komend linux") # Linux cmd arguments
    window.btn_kernel.setText("Przeglądaj") # Browse
    window.btn_initrd.setText("Przeglądaj") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Sieć") # Network adapter
    window.lbl_sound.setText("Karta dźwiękowa") # Sound card
    window.lbl_addargs.setText("Dodatkowe argumenty (jeżeli potrzebne)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Rdzenie procesora") # CPU cores
    window.chb_usb.setText("Dodaj wsparcie USB") # Add USB support
    window.lbl_accel.setText("Akceleracja") # Acceleration
    
def translateErrDialogPL(window, errcode):
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
    
    window.pushButton.setText("Okej") # OK