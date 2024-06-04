from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_NewVM2 import Ui_Dialog
import sqlite3
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific
    
import subprocess
import errors.logman
import errors.logID
import errors.errCodes
from dialogExecution.errDialog import ErrDialog
import translations.de
import translations.uk
import translations.en
import translations.fr
import translations.es
import translations.ro
import translations.be
import translations.cz
import translations.ru
import translations.pt
import translations.it
import translations.pl
import locale
import plugins.pluginmgr.hw_reader as hwpr # HWPR = HardWare Plug-in Reader

class NewVirtualMachineDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        # Initializing the dialog for creating the VM.
        self.logman = errors.logman.LogMan()
        self.logman.logFile = self.logman.setLogFile()

        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        
        self.setWindowTitle("EmuGUI - Create new VM")
        
        self.langDetect()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()

        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

        with open(tempVmDef, "w+") as tempVmDefFile:
            tempVmDefFile.write("overwrite")

        i = 0

        while i < self.cb_vhdU.count():
            if self.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
                self.cb_vhdU.setCurrentIndex(i)
                break

            i += 1

        self.firstStage()
        self.vhdAddingChange()
        self.hw_plugins = hwpr.read_hw_plugin()
        self.setupCB()

        self.logman.writeToLogFile(
            f"{errors.errCodes.errCodes[48]}: GUI \"New virtual machine\" opened successfully"
            )

    def connectSignalsSlots(self):
        # Page 1 (Architecture selection)
        self.btn_next1.clicked.connect(self.archSystem)
        self.btn_cancel1.clicked.connect(self.close)

        # Page 2 (Machine preparation)
        self.pb_prev2.clicked.connect(self.firstStage)
        self.pb_next2.clicked.connect(self.vhdMenu)
        self.pb_cancel2.clicked.connect(self.close)

        # Page 3 (VHD creation)
        self.btn_vhdP.clicked.connect(self.vhdBrowseLocation)
        self.btn_prev3.clicked.connect(self.archSystem)
        self.btn_next3.clicked.connect(self.vgaNetworkMenu)
        self.btn_cancel3.clicked.connect(self.close)
        self.cb_vhdU.currentTextChanged.connect(self.vhdAddingChange)

        # Page 4 (VGA and network)
        self.btn_prev4.clicked.connect(self.vhdMenu)
        self.btn_cancel4.clicked.connect(self.close)
        self.btn_next4.clicked.connect(self.extBios)

        # Page 5 (External BIOS)
        self.btn_prev5.clicked.connect(self.vgaNetworkMenu)
        self.btn_cancel5.clicked.connect(self.close)
        self.btn_next5.clicked.connect(self.soundCard)
        self.btn_biosF.clicked.connect(self.extBiosFileLocation)

        # Page 6 (Sound card)
        self.btn_prev6.clicked.connect(self.extBios)
        self.btn_cancel6.clicked.connect(self.close)
        self.btn_next6.clicked.connect(self.linuxVMSpecific)

        # Page 7 (Linux-specific options)
        self.btn_kernel.clicked.connect(self.linuxKernelBrowseLocation)
        self.btn_initrd.clicked.connect(self.linuxInitridBrowseLocation)
        self.btn_prev7.clicked.connect(self.soundCard)
        self.btn_cancel7.clicked.connect(self.close)
        self.btn_next7.clicked.connect(self.accelSettings)

        # Page 8 (Acceleration options)
        self.btn_prev8.clicked.connect(self.linuxVMSpecific)
        self.btn_next8.clicked.connect(self.win2kHacker)
        self.btn_cancel8.clicked.connect(self.close)

        # Page 9 (Additional arguments)
        self.btn_prev9.clicked.connect(self.accelSettings)
        self.btn_finish.clicked.connect(self.finishCreation)
        self.btn_cancel9.clicked.connect(self.close)

    def setupCB(self):
        for plugin in self.hw_plugins:
            try:
                self.cb_vga.addItems(plugin["graphics"])

            except:
                pass

            try:
                self.cb_net.addItems(plugin["networking"])

            except:
                pass

            try:
                self.cb_sound.addItems(plugin["sound"])

            except:
                pass

            try:
                self.cb_usb.addItems(plugin["usb_controllers"])

            except:
                pass

    def langDetect(self):
        self.lbl_biosLoc.setWordWrap(True)

        select_language = """
        SELECT name, value FROM settings
        WHERE name = "lang";
        """

        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        try:
            cursor.execute(select_language)
            connection.commit()
            result = cursor.fetchall()

            # Language modes
            # system: language of OS
            # en: English
            # de: German
            langmode = "system"

            try:
                qemu_img_slot = str(result[0])

                if result[0][1] == "en":
                    langmode = "en"

                elif result[0][1] == "de":
                    langmode = "de"

                elif result[0][1] == "uk":
                    langmode = "uk"

                elif result[0][1] == "fr":
                    langmode = "fr"

                elif result[0][1] == "es":
                    langmode = "es"

                elif result[0][1] == "ro":
                    langmode = "ro"

                elif result[0][1] == "ru":
                    langmode = "ru"

                elif result[0][1] == "be":
                    langmode = "be"

                elif result[0][1] == "cz":
                    langmode = "cz"

                elif result[0][1] == "pt":
                    langmode = "pt"

                elif result[0][1] == "pl":
                    langmode = "pl"

                elif result[0][1] == "it":
                    langmode = "it"

                elif result[0][1] == "system":
                    langmode = "system"

                print("Language mode successfully taken from database.")

                self.logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[49]}: Language \"{langmode}\" taken from database successfully"
                )

                self.setLanguage(langmode)

            except:
                langmode = "system"

                print("Language mode not accessable. Trying to use system language.")

                self.logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[50]}: Language could not be taken from database. Trying to use system language."
                )

                self.setLanguage(langmode)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            self.logman.writeToLogFile(
                f"{errors.errCodes.errCodes[50]}: Could not connect to the database to detect the language. Trying to use system language."
                )

            self.setLanguage("system")

    def setLanguage(self, langmode):
        if langmode == "system" or langmode == None:
            languageToUse = locale.getlocale()[0]

        else:
            languageToUse = langmode

        if languageToUse != None:
            if languageToUse.startswith("de"):
                translations.de.translateNewVmDE(self)

            elif languageToUse.startswith("uk"):
                translations.uk.translateNewVmUK(self)

            elif languageToUse.startswith("fr"):
                translations.fr.translateNewVmFR(self)

            elif languageToUse.startswith("es"):
                translations.es.translateNewVmES(self)

            elif languageToUse.startswith("ro"):
                translations.ro.translateNewVmRO(self)

            elif languageToUse.startswith("ru"):
                translations.ru.translateNewVmRU(self)

            elif languageToUse.startswith("be"):
                translations.be.translateNewVmBE(self)

            elif languageToUse.startswith("cz"):
                translations.cz.translateNewVmCZ(self)

            elif languageToUse.startswith("pt"):
                translations.pt.translateNewVmPT(self)

            elif languageToUse.startswith("pl"):
                translations.pl.translateNewVmPL(self)

            elif languageToUse.startswith("it"):
                translations.it.translateNewVmIT(self)

            else:
                translations.en.translateNewVmEN(self)

            self.logman.writeToLogFile(
                f"{errors.errCodes.errCodes[52]}: Language \"{languageToUse}\" set successfully."
                )
        
        else:
            self.logman.writeToLogFile(
                f"{errors.errCodes.errCodes[51]}: The language couldn't be set via the locale module or the database. Trying to access temporary files."
                )
            
            if platform.system() == "Windows":
                langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
            
            else:
                langfile = platformSpecific.unixSpecific.unixLanguageFile()
            
            try:
                with open(langfile, "r+") as language:
                    languageContent = language.readlines()
                    languageToUse = languageContent[0].replace("\n", "")
                
                if languageToUse != None:
                    if languageToUse.startswith("de"):
                        translations.de.translateNewVmDE(self)

                    elif languageToUse.startswith("uk"):
                        translations.uk.translateNewVmUK(self)

                    elif languageToUse.startswith("fr"):
                        translations.fr.translateNewVmFR(self)

                    elif languageToUse.startswith("es"):
                        translations.es.translateNewVmES(self)

                    elif languageToUse.startswith("ro"):
                        translations.ro.translateNewVmRO(self)

                    elif languageToUse.startswith("ru"):
                        translations.ru.translateNewVmRU(self)

                    elif languageToUse.startswith("be"):
                        translations.be.translateNewVmBE(self)

                    elif languageToUse.startswith("cz"):
                        translations.cz.translateNewVmCZ(self)

                    elif languageToUse.startswith("pt"):
                        translations.pt.translateNewVmPT(self)

                    elif languageToUse.startswith("pl"):
                        translations.pl.translateNewVmPL(self)

                    elif languageToUse.startswith("it"):
                        translations.it.translateNewVmIT(self)

                    else:
                        translations.en.translateNewVmEN(self)

                    self.logman.writeToLogFile(
                        f"{errors.errCodes.errCodes[52]}: Language \"{languageToUse}\" set successfully."
                    )
            
            except:
                print("Translation can't be figured out. Using English language.")
                translations.en.translateNewVmEN(self)

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[11])

                self.logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[11]}: The desired language couldn't be applied and English must be used."
                )

                dialog = ErrDialog(self)
                dialog.exec()

    def archSystem(self):
        # Here, it checks the name first, than the architecture.

        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        check_vm_name = f"""
        SELECT name FROM virtualmachines
        WHERE name = "{self.le_vmname.text()}";
        """

        try:
            cursor.execute(check_vm_name)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[9])

                self.logman.writeToLogFile(
                    f"{errors.errCodes.errCodes[9]}: The VM {result[0]} already exists."
                )

                dialog = ErrDialog(self)
                dialog.exec()

            except:
                while 1 < self.cb_machine.count():
                    self.cb_machine.removeItem(1)

                while 1 < self.cb_cpu.count():
                    self.cb_cpu.removeItem(1)

                if self.cb_arch.currentText() == "i386" or self.cb_arch.currentText() == "x86_64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["x86_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["x86_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "mipsel":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["mipsel_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["mipsel_cpus"])

                        except:
                            pass
        
                elif self.cb_arch.currentText() == "ppc" or self.cb_arch.currentText() == "ppc64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["ppc_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["ppc_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "riscv32":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["riscv32_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["riscv32_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "riscv64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["riscv64_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["riscv64_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "alpha":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["alpha_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["alpha_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "mips64el":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["mips64el_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["mips64el_cpus"])

                        except:
                            pass
                
                elif self.cb_arch.currentText() == "aarch64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["aarch64_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["aarch64_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "arm":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["arm_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["arm_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "sparc":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["sparc_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["sparc_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "sparc64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["sparc64_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["sparc64_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "mips":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["mips_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["mips_cpus"])

                        except:
                            pass

                elif self.cb_arch.currentText() == "mips64":
                    for plugin in self.hw_plugins:
                        try:
                            self.cb_machine.addItems(plugin["mips64_machines"])

                        except:
                            pass

                        try:
                            self.cb_cpu.addItems(plugin["mips64_cpus"])

                        except:
                            pass

                self.stackedWidget.setCurrentIndex(1)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[12])

            self.logman.writeToLogFile(
                f"{errors.errCodes.errCodes[12]}: Could not connect to the database to figure out if the name was already in use."
            )

            dialog = ErrDialog(self)
            dialog.exec()

    def vhdMenu(self):
        self.stackedWidget.setCurrentIndex(2)

    def vhdAddingChange(self):
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        with open("translations/addnovhd.txt", "r+", encoding="utf8") as noVhdFile:
            noVhdContent = noVhdFile.read()

        if creNewVhdContent.__contains__(self.cb_vhdU.currentText()):
            # For new and existing
            self.le_vhdP.setEnabled(True)
            self.btn_vhdP.setEnabled(True)

            # For new
            self.cb_vhdF.setEnabled(True)
            self.sb_maxsize.setEnabled(True)
            self.cb_maxsize.setEnabled(True)

        elif addExistVhdContent.__contains__(self.cb_vhdU.currentText()):
            # For new and existing
            self.le_vhdP.setEnabled(True)
            self.btn_vhdP.setEnabled(True)

            # For new
            self.cb_vhdF.setEnabled(False)
            self.sb_maxsize.setEnabled(False)
            self.cb_maxsize.setEnabled(False)

        elif noVhdContent.__contains__(self.cb_vhdU.currentText()):
            # For new and existing
            self.le_vhdP.setEnabled(False)
            self.btn_vhdP.setEnabled(False)

            # For new
            self.cb_vhdF.setEnabled(False)
            self.sb_maxsize.setEnabled(False)
            self.cb_maxsize.setEnabled(False)

    def vhdBrowseLocation(self):
        # This code makes it possible to search a location for your VHD.
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        if creNewVhdContent.__contains__(self.cb_vhdU.currentText()):        
            filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Save VHD file', dir='.', filter='Hard disk file (*.img);;QCOW2 disk image (*.qcow2);;QCOW disk image (*.qcow);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;Virtual PC hard disks (*.vpc);;All files (*.*)')

            if filename:
                self.le_vhdP.setText(filename)

        elif addExistVhdContent.__contains__(self.cb_vhdU.currentText()):        
            filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open VHD file', dir='.', filter='Hard disk file (*.img);;QCOW2 disk image (*.qcow2);;QCOW disk image (*.qcow);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;Virtual PC hard disks (*.vpc);;All files (*.*)')

            if filename:
                self.le_vhdP.setText(filename)

    def firstStage(self):
        self.stackedWidget.setCurrentIndex(0)

    def vgaNetworkMenu(self):
        self.stackedWidget.setCurrentIndex(3)

    def extBios(self):
        self.stackedWidget.setCurrentIndex(4)

    def extBiosFileLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select BIOS file', dir='.', filter='BIN files (*.bin);;All files (*.*)')

        if filename:
            self.lineEdit_8.setText(filename)

    def soundCard(self):
        self.stackedWidget.setCurrentIndex(5)

    def linuxVMSpecific(self):
        self.stackedWidget.setCurrentIndex(6)

    def linuxKernelBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux kernel', dir='.', filter='All files (*.*)')

        if filename:
            self.le_kernel.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.le_initrd.setText(filename)

    def accelSettings(self):
        self.stackedWidget.setCurrentIndex(7)

    def win2kHacker(self):
        self.stackedWidget.setCurrentIndex(8)

    def finishCreation(self):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideVariants:
            letQemuDecideVariantsStr = letQemuDecideVariants.read()

        with open("translations/systemdefault.txt", "r+", encoding="utf8") as sysDefFile:
            sysDefContent = sysDefFile.read()

        # This creates your VM in the first place

        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        machine = self.cb_machine.currentText()
        cpu = self.cb_cpu.currentText()

        if cpu.startswith("Icelake-Client"):
            cpu = "Icelake-Client"

        ram = self.sb_ram.value()

        if letQemuDecideVariantsStr.__contains__(machine):
            machine = "Let QEMU decide"

        if letQemuDecideVariantsStr.__contains__(cpu):
            cpu = "Let QEMU decide"

        if self.le_vhdP.text() == "" or self.le_vhdP.isEnabled() == False:
            vhd = "NULL"
        
        else:
            vhd = self.le_vhdP.text()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

            with open(tempVmDef, "r+") as tempVmDefFile:
                vmSpecsRaw = tempVmDefFile.readlines()

            vhdAction = vmSpecsRaw[0]

            if self.cb_vhdF.isEnabled():
                vhdAction = "overwrite"

            else:
                vhdAction = "keep"

            get_qemu_img_bin = """
            SELECT value FROM settings
            WHERE name = "qemu-img"
            """

            vhd_cmd = ""

            try:
                cursor.execute(get_qemu_img_bin)
                connection.commit()
                result = cursor.fetchall()
                qemu_binary = result[0][0]
                vhd_size_in_b = None

                if self.cb_maxsize.currentText().startswith("K"):
                    vhd_size_in_b = self.sb_maxsize.value() * 1024

                elif self.cb_maxsize.currentText().startswith("M"):
                    vhd_size_in_b = self.sb_maxsize.value() * 1024 * 1024

                elif self.cb_maxsize.currentText().startswith("G"):
                    vhd_size_in_b = self.sb_maxsize.value() * 1024 * 1024 * 1024

                print(vhd_size_in_b)

                vhd_cmd = f"{qemu_binary} create -f {self.cb_vhdF.currentText()} \"{vhd}\" {str(vhd_size_in_b)}"

                if vhdAction.startswith("overwrite"):
                    subprocess.Popen(vhd_cmd)

                print("The query was executed and the virtual disk created successfully.")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                print(f"The query was executed successfully, but the virtual disk couldn't be created. Trying to use subprocess.run")

                try:
                    #vhd_cmd_split = vhd_cmd.split(" ")
                    vhd_cmd_split = [qemu_binary, "create", "-f", self.cb_vhdF.currentText(), vhd, str(vhd_size_in_b)]

                    if vhdAction.startswith("overwrite"):
                        subprocess.run(vhd_cmd_split)
                
                except:
                    print("The virtual disk could not be created. Please check if the path and the QEMU settings are correct.")

        if letQemuDecideVariantsStr.__contains__(self.cb_vga.currentText()):
            vga = "Let QEMU decide"
        
        else:
            vga = self.cb_vga.currentText()

        if self.cb_net.currentText() == "none":
            networkAdapter = "none"
        
        else:
            networkAdapter = self.cb_net.currentText()

        if self.checkBox.isChecked():
            usbtablet = 1

        else:
            usbtablet = 0

        if self.checkBox_2.isChecked():
            win2k = 1

        else:
            win2k = 0

        ext_bios_dir = self.le_biosLoc.text()

        add_args = self.le_addargs.text()

        if self.chb_usb.isChecked() or self.checkBox.isChecked() or self.cb_mouse.currentText() == "USB Mouse":
            usb_support = 1

        elif self.cb_kbd.currentText() == "USB Tablet Device" or self.cb_kbd.currentText() == "USB Keyboard":
            usb_support = 1

        else:
            usb_support = 0

        if sysDefContent.__contains__(self.cb_kbdlayout.currentText()):
            kbdlayout = "en-us"

        else:
            kbdlayout = self.cb_kbdlayout.currentText()

        if letQemuDecideVariantsStr.__contains__(self.cb_cdc1.currentText()):
            cd_control1 = "Let QEMU decide"
        
        else:
            cd_control1 = self.cb_cdc1.currentText()

        if letQemuDecideVariantsStr.__contains__(self.cb_cdc2.currentText()):
            cd_control2 = "Let QEMU decide"
        
        else:
            cd_control2 = self.cb_cdc2.currentText()

        if letQemuDecideVariantsStr.__contains__(self.cb_hddC.currentText()):
            hda_control = "Let QEMU decide"
        
        else:
            hda_control = self.cb_hddC.currentText()

        if self.cb_accel.currentText() == "HAXM (depreciated)":
            accelerator = "HAXM"
        
        else:
            accelerator = self.cb_accel.currentText()
        
        insert_into_vm_database = f"""
        INSERT INTO virtualmachines (
            name,
            architecture,
            machine,
            cpu,
            ram,
            hda,
            vga,
            net,
            usbtablet,
            win2k,
            dirbios,
            additionalargs,
            sound,
            linuxkernel,
            linuxinitrid,
            linuxcmd,
            mousetype,
            cores,
            filebios,
            keyboardtype,
            usbsupport,
            usbcontroller,
            kbdtype,
            acceltype,
            storagecontrollercd1,
            storagecontrollercd2,
            hdacontrol
        ) VALUES (
            "{self.le_vmname.text()}",
            "{self.cb_arch.currentText()}",
            "{machine}",
            "{cpu}",
            {ram},
            "{vhd}",
            "{vga}",
            "{networkAdapter}",
            {usbtablet},
            {win2k},
            "{ext_bios_dir}",
            "{add_args}",
            "{self.cb_sound.currentText()}",
            "{self.le_kernel.text()}",
            "{self.le_initrd.text()}",
            "{self.le_cmd.text()}",
            "{self.cb_mouse.currentText()}",
            {self.sb_cores.value()},
            "{self.le_biosF.text()}",
            "{self.cb_kbd.currentText()}",
            {usb_support},
            "{self.cb_usb.currentText()}",
            "{kbdlayout}",
            "{accelerator}",
            "{cd_control1}",
            "{cd_control2}",
            "{hda_control}"
        );
        """

        cursor = connection.cursor()

        try:
            cursor.execute(insert_into_vm_database)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[53])

            self.logman.writeToLogFile(
                f"{errors.errCodes.errCodes[53]}: The VM couldn't be created due to a database issue."
            )

            dialog = ErrDialog(self)
            dialog.exec()

        self.close()