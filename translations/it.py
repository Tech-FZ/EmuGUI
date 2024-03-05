from translations.systemdefaultset import *

def translateMainIT(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Principale") # Main
    window.tabWidget.setTabText(1, "Impostazioni") # Settings

    # Main tab
    window.pushButton_8.setText("Nuova macchina virtuale") # New virtual machine
    window.pushButton_9.setText("Avvia macchina virtuale") # Start virtual machine
    window.pushButton_10.setText("Modifica la macchina virtuale selezionata") # Edit selected virtual machine
    window.pushButton_11.setText("Elimina la macchina virtuale selezionata") # Delete selected virtual machine
    window.pushButton_22.setText("Esporta la macchina virtuale selezionata") # Export selected virtual machine
    window.pushButton_23.setText("Importa macchina virtuale") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Generale") # General
    window.tabWidget_2.setTabText(3, "Informazioni su EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Lingua") # Language
    window.pushButton_15.setText("Applica") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Predefinito di sistema", window.comboBox_4, i) # System default
        #if window.comboBox_4.itemText(i) == "System default" or window.comboBox_4.itemText(i) == "Systemstandard":
        #    window.comboBox_4.setItemText(i, "System default") # System default
        #    break

        i += 1

        #if window.comboBox_4.itemText(i) == "По умолчанию системы" or window.comboBox_4.itemText(i) == "Па змаўчанні сістэмы":
        #    window.comboBox_4.setItemText(i, "System default") # System default
        #    break

        #i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Predefinito di sistema", window.comboBox_5, i) # System default
        #if window.comboBox_5.itemText(i) == "System default" or window.comboBox_5.itemText(i) == "Systemstandard":
        #    window.comboBox_5.setItemText(i, "System default") # System default
        #    break

        i += 1

        #if window.comboBox_5.itemText(i) == "По умолчанию системы" or window.comboBox_5.itemText(i) == "Па змаўчанні сістэмы":
        #    window.comboBox_5.setItemText(i, "System default") # System default
        #    break

        #i += 1

    # QEMU tab
    window.label.setText("Percorso di qemu-img") # qemu-img Path
    window.label_2.setText("Percorso di qemu-system-i386") # qemu-system-i386 Path
    window.label_3.setText("Percorso di qemu-system-x86_64") # qemu-system-x86_64 Path
    window.label_4.setText("Percorso di qemu-system-ppc") # qemu-system-ppc Path
    window.label_5.setText("Percorso di qemu-system-mips64el") # qemu-system-mips64el Path
    window.label_9.setText("Percorso di qemu-system-aarch64") # qemu-system-aarch64 Path
    window.label_11.setText("Percorso di qemu-system-arm") # qemu-system-arm Path
    window.label_16.setText("Percorso di qemu-system-ppc64") # qemu-system-ppc64 Path
    window.label_17.setText("Percorso di qemu-system-mipsel") # qemu-system-mipsel Path
    window.label_18.setText("Percorso di qemu-system-mips") # qemu-system-mips Path
    window.label_19.setText("Percorso di qemu-system-mips64") # qemu-system-mips64 Path
    window.label_12.setText("Percorso di qemu-system-sparc") # qemu-system-sparc Path
    window.label_13.setText("Percorso di qemu-system-sparc64") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("Percorso di qemu-system-alpha") # qemu-system-alpha Path
    window.lbl_riscv32.setText("Percorso di qemu-system-riscv32") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("Percorso di qemu-system-riscv64") # qemu-system-riscv64 Path

    window.pushButton.setText("Sfoglia") # Browse
    window.pushButton_2.setText("Sfoglia") # Browse
    window.pushButton_3.setText("Sfoglia") # Browse
    window.pushButton_4.setText("Sfoglia") # Browse
    window.pushButton_5.setText("Sfoglia") # Browse
    window.pushButton_7.setText("Sfoglia") # Browse
    window.pushButton_12.setText("Sfoglia") # Browse
    window.pushButton_16.setText("Sfoglia") # Browse
    window.pushButton_17.setText("Sfoglia") # Browse
    window.pushButton_18.setText("Sfoglia") # Browse
    window.pushButton_19.setText("Sfoglia") # Browse
    window.pushButton_13.setText("Sfoglia") # Browse
    window.pushButton_14.setText("Sfoglia") # Browse
    window.btn_alpha.setText("Sfoglia") # Browse
    window.btn_riscv32.setText("Sfoglia") # Browse
    window.btn_riscv64.setText("Sfoglia") # Browse
    window.pushButton_6.setText("Applica") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Creato con Python e tecnologia PyQt. Rilasciato sotto la licenza GNU General Public License 3.0")

    window.label_10.setText(
        """
        AVVISO: Questo programma è rilasciato SENZA ALCUNA GARANZIA sotto la legge applicabile. Vedi i dettagli nella licenza GNU GPL.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner creato da Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI nei social media (in Inglese)") # EmuGUI on social media (in English)

def translateNewVmIT(window):
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

def translateNewVmITOld(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.label.setText("Nome") # Name
    window.label_3.setText("Architettura") # Architecture
    window.comboBox.setPlaceholderText("Scegli un’architettura") # Please choose an architecture

    window.pushButton_3.setText("Avanti >") # Next >
    window.pushButton_2.setText("Annulla") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Macchina") # Machine
    window.label_5.setText("CPU") # CPU
    window.label_6.setText("RAM in MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Scegli una macchina") # Please select a machine
    window.comboBox_3.setPlaceholderText("Scegli un processore") # Please select a processor

    window.pushButton_5.setText("< Indietro") # < Previous
    window.pushButton_4.setText("Avanti >") # Next >
    window.pushButton_6.setText("Annulla") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Macchina") # Machine
    window.label_8.setText("CPU") # CPU
    window.label_7.setText("RAM in MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Scegli una macchina") # Please select a machine
    window.comboBox_5.setPlaceholderText("Scegli un processore") # Please select a processor

    window.pushButton_7.setText("< Indietro") # < Previous
    window.pushButton_8.setText("Avanti >") # Next >
    window.pushButton_9.setText("Annulla") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Macchina") # Machine
    window.label_11.setText("CPU") # CPU
    window.label_10.setText("RAM in MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Scegli una macchina") # Please select a machine
    window.comboBox_7.setPlaceholderText("Scegli un processore") # Please select a processor

    window.pushButton_10.setText("< Indietro") # < Previous
    window.pushButton_11.setText("Avanti >") # Next >
    window.pushButton_12.setText("Annulla") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Macchina") # Machine
    window.label_30.setText("CPU") # CPU
    window.label_29.setText("RAM in MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Scegli una macchina") # Please select a machine
    window.comboBox_15.setPlaceholderText("Scegli un processore") # Please select a processor

    window.pushButton_33.setText("< Indietro") # < Previous
    window.pushButton_34.setText("Avanti >") # Next >
    window.pushButton_35.setText("Annulla") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Macchina") # Machine
    window.label_35.setText("RAM in MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Scegli una macchina") # Please select a machine

    window.pushButton_37.setText("< Indietro") # < Previous
    window.pushButton_38.setText("Avanti >") # Next >
    window.pushButton_39.setText("Annulla") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Macchina") # Machine
    window.label_36.setText("RAM in MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Scegli una macchina") # Please select a machine

    window.pushButton_41.setText("< Indietro") # < Previous
    window.pushButton_40.setText("Avanti >") # Next >
    window.pushButton_42.setText("Annulla") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("Utilizzo Hard Disk Virtuale") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Crea un nuovo hard disk virtuale") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Aggiungi un hard disk virtuale esistente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Non aggiungere un hard disk virtuale") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("Percorso Hard Disk Virtuale") # VHD path
    window.label_14.setText("Formato Hard Disk Virtuale") # VHD file format
    window.label_15.setText("Dimensione massima") # Maximum size
    window.label_73.setText("Controller disco rigido") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Seleziona un formato del file)") # (Please select a file format)

    window.pushButton_13.setText("Sfoglia") # Browse
    window.pushButton_16.setText("< Indietro") # < Previous
    window.pushButton_14.setText("Avanti >") # Next >
    window.pushButton_15.setText("Annulla") # Cancel

    # Fourth page
    window.label_16.setText("Scheda grafica") # VGA
    window.label_17.setText("Rete") # Network
    window.label_28.setText("Mouse") # Mouse

    window.comboBox_10.setPlaceholderText("(Seleziona una scheda grafica)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Seleziona un adattatore di rete)") # (Please select a network adapter)

    window.pushButton_18.setText("< Indietro") # < Previous
    window.pushButton_17.setText("Avanti >") # Next >
    window.pushButton_19.setText("Annulla") # Cancel

    # Fifth page
    window.label_19.setText(
        "Posizione del file del\nBIOS esterno (Lascia\nvuoto per usare il\nBIOS predefinito)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("File del BIOS esterno") # External BIOS file

    window.pushButton_36.setText("Sfoglia") # Browse
    window.pushButton_25.setText("< Indietro") # < Previous
    window.pushButton_24.setText("Avanti >") # Next >
    window.pushButton_23.setText("Annulla") # Cancel

    # Sixth page
    window.label_23.setText("Scheda audio") # Sound card
    window.label_33.setText("Core della CPU")# CPU cores
    window.label_34.setText("Tastiera") # Keyboard
    window.label_21.setText("Layout Tastiera") # Keyboard layout

    window.pushButton_28.setText("< Indietro") # < Previous
    window.pushButton_27.setText("Avanti >") # Next >
    window.pushButton_26.setText("Annulla") # Cancel

    # Seventh page
    window.label_24.setText("Kernel linux") # Linux kernel
    window.label_25.setText("Immagine initrd Linux") # Linux initrd image
    window.label_26.setText("Parametri linea di comando Linux") # Linux cmd args

    window.pushButton.setText("Sfoglia") # Browse
    window.pushButton_32.setText("Sfoglia") # Browse
    window.pushButton_31.setText("< Indietro") # < Previous
    window.pushButton_30.setText("Avanti >") # Next >
    window.pushButton_29.setText("Annulla") # Cancel

    # Eighth page
    window.label_71.setText("Accelerazione") # Acceleration
    window.label_70.setText("Controller CD 1") # CD controller 1
    window.label_72.setText("Controller CD 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    window.pushButton_81.setText("< Indietro") # < Previous
    window.pushButton_77.setText("Avanti >") # Next >
    window.pushButton_80.setText("Annulla") # Cancel

    # Ninth page
    window.label_2.setText("Parametri aggiuntivi (se necessario)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Aggiungi supporto USB") # Add USB support

    window.pushButton_22.setText("< Indietro") # < Previous
    window.pushButton_20.setText("Fine") # Finish
    window.pushButton_21.setText("Annulla") # Cancel

def translateStartVmIT(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Data e Ora") # Date & Time
    window.label_3.setText("Avvia da") # Boot from
    window.label_6.setText("Percorso TPM (solo Linux)") # TPM path (Linux only)
    window.label_7.setText("Crea il TPM dal terminale!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Nota: Se la VM non si avvia in 5 minuti, prova a controllare le impostazioni della VM e di QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Sfoglia") # Browse
    window.pushButton_2.setText("Sfoglia") # Browse
    window.pushButton_6.setText("Sfoglia") # Browse
    window.pushButton_5.setText("Imposta il sistema a") # Set to system
    window.pushButton_3.setText("Avvia VM") # Start VM
    window.pushButton_4.setText("Annulla") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

def translateVmExistsIT(window):
    window.label.setText(
        "Spiacente, una VM con questo nome esiste già."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Considera di eliminare quella VM o di pensare ad un nuovo nome."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsIT(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Sorry, but the disk you want to create is already existant."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Do you want to keep or overwrite it?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Overwrite") # Overwrite
    window.pushButton_2.setText("Keep") # Keep

"""
def translateUpdateAvailableIT(window):
    window.label.setText(
        "An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.\n\nThe \"I want to download a pre-release from GitLab!\" button is only here temporarily as the stable repository hasn't been hosted on there yet at the time this pre-release version has been worked on."
        ) # An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.

    window.pushButton.setText("Yes") # Yes
    window.pushButton_2.setText("No") # No

def translateNoUpdateAvailableIT(window):
    window.label.setText("You are already running the latest version of EmuGUI.") # You are already running the latest version of EmuGUI.
    window.label_2.setText("...or don't have an internet connection.") # ...or don't have an internet connection.

    window.pushButton.setText("OK") # OK
"""

def translateSettingsPendingIT(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("You didn't setup the QEMU paths.")
    window.label_2.setText("Please go to settings to do that and try again afterwards.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewIT(window):
    window.label.setText(
        "Questa macchina virtuale è stat fatta con una versione di EmuGUI più nuova. Per favore usa una versione sucessiva!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingIT(window, arch):
    window.label.setText(
        f"Spiacente, ma EmuGUI non è configurato per usare “qemu-system-{arch}”.\nQuesto componente è tuttavia necessario per avviare la macchina virtuale.\nVai su Impostazioni/QEMU per risolvere questo problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingIT(window):
    window.label.setText(
        "Spiacente, ma EmuGUI non è configurato per usare “qemu-img”.\nQuesto componente è tuttavia necessario per creare o modificare le macchine virtuali.\nVai su Impostazioni/QEMU per risolvere questo problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMIT(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.pushButton.setText("Annulla") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Generale") # General
    window.tabWidget.setTabText(1, "Macchina") # Machine
    window.tabWidget.setTabText(2, "Hard Disk Virtuali") # Virtual hard disks
    window.tabWidget.setTabText(3, "Periferiche") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Componenti aggiuntivi") # Additional components

    # Translations for General tab
    window.label.setText("Nome") # Name
    window.label_2.setText("Architettura") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("CPU") # CPU
    window.label_18.setText("Macchina") # Machine
    window.label_19.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("CPU") # CPU
    window.label_22.setText("Macchina") # Machine
    window.label_21.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("CPU") # CPU
    window.label_25.setText("Macchina") # Machine
    window.label_24.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("CPU") # CPU
    window.label_28.setText("Macchina") # Machine
    window.label_27.setText("RAM in MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("Utilizzo Hard Disk Virtuale") # VHD usage
    window.label_4.setText("Percorso Hard Disk Virtuale") # VHD path
    window.label_5.setText("Formato Hard Disk Virtuale") # VHD file format
    window.label_6.setText("Dimensione massima") # Maximum size
    window.pushButton_3.setText("Sfoglia") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Crea un nuovo hard disk virtuale") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Aggiungi un hard disk virtuale esistente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Non aggiungere un hard disk virtuale") # Don't add a virtual hard drive
            break

        i += 1

    window.label_37.setText("Controller CD 1") # CD controller 1
    window.label_72.setText("Controller CD 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("Controller disco rigido") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Lascia che QEMU decida") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Tipo di mouse") # Mouse type
    window.label_8.setText("Tipo di tastiera") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Posizione del file del BIOS esterno (Lascia vuoto per usare il BIOS predefinito)")
    window.label_12.setText("File del BIOS esterno") # External BIOS file
    window.pushButton_4.setText("Sfoglia") # Browse

    # Translations for Linux tab
    window.label_13.setText("Kernel linux") # Linux kernel
    window.label_14.setText("Immagine initrd Linux") # Linux initrd image
    window.label_15.setText("Parametri linea di comando Linux") # Linux cmd arguments
    window.pushButton_5.setText("Sfoglia") # Browse
    window.pushButton_6.setText("Sfoglia") # Browse

    # Translations for Additional components tab
    window.label_9.setText("Scheda grafica") # VGA
    window.label_10.setText("Rete") # Network adapter
    window.label_16.setText("Scheda audio") # Sound card
    window.label_29.setText("Parametri aggiuntivi (se necessario)") # Additional arguments (if necessary)
    window.label_30.setText("Core della CPU") # CPU cores
    window.checkBox.setText("Aggiungi supporto USB") # Add USB support
    window.label_36.setText("Accelerazione") # Acceleration

def translateErrDialogIT(window, errcode):
    window.setWindowTitle(f"EmuGUI - Errore")

    if errcode.startswith("C"):
        window.label.setText("EmuGUI ha riscontrato un errore critico e necessita di essere chiuso.") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI ha riscontrato un errore.") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI doveva avvisarti.") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI ha qualcosa da dire.") # EmuGUI has something to say.

    window.label_2.setText("Codice errore: " + errcode) # Error Code:

    window.label_3.setText(
        "Se riscontri questo errore più volte, contatta il tuo amministratore e/o chiedi aiuto nel server Discord di EmuGUI o sulla sua repository di GitHub."
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("OK") # OK