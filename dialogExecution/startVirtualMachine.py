# Importing required modules (PySide 6, platform, sqlite3, subprocess, internal program files)
from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_StartVM import Ui_Dialog
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import sqlite3
import subprocess
from PySide6.QtCore import QDateTime
from random import randint
import magic
import translations.de
import translations.uk
import translations.en
import locale

class StartVirtualMachineDialog(QDialog, Ui_Dialog):
    # Initializing VM starting
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.langDetect()
        self.vmSpecs = self.readTempVmFile()
        print(self.vmSpecs)
        self.setWindowTitle(f"EmuGUI - Start {self.vmSpecs[0]}")
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()

    def connectSignalsSlots(self):
        # This code connects the buttons to their functions
        self.pushButton.clicked.connect(self.set_fda_path)
        self.pushButton_2.clicked.connect(self.set_cdrom_path)
        self.pushButton_3.clicked.connect(self.start_virtual_machine)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.set_date_to_system)

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
            translations.de.translateStartVmDE(self)

        elif languageToUse.startswith("uk"):
            translations.uk.translateStartVmUK(self)

        else:
            translations.en.translateStartVmEN(self)

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

    # These are asked every time you want to run the VMs.

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

    # Here, it chooses the architecture for your VM and starts the right thing.

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

        qemu_ppc64_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-ppc64';
        """

        qemu_mips64el_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-mips64el';
        """

        qemu_mipsel_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-mipsel';
        """

        qemu_aarch64_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-aarch64';
        """

        qemu_arm_bin = """
        SELECT value FROM settings
        WHERE name = 'qemu-system-arm';
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

        qemu_cmd = ""

        try:
            if self.vmSpecs[1] == "i386":
                cursor.execute(qemu_i386_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "x86_64":
                cursor.execute(qemu_x86_64_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "ppc":
                cursor.execute(qemu_ppc_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "ppc64":
                cursor.execute(qemu_ppc64_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)
            
            elif self.vmSpecs[1] == "mips64el":
                cursor.execute(qemu_mips64el_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "mipsel":
                cursor.execute(qemu_mipsel_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "aarch64":
                cursor.execute(qemu_aarch64_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            elif self.vmSpecs[1] == "arm":
                cursor.execute(qemu_arm_bin)
                connection.commit()
                result = cursor.fetchall()

                print(result)

            qemu_to_execute = result[0][0]

            if platform.system() == "Windows":
                qemu_cmd = f"{qemu_to_execute} -m {self.vmSpecs[4]} -rtc base=\"{dateTimeForVM}\",clock=vm -smp {self.vmSpecs[17]}"

            else:
                qemu_cmd = f"{qemu_to_execute} -m {self.vmSpecs[4]} -rtc base={dateTimeForVM},clock=vm -smp {self.vmSpecs[17]}"

            if magic.from_file(self.vmSpecs[5]) == "block special":
                if platform.system() == "Windows":
                    qemu_cmd = qemu_cmd + f" -drive format=raw,file=\"{self.vmSpecs[5]}\""
                
                else:
                    qemu_cmd = qemu_cmd + f" -drive format=raw,file={self.vmSpecs[5]}"

            else:
                if platform.system() == "Windows":
                    qemu_cmd = qemu_cmd + f" -hda \"{self.vmSpecs[5]}\""

                else:
                    qemu_cmd = qemu_cmd + f" -hda {self.vmSpecs[5]}"

            if self.vmSpecs[2] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -M {self.vmSpecs[2]}"

            if self.vmSpecs[3] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -cpu {self.vmSpecs[3]}"

            if self.vmSpecs[6] != "Let QEMU decide":
                if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    if self.vmSpecs[6] == "std":
                        qemu_cmd = qemu_cmd + f" -device VGA -display gtk"
                    
                    else:
                        qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[6]} -display gtk"

                else:
                    qemu_cmd = qemu_cmd + f" -vga {self.vmSpecs[6]}"

            if self.vmSpecs[7] != "none":
                if self.vmSpecs[1] == "i386" or self.vmSpecs[1] == "x86_64" or self.vmSpecs[1] == "ppc" or self.vmSpecs[1] == "ppc64":
                    qemu_cmd = qemu_cmd + f" -net nic,model={self.vmSpecs[7]} -net user"

                elif self.vmSpecs[1] == "mips64el" or self.vmSpecs[1] == "mipsel":
                    qemu_cmd = qemu_cmd + f" -nic user,model={self.vmSpecs[7]}"

                elif self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    # Due to the circumstances here, for the VM, a random MAC address is
                    # generated at runtime. Due to that, the MAC changes every time you
                    # start your virtual machine.

                    mac_gen = []
                    i = 0

                    while i < 6:
                        firstLetter = randint(0, 15)
                        secondLetter = randint(0, 15)

                        if firstLetter == 0:
                            firstLetter = "0"

                        elif firstLetter == 1:
                            firstLetter = "1"

                        elif firstLetter == 2:
                            firstLetter = "2"

                        elif firstLetter == 3:
                            firstLetter = "3"

                        elif firstLetter == 4:
                            firstLetter = "4"

                        elif firstLetter == 5:
                            firstLetter = "5"

                        elif firstLetter == 6:
                            firstLetter = "6"

                        elif firstLetter == 7:
                            firstLetter = "7"

                        elif firstLetter == 8:
                            firstLetter = "8"

                        elif firstLetter == 9:
                            firstLetter = "9"

                        elif firstLetter == 10:
                            firstLetter = "a"

                        elif firstLetter == 11:
                            firstLetter = "b"

                        elif firstLetter == 12:
                            firstLetter = "c"

                        elif firstLetter == 13:
                            firstLetter = "d"

                        elif firstLetter == 14:
                            firstLetter = "e"

                        elif firstLetter == 15:
                            firstLetter = "f"

                        if secondLetter == 0:
                            secondLetter = "0"

                        elif secondLetter == 1:
                            secondLetter = "1"

                        elif secondLetter == 2:
                            secondLetter = "2"

                        elif secondLetter == 3:
                            secondLetter = "3"

                        elif secondLetter == 4:
                            secondLetter = "4"

                        elif secondLetter == 5:
                            secondLetter = "5"

                        elif secondLetter == 6:
                            secondLetter = "6"

                        elif secondLetter == 7:
                            secondLetter = "7"

                        elif secondLetter == 8:
                            secondLetter = "8"

                        elif secondLetter == 9:
                            secondLetter = "9"

                        elif secondLetter == 10:
                            secondLetter = "a"

                        elif secondLetter == 11:
                            secondLetter = "b"

                        elif secondLetter == 12:
                            secondLetter = "c"

                        elif secondLetter == 13:
                            secondLetter = "d"

                        elif secondLetter == 14:
                            secondLetter = "e"

                        elif secondLetter == 15:
                            secondLetter = "f"

                        mac_part = firstLetter + secondLetter
                        mac_gen.append(mac_part)
                        i += 1

                    mac_to_use = f"{mac_gen[0]}:{mac_gen[1]}:{mac_gen[2]}:{mac_gen[3]}:{mac_gen[4]}:{mac_gen[5]}"
                    qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[7]},netdev=hostnet0,mac={mac_to_use} -netdev user,id=hostnet0"

            if self.vmSpecs[20] == "1":
                qemu_cmd = qemu_cmd + f" -usb -device {self.vmSpecs[21]}"
            
            if self.vmSpecs[7] == "1":
                print("WARNING: Using the checkbox for the USB tablet is depreciated.")
                print("This feature is going to be removed in a future update.")
                print("Please use the combo box for this task instead.")
                qemu_cmd = qemu_cmd + " -usbdevice tablet"

            if self.vmSpecs[8] == "1" and self.vmSpecs[0] == "i386":
                qemu_cmd = qemu_cmd + " -win2k-hack"

            if fda_file != "":
                if platform.system() == "Windows":
                    qemu_cmd = qemu_cmd + f" -drive format=raw,file=\"{fda_file}\",index=0,if=floppy"

                else:
                    qemu_cmd = qemu_cmd + f" -drive format=raw,file={fda_file},index=0,if=floppy"

            if cdrom_file != "":
                if platform.system() == "Windows":
                    qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file}\""

                else:
                    qemu_cmd = qemu_cmd + f" -cdrom {cdrom_file}"

            if bootfrom == "c" or bootfrom == "a" and fda_file == "" or bootfrom == "d" and cdrom_file == "":
                qemu_cmd = qemu_cmd + " -boot c"

            elif bootfrom == "a" and fda_file != "":
                qemu_cmd = qemu_cmd + " -boot a"
            
            elif bootfrom == "d" and cdrom_file != "":
                qemu_cmd = qemu_cmd + " -boot d"

            if self.vmSpecs[10] != "":
                qemu_cmd = qemu_cmd + f" -L {self.vmSpecs[10]}"

            if self.vmSpecs[12] != "none":
                qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[12]}"

                if self.vmSpecs[12] == "intel-hda":
                    qemu_cmd = qemu_cmd + " -device hda-duplex"

            if self.vmSpecs[13] != "":
                qemu_cmd = qemu_cmd + f" -kernel \"{self.vmSpecs[13]}\""

            if self.vmSpecs[14] != "":
                qemu_cmd = qemu_cmd + f" -initrd \"{self.vmSpecs[14]}\""

            if self.vmSpecs[15] != "":
                qemu_cmd = qemu_cmd + f" -append \"{self.vmSpecs[15]}\""

            if self.vmSpecs[16] == "USB Mouse" and self.vmSpecs[7] == "0":
                if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    qemu_cmd = qemu_cmd + " -device usb-mouse"

                else:
                    qemu_cmd = qemu_cmd + " -usbdevice mouse"

            if self.vmSpecs[16] == "USB Tablet Device" and self.vmSpecs[7] == "0":
                if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    qemu_cmd = qemu_cmd + " -device usb-tablet"

                else:
                    qemu_cmd = qemu_cmd + " -usbdevice tablet"

            if self.vmSpecs[18] != "" and self.vmSpecs[18] != None and self.vmSpecs[18] != "None":
                qemu_cmd = qemu_cmd + f" -bios \"{self.vmSpecs[18]}\""

            if self.vmSpecs[19] == "USB Keyboard":
                qemu_cmd = qemu_cmd + " -device usb-kbd"

            if self.vmSpecs[11] != "":
                qemu_cmd = qemu_cmd + f" {self.vmSpecs[11]}"
            
            subprocess.Popen(qemu_cmd)

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
        
        except:
            print("Qemu couldn't be executed. Trying subprocess.run")

            try:
                qemu_cmd_split = qemu_cmd.split(" ")
                subprocess.run(qemu_cmd_split)
            
            except:
                print("Qemu couldn't be executed. Please check if the settings of your VM and/or the QEMU paths are correct.")
        
        self.close()