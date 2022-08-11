from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_NewVM import Ui_Dialog
import sqlite3
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import subprocess
from dialogExecution.vhdExistsDialog import VhdAlreadyExists
from dialogExecution.vmExistsDialog import VmAlreadyExistsDialog
import translations.de
import translations.uk
import translations.en
import locale

class EditVirtualMachineDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        # This is preparing the dialog required.
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.langDetect()
        self.vmSpecs = self.readTempVmFile()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

        with open(tempVmDef, "w+") as tempVmDefFile:
            tempVmDefFile.write("keep")

        self.firstStage()

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

        # Page 3 (VHD creation)
        self.pushButton_13.clicked.connect(self.vhdBrowseLocation)
        self.pushButton_16.clicked.connect(self.archSystem)
        self.pushButton_14.clicked.connect(self.vgaNetworkMenu)
        self.pushButton_15.clicked.connect(self.close)

        # Page 4 (VGA and network)
        self.pushButton_18.clicked.connect(self.vhdMenu)
        self.pushButton_19.clicked.connect(self.close)
        self.pushButton_17.clicked.connect(self.extBios)

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
        self.pushButton_30.clicked.connect(self.win2kHacker)

        # Page 8 (Additional arguments)
        self.pushButton_22.clicked.connect(self.linuxVMSpecific)
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

        if languageToUse.startswith("de"):
            translations.de.translateNewVmDE(self)

        elif languageToUse.startswith("uk"):
            translations.uk.translateNewVmUK(self)

        else:
            translations.en.translateNewVmEN(self)

    # First, it will check the architecture of your VM.

    def machineCpuI386Amd64(self, machine, cpu):
        i = 0

        while i < self.comboBox_2.count():
            if self.comboBox_2.itemText(i) == machine:
                self.comboBox_2.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_3.count():
            if self.comboBox_3.itemText(i) == cpu:
                self.comboBox_3.setCurrentIndex(i)
                break

            i += 1

    def machineCpuPpc(self, machine, cpu):
        i = 0

        while i < self.comboBox_4.count():
            if self.comboBox_4.itemText(i) == machine:
                self.comboBox_4.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_5.count():
            if self.comboBox_5.itemText(i) == cpu:
                self.comboBox_5.setCurrentIndex(i)
                break

            i += 1

    def machineCpuMips64el(self, machine, cpu):
        i = 0

        while i < self.comboBox_6.count():
            if self.comboBox_6.itemText(i) == machine:
                self.comboBox_6.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_7.count():
            if self.comboBox_7.itemText(i) == cpu:
                self.comboBox_7.setCurrentIndex(i)
                break

            i += 1

    def machineCpuAarch64(self, machine, cpu):
        i = 0

        while i < self.comboBox_14.count():
            if self.comboBox_14.itemText(i) == machine:
                self.comboBox_14.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_15.count():
            if self.comboBox_15.itemText(i) == cpu:
                self.comboBox_15.setCurrentIndex(i)
                break

            i += 1

    def readTempVmFile(self):
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

        if vmSpecs[1] == "i386" or vmSpecs[1] == "x86_64":
            self.machineCpuI386Amd64(vmSpecs[2], vmSpecs[3])
            self.spinBox.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "mips64el" or vmSpecs[1] == "mipsel":
            self.machineCpuMips64el(vmSpecs[2], vmSpecs[3])
            self.spinBox_3.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "ppc" or vmSpecs[1] == "ppc64":
            self.machineCpuPpc(vmSpecs[2], vmSpecs[3])
            self.spinBox_2.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "aarch64" or vmSpecs[1] == "arm":
            self.machineCpuAarch64(vmSpecs[2], vmSpecs[3])
            self.spinBox_5.setValue(int(vmSpecs[4]))

        self.lineEdit_6.setText(vmSpecs[5])

        i = 0

        while i < self.comboBox_10.count():
            if self.comboBox_10.itemText(i) == vmSpecs[6]:
                self.comboBox_10.setCurrentIndex(i)
                break

            i += 1

        i = 0

        while i < self.comboBox_11.count():
            if self.comboBox_11.itemText(i) == vmSpecs[7]:
                self.comboBox_11.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[8] == "1":
            self.checkBox.setChecked(True)

        self.lineEdit_3.setText(vmSpecs[10])

        if vmSpecs[9] == "1":
            self.checkBox_2.setChecked(True)

        self.lineEdit_2.setText(vmSpecs[11])

        i = 0

        while i < self.comboBox_12.count():
            if self.comboBox_12.itemText(i) == vmSpecs[12]:
                self.comboBox_12.setCurrentIndex(i)
                break

            i += 1

        self.lineEdit_4.setText(vmSpecs[13])
        self.lineEdit_5.setText(vmSpecs[14])
        self.lineEdit_7.setText(vmSpecs[15])

        i = 0

        while i < self.comboBox_13.count():
            if self.comboBox_13.itemText(i) == vmSpecs[16]:
                self.comboBox_13.setCurrentIndex(i)
                break

            i += 1

        self.lineEdit_8.setText(vmSpecs[18])
        self.spinBox_6.setValue(int(vmSpecs[17]))

        i = 0

        while i < self.comboBox_16.count():
            if self.comboBox_16.itemText(i) == vmSpecs[19]:
                self.comboBox_16.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[20] == "1":
            self.checkBox_3.setChecked(True)

        i = 0

        while i < self.comboBox_17.count():
            if self.comboBox_17.itemText(i) == vmSpecs[21]:
                self.comboBox_17.setCurrentIndex(i)
                break

            i += 1

        if vmSpecs[20] == "1":
            self.checkBox_3.setChecked(True)

        return vmSpecs

    def archSystem(self):
        # It checks name and architecture.

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

                if self.lineEdit.text() != self.vmSpecs[0]:
                    dialog2 = VmAlreadyExistsDialog(self)
                    dialog2.exec()

                else:
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
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def vhdMenu(self):
        self.stackedWidget.setCurrentIndex(5)

    def vhdBrowseLocation(self):
        # This code lets you browse the VHD location.

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Save VHD file', dir='.', filter='Hard disk file (*.img);;VirtualBox disk image (*.vdi);;VMware disk file (*.vmdk);;Virtual hard disk file with extra features (*.vhdx);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)
            
            try:
                file = open(filename, "r")
                file.close()
                dialog = VhdAlreadyExists(self)
                dialog.exec()
            
            except:
                pass

    def firstStage(self):
        self.stackedWidget.setCurrentIndex(0)

    def vgaNetworkMenu(self):
        self.stackedWidget.setCurrentIndex(6)

    def extBios(self):
        self.stackedWidget.setCurrentIndex(7)

    def extBiosFileLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select BIOS file', dir='.', filter='BIN files (*.bin);;All files (*.*)')

        if filename:
            self.lineEdit_8.setText(filename)

    def soundCard(self):
        self.stackedWidget.setCurrentIndex(8)

    def linuxVMSpecific(self):
        self.stackedWidget.setCurrentIndex(9)

    def linuxKernelBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux kernel', dir='.', filter='All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def win2kHacker(self):
        self.stackedWidget.setCurrentIndex(10)

    def finishCreation(self):
        # This applies the changes to your VM.
        
        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "x86_64":
            machine = self.comboBox_2.currentText()
            cpu = self.comboBox_3.currentText()
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

        if self.lineEdit_6.text() == "":
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

                    print("The query was executed and the virtual disk created successfully.")
                
                except:
                    print("The virtual disk could not be created. Please check if the path and the QEMU settings are correct.")

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
        
        insert_into_vm_database = f"""
        UPDATE virtualmachines
        SET name = "{self.lineEdit.text()}", architecture = "{self.comboBox.currentText()}", machine = "{machine}", cpu = "{cpu}",
        ram = {ram}, hda = "{vhd}", vga = "{self.comboBox_10.currentText()}", net = "{networkAdapter}", usbtablet = {usbtablet},
        win2k = {win2k}, dirbios = "{ext_bios_dir}", additionalargs = "{add_args}", sound = "{self.comboBox_12.currentText()}",
        linuxkernel = "{self.lineEdit_4.text()}", linuxinitrid = "{self.lineEdit_5.text()}", linuxcmd = "{self.lineEdit_7.text()}",
        mousetype = "{self.comboBox_13.currentText()}", cores = {self.spinBox_6.value()}, filebios = "{self.lineEdit_8.text()}",
        keyboardtype = "{self.comboBox_16.currentText()}", usbsupport = {usb_support}, usbcontroller = "{self.comboBox_17.currentText()}"
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