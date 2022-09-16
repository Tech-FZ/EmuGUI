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

class EditVMNewDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.langDetect()
        self.vmSpecs = self.readTempVmFile()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close())

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

        elif vmSpecs[1] == "mips64el" or vmSpecs[1] == "mipsel" or vmSpecs[1] == "mips64" or vmSpecs[1] == "mips":
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
            if self.comboBox_10.itemText(i) == "Let QEMU decide" or self.comboBox_10.itemText(i) == "QEMU überlassen":
                if vmSpecs[6] == "Let QEMU decide":
                    self.comboBox_10.setCurrentIndex(i)
                    break

            elif self.comboBox_10.itemText(i) == vmSpecs[6]:
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

    def finishCreation(self):
        # This applies the changes to your VM.
        
        if platform.system() == "Windows":
            connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            connection = platformSpecific.unixSpecific.setupUnixBackend()

        cursor = connection.cursor()

        if self.comboBox.currentText() == "i386" or self.comboBox.currentText() == "x86_64":
            machine = self.comboBox_12.currentText()
            cpu = self.comboBox_11.currentText()
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

        if machine == "Let QEMU decide" or machine == "QEMU überlassen":
            machine = "Let QEMU decide"

        if cpu == "Let QEMU decide" or cpu == "QEMU überlassen":
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

        if self.comboBox_7.currentText() == "Let QEMU decide" or self.comboBox_7.currentText() == "QEMU überlassen":
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
        
        insert_into_vm_database = f"""
        UPDATE virtualmachines
        SET name = "{self.lineEdit.text()}", architecture = "{self.comboBox.currentText()}", machine = "{machine}", cpu = "{cpu}",
        ram = {ram}, hda = "{vhd}", vga = "{vga}", net = "{networkAdapter}", usbtablet = {usbtablet},
        win2k = {win2k}, dirbios = "{ext_bios_dir}", additionalargs = "{add_args}", sound = "{self.comboBox_10.currentText()}",
        linuxkernel = "{self.lineEdit_5.text()}", linuxinitrid = "{self.lineEdit_6.text()}", linuxcmd = "{self.lineEdit_7.text()}",
        mousetype = "{self.comboBox_5.currentText()}", cores = {self.spinBox_6.value()}, filebios = "{self.lineEdit_4.text()}",
        keyboardtype = "{self.comboBox_6.currentText()}", usbsupport = {usb_support}, usbcontroller = "{self.comboBox_9.currentText()}"
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