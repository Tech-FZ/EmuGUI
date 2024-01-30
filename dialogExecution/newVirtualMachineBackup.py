from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_NewVM import Ui_Dialog
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
from dialogExecution.vmExistsDialog import VmAlreadyExistsDialog
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

        while i < self.comboBox_18.count():
            if self.comboBox_18.itemText(i) == "Create a new virtual hard drive":
                self.comboBox_18.setCurrentIndex(i)
                break

            i += 1

        self.firstStage()
        self.vhdAddingChange()

        self.logman.writeToLogFile(
            f"{errors.errCodes.errCodes[48]}: GUI \"New virtual machine\" opened successfully"
            )

    def connectSignalsSlots(self):
        # Page 1 (Architecture selection)
        self.pushButton_3.clicked.connect(self.archSystem)
        self.pushButton_2.clicked.connect(self.close)

        # Page 2.1 (i386/x86_64 machine preparation)
        self.pushButton_5.clicked.connect(self.firstStage)
        self.pushButton_4.clicked.connect(self.vhdMenu)
        self.pushButton_6.clicked.connect(self.close)

        # Page 2.2 (ppc machine preparation)
        self.pushButton_7.clicked.connect(self.firstStage)
        self.pushButton_8.clicked.connect(self.vhdMenu)
        self.pushButton_9.clicked.connect(self.close)

        # Page 2.3 (mips64el machine preparation)
        self.pushButton_10.clicked.connect(self.firstStage)
        self.pushButton_11.clicked.connect(self.vhdMenu)
        self.pushButton_12.clicked.connect(self.close)

        # Page 2.4 (aarch64/arm machine preparation)
        self.pushButton_33.clicked.connect(self.firstStage)
        self.pushButton_34.clicked.connect(self.vhdMenu)
        self.pushButton_35.clicked.connect(self.close)

        # Page 2.5 (sparc machine preparation)
        self.pushButton_37.clicked.connect(self.firstStage)
        self.pushButton_38.clicked.connect(self.vhdMenu)
        self.pushButton_39.clicked.connect(self.close)

        # Page 2.6 (sparc64 machine preparation)
        self.pushButton_41.clicked.connect(self.firstStage)
        self.pushButton_40.clicked.connect(self.vhdMenu)
        self.pushButton_42.clicked.connect(self.close)

        # Page 3 (VHD creation)
        self.pushButton_13.clicked.connect(self.vhdBrowseLocation)
        self.pushButton_16.clicked.connect(self.archSystem)
        self.pushButton_14.clicked.connect(self.vgaNetworkMenu)
        self.pushButton_15.clicked.connect(self.close)

        # Page 4 (VGA and network)
        self.pushButton_18.clicked.connect(self.vhdMenu)
        self.pushButton_19.clicked.connect(self.close)
        self.pushButton_17.clicked.connect(self.extBios)
        self.comboBox_18.currentTextChanged.connect(self.vhdAddingChange)

        # Page 5 (External BIOS)
        self.pushButton_25.clicked.connect(self.vgaNetworkMenu)
        self.pushButton_23.clicked.connect(self.close)
        self.pushButton_24.clicked.connect(self.soundCard)
        self.pushButton_36.clicked.connect(self.extBiosFileLocation)

        # Page 6 (Sound card)
        self.pushButton_28.clicked.connect(self.extBios)
        self.pushButton_26.clicked.connect(self.close)
        self.pushButton_27.clicked.connect(self.linuxVMSpecific)

        # Page 7 (Linux-specific options)
        self.pushButton.clicked.connect(self.linuxKernelBrowseLocation)
        self.pushButton_32.clicked.connect(self.linuxInitridBrowseLocation)
        self.pushButton_31.clicked.connect(self.soundCard)
        self.pushButton_29.clicked.connect(self.close)
        self.pushButton_30.clicked.connect(self.accelSettings)

        # Page 8 (Acceleration options)
        self.pushButton_81.clicked.connect(self.linuxVMSpecific)
        self.pushButton_77.clicked.connect(self.win2kHacker)
        self.pushButton_80.clicked.connect(self.close)

        # Page 9 (Additional arguments)
        self.pushButton_22.clicked.connect(self.accelSettings)
        self.pushButton_20.clicked.connect(self.finishCreation)
        self.pushButton_21.clicked.connect(self.close)

    def langDetect(self):
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
        WHERE name = "{self.lineEdit.text()}";
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
                if self.comboBox.currentText() == "i386":
                    self.stackedWidget.setCurrentIndex(1)

                elif self.comboBox.currentText() == "x86_64":
                    self.stackedWidget.setCurrentIndex(1)
        
                elif self.comboBox.currentText() == "ppc" or self.comboBox.currentText() == "ppc64":
                    self.stackedWidget.setCurrentIndex(2)

                elif self.comboBox.currentText() == "mips64el" or self.comboBox.currentText() == "mipsel":
                    self.stackedWidget.setCurrentIndex(3)
                
                elif self.comboBox.currentText() == "aarch64" or self.comboBox.currentText() == "arm":
                    self.stackedWidget.setCurrentIndex(4)

                elif self.comboBox.currentText() == "sparc":
                    self.stackedWidget.setCurrentIndex(5)

                elif self.comboBox.currentText() == "sparc64":
                    self.stackedWidget.setCurrentIndex(6)
        
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
        self.stackedWidget.setCurrentIndex(7)

    def vhdAddingChange(self):
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        with open("translations/addnovhd.txt", "r+", encoding="utf8") as noVhdFile:
            noVhdContent = noVhdFile.read()

        if creNewVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_6.setEnabled(True)
            self.pushButton_13.setEnabled(True)

            # For new
            self.comboBox_8.setEnabled(True)
            self.spinBox_4.setEnabled(True)
            self.comboBox_9.setEnabled(True)

        elif addExistVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_6.setEnabled(True)
            self.pushButton_13.setEnabled(True)

            # For new
            self.comboBox_8.setEnabled(False)
            self.spinBox_4.setEnabled(False)
            self.comboBox_9.setEnabled(False)

        elif noVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_6.setEnabled(False)
            self.pushButton_13.setEnabled(False)

            # For new
            self.comboBox_8.setEnabled(False)
            self.spinBox_4.setEnabled(False)
            self.comboBox_9.setEnabled(False)

    def vhdBrowseLocation(self):
        # This code makes it possible to search a location for your VHD.
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        if creNewVhdContent.__contains__(self.comboBox_18.currentText()):        
            filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Save VHD file', dir='.', filter='Hard disk file (*.img);;QCOW2 disk image (*.qcow2);;QCOW disk image (*.qcow);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;Virtual PC hard disks (*.vpc);;All files (*.*)')

            if filename:
                self.lineEdit_6.setText(filename)

        elif addExistVhdContent.__contains__(self.comboBox_18.currentText()):        
            filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open VHD file', dir='.', filter='Hard disk file (*.img);;QCOW2 disk image (*.qcow2);;QCOW disk image (*.qcow);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;Virtual PC hard disks (*.vpc);;All files (*.*)')

            if filename:
                self.lineEdit_6.setText(filename)

    def firstStage(self):
        self.stackedWidget.setCurrentIndex(0)

    def vgaNetworkMenu(self):
        self.stackedWidget.setCurrentIndex(8)

    def extBios(self):
        self.stackedWidget.setCurrentIndex(9)

    def extBiosFileLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select BIOS file', dir='.', filter='BIN files (*.bin);;All files (*.*)')

        if filename:
            self.lineEdit_8.setText(filename)

    def soundCard(self):
        self.stackedWidget.setCurrentIndex(10)

    def linuxVMSpecific(self):
        self.stackedWidget.setCurrentIndex(11)

    def linuxKernelBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux kernel', dir='.', filter='All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def accelSettings(self):
        self.stackedWidget.setCurrentIndex(12)

    def win2kHacker(self):
        self.stackedWidget.setCurrentIndex(13)

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

        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "x86_64":
            machine = self.comboBox_2.currentText()
            cpu = self.comboBox_3.currentText()

            if cpu.startswith("Icelake-Client"):
                cpu = "Icelake-Client"

            ram = self.spinBox.value()
        
        elif self.comboBox.currentText() == "ppc" or self.comboBox.currentText() == "ppc64":
            machine = self.comboBox_4.currentText()
            cpu = self.comboBox_5.currentText()
            ram = self.spinBox_2.value()

        elif self.comboBox.currentText() == "mips64el" or self.comboBox.currentText() == "mipsel":
            machine = self.comboBox_6.currentText()
            cpu = self.comboBox_7.currentText()
            ram = self.spinBox_3.value()

        elif self.comboBox.currentText() == "aarch64" or self.comboBox.currentText() == "arm":
            machine = self.comboBox_14.currentText()
            cpu = self.comboBox_15.currentText()
            ram = self.spinBox_5.value()

        elif self.comboBox.currentText() == "sparc":
            machine = self.comboBox_20.currentText()
            cpu = "Let QEMU decide"
            ram = self.spinBox_7.value()

        elif self.comboBox.currentText() == "sparc64":
            machine = self.comboBox_21.currentText()
            cpu = "Let QEMU decide"
            ram = self.spinBox_8.value()

        if letQemuDecideVariantsStr.__contains__(machine):
            machine = "Let QEMU decide"

        if letQemuDecideVariantsStr.__contains__(cpu):
            cpu = "Let QEMU decide"

        if self.lineEdit_6.text() == "" or self.lineEdit_6.isEnabled() == False:
            vhd = "NULL"
        
        else:
            vhd = self.lineEdit_6.text()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

            with open(tempVmDef, "r+") as tempVmDefFile:
                vmSpecsRaw = tempVmDefFile.readlines()

            vhdAction = vmSpecsRaw[0]

            if self.comboBox_8.isEnabled():
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

                if self.comboBox_9.currentText().startswith("K"):
                    vhd_size_in_b = self.spinBox_4.value() * 1024

                elif self.comboBox_9.currentText().startswith("M"):
                    vhd_size_in_b = self.spinBox_4.value() * 1024 * 1024

                elif self.comboBox_9.currentText().startswith("G"):
                    vhd_size_in_b = self.spinBox_4.value() * 1024 * 1024 * 1024

                print(vhd_size_in_b)

                if platform.system() == "Windows":
                    vhd_cmd = f"{qemu_binary} create -f {self.comboBox_8.currentText()} \"{vhd}\" {str(vhd_size_in_b)}"

                else:
                    vhd_cmd = f"{qemu_binary} create -f {self.comboBox_8.currentText()} {vhd} {str(vhd_size_in_b)}"

                if vhdAction.startswith("overwrite"):
                    subprocess.Popen(vhd_cmd)

                print("The query was executed and the virtual disk created successfully.")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                print(f"The query was executed successfully, but the virtual disk couldn't be created. Trying to use subprocess.run")

                try:
                    vhd_cmd_split = vhd_cmd.split(" ")

                    if vhdAction.startswith("overwrite"):
                        subprocess.run(vhd_cmd_split)
                
                except:
                    print("The virtual disk could not be created. Please check if the path and the QEMU settings are correct.")

        if letQemuDecideVariantsStr.__contains__(self.comboBox_10.currentText()):
            vga = "Let QEMU decide"
        
        else:
            vga = self.comboBox_10.currentText()

        if self.comboBox_11.currentText() == "none":
            networkAdapter = "none"
        
        else:
            networkAdapter = self.comboBox_11.currentText()

        if self.checkBox.isChecked():
            usbtablet = 1

        else:
            usbtablet = 0

        if self.checkBox_2.isChecked():
            win2k = 1

        else:
            win2k = 0

        ext_bios_dir = self.lineEdit_3.text()

        add_args = self.lineEdit_2.text()

        if self.checkBox_3.isChecked() or self.checkBox.isChecked() or self.comboBox_13.currentText() == "USB Mouse":
            usb_support = 1

        elif self.comboBox_13.currentText() == "USB Tablet Device" or self.comboBox_16.currentText() == "USB Keyboard":
            usb_support = 1

        else:
            usb_support = 0

        if sysDefContent.__contains__(self.comboBox_19.currentText()):
            kbdlayout = "en-us"

        else:
            kbdlayout = self.comboBox_19.currentText()

        if letQemuDecideVariantsStr.__contains__(self.comboBox_44.currentText()):
            cd_control1 = "Let QEMU decide"
        
        else:
            cd_control1 = self.comboBox_44.currentText()

        if letQemuDecideVariantsStr.__contains__(self.comboBox_45.currentText()):
            cd_control2 = "Let QEMU decide"
        
        else:
            cd_control2 = self.comboBox_45.currentText()

        if letQemuDecideVariantsStr.__contains__(self.comboBox_46.currentText()):
            hda_control = "Let QEMU decide"
        
        else:
            hda_control = self.comboBox_46.currentText()

        if self.comboBox_43.currentText() == "HAXM (depreciated)":
            accelerator = "HAXM"
        
        else:
            accelerator = self.comboBox_43.currentText()
        
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
            "{self.lineEdit.text()}",
            "{self.comboBox.currentText()}",
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
            "{self.comboBox_12.currentText()}",
            "{self.lineEdit_4.text()}",
            "{self.lineEdit_5.text()}",
            "{self.lineEdit_7.text()}",
            "{self.comboBox_13.currentText()}",
            {self.spinBox_6.value()},
            "{self.lineEdit_8.text()}",
            "{self.comboBox_16.currentText()}",
            {usb_support},
            "{self.comboBox_17.currentText()}",
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