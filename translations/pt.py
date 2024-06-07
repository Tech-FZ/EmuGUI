from translations.systemdefaultset import *

def translateMainPT(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Principal") # Main
    window.tabWidget.setTabText(1, "Configurações") # Settings

    # Main tab
    window.pushButton_8.setText("Nova Máquina Virtual") # New virtual machine
    window.pushButton_9.setText("Iniciar Máquina Virtual") # Start virtual machine
    window.pushButton_10.setText("Editar Máquina Virtual Selecionada") # Edit selected virtual machine
    window.pushButton_11.setText("Excluir Máquina Virtual Selecionada") # Delete selected virtual machine
    window.pushButton_22.setText("Export selected virtual machine") # Export selected virtual machine
    window.pushButton_23.setText("Import virtual machine") # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Geral") # General
    window.tabWidget_2.setTabText(3, "Sobre o EmuGUI") # About EmuGUI

    # General tab
    window.label_15.setText("Linguagem") # Language
    window.pushButton_15.setText("Aplicar") # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("Padrão do Sistema", window.comboBox_4, i) # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("Padrão do Sistema", window.comboBox_5, i) # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img Caminho") # qemu-img Path
    window.label_2.setText("qemu-system-i386 Caminho") # qemu-system-i386 Path
    window.label_3.setText("qemu-system-x86_64 Caminho") # qemu-system-x86_64 Path
    window.label_4.setText("qemu-system-ppc Caminho") # qemu-system-ppc Path
    window.label_5.setText("qemu-system-mips64el Caminho") # qemu-system-mips64el Path
    window.label_9.setText("qemu-system-aarch64 Caminho") # qemu-system-aarch64 Path
    window.label_11.setText("qemu-system-arm Caminho") # qemu-system-arm Path
    window.label_16.setText("qemu-system-ppc64 Caminho") # qemu-system-ppc64 Path
    window.label_17.setText("qemu-system-mipsel Caminho") # qemu-system-mipsel Path
    window.label_18.setText("qemu-system-mips Caminho") # qemu-system-mips Path
    window.label_19.setText("qemu-system-mips64 Caminho") # qemu-system-mips64 Path
    window.label_12.setText("qemu-system-sparc Caminho") # qemu-system-sparc Path
    window.label_13.setText("qemu-system-sparc64 Caminho") # qemu-system-sparc64 Path
    window.lbl_alpha.setText("qemu-system-alpha Caminho") # qemu-system-alpha Path
    window.lbl_riscv32.setText("qemu-system-riscv32 Caminho") # qemu-system-riscv32 Path
    window.lbl_riscv64.setText("qemu-system-riscv64 Caminho") # qemu-system-riscv64 Path

    window.pushButton.setText("Procurar") # Browse
    window.pushButton_2.setText("Procurar") # Browse
    window.pushButton_3.setText("Procurar") # Browse
    window.pushButton_4.setText("Procurar") # Browse
    window.pushButton_5.setText("Procurar") # Browse
    window.pushButton_7.setText("Procurar") # Browse
    window.pushButton_12.setText("Procurar") # Browse
    window.pushButton_16.setText("Procurar") # Browse
    window.pushButton_17.setText("Procurar") # Browse
    window.pushButton_18.setText("Procurar") # Browse
    window.pushButton_19.setText("Procurar") # Browse
    window.pushButton_13.setText("Procurar") # Browse
    window.pushButton_14.setText("Procurar") # Browse
    window.btn_alpha.setText("Procurar") # Browse
    window.btn_riscv32.setText("Procurar") # Browse
    window.btn_riscv64.setText("Procurar") # Browse
    window.pushButton_6.setText("Aplicar") # Apply
    window.btn_apply_qemu2.setText("Aplicar") # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("Feito em Python e com a tecnologia PyQT, licenciado com a licença GNU General Public License 3.0")

    window.label_10.setText(
        """
        AVISO: Esse aplicativo vem com NENHUMA GARANTIA sobre leis aplicáveis, Por favor verifique a licença GNU GPL para detalhes.
        """
        ) # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner feito por Tech-FZ.") # Banner made by (insert author of current banner here).

    window.label_21.setText("EmuGUI em redes sociais (em Inglês)") # EmuGUI on social media (in English)

def translateNewVmPT(window):
    window.setWindowTitle("EmuGUI - Create new VM")

    # First page
    window.lbl_vmname.setText("Nome") # Name
    window.lbl_arch.setText("Arquitetura") # Architecture
    window.cb_arch.setPlaceholderText("Please choose an architecture") # Please choose an architecture

    window.btn_next1.setText("Proximo >") # Next >
    window.btn_cancel1.setText("Cancelar") # Cancel

    # Second page
    window.lbl_machine.setText("Máquina") # Machine
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_ram.setText("RAM em MB") # RAM in MB

    window.cb_machine.setPlaceholderText("Please select a machine") # Please select a machine
    window.cb_cpu.setPlaceholderText("Please select a processor") # Please select a processor

    window.pb_prev2.setText("< Anterior") # < Previous
    window.pb_next2.setText("Proximo >") # Next >
    window.pb_cancel2.setText("Cancelar") # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("Uso do VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "Crie um novo disco virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "Adicionar um disco virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "Não adicionar um disco virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("Caminho do VHD") # VHD path
    window.lbl_vhdF.setText("Formato de arquivo VHD") # VHD file format
    window.lbl_maxsize.setText("Tamanho máximo") # Maximum size
    window.lbl_hddC.setText("Controladora de HDD") # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(Please select a file format)") # (Please select a file format)

    window.btn_vhdP.setText("Procurar") # Browse
    window.btn_prev3.setText("< Anterior") # < Previous
    window.btn_next3.setText("Proximo >") # Next >
    window.btn_cancel3.setText("Cancelar") # Cancel

    # Fourth page
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Rede") # Network
    window.lbl_mouse.setText("Mouse") # Mouse

    window.cb_vga.setPlaceholderText("(Please select a graphics adapter)") # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(Please select a network adapter)") # (Please select a network adapter)

    window.btn_prev4.setText("< Anterior") # < Previous
    window.btn_next4.setText("Proximo >") # Next >
    window.btn_cancel4.setText("Cancelar") # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "Localização do arquivo de BIOS externo (deixe em branco dentro para usar a BIOS padrão)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("Arquivo BIOS externo") # External BIOS file

    window.btn_biosF.setText("Procurar") # Browse
    window.btn_prev5.setText("< Anterior") # < Previous
    window.btn_next5.setText("Proximo >") # Next >
    window.btn_cancel5.setText("Cancelar") # Cancel

    # Sixth page
    window.lbl_sound.setText("Placa de Som") # Sound card
    window.lbl_cores.setText("Núcleos de CPU")# CPU cores
    window.lbl_kbd.setText("Teclado") # Keyboard
    window.lbl_kbdlayout.setText("Layout do teclado") # Keyboard layout

    window.btn_prev6.setText("< Anterior") # < Previous
    window.btn_next6.setText("Proximo >") # Next >
    window.btn_cancel6.setText("Cancelar") # Cancel

    # Seventh page
    window.lbl_kernel.setText("Kernel do Linux") # Linux kernel
    window.lbl_initrd.setText("Imagem initrd do Linux") # Linux initrd image
    window.lbl_cmd.setText("Linux cmd args") # Linux cmd args

    window.btn_kernel.setText("Procurar") # Browse
    window.btn_initrd.setText("Procurar") # Browse
    window.btn_prev7.setText("< Anterior") # < Previous
    window.btn_next7.setText("Proximo >") # Next >
    window.btn_cancel7.setText("Cancelar") # Cancel

    # Eighth page
    window.lbl_accel.setText("Aceleração") # Acceleration
    window.lbl_cdc1.setText("Controladora de CD 1") # CD controller 1
    window.lbl_cdc2.setText("Controladora de CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< Anterior") # < Previous
    window.btn_next8.setText("Proximo >") # Next >
    window.btn_cancel8.setText("Cancelar") # Cancel

    # Ninth page
    window.lbl_addargs.setText("Argumentos adicionais (Se preciso)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("Adicionar suporte USB") # Add USB support

    window.btn_prev9.setText("< Anterior") # < Previous
    window.btn_finish.setText("Concluir") # Finish
    window.btn_cancel9.setText("Cancelar") # Cancel

def translateStartVmPT(window, vmname):
    window.setWindowTitle(f"EmuGUI - Start {vmname}")
    window.label_4.setText("Data & Hora") # Date & Time
    window.label_3.setText("Ligar de") # Boot from
    window.label_6.setText("Caminho TPM (Somente Linux)") # TPM path (Linux only)
    window.label_7.setText("Criar TPM do terminal!") # Create the TPM from the terminal!

    window.label_5.setText("""
    OBS: Se a Máquina Virtual não iniciar com 5 minutos, então você deve verificar as configurações da Máquina Virtual e do QEMU
    """) # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("Procurar") # Browse
    window.pushButton_2.setText("Procurar") # Browse
    window.pushButton_6.setText("Procurar") # Browse
    window.pushButton_5.setText("Deixar para o Sistema") # Set to system
    window.pushButton_3.setText("Iniciar Máquina Virtual") # Start VM
    window.pushButton_4.setText("Cancelar") # Cancel
    window.checkBox.setText("Use RTC option") # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

def translateVmExistsPT(window):
    window.label.setText(
        "Desculpe, mas uma máquina virtual com esse nome já existe."
        ) # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "Por favor, apague a outra máquina virtual ou pense em um nome novo."
        ) # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("OK") # OK

def translateVhdExistsPT(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "Desculpe, Mas o disco que você quer criar já existe."
        ) # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("Você quer manter ou sobrescrever?") # Do you want to keep or overwrite it?

    window.pushButton.setText("Sobreescrever") # Overwrite
    window.pushButton_2.setText("Manter") # Keep

def translateSettingsPendingPT(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("Você não configurou os caminhos do QEMU.")
    window.label_2.setText("Por favor, vá para as configurações para fazer isso e tente novamente após.")

    window.pushButton.setText("OK") # OK

def translateVmTooNewPT(window):
    window.label.setText(
        "Essa Máquina Virtual foi feita com uma versão do EmuGUI Que é muito nova. Por favor use uma versão mais antiga!"
        ) # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK") # OK

def translateQemuSysMissingPT(window, arch):
    window.label.setText(
        f"Desculpe, Mas o EmuGUI Não está configurado para usar “qemu-system-{arch}” ainda.\nPorém, esse componente é necessário para iniciar a Máquina Virtual.\nPor favor, Arrume isso nas configurações/QEMU Para resolver esse problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateQemuImgMissingPT(window):
    window.label.setText(
        "Desculpe, Mas o EmuGUI Não está configurado para usar “qemu-img-*” ainda.\nPorém, esse componente é necessário para criar ou editar Máquinas Virtuais.\nPor favor, Arrume isso nas configurações/QEMU Para resolver esse problema."
        ) # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK") # OK

def translateEditVMPT(window, vmname):
    window.setWindowTitle(f"EmuGUI - Edit {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("Cancelar") # Cancel
    window.btn_ok.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Geral") # General
    window.tabWidget.setTabText(1, "Máquina") # Machine
    window.tabWidget.setTabText(2, "Discos Virtuais") # Virtual hard disks
    window.tabWidget.setTabText(3, "Perifericos") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Componentes adicionais") # Additional components

    # Translations for General tab
    window.lbl_name.setText("Nome") # Name
    window.lbl_arch.setText("Arquitetura") # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("CPU") # CPU
    window.lbl_machine.setText("Máquina") # Machine
    window.lbl_ram.setText("RAM em MB") # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("Uso do VHD") # VHD usage
    window.lbl_vhdp.setText("Caminho do VHD") # VHD path
    window.lbl_vhdf.setText("Formato de arquivo VHD") # VHD file format
    window.lbl_maxsize.setText("Tamanho máximo") # Maximum size
    window.btn_vhdp.setText("Procurar") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "Crie um novo disco virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "Adicionar um disco virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "Não adicionar um disco virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("Controladora de CD 1") # CD controller 1
    window.lbl_cdc2.setText("Controladora de CD 2") # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("Controladora de HDD") # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "Deixe o QEMU decidir") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("Mouse") # Mouse type
    window.lbl_kbdtype.setText("Tipo de Teclado") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("Localização do arquivo de BIOS externo (deixe em branco dentro para usar a BIOS padrão)")
    window.lbl_biosf.setText("Arquivo BIOS externo") # External BIOS file
    window.btn_biosf.setText("Procurar") # Browse

    # Translations for Linux tab
    window.lbl_kernel.setText("Kernel do Linux") # Linux kernel
    window.lbl_initrd.setText("Imagem initrd do Linux") # Linux initrd image
    window.lbl_cmd.setText("Linux cmd arguments") # Linux cmd arguments
    window.btn_kernel.setText("Procurar") # Browse
    window.btn_initrd.setText("Procurar") # Browse

    # Translations for Additional components tab
    window.lbl_vga.setText("VGA") # VGA
    window.lbl_net.setText("Rede") # Network adapter
    window.lbl_sound.setText("Placa de Som") # Sound card
    window.lbl_addargs.setText("Argumentos adicionais (Se preciso)") # Additional arguments (if necessary)
    window.lbl_cpuc.setText("Núcleos de CPU") # CPU cores
    window.chb_usb.setText("Adicionar suporte USB") # Add USB support
    window.lbl_accel.setText("Aceleração") # Acceleration

def translateErrDialogPT(window, errcode):
    window.setWindowTitle(f"EmuGUI - Erro")
    
    if errcode.startswith("C"):
        window.label.setText("EmuGUI encountered a critical error and needs to be closed.") # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI encontrou um erro.") # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI tem um alerta para você.") # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI tem algo para falar.") # EmuGUI has something to say.

    window.label_2.setText("Erro Código: " + errcode) # Error Code:

    window.label_3.setText(
        "Se esse erro ocorrer múltiplas vezes, entre em contato com o administrador e/ou peça ajuda no servidor de Discord do EmuGUI ou no repositório do GitHub."
        ) # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.
    
    window.pushButton.setText("OK") # OK