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
    window.tabWidget_2.setTabText(2, "Sobre o EmuGUI") # About EmuGUI

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
    window.pushButton_6.setText("Aplicar") # Apply

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
    window.label.setText("Nome") # Name
    window.label_3.setText("Arquitetura") # Architecture
    window.comboBox.setPlaceholderText("Por favor escolha uma arquitetura.") # Please choose an architecture

    window.pushButton_3.setText("Proximo >") # Next >
    window.pushButton_2.setText("Cancelar") # Cancel

    # Second page (i386/x64 machines)
    window.label_4.setText("Máquina") # Machine
    window.label_5.setText("CPU") # CPU
    window.label_6.setText("RAM em MB") # RAM in MB

    window.comboBox_2.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine
    window.comboBox_3.setPlaceholderText("Por favor escolha um processador") # Please select a processor

    window.pushButton_5.setText("< Anterior") # < Previous
    window.pushButton_4.setText("Proximo >") # Next >
    window.pushButton_6.setText("Cancelar") # Cancel

    # Combo boxes on i386/x64 page
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Let QEMU decide" or window.comboBox_2.itemText(i) == "QEMU überlassen":
            window.comboBox_2.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_3.count():
        if window.comboBox_3.itemText(i) == "Let QEMU decide" or window.comboBox_3.itemText(i) == "QEMU überlassen":
            window.comboBox_3.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Second page (PowerPC machines)
    window.label_9.setText("Máquina") # Machine
    window.label_8.setText("CPU") # CPU
    window.label_7.setText("RAM em MB") # RAM in MB

    window.comboBox_4.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine
    window.comboBox_5.setPlaceholderText("Por favor escolha um processador") # Please select a processor

    window.pushButton_7.setText("< Anterior") # < Previous
    window.pushButton_8.setText("Proximo >") # Next >
    window.pushButton_9.setText("Cancelar") # Cancel

    # Combo boxes on PPC page
    i = 0

    while i < window.comboBox_4.count():
        if window.comboBox_4.itemText(i) == "Let QEMU decide" or window.comboBox_4.itemText(i) == "QEMU überlassen":
            window.comboBox_4.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_5.count():
        if window.comboBox_5.itemText(i) == "Let QEMU decide" or window.comboBox_5.itemText(i) == "QEMU überlassen":
            window.comboBox_5.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Second page (MIPSel machines)
    window.label_12.setText("Máquina") # Machine
    window.label_11.setText("CPU") # CPU
    window.label_10.setText("RAM em MB") # RAM in MB

    window.comboBox_6.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine
    window.comboBox_7.setPlaceholderText("Por favor escolha um processador") # Please select a processor

    window.pushButton_10.setText("< Anterior") # < Previous
    window.pushButton_11.setText("Proximo >") # Next >
    window.pushButton_12.setText("Cancelar") # Cancel

    # Combo boxes on MIPSel page
    i = 0

    while i < window.comboBox_6.count():
        if window.comboBox_6.itemText(i) == "Let QEMU decide" or window.comboBox_6.itemText(i) == "QEMU überlassen":
            window.comboBox_6.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_7.count():
        if window.comboBox_7.itemText(i) == "Let QEMU decide" or window.comboBox_7.itemText(i) == "QEMU überlassen":
            window.comboBox_7.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Second page (ARM machines)
    window.label_31.setText("Máquina") # Machine
    window.label_30.setText("CPU") # CPU
    window.label_29.setText("RAM em MB") # RAM in MB

    window.comboBox_14.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine
    window.comboBox_15.setPlaceholderText("Por favor escolha um processador") # Please select a processor

    window.pushButton_33.setText("< Anterior") # < Previous
    window.pushButton_34.setText("Proximo >") # Next >
    window.pushButton_35.setText("Cancelar") # Cancel

    # Combo boxes on ARM page
    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC32 machines)
    window.label_22.setText("Máquina") # Machine
    window.label_35.setText("RAM em MB") # RAM in MB

    window.comboBox_20.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine

    window.pushButton_37.setText("< Anterior") # < Previous
    window.pushButton_38.setText("Proximo >") # Next >
    window.pushButton_39.setText("Cancelar") # Cancel

    # Combo boxes on SPARC32 page
    i = 0

    while i < window.comboBox_20.count():
        if window.comboBox_20.itemText(i) == "Let QEMU decide" or window.comboBox_20.itemText(i) == "QEMU überlassen":
            window.comboBox_20.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Second page (SPARC64 machines)
    window.label_37.setText("Máquina") # Machine
    window.label_36.setText("RAM em MB") # RAM in MB

    window.comboBox_21.setPlaceholderText("Por favor escolha uma máquina") # Please select a machine

    window.pushButton_41.setText("< Anterior") # < Previous
    window.pushButton_40.setText("Proximo >") # Next >
    window.pushButton_42.setText("Cancelar") # Cancel

    # Combo boxes on SPARC64 page
    i = 0

    while i < window.comboBox_21.count():
        if window.comboBox_21.itemText(i) == "Let QEMU decide" or window.comboBox_21.itemText(i) == "QEMU überlassen":
            window.comboBox_21.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Third page
    window.label_20.setText("Uso do VHD") # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_18.setItemText(i, "Crie um novo disco virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_18.setItemText(i, "Adicionar um disco virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_18.setItemText(i, "Não adicionar um Disco Virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.label_13.setText("Caminho do VHD") # VHD path
    window.label_14.setText("Formato de Arquivo VHD") # VHD file format
    window.label_15.setText("Tamanho Maximo") # Maximum size
    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    window.comboBox_8.setPlaceholderText("(Por favor, escolha um formato para o arquivo.)") # (Please select a file format)

    window.pushButton_13.setText("Procurar") # Browse
    window.pushButton_16.setText("< Anterior") # < Previous
    window.pushButton_14.setText("Proximo >") # Next >
    window.pushButton_15.setText("Cancelar") # Cancel

    # Fourth page
    window.label_16.setText("VGA") # VGA
    window.label_17.setText("Internet") # Network
    window.label_28.setText("Mouse") # Mouse

    window.comboBox_10.setPlaceholderText("(Por favor, escolha um driver para os gráficos)") # (Please select a graphics adapter)
    window.comboBox_11.setPlaceholderText("(Por favor, escolha um driver para o adaptador de Internet)") # (Please select a network adapter)

    window.pushButton_18.setText("< Anterior") # < Previous
    window.pushButton_17.setText("Proximo >") # Next >
    window.pushButton_19.setText("Cancelar") # Cancel

    # Fifth page
    window.label_19.setText(
        "Localização do arquivo\nde BIOS Externo\n(deixe sem nada\ndentro para usar\na BIOS padrão)"
        ) # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.label_32.setText("Arquivo Externo da BIOS") # External BIOS file

    window.pushButton_36.setText("Procurar") # Browse
    window.pushButton_25.setText("< Anterior") # < Previous
    window.pushButton_24.setText("Proximo >") # Next >
    window.pushButton_23.setText("Cancelar") # Cancel

    # Sixth page
    window.label_23.setText("Placa de Som") # Sound card
    window.label_33.setText("Cores da CPU")# CPU cores
    window.label_34.setText("Teclado") # Keyboard
    window.label_21.setText("Layout do Teclado") # Keyboard layout

    window.pushButton_28.setText("< Anterior") # < Previous
    window.pushButton_27.setText("Proximo >") # Next >
    window.pushButton_26.setText("Cancelar") # Cancel

    # Seventh page
    window.label_24.setText("Linux kernel") # Linux kernel
    window.label_25.setText("Imagem do Linux initrd") # Linux initrd image
    window.label_26.setText("Linux cmd args") # Linux cmd args

    window.pushButton.setText("Procurar") # Browse
    window.pushButton_32.setText("Procurar") # Browse
    window.pushButton_31.setText("< Anterior") # < Previous
    window.pushButton_30.setText("Proximo >") # Next >
    window.pushButton_29.setText("Cancelar") # Cancel

    # Eighth page
    window.label_71.setText("Acceleration") # Acceleration
    window.label_70.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1
    
    window.pushButton_81.setText("< Anterior") # < Previous
    window.pushButton_77.setText("Proximo >") # Next >
    window.pushButton_80.setText("Cancelar") # Cancel

    # Ninth page
    window.label_2.setText("Argumentos Adicionais (Se preciso)") # Additional arguments (if needed)

    window.checkBox_2.setText("I want to install Windows 2000\n(depreciated)") # I want to install Windows 2000\n(depreciated)
    window.checkBox_3.setText("Adicionar Suporte USB") # Add USB support

    window.pushButton_22.setText("< Anterior") # < Previous
    window.pushButton_20.setText("Finalizar") # Finish
    window.pushButton_21.setText("Cancelar") # Cancel

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
    window.pushButton_5.setText("Deixar para o Sistema") # Set to system
    window.pushButton_3.setText("Iniciar Máquina Virtual") # Start VM
    window.pushButton_4.setText("Cancelar") # Cancel

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
    window.pushButton.setText("Cancelar") # Cancel
    window.pushButton_2.setText("OK") # OK

    # Tab names
    window.tabWidget.setTabText(0, "Geral") # General
    window.tabWidget.setTabText(1, "Máquina") # Machine
    window.tabWidget.setTabText(2, "Discos Virtuais") # Virtual hard disks
    window.tabWidget.setTabText(3, "Perifericos") # Peripherals
    window.tabWidget.setTabText(4, "BIOS") # BIOS
    window.tabWidget.setTabText(6, "Componentes Adicionais") # Additional components

    # Translations for General tab
    window.label.setText("Nome") # Name
    window.label_2.setText("Arquitetura") # Architecture

    # Translations for Machine tab

    # i386 and x64
    window.label_17.setText("CPU") # CPU
    window.label_18.setText("Máquina") # Machine
    window.label_19.setText("RAM em MB") # RAM in MB

    i = 0

    while i < window.comboBox_11.count():
        if window.comboBox_11.itemText(i) == "Let QEMU decide" or window.comboBox_11.itemText(i) == "QEMU überlassen":
            window.comboBox_11.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_12.count():
        if window.comboBox_12.itemText(i) == "Let QEMU decide" or window.comboBox_12.itemText(i) == "QEMU überlassen":
            window.comboBox_12.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # PowerPC
    window.label_20.setText("CPU") # CPU
    window.label_22.setText("Máquina") # Machine
    window.label_21.setText("RAM em MB") # RAM in MB

    i = 0

    while i < window.comboBox_13.count():
        if window.comboBox_13.itemText(i) == "Let QEMU decide" or window.comboBox_13.itemText(i) == "QEMU überlassen":
            window.comboBox_13.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_14.count():
        if window.comboBox_14.itemText(i) == "Let QEMU decide" or window.comboBox_14.itemText(i) == "QEMU überlassen":
            window.comboBox_14.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # MIPS
    window.label_23.setText("CPU") # CPU
    window.label_25.setText("Máquina") # Machine
    window.label_24.setText("RAM em MB") # RAM in MB

    i = 0

    while i < window.comboBox_15.count():
        if window.comboBox_15.itemText(i) == "Let QEMU decide" or window.comboBox_15.itemText(i) == "QEMU überlassen":
            window.comboBox_15.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_16.count():
        if window.comboBox_16.itemText(i) == "Let QEMU decide" or window.comboBox_16.itemText(i) == "QEMU überlassen":
            window.comboBox_16.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # ARM
    window.label_26.setText("CPU") # CPU
    window.label_28.setText("Máquina") # Machine
    window.label_27.setText("RAM em MB") # RAM in MB

    i = 0

    while i < window.comboBox_17.count():
        if window.comboBox_17.itemText(i) == "Let QEMU decide" or window.comboBox_17.itemText(i) == "QEMU überlassen":
            window.comboBox_17.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_18.count():
        if window.comboBox_18.itemText(i) == "Let QEMU decide" or window.comboBox_18.itemText(i) == "QEMU überlassen":
            window.comboBox_18.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.label_3.setText("Uso do VHD") # VHD usage
    window.label_4.setText("Caminho do VHD") # VHD path
    window.label_5.setText("Formato de Arquivo VHD") # VHD file format
    window.label_6.setText("Tamanho Maximo") # Maximum size
    window.pushButton_3.setText("Procurar") # Browse
    
    # Combobox for VHD usage
    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Create a new virtual hard drive":
            window.comboBox_2.setItemText(i, "Crie um novo disco virtual") # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Add an existing virtual hard drive":
            window.comboBox_2.setItemText(i, "Adicionar um disco virtual existente") # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.comboBox_2.count():
        if window.comboBox_2.itemText(i) == "Don't add a virtual hard drive":
            window.comboBox_2.setItemText(i, "Não adicionar um Disco Virtual") # Don't add a virtual hard drive
            break

        i += 1

    window.label_37.setText("CD controller 1") # CD controller 1
    window.label_72.setText("CD controller 2") # CD controller 2

    i = 0

    while i < window.comboBox_44.count():
        if window.comboBox_44.itemText(i) == "Let QEMU decide" or window.comboBox_44.itemText(i) == "QEMU überlassen":
            window.comboBox_44.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.comboBox_45.count():
        if window.comboBox_45.itemText(i) == "Let QEMU decide" or window.comboBox_45.itemText(i) == "QEMU überlassen":
            window.comboBox_45.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    window.label_73.setText("HDD controller") # HDD controller

    i = 0

    while i < window.comboBox_46.count():
        if window.comboBox_46.itemText(i) == "Let QEMU decide" or window.comboBox_46.itemText(i) == "QEMU überlassen":
            window.comboBox_46.setItemText(i, "Deixe o QEMU Decidir") # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.label_7.setText("Mouse type") # Mouse type
    window.label_8.setText("Tipo de Teclado") # Keyboard type
    
    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.label_11.setText("Localização do arquivo de BIOS Externo (deixe sem nada dentro para usar a BIOS padrão)")
    window.label_12.setText("Arquivo Externo da BIOS") # External BIOS file
    window.pushButton_4.setText("Procurar") # Browse

    # Translations for Linux tab
    window.label_13.setText("Linux kernel") # Linux kernel
    window.label_14.setText("Imagem do Linux initrd") # Linux initrd image
    window.label_15.setText("Linux cmd arguments") # Linux cmd arguments
    window.pushButton_5.setText("Procurar") # Browse
    window.pushButton_6.setText("Procurar") # Browse

    # Translations for Additional components tab
    window.label_9.setText("VGA") # VGA
    window.label_10.setText("Internet") # Network adapter
    window.label_16.setText("Placa de Som") # Sound card
    window.label_29.setText("Argumentos Adicionais (Se preciso)") # Additional arguments (if necessary)
    window.label_30.setText("Cores da CPU") # CPU cores
    window.checkBox.setText("Adicionar Suporte USB") # Add USB support
    window.label_36.setText("Acceleration") # Acceleration

def translateErrDialogPT(window, errcode):
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