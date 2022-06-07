# Importing required modules (PySide 6, platform, sqlite3, subprocess, internal program files)
from PySide6.QtWidgets import *
from uiScripts.ui_StartVM import Ui_Dialog
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import sqlite3
import subprocess
from PySide6.QtCore import QDateTime

class StartVirtualMachineDialog(QDialog, Ui_Dialog):
    # Initializing VM starting
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.vmSpecs = self.readTempVmFile()
        print(self.vmSpecs)

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.set_fda_path)
        self.pushButton_2.clicked.connect(self.set_cdrom_path)
        self.pushButton_3.clicked.connect(self.start_virtual_machine)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.set_date_to_system)

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

        return vmSpecs

    def set_fda_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select floppy disk', dir='.', filter='Floppy image (*.img);;Floppy file (*.flp);;Floppy image (*.ima);;All files (*.*)')

        if filename:
            self.lineEdit.setText(filename)

    def set_cdrom_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select cdrom file', dir='.', filter='ISO image (*.iso);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_date_to_system(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def start_virtual_machine(self):
        qemu_i386_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-i386';
        """

        qemu_x86_64_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-x86_64';
        """

        qemu_ppc_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-ppc';
        """

        qemu_mips64el_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-mips64el';
        """

        connection = self.connection
        cursor = connection.cursor()

        fda_file = self.lineEdit.text()
        cdrom_file = self.lineEdit_2.text()
        bootfrom = self.comboBox.currentText()
        dateTimeForVM = self.dateTimeEdit.text()

        print(fda_file)
        print(cdrom_file)
        print(bootfrom)
        print(dateTimeForVM)

        try:
            if self.vmSpecs[0] == "i386":
                cursor.execute(qemu_i386_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[0] == "x86_64":
                cursor.execute(qemu_x86_64_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[0] == "ppc":
                cursor.execute(qemu_ppc_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)
            
            elif self.vmSpecs[0] == "mips64el":
                cursor.execute(qemu_mips64el_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            qemu_to_execute = result[0][0]
            qemu_cmd = f"{qemu_to_execute} -m {self.vmSpecs[3]} -hda \"{self.vmSpecs[4]}\" -rtc base=\"{dateTimeForVM}\",clock=vm"

            if self.vmSpecs[1] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -M {self.vmSpecs[1]}"

            if self.vmSpecs[2] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -cpu {self.vmSpecs[2]}"

            if self.vmSpecs[5] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -vga {self.vmSpecs[5]}"

            if self.vmSpecs[6] != "none":
                if self.vmSpecs[0] == "i386" or self.vmSpecs[0] == "x86_64":
                    qemu_cmd = qemu_cmd + f" -net nic,model={self.vmSpecs[6]} -net user"

                elif self.vmSpecs[0] == "mips64el":
                    qemu_cmd = qemu_cmd + f" -nic user,model={self.vmSpecs[6]}"
            
            if self.vmSpecs[7] == "1":
                qemu_cmd = qemu_cmd + " -usbdevice tablet"

            if self.vmSpecs[8] == "1" and self.vmSpecs[0] == "i386":
                qemu_cmd = qemu_cmd + " -win2k-hack"

            if fda_file != "":
                qemu_cmd = qemu_cmd + f" -fda \"{fda_file}\""

            if cdrom_file != "":
                qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file}\""

            if bootfrom == "c" or bootfrom == "a" and fda_file == "" or bootfrom == "d" and cdrom_file == "":
                qemu_cmd = qemu_cmd + " -boot c"

            elif bootfrom == "a" and fda_file != "":
                qemu_cmd = qemu_cmd + " -boot a"
            
            elif bootfrom == "d" and cdrom_file != "":
                qemu_cmd = qemu_cmd + " -boot d"

            if self.vmSpecs[9] != "":
                qemu_cmd = qemu_cmd + f" -L \"{self.vmSpecs[9]}\""

            if self.vmSpecs[10] != "":
                qemu_cmd = qemu_cmd + f" {self.vmSpecs[10]}"
            
            subprocess.Popen(qemu_cmd)

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
        
        except:
            print("Qemu couldn't be executed. Please check the settings.")
        
        self.close()