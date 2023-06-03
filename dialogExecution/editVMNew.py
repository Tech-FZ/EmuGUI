from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_EditVM import Ui_Dialog
import sqlite3
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific
    
import subprocess
from dialogExecution.vmExistsDialog import VmAlreadyExistsDialog
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
import locale

class EditVMNewDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        self.connectSignalsSlots()
        self.tabWidget.setCurrentIndex(0)
        self.langDetect()
        self.vmSpecs = self.readTempVmFile()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.finishCreation)
        self.comboBox_2.currentTextChanged.connect(self.vhdAddingChange)
        self.comboBox.currentTextChanged.connect(self.archChanged)
        self.pushButton_3.clicked.connect(self.vhdBrowseLocation)
        self.pushButton_4.clicked.connect(self.extBiosFileLocation)
        self.pushButton_5.clicked.connect(self.linuxKernelBrowseLocation)
        self.pushButton_6.clicked.connect(self.linuxInitridBrowseLocation)
    
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

                elif result[0][1] == "it":
                    langmode = "it"

                elif result[0][1] == "system":
                    langmode = "system"

                self.setLanguage(langmode)
                print("The query was executed successfully. The language slot already is in the database.")

            except:
                langmode = "system"
                self.setLanguage(langmode)
                print("The query was executed successfully. The language slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def setLanguage(self, langmode):
        if langmode == "system" or langmode == None:
            languageToUse = locale.getlocale()[0]

        else:
            languageToUse = langmode

        print(languageToUse)

        if languageToUse != None:
            if languageToUse.startswith("de"):
                translations.de.translateEditVMDE(self)

            elif languageToUse.startswith("uk"):
                translations.uk.translateEditVMUK(self)

            elif languageToUse.startswith("fr"):
                translations.fr.translateEditVMFR(self)

            elif languageToUse.startswith("es"):
                translations.es.translateEditVMES(self)

            elif languageToUse.startswith("ro"):
                translations.ro.translateEditVMRO(self)

            elif languageToUse.startswith("ru"):
                translations.ru.translateEditVMRU(self)

            elif languageToUse.startswith("be"):
                translations.be.translateEditVMBE(self)

            elif languageToUse.startswith("cz"):
                translations.cz.translateEditVMCZ(self)

            elif languageToUse.startswith("pt"):
                translations.pt.translateEditVMPT(self)
            
            elif languageToUse.startswith("it"):
                translations.it.translateEditVMIT(self)

            else:
                translations.en.translateEditVMEN(self)
        
        else:
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
                        translations.de.translateEditVMDE(self)

                    elif languageToUse.startswith("uk"):
                        translations.uk.translateEditVMUK(self)

                    elif languageToUse.startswith("fr"):
                        translations.fr.translateEditVMFR(self)

                    elif languageToUse.startswith("es"):
                        translations.es.translateEditVMES(self)

                    elif languageToUse.startswith("ro"):
                        translations.ro.translateEditVMRO(self)

                    elif languageToUse.startswith("ru"):
                        translations.ru.translateEditVMRU(self)

                    elif languageToUse.startswith("be"):
                        translations.be.translateEditVMBE(self)

                    elif languageToUse.startswith("cz"):
                        translations.cz.translateEditVMCZ(self)

                    elif languageToUse.startswith("pt"):
                        translations.pt.translateEditVMPT(self)

                    elif languageToUse.startswith("it"):
                        translations.it.translateEditVMIT(self)

                    else:
                        translations.en.translateEditVMEN(self)
            
            except:
                print("Translation can't be figured out. Using English language.")
                translations.en.translateEditVMEN(self)

    def machineCpuI386Amd64(self, machine, cpu):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_12.count():
            if letQemuDecideContent.__contains__(self.comboBox_12.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_12.setCurrentIndex(i)
                    break

            elif self.comboBox_12.itemText(i) == machine:
                self.comboBox_12.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_11.count():
            if letQemuDecideContent.__contains__(self.comboBox_11.itemText(i)):
                if cpu == "Let QEMU decide":
                    self.comboBox_11.setCurrentIndex(i)
                    break

            if self.comboBox_11.itemText(i) == "Icelake-Client (depreciated)":
                if cpu == "Icelake-Client":
                    self.comboBox_11.setCurrentIndex(i)
                    break

            if self.comboBox_11.itemText(i) == cpu:
                self.comboBox_11.setCurrentIndex(i)
                break

            i += 1

    def machineCpuPpc(self, machine, cpu):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_14.count():
            if letQemuDecideContent.__contains__(self.comboBox_14.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_14.setCurrentIndex(i)
                    break

            elif self.comboBox_14.itemText(i) == machine:
                self.comboBox_14.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_13.count():
            if letQemuDecideContent.__contains__(self.comboBox_13.itemText(i)):
                if cpu == "Let QEMU decide":
                    self.comboBox_13.setCurrentIndex(i)
                    break

            if self.comboBox_13.itemText(i) == cpu:
                self.comboBox_13.setCurrentIndex(i)
                break

            i += 1

    def machineCpuMips64el(self, machine, cpu):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_16.count():
            if letQemuDecideContent.__contains__(self.comboBox_16.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_16.setCurrentIndex(i)
                    break

            elif self.comboBox_16.itemText(i) == machine:
                self.comboBox_16.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_15.count():
            if letQemuDecideContent.__contains__(self.comboBox_15.itemText(i)):
                if cpu == "Let QEMU decide":
                    self.comboBox_15.setCurrentIndex(i)
                    break

            elif self.comboBox_15.itemText(i) == cpu:
                self.comboBox_15.setCurrentIndex(i)
                break

            i += 1

    def machineCpuAarch64(self, machine, cpu):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_17.count():
            if letQemuDecideContent.__contains__(self.comboBox_17.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_17.setCurrentIndex(i)
                    break

            elif self.comboBox_17.itemText(i) == machine:
                self.comboBox_17.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_18.count():
            if letQemuDecideContent.__contains__(self.comboBox_18.itemText(i)):
                if cpu == "Let QEMU decide":
                    self.comboBox_18.setCurrentIndex(i)
                    break

            elif self.comboBox_18.itemText(i) == cpu:
                self.comboBox_18.setCurrentIndex(i)
                break

            i += 1

    def machineSparc(self, machine):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_20.count():
            if letQemuDecideContent.__contains__(self.comboBox_20.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_20.setCurrentIndex(i)
                    break

            elif self.comboBox_20.itemText(i) == machine:
                self.comboBox_20.setCurrentIndex(i)
                break

            i += 1

    def machineSparc64(self, machine):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        i = 0

        while i < self.comboBox_21.count():
            if letQemuDecideContent.__contains__(self.comboBox_21.itemText(i)):
                if machine == "Let QEMU decide":
                    self.comboBox_21.setCurrentIndex(i)
                    break

            elif self.comboBox_21.itemText(i) == machine:
                self.comboBox_21.setCurrentIndex(i)
                break

            i += 1

    def vhdAddingChange(self):
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        with open("translations/addnovhd.txt", "r+", encoding="utf8") as noVhdFile:
            noVhdContent = noVhdFile.read()

        if creNewVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)

            # For new
            self.comboBox_3.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.comboBox_4.setEnabled(True)

        elif addExistVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)

            # For new
            self.comboBox_3.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.comboBox_4.setEnabled(False)

        elif noVhdContent.__contains__(self.comboBox_18.currentText()):
            # For new and existing
            self.lineEdit_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)

            # For new
            self.comboBox_3.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.comboBox_4.setEnabled(False)

    def vhdBrowseLocation(self):
        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Save/Open VHD file', dir='.', filter='Hard disk file (*.img);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def archChanged(self):
        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "amd64":
            self.stackedWidget.setCurrentIndex(0)

        elif self.comboBox.currentText() == "ppc" or self.comboBox.currentText() == "ppc64":
            self.stackedWidget.setCurrentIndex(1)

        elif self.comboBox.currentText() == "mips" or self.comboBox.currentText() == "mipsel":
            self.stackedWidget.setCurrentIndex(2)
        
        elif self.comboBox.currentText() == "mips64" or self.comboBox.currentText() == "mips64el":
            self.stackedWidget.setCurrentIndex(2)

        elif self.comboBox.currentText() == "arm" or self.comboBox.currentText() == "aarch64":
            self.stackedWidget.setCurrentIndex(3)

        elif self.comboBox.currentText() == "sparc":
            self.stackedWidget.setCurrentIndex(4)

        elif self.comboBox.currentText() == "sparc64":
            self.stackedWidget.setCurrentIndex(5)

    def extBiosFileLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select BIOS file', dir='.', filter='BIN files (*.bin);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def linuxKernelBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux kernel', dir='.', filter='All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def readTempVmFile(self):
        with open("translations/createnewvhd.txt", "r+", encoding="utf8") as creNewVhdFile:
            creNewVhdContent = creNewVhdFile.read()

        with open("translations/addexistingvhd.txt", "r+", encoding="utf8") as addExistVhdFile:
            addExistVhdContent = addExistVhdFile.read()

        with open("translations/addnovhd.txt", "r+", encoding="utf8") as noVhdFile:
            noVhdContent = noVhdFile.read()

        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideFile:
            letQemuDecideContent = letQemuDecideFile.read()

        # Searching temporary files
        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

        vmSpecs = []

        with open(tempVmDef, "r+") as tempVmDefFile:
            vmSpecsRaw = tempVmDefFile.readlines()

        for vmSpec in vmSpecsRaw:
            vmSpecNew = vmSpec.replace("\n", "")
            vmSpecs.append(vmSpecNew)

        # Setting VM variables

        self.lineEdit.setText(vmSpecs[0])
        self.setWindowTitle(f"EmuGUI - Edit {vmSpecs[0]}")

        i = 0

        while i < self.comboBox.count():
            if self.comboBox.itemText(i) == vmSpecs[1]:
                self.comboBox.setCurrentIndex(i)
                break

            i += 1

        self.archChanged()

        if vmSpecs[1] == "i386" or vmSpecs[1] == "x86_64":
            self.machineCpuI386Amd64(vmSpecs[2], vmSpecs[3])
            self.spinBox_2.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "mips64el" or vmSpecs[1] == "mipsel" or vmSpecs[1] == "mips64" or vmSpecs[1] == "mips":
            self.machineCpuMips64el(vmSpecs[2], vmSpecs[3])
            self.spinBox_4.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "ppc" or vmSpecs[1] == "ppc64":
            self.machineCpuPpc(vmSpecs[2], vmSpecs[3])
            self.spinBox_3.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "aarch64" or vmSpecs[1] == "arm":
            self.machineCpuAarch64(vmSpecs[2], vmSpecs[3])
            self.spinBox_5.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "sparc":
            self.machineSparc(vmSpecs[2])
            self.spinBox_7.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "sparc64":
            self.machineSparc64(vmSpecs[2])
            self.spinBox_8.setValue(int(vmSpecs[4]))

        if vmSpecs[5] != "NULL":
            self.lineEdit_2.setText(vmSpecs[5])
            i = 0

            while i < self.comboBox_2.count():
                if addExistVhdContent.__contains__(self.comboBox_2.itemText(i)): #self.comboBox_2.itemText(i) == "Add existing virtual hard drive" or self.comboBox_2.itemText(i) == "Existierende virtuelle Festplatte anfügen":
                    self.comboBox_2.setCurrentIndex(i)
                    break

                i += 1

        else:
            i = 0

            while i < self.comboBox_2.count():
                if noVhdContent.__contains__(self.comboBox_2.itemText(i)): #self.comboBox_2.itemText(i) == "Don't add a virtual hard drive" or self.comboBox_2.itemText(i) == "Keine virtuelle Festplatte anfügen":
                    self.comboBox_2.setCurrentIndex(i)
                    break

                i += 1

        self.vhdAddingChange()

        i = 0

        while i < self.comboBox_7.count():
            if vmSpecs[6] == "Let QEMU decide":
                if letQemuDecideContent.__contains__(self.comboBox_7.itemText(i)):
                    self.comboBox_7.setCurrentIndex(i)
                    break

            i += 1

        i = 0

        while i < self.comboBox_8.count():
            if self.comboBox_8.itemText(i) == vmSpecs[7]:
                self.comboBox_8.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[8] == "1":
            self.checkBox_2.setChecked(True)

        self.lineEdit_3.setText(vmSpecs[10])

        if vmSpecs[9] == "1":
            self.checkBox_3.setChecked(True)

        self.lineEdit_8.setText(vmSpecs[11])

        i = 0

        while i < self.comboBox_10.count():
            if self.comboBox_10.itemText(i) == vmSpecs[12]:
                self.comboBox_10.setCurrentIndex(i)
                break

            i += 1

        self.lineEdit_5.setText(vmSpecs[13])
        self.lineEdit_6.setText(vmSpecs[14])
        self.lineEdit_7.setText(vmSpecs[15])

        i = 0

        while i < self.comboBox_5.count():
            if self.comboBox_5.itemText(i) == vmSpecs[16]:
                self.comboBox_5.setCurrentIndex(i)
                break

            i += 1

        self.lineEdit_4.setText(vmSpecs[18])
        self.spinBox_6.setValue(int(vmSpecs[17]))

        i = 0

        while i < self.comboBox_6.count():
            if self.comboBox_6.itemText(i) == vmSpecs[19]:
                self.comboBox_6.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[20] == "1":
            self.checkBox.setChecked(True)

        i = 0

        while i < self.comboBox_9.count():
            if self.comboBox_9.itemText(i) == vmSpecs[21]:
                self.comboBox_9.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[20] == "1":
            self.checkBox.setChecked(True)

        i = 0

        while i < self.comboBox_19.count():
            if self.comboBox_19.itemText(i) == vmSpecs[22]:
                self.comboBox_19.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_22.count():
            if self.comboBox_22.itemText(i) == vmSpecs[23]:
                self.comboBox_22.setCurrentIndex(i)
                break

            i += 1
        
        return vmSpecs

    def finishCreation(self):
        with open("translations/letqemudecide.txt", "r+", encoding="utf8") as letQemuDecideVariants:
            letQemuDecideVariantsStr = letQemuDecideVariants.read()

        with open("translations/systemdefault.txt", "r+", encoding="utf8") as sysDefFile:
            sysDefContent = sysDefFile.read()

        # This applies the changes to your VM.
        
        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "x86_64":
            machine = self.comboBox_12.currentText()
            cpu = self.comboBox_11.currentText()

            if cpu.startswith("Icelake-Client"):
                cpu = "Icelake-Client"

            ram = self.spinBox_2.value()
        
        elif self.comboBox.currentText() == "ppc" or self.comboBox.currentText() == "ppc64":
            machine = self.comboBox_14.currentText()
            cpu = self.comboBox_13.currentText()
            ram = self.spinBox_3.value()

        elif self.comboBox.currentText() == "mips64el" or self.comboBox.currentText() == "mipsel":
            machine = self.comboBox_16.currentText()
            cpu = self.comboBox_15.currentText()
            ram = self.spinBox_4.value()

        elif self.comboBox.currentText() == "mips64" or self.comboBox.currentText() == "mips":
            machine = self.comboBox_16.currentText()
            cpu = self.comboBox_15.currentText()
            ram = self.spinBox_4.value()

        elif self.comboBox.currentText() == "aarch64" or self.comboBox.currentText() == "arm":
            machine = self.comboBox_18.currentText()
            cpu = self.comboBox_17.currentText()
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

        if self.lineEdit_2.text() == "" or self.lineEdit_2.isEnabled() == False:
            vhd = "NULL"
        
        else:
            vhd = self.lineEdit_2.text()

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

            with open(tempVmDef, "r+") as tempVmDefFile:
                vmSpecsRaw = tempVmDefFile.readlines()

            vhdAction = vmSpecsRaw[0]

            if self.comboBox_3.isEnabled():
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

                if self.comboBox_4.currentText().startswith("K"):
                    vhd_size_in_b = self.spinBox.value() * 1024

                elif self.comboBox_4.currentText().startswith("M"):
                    vhd_size_in_b = self.spinBox.value() * 1024 * 1024

                elif self.comboBox_4.currentText().startswith("G"):
                    vhd_size_in_b = self.spinBox.value() * 1024 * 1024 * 1024

                print(vhd_size_in_b)

                if platform.system() == "Windows":
                    vhd_cmd = f"{qemu_binary} create -f {self.comboBox_3.currentText()} \"{vhd}\" {str(vhd_size_in_b)}"

                else:
                    vhd_cmd = f"{qemu_binary} create -f {self.comboBox_3.currentText()} {vhd} {str(vhd_size_in_b)}"

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

                    print("The query was executed and the virtual disk created successfully.")
                
                except:
                    print("The virtual disk could not be created. Please check if the path and the QEMU settings are correct.")

        if letQemuDecideVariantsStr.__contains__(self.comboBox_7.currentText()):
            vga = "Let QEMU decide"
        
        else:
            vga = self.comboBox_7.currentText()

        if self.comboBox_8.currentText() == "none":
            networkAdapter = "none"
        
        else:
            networkAdapter = self.comboBox_8.currentText()

        if self.checkBox_2.isChecked():
            usbtablet = 1

        else:
            usbtablet = 0

        if self.checkBox_3.isChecked():
            win2k = 1

        else:
            win2k = 0

        ext_bios_dir = self.lineEdit_3.text()

        add_args = self.lineEdit_8.text()

        if self.checkBox_2.isChecked() or self.checkBox.isChecked() or self.comboBox_5.currentText() == "USB Mouse":
            usb_support = 1

        elif self.comboBox_5.currentText() == "USB Tablet Device" or self.comboBox_6.currentText() == "USB Keyboard":
            usb_support = 1

        else:
            usb_support = 0

        if sysDefContent.__contains__(self.comboBox_19.currentText()):
            kbdlayout = "en-us"

        else:
            kbdlayout = self.comboBox_19.currentText()
        
        insert_into_vm_database = f"""
        UPDATE virtualmachines
        SET name = "{self.lineEdit.text()}", architecture = "{self.comboBox.currentText()}", machine = "{machine}", cpu = "{cpu}",
        ram = {ram}, hda = "{vhd}", vga = "{vga}", net = "{networkAdapter}", usbtablet = {usbtablet},
        win2k = {win2k}, dirbios = "{ext_bios_dir}", additionalargs = "{add_args}", sound = "{self.comboBox_10.currentText()}",
        linuxkernel = "{self.lineEdit_5.text()}", linuxinitrid = "{self.lineEdit_6.text()}", linuxcmd = "{self.lineEdit_7.text()}",
        mousetype = "{self.comboBox_5.currentText()}", cores = {self.spinBox_6.value()}, filebios = "{self.lineEdit_4.text()}",
        keyboardtype = "{self.comboBox_6.currentText()}", usbsupport = {usb_support}, usbcontroller = "{self.comboBox_9.currentText()}",
        kbdtype = "{kbdlayout}", acceltype = "{self.comboBox_22.currentText()}"
        WHERE name = "{self.vmSpecs[0]}";
        """

        cursor = connection.cursor()

        try:
            cursor.execute(insert_into_vm_database)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        self.close()