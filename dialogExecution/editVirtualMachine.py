from PySide6.QtWidgets import *
from uiScripts.ui_NewVM import Ui_Dialog
import sqlite3
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import subprocess
from dialogExecution.vhdExistsDialog import VhdAlreadyExists
from dialogExecution.vmExistsDialog import VmAlreadyExistsDialog

class EditVirtualMachineDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.vmSpecs = self.readTempVmFile()
        self.setWindowTitle(f"EmuGUI - Edit {self.vmSpecs[0]}")

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

        self.lineEdit.setText(vmSpecs[0])

        if vmSpecs[1] == "i386":
            self.comboBox.setCurrentIndex(0)
            self.machineCpuI386Amd64(vmSpecs[2], vmSpecs[3])
            self.spinBox.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "x86_64":
            self.comboBox.setCurrentIndex(1)
            self.machineCpuI386Amd64(vmSpecs[2], vmSpecs[3])
            self.spinBox.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "mips64el":
            self.comboBox.setCurrentIndex(2)
            self.machineCpuMips64el(vmSpecs[2], vmSpecs[3])
            self.spinBox_3.setValue(int(vmSpecs[4]))

        elif vmSpecs[1] == "ppc":
            self.comboBox.setCurrentIndex(3)
            self.machineCpuPpc(vmSpecs[2], vmSpecs[3])
            self.spinBox_2.setValue(int(vmSpecs[4]))

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

        return vmSpecs

    def archSystem(self):
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
        
                    elif self.comboBox.currentText() == "ppc":
                        self.stackedWidget.setCurrentIndex(2)

                    elif self.comboBox.currentText() == "mips64el":
                        self.stackedWidget.setCurrentIndex(3)

            except:
                if self.comboBox.currentText() == "i386":
                    self.stackedWidget.setCurrentIndex(1)

                elif self.comboBox.currentText() == "x86_64":
                    self.stackedWidget.setCurrentIndex(1)
        
                elif self.comboBox.currentText() == "ppc":
                    self.stackedWidget.setCurrentIndex(2)

                elif self.comboBox.currentText() == "mips64el":
                    self.stackedWidget.setCurrentIndex(3)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def vhdMenu(self):
        self.stackedWidget.setCurrentIndex(4)

    def vhdBrowseLocation(self):
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
        self.stackedWidget.setCurrentIndex(5)

    def extBios(self):
        self.stackedWidget.setCurrentIndex(6)

    def soundCard(self):
        self.stackedWidget.setCurrentIndex(7)

    def linuxVMSpecific(self):
        self.stackedWidget.setCurrentIndex(8)

    def linuxKernelBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux kernel', dir='.', filter='All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def linuxInitridBrowseLocation(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select Linux initrid image', dir='.', filter='IMG files (*.img);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def win2kHacker(self):
        self.stackedWidget.setCurrentIndex(9)

    def finishCreation(self):
        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "x86_64":
            machine = self.comboBox_2.currentText()
            cpu = self.comboBox_3.currentText()
            ram = self.spinBox.value()
        
        elif self.comboBox.currentText() == "ppc":
            machine = self.comboBox_4.currentText()
            cpu = self.comboBox_5.currentText()
            ram = self.spinBox_2.value()

        elif self.comboBox.currentText() == "mips64el":
            machine = self.comboBox_6.currentText()
            cpu = self.comboBox_7.currentText()
            ram = self.spinBox_3.value()

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

                if vhdAction.startswith("overwrite"):
                    subprocess.Popen(f"{qemu_binary} create -f {self.comboBox_8.currentText()} \"{vhd}\" {str(vhd_size_in_b)}")

                print("The query was executed and the virtual disk created successfully.")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                print(f"The query was executed successfully, but the virtual disk couldn't be created.")

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
        
        insert_into_vm_database = f"""
        UPDATE virtualmachines
        SET name = "{self.lineEdit.text()}", architecture = "{self.comboBox.currentText()}", machine = "{machine}", cpu = "{cpu}",
        ram = {ram}, hda = "{vhd}", vga = "{self.comboBox_10.currentText()}", net = "{networkAdapter}", usbtablet = {usbtablet},
        win2k = {win2k}, dirbios = "{ext_bios_dir}", additionalargs = "{add_args}", sound = "{self.comboBox_12.currentText()}",
        linuxkernel = "{self.lineEdit_4.text()}", linuxinitrid = "{self.lineEdit_5.text()}", linuxcmd = "{self.lineEdit_7.text()}"
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