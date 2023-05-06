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

    # Settings tabs
    window.tabWidget_2.setTabText(0, "General") # General
    window.tabWidget_2.setTabText(2, "Sobre EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Idioma") # Language
    window.pushButton_15.setText("Aplicar") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Predeterminado del sistema", window.comboBox_4, i) # System default
        #if window.comboBox_4.itemText(i) == "System default" or window.comboBox_4.itemText(i) == "Systemstandard":
        #    window.comboBox_4.setItemText(i, "System default") # System default
        #    break

        #i += 1

        #if window.comboBox_4.itemText(i) == "По умолчанию системы" or window.comboBox_4.itemText(i) == "Па змаўчанні сістэмы":
        #    window.comboBox_4.setItemText(i, "System default") # System default
        #    break

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Predeterminado del sistema", window.comboBox_5, i) # System default
        #if window.comboBox_5.itemText(i) == "System default" or window.comboBox_5.itemText(i) == "Systemstandard":
        #    window.comboBox_5.setItemText(i, "System default") # System default
        #    break

        #i += 1

        #if window.comboBox_5.itemText(i) == "По умолчанию системы" or window.comboBox_5.itemText(i) == "Па змаўчанні сістэмы":
        #    window.comboBox_5.setItemText(i, "System default") # System default
        #    break

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
    window.pushButton_6.setText("Aplicar") # Apply

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
    # First page
    window.label.setText("Nombre") # Name
    window.label_3.setText("Arquitectura") # Architecture
    window.comboBox.setPlaceholderText("Por favor elija una arquitectura") # Please choose an architecture

    window.pushButton_3.setText("Siguiente >") # Next >
    window.pushButton_2.setText("Cancelar") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Máquina") # Machine
    window.label_5.setText("CPU") # CPU
    window.label_6.setText("RAM en MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Por favor elija una máquina") # Please select a machine
    window.comboBox_3.setPlaceholderText("Por favor elija un procesador") # Please select a processor

    window.pushButton_5.setText("< Atrás") # < Previous
    window.pushButton_4.setText("Siguiente >") # Next >
    window.pushButton_6.setText("Cancelar") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_2.itemText(i) == "Пусть QEMU решает":
            window.comboBox_2.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_3.itemText(i) == "Пусть QEMU решает":
            window.comboBox_3.setItemText(i, "Let QEMU decide") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Máquina") # Machine
    window.label_8.setText("CPU") # CPU
    window.label_7.setText("RAM en MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Por favor elija una máquina") # Please select a machine
    window.comboBox_5.setPlaceholderText("Por favor elija un procesador") # Please select a processor

    window.pushButton_7.setText("< Atrás") # < Previous
    window.pushButton_8.setText("Siguiente >") # Next >
    window.pushButton_9.setText("Cancelar") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_4.itemText(i) == "Пусть QEMU решает":
            window.comboBox_4.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_5.itemText(i) == "Пусть QEMU решает":
            window.comboBox_5.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Máquina") # Machine
    window.label_11.setText("CPU") # CPU
    window.label_10.setText("RAM en MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Por favor elija una máquina") # Please select a machine
    window.comboBox_7.setPlaceholderText("Por favor elija un procesador") # Please select a processor

    window.pushButton_10.setText("< Atrás") # < Previous
    window.pushButton_11.setText("Siguiente >") # Next >
    window.pushButton_12.setText("Cancelar") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_6.itemText(i) == "Пусть QEMU решает":
            window.comboBox_6.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_7.itemText(i) == "Пусть QEMU решает":
            window.comboBox_7.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Máquina") # Machine
    window.label_30.setText("CPU") # CPU
    window.label_29.setText("RAM en MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Por favor elija una máquina") # Please select a machine
    window.comboBox_15.setPlaceholderText("Por favor elija un procesador") # Please select a processor

    window.pushButton_33.setText("< Atrás") # < Previous
    window.pushButton_34.setText("Siguiente >") # Next >
    window.pushButton_35.setText("Cancelar") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_14.itemText(i) == "Пусть QEMU решает":
            window.comboBox_14.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_15.itemText(i) == "Пусть QEMU решает":
            window.comboBox_15.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Máquina") # Machine
    window.label_35.setText("RAM en MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Por favor elija una máquina") # Please select a machine

    window.pushButton_37.setText("< Atrás") # < Previous
    window.pushButton_38.setText("Siguiente >") # Next >
    window.pushButton_39.setText("Cancelar") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_20.itemText(i) == "Пусть QEMU решает":
            window.comboBox_20.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Máquina") # Machine
    window.label_36.setText("RAM en MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Por favor elija una máquina") # Please select a machine

    window.pushButton_41.setText("< Atrás") # < Previous
    window.pushButton_40.setText("Siguiente >") # Next >
    window.pushButton_42.setText("Cancelar") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_21.itemText(i) == "Пусть QEMU решает":
            window.comboBox_21.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("Uso del VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Neue virtuelle Festplatte erstellen":
            window.comboBox_18.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Создать новый виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Existierende virtuelle Festplatte anfügen":
            window.comboBox_18.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Добавить существующий виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Keine virtuelle Festplatte anfügen":
            window.comboBox_18.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        elif window.comboBox_18.itemText(i) == "Не добавлять виртуальный жесткий диск":
            window.comboBox_18.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("Ruta del VHD") # VHD path
    window.label_14.setText("Formato de archivo del VHD") # VHD file format
    window.label_15.setText("Tamaño máximo") # Maximum size

    window.comboBox_8.setPlaceholderText("(Por favor elija un formato)") # (Please select a file format)

    window.pushButton_13.setText("Buscar") # Browse
    window.pushButton_16.setText("< Atrás") # < Previous
    window.pushButton_14.setText("Siguiente >") # Next >
    window.pushButton_15.setText("Cancelar") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Red") # Network
    window.label_28.setText("Ratón") # Mouse

    window.comboBox_10.setPlaceholderText("(Por favor elija un adaptador de gráficos)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Por favor elija un adaptador de red)") # (Please select a network adapter)

    window.pushButton_18.setText("< Atrás") # < Previous
    window.pushButton_17.setText("Siguiente >") # Next >
    window.pushButton_19.setText("Cancelar") # Cancel

    # Fifth page
    window.label_19.setText(
        "Ubicación de archivo\nBIOS externo (dejar\nvacío para usar\nel BIOS por defecto)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("Archivo BIOS externo") # External BIOS file

    window.pushButton_36.setText("Buscar") # Browse
    window.pushButton_25.setText("< Atrás") # < Previous
    window.pushButton_24.setText("Siguiente >") # Next >
    window.pushButton_23.setText("Cancelar") # Cancel

    # Sixth page
    window.label_23.setText("Tarjeta de sonido") # Sound card
    window.label_33.setText("Núcleos del CPU") # CPU cores
    window.label_34.setText("Teclado") # Keyboard
    window.label_21.setText("Disposición del teclado") # Keyboard layout

    window.pushButton_28.setText("< Atrás") # < Previous
    window.pushButton_27.setText("Siguiente >") # Next >
    window.pushButton_26.setText("Cancelar") # Cancel

    # Seventh page
    window.label_24.setText("Kernel de Linux") # Linux kernel
    window.label_25.setText("Imagen de initrd de Linux") # Linux initrd image
    window.label_26.setText("Argumentos de cmd de Linux") # Linux cmd args

    window.pushButton.setText("Buscar") # Browse
    window.pushButton_32.setText("Buscar") # Browse
    window.pushButton_31.setText("< Atrás") # < Previous
    window.pushButton_30.setText("Siguiente >") # Next >
    window.pushButton_29.setText("Cancelar") # Cancel

    # Eighth page
    window.label_2.setText("Argumentos adicionales (si son necesarios)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Añadir soporte USB") # Add USB support

    window.pushButton_22.setText("< Atrás") # < Previous
    window.pushButton_20.setText("Finish") # Finish
    window.pushButton_21.setText("Cancelar") # Cancel

def translateStartVmES(window):
    window.label_4.setText("Fecha y hora") # Date & Time
    window.label_3.setText("Bootear de") # Boot from

    window.label_5.setText("""
    Nota: Si la máquina virtual no inicia despues de 5 minutos, deberías chequear la máquina y las configuraciones de QEMU.
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Buscar") # Browse
    window.pushButton_2.setText("Buscar") # Browse
    window.pushButton_5.setText("Establecer en el sistema") # Set to system
    window.pushButton_3.setText("Iniciar máquina virtual") # Start VM
    window.pushButton_4.setText("Cancelar") # Cancel

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox.itemText(i) == "Пусть QEMU решает":
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

"""
def translateUpdateAvailableEN(window):
    window.label.setText(
        "An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.\n\nThe \"I want to download a pre-release from GitLab!\" button is only here temporarily as the stable repository hasn't been hosted on there yet at the time this pre-release version has been worked on."
        ) # An update is available! Do you want to be redirected to download?\nNote: If you check for pre-release updates, you will be redirected to the pre-release repository on Codeberg regardless of your preferred update mirror.

    window.pushButton.setText("Yes") # Yes
    window.pushButton_2.setText("No") # No

def translateNoUpdateAvailableEN(window):
    window.label.setText("You are already running the latest version of EmuGUI.") # You are already running the latest version of EmuGUI.
    window.label_2.setText("...or don't have an internet connection.") # ...or don't have an internet connection.

    window.pushButton.setText("OK") # OK
"""

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

def translateEditVMES(window):
    # Buttons on all tabs
    window.pushButton.setText("Cancelar") # Cancel
    window.pushButton_2.setText("Aceptar") # OK

    # Tab names
    window.tabWidget.setTabText(0, "General") # General
    window.tabWidget.setTabText(1, "Máquina") # Machine
    window.tabWidget.setTabText(2, "Discos duros virtuales") # Virtual hard disks
    window.tabWidget.setTabText(3, "Periféricos") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Componentes adicionales") # Additional components

    # Translations for General tab
    window.label.setText("Nombre") # Name
    window.label_2.setText("Arquitectura") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("CPU") # CPU
    window.label_18.setText("Máquina") # Machine
    window.label_19.setText("RAM en MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_11.itemText(i) == "Пусть QEMU решает":
            window.comboBox_11.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_12.itemText(i) == "Пусть QEMU решает":
            window.comboBox_12.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("CPU") # CPU
    window.label_22.setText("Máquina") # Machine
    window.label_21.setText("RAM en MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_13.itemText(i) == "Пусть QEMU решает":
            window.comboBox_13.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_14.itemText(i) == "Пусть QEMU решает":
            window.comboBox_14.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("CPU") # CPU
    window.label_25.setText("Máquina") # Machine
    window.label_24.setText("RAM en MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_15.itemText(i) == "Пусть QEMU решает":
            window.comboBox_15.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_16.itemText(i) == "Пусть QEMU решает":
            window.comboBox_16.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("CPU") # CPU
    window.label_28.setText("Máquina") # Machine
    window.label_27.setText("RAM en MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_17.itemText(i) == "Пусть QEMU решает":
            window.comboBox_17.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        elif window.comboBox_18.itemText(i) == "Пусть QEMU решает":
            window.comboBox_18.setItemText(i, "Dejar que QEMU decida") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("Uso del VHD") # VHD usage
    window.label_4.setText("Ruta del VHD") # VHD path
    window.label_5.setText("Formato de archivo del VHD") # VHD file format
    window.label_6.setText("Tamaño máximo") # Maximum size
    window.pushButton_3.setText("Buscar") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Neue virtuelle Festplatte erstellen":
            window.comboBox_2.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Создать новый виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "Crear nuevo disco duro virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Existierende virtuelle Festplatte anfügen":
            window.comboBox_2.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Добавить существующий виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "Añadir un disco duro virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Keine virtuelle Festplatte anfügen":
            window.comboBox_2.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        elif window.comboBox_2.itemText(i) == "Не добавлять виртуальный жесткий диск":
            window.comboBox_2.setItemText(i, "No añadir un disco duro virtual") # Don't add a virtual hard drive
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Tipo de ratón") # Mouse type
    window.label_8.setText("Tipo de teclado") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Ubicación de archivo BIOS externo (dejar vacío para usar el BIOS por defecto)")
    window.label_12.setText("Archivo BIOS externo") # External BIOS file
    window.pushButton_4.setText("Buscar") # Browse

    # Translations for Linux tab
    window.label_13.setText("Kernel de Linux") # Linux kernel
    window.label_14.setText("Imagen de initrd de Linux") # Linux initrd image
    window.label_15.setText("Argumentos de cmd de Linux") # Linux cmd arguments
    window.pushButton_5.setText("Buscar") # Browse
    window.pushButton_6.setText("Buscar") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Red") # Network adapter
    window.label_16.setText("Tarjeta de sonido") # Sound card
    window.label_29.setText("Argumentos adicionales (si son necesarios)") # Additional arguments (if necessary)
    window.label_30.setText("Núcleos del CPU") # CPU cores
    window.checkBox.setText("Añadir soporte USB") # Add USB support