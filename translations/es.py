from translations.systemdefaultset import *

def translateMainES(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Principal") # Main
    window.tabWidget.setTabText(1, "Configuración") # Settings

    # Main tab
    window.pushButton_8.setText("Nueva máquina virtual") # New virtual machine
    window.pushButton_9.setText("Iniciar máquina virtual") # Start virtual machine
    window.pushButton_10.setText("Editar la máquina virtual seleccionada") # Edit selected virtual machine
    window.pushButton_11.setText("Eliminar la máquina virtual seleccionada") # Delete selected virtual machine
    window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    window.pushButton_23.setText("Import virtual machine") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "General") # General
    window.tabWidget_2.setTabText(3, "Sobre EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Idioma") # Language
    window.pushButton_15.setText("Aplicar") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Predeterminado del sistema", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Predeterminado del sistema", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("Ruta de qemu-img") # qemu-img Path
    window.label_2.setText("Ruta de qemu-system-i386") # qemu-system-i386 Path
    window.label_3.setText("Ruta de qemu-system-x86_64") # qemu-system-x86_64 Path
    window.label_4.setText("Ruta de qemu-system-ppc") # qemu-system-ppc Path
    window.label_5.setText("Ruta de qemu-system-mips64el") # qemu-system-mips64el Path
    window.label_9.setText("Ruta de qemu-system-aarch64") # qemu-system-aarch64 Path
    window.label_11.setText("Ruta de qemu-system-arm") # qemu-system-arm Path
    window.label_16.setText("Ruta de qemu-system-ppc64") # qemu-system-ppc64 Path
    window.label_17.setText("Ruta de qemu-system-mipsel") # qemu-system-mipsel Path
    window.label_18.setText("Ruta de qemu-system-mips") # qemu-system-mips Path
    window.label_19.setText("Ruta de qemu-system-mips64") # qemu-system-mips64 Path
    window.label_12.setText("Ruta de qemu-system-sparc") # qemu-system-sparc Path
    window.label_13.setText("Ruta de qemu-system-sparc64") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("Ruta de qemu-system-alpha") # qemu-system-alpha Path
    window.lbl_riscv32.setText("Ruta de qemu-system-riscv32") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("Ruta de qemu-system-riscv64") # qemu-system-riscv64 Path

    window.pushButton.setText("Buscar") # Browse
    window.pushButton_2.setText("Buscar") # Browse
    window.pushButton_3.setText("Buscar") # Browse
    window.pushButton_4.setText("Buscar") # Browse
    window.pushButton_5.setText("Buscar") # Browse
    window.pushButton_7.setText("Buscar") # Browse
    window.pushButton_12.setText("Buscar") # Browse
    window.pushButton_16.setText("Buscar") # Browse
    window.pushButton_17.setText("Buscar") # Browse
    window.pushButton_18.setText("Buscar") # Browse
    window.pushButton_19.setText("Buscar") # Browse
    window.pushButton_13.setText("Buscar") # Browse
    window.pushButton_14.setText("Buscar") # Browse
    window.btn_alpha.setText("Buscar") # Browse
    window.btn_riscv32.setText("Buscar") # Browse
    window.btn_riscv64.setText("Buscar") # Browse
    window.pushButton_6.setText("Aplicar") # Apply
    window.btn_apply_qemu2.setText("Aplicar") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Hecho en Python y tecnología PyQt licenciado sobre la licencia del Público General GNU 3.0")

    window.label_10.setText(
        """
        ADVERTENCIA: Este programa viene ABSOLUTAMENTE SIN GARANTÍA sobre la ley aplicable. Por favor vea la licencia de GNU GPL para detalles.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner creado por Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("Redes sociales de EmuGUI (en inglés)") # EmuGUI on social media (in English)

def translateNewVmES(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.lbl_vmname.setText("Nombre") # Name
    window.lbl_arch.setText("Arquitectura") # Architecture
    window.cb_arch.setPlaceholderText("Por favor elige una arquitectura") # Please choose an architecture

    window.btn_next1.setText("Siguiente >") # Next >
    window.btn_cancel1.setText("Cancelar") # Cancel

    # Second page
    window.lbl_machine.setText("Máquina") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM en MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Atrás") # < Previous
    window.pb_next2.setText("Siguiente >") # Next >
    window.pb_cancel2.setText("Cancelar") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Uso del VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Ruta del VHD") # VHD path
    window.lbl_vhdF.setText("Formato de archivo del VHD") # VHD file format
    window.lbl_maxsize.setText("Tamaño máximo") # Maximum size
    window.lbl_hddC.setText("Controlador HDD") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Buscar") # Browse
    window.btn_prev3.setText("< Atrás") # < Previous
    window.btn_next3.setText("Siguiente >") # Next >
    window.btn_cancel3.setText("Cancelar") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Red") # Network
    window.lbl_mouse.setText("Ratón") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Atrás") # < Previous
    window.btn_next4.setText("Siguiente >") # Next >
    window.btn_cancel4.setText("Cancelar") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Ubicación de archivo\nBIOS externo (dejar\nvacío para usar el BIOS por defecto)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Archivo BIOS externo") # External BIOS file

    window.btn_biosF.setText("Buscar") # Browse
    window.btn_prev5.setText("< Atrás") # < Previous
    window.btn_next5.setText("Next >") # Next >
    window.btn_cancel5.setText("Cancelar") # Cancel

    # Sixth page
    window.lbl_sound.setText("Tarjeta de sonido") # Sound card
    window.lbl_cores.setText("Núcleos del CPU")# CPU cores
    window.lbl_kbd.setText("Teclado") # Keyboard
    window.lbl_kbdlayout.setText("Disposición del teclado") # Keyboard layout

    window.btn_prev6.setText("< Atrás") # < Previous
    window.btn_next6.setText("Siguiente >") # Next >
    window.btn_cancel6.setText("Cancelar") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Kernel de Linux") # Linux kernel
    window.lbl_initrd.setText("Imagen de initrd de Linux") # Linux initrd image
    window.lbl_cmd.setText("Argumentos de cmd de Linux") # Linux cmd args

    window.btn_kernel.setText("Buscar") # Browse
    window.btn_initrd.setText("Buscar") # Browse
    window.btn_prev7.setText("< Atrás") # < Previous
    window.btn_next7.setText("Siguiente >") # Next >
    window.btn_cancel7.setText("Cancelar") # Cancel

    # Eighth page
    window.lbl_accel.setText("Aceleración") # Acceleration
    window.lbl_cdc1.setText("Controlador de CD 1") # CD controller 1
    window.lbl_cdc2.setText("Controlador de CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Atrás") # < Previous
    window.btn_next8.setText("Siguiente >") # Next >
    window.btn_cancel8.setText("Cancelar") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Argumentos adicionales (si son necesarios)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Añadir soporte USB") # Add USB support

    window.btn_prev9.setText("< Atrás") # < Previous
    window.btn_finish.setText("Finalizar") # Finish
    window.btn_cancel9.setText("Cancelar") # Cancel

def translateStartVmES(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Fecha y hora") # Date & Time
    window.label_3.setText("Bootear de") # Boot from
    window.label_6.setText("TPM path (Linux only)") # TPM path (Linux only)
    window.label_7.setText("Create the TPM from the terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    Nota: Si la máquina virtual no inicia despues de 5 minutos, deberías chequear la máquina y las configuraciones de QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Buscar") # Browse
    window.pushButton_2.setText("Buscar") # Browse
    window.pushButton_6.setText("Buscar") # Browse
    window.pushButton_5.setText("Establecer en el sistema") # Set to system
    window.pushButton_3.setText("Iniciar máquina virtual") # Start VM
    window.pushButton_4.setText("Cancelar") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

def translateVmExistsES(window):
    window.label.setText(
        "¡Una máquina virtual con este nombre ya existe!"
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Considere eliminar la máquina virtual o ponerle un nuevo nombre."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("Aceptar") # OK

def translateVhdExistsES(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "El disco que quiere crear ya existe."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("¿Quiere sobreescribir o dejarlo?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Sobreescribir") # Overwrite
    window.pushButton_2.setText("Dejar") # Keep

def translateSettingsPendingES(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("No ha configurado las rutas de QEMU.")
    window.label_2.setText("Vaya a configuraciones para establecerlas y probar de nuevo.")

    window.pushButton.setText("Aceptar") # OK

def translateVmTooNewES(window):
    window.label.setText(
        "Esta máquina virtual fue creada con una versión de EmuGUI más nueva de la que usted tiene. Use la versión correcta!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("Aceptar") # OK

def translateQemuSysMissingES(window, arch):
    window.label.setText(
        f"EmuGUI no está configurado aún para usar “qemu-system-{arch}”.\nEste componente se necesita para iniciar la máquina virtual.\nVaya a Configuración/QEMU para resolver este problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("Aceptar") # OK

def translateQemuImgMissingES(window):
    window.label.setText(
        "EmuGUI aún no está configurado para usar “qemu-img”.\nEste componente se necesita para crear o editar máquinas virtuales.\nVaya a Configuración/QEMU para resolver este problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("Aceptar") # OK

def translateEditVMES(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("Cancelar") # Cancel
    window.btn_ok.setText("Aceptar") # OK

    # Tab names
    window.tabWidget.setTabText(0, "General") # General
    window.tabWidget.setTabText(1, "Máquina") # Machine
    window.tabWidget.setTabText(2, "Discos duros virtuales") # Virtual hard disks
    window.tabWidget.setTabText(3, "Periféricos") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Componentes adicionales") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Nombre") # Name
    window.lbl_arch.setText("Arquitectura") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("Máquina") # Machine
    window.lbl_ram.setText("RAM en MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Uso del VHD") # VHD usage
    window.lbl_vhdp.setText("Ruta del VHD") # VHD path
    window.lbl_vhdf.setText("Formato de archivo del VHD") # VHD file format
    window.lbl_maxsize.setText("Tamaño máximo") # Maximum size
    window.btn_vhdp.setText("Buscar") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("Controlador de CD 1") # CD controller 1
    window.lbl_cdc2.setText("Controlador de CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("Controlador HDD") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Tipo de ratón") # Mouse type
    window.lbl_kbdtype.setText("Tipo de teclado") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Ubicación de archivo BIOS externo (dejar vacío para usar el BIOS por defecto)")
    window.lbl_biosf.setText("Archivo BIOS externo") # External BIOS file
    window.btn_biosf.setText("Buscar") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Kernel de Linux") # Linux kernel
    window.lbl_initrd.setText("Imagen de initrd de Linux") # Linux initrd image
    window.lbl_cmd.setText("Argumentos de cmd de Linux") # Linux cmd arguments
    window.btn_kernel.setText("Buscar") # Browse
    window.btn_initrd.setText("Buscar") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Red") # Network adapter
    window.lbl_sound.setText("Tarjeta de sonido") # Sound card
    window.lbl_addargs.setText("Additional arguments (if necessary)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Núcleos del CPU") # CPU cores
    window.chb_usb.setText("Añadir soporte USB") # Add USB support
    window.lbl_accel.setText("Aceleración") # Acceleration

def translateErrDialogES(window, errcode):
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
    
    window.pushButton.setText("Aceptar") # OK