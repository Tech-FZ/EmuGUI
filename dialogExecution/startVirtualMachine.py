# Importing required modules (PySide 6, platform, sqlite3, subprocess, internal program files)
from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_StartVM import Ui_Dialog
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific
    import shlex
    
import sqlite3
import subprocess
from PySide6.QtCore import QDateTime
from random import randint
import magic
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
import errors.errCodes
from dialogExecution.errDialog import ErrDialog

class StartVirtualMachineDialog(QDialog, Ui_Dialog):
    # Initializing VM starting
    def __init__(self, parent=None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        self.connectSignalsSlots()
        
        self.architectures = [
            "i386", "x86_64", "ppc", "ppc64", "mips64", "mips64el",
            "mipsel", "mips", "aarch64", "arm", "sparc", "sparc64"
        ]

        try:
            self.vmSpecs = self.readTempVmFile()

        except:
            if platform.system() == "Windows":
                errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
            else:
                errorFile = platformSpecific.unixSpecific.unixErrorFile()

            with open(errorFile, "w+") as errCodeFile:
                errCodeFile.write(errors.errCodes.errCodes[13])

            dialog = ErrDialog(self)
            dialog.exec()

        print(self.vmSpecs)
        self.setWindowTitle(f"EmuGUI - Start {self.vmSpecs[0]}")
        self.langDetect()
        self.timeUsageTrigger()
        
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
        self.pushButton_6.clicked.connect(self.set_cdrom2_path)
        self.pushButton_3.clicked.connect(self.start_virtual_machine)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.set_date_to_system)
        self.checkBox.clicked.connect(self.timeUsageTrigger)

    def timeUsageTrigger(self):
        if self.checkBox.isChecked():
            self.dateTimeEdit.setEnabled(True)
            self.pushButton_5.setEnabled(True)

        else:
            self.dateTimeEdit.setEnabled(False)
            self.pushButton_5.setEnabled(False)

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

        if languageToUse != None:
            if languageToUse.startswith("de"):
                translations.de.translateStartVmDE(self, self.vmSpecs[0])

            elif languageToUse.startswith("uk"):
                translations.uk.translateStartVmUK(self, self.vmSpecs[0])

            elif languageToUse.startswith("fr"):
                translations.fr.translateStartVmFR(self, self.vmSpecs[0])

            elif languageToUse.startswith("es"):
                translations.es.translateStartVmES(self, self.vmSpecs[0])

            elif languageToUse.startswith("ro"):
                translations.ro.translateStartVmRO(self, self.vmSpecs[0])

            elif languageToUse.startswith("ru"):
                translations.ru.translateStartVmRU(self, self.vmSpecs[0])

            elif languageToUse.startswith("be"):
                translations.be.translateStartVmBE(self, self.vmSpecs[0])

            elif languageToUse.startswith("cz"):
                translations.cz.translateStartVmCZ(self, self.vmSpecs[0])

            elif languageToUse.startswith("pt"):
                translations.pt.translateStartVmPT(self, self.vmSpecs[0])

            elif languageToUse.startswith("pl"):
                translations.pl.translateStartVmPL(self, self.vmSpecs[0])

            elif languageToUse.startswith("it"):
                translations.it.translateStartVmIT(self, self.vmSpecs[0])

            else:
                translations.en.translateStartVmEN(self, self.vmSpecs[0])
        
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
                        translations.de.translateStartVmDE(self, self.vmSpecs[0])

                    elif languageToUse.startswith("uk"):
                        translations.uk.translateStartVmUK(self, self.vmSpecs[0])

                    elif languageToUse.startswith("fr"):
                        translations.fr.translateStartVmFR(self, self.vmSpecs[0])

                    elif languageToUse.startswith("es"):
                        translations.es.translateStartVmES(self, self.vmSpecs[0])

                    elif languageToUse.startswith("ro"):
                        translations.ro.translateStartVmRO(self, self.vmSpecs[0])

                    elif languageToUse.startswith("ru"):
                        translations.ru.translateStartVmRU(self, self.vmSpecs[0])

                    elif languageToUse.startswith("be"):
                        translations.be.translateStartVmBE(self, self.vmSpecs[0])

                    elif languageToUse.startswith("cz"):
                        translations.cz.translateStartVmCZ(self, self.vmSpecs[0])

                    elif languageToUse.startswith("pt"):
                        translations.pt.translateStartVmPT(self, self.vmSpecs[0])

                    elif languageToUse.startswith("pl"):
                        translations.pl.translateStartVmPL(self, self.vmSpecs[0])

                    elif languageToUse.startswith("it"):
                        translations.it.translateStartVmIT(self, self.vmSpecs[0])

                    else:
                        translations.en.translateStartVmEN(self, self.vmSpecs[0])
            
            except:
                print("Translation can't be figured out. Using English language.")

                if platform.system() == "Windows":
                    errorFile = platformSpecific.windowsSpecific.windowsErrorFile()
        
                else:
                    errorFile = platformSpecific.unixSpecific.unixErrorFile()

                with open(errorFile, "w+") as errCodeFile:
                    errCodeFile.write(errors.errCodes.errCodes[11])

                dialog = ErrDialog(self)
                dialog.exec()

                translations.en.translateStartVmEN(self, self.vmSpecs[0])
                

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
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select first cdrom file', dir='.', filter='ISO image (*.iso);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_cdrom2_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select second cdrom file', dir='.', filter='ISO image (*.iso);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def set_date_to_system(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    # Here, it chooses the architecture for your VM and starts the right thing.

    def start_virtual_machine(self):
        connection = self.connection
        cursor = connection.cursor()

        fda_file = self.lineEdit.text()
        cdrom_file = self.lineEdit_2.text()
        cdrom_file2 = self.lineEdit_4.text()
        bootfrom = self.comboBox.currentText()
        dateTimeForVM = self.dateTimeEdit.text()

        print(fda_file)
        print(cdrom_file)
        print(bootfrom)
        print(dateTimeForVM)

        qemu_cmd = ""

        try:
            for architecture in self.architectures:
                if self.vmSpecs[1] == architecture:
                    sel_query = f"""
                    SELECT value FROM settings
                    WHERE name = 'qemu-system-{architecture}';
                    """

                    cursor.execute(sel_query)
                    connection.commit()
                    result = cursor.fetchall()
                    print(result)
                    break

            qemu_to_execute = result[0][0]

            if platform.system() == "Windows":
                qemu_cmd = f"{qemu_to_execute} -m {self.vmSpecs[4]} -smp {self.vmSpecs[17]} -k {self.vmSpecs[21]}"

            else:
                qemu_cmd = f"{qemu_to_execute} -m {self.vmSpecs[4]} -smp {self.vmSpecs[17]} -k {self.vmSpecs[21]}"

            if self.checkBox.isChecked():
                qemu_cmd = qemu_cmd + f" -rtc base=\"{dateTimeForVM}\",clock=vm"

            if self.vmSpecs[5] != "NULL":
                if magic.from_file(self.vmSpecs[5]) == "block special":
                    if platform.system() == "Windows":
                        qemu_cmd = qemu_cmd + f" -drive format=raw,file=\"{self.vmSpecs[5]}\""
                
                    else:
                        qemu_cmd = qemu_cmd + f" -drive format=raw,file={self.vmSpecs[5]}"

                else:
                    if self.vmSpecs[26] == "Let QEMU decide":
                        if platform.system() == "Windows":
                            qemu_cmd = qemu_cmd + f" -hda \"{self.vmSpecs[5]}\""

                        else:
                            qemu_cmd = qemu_cmd + f" -hda {self.vmSpecs[5]}"

                    elif self.vmSpecs[26] == "IDE":
                        if platform.system() == "Windows":
                            qemu_cmd = qemu_cmd + f" -drive file=\"{self.vmSpecs[5]}\",if=ide,media=disk"

                        else:
                            qemu_cmd = qemu_cmd + f" -drive file={self.vmSpecs[5]},if=ide,media=disk"

                    elif self.vmSpecs[26] == "VirtIO SCSI":
                        if platform.system() == "Windows":
                            qemu_cmd = qemu_cmd + f" -device virtio-scsi-pci,id=scsi0 -drive file=\"{self.vmSpecs[5]}\",if=none,discard=unmap,aio=native,cache=none,id=hd1 -device scsi-hd,drive=hd1,bus=scsi0.0"

                        else:
                            qemu_cmd = qemu_cmd + f" -device virtio-scsi-pci,id=scsi0 -drive file={self.vmSpecs[5]},if=none,discard=unmap,aio=native,cache=none,id=hd1 -device scsi-hd,drive=hd1,bus=scsi0.0"

                    elif self.vmSpecs[26] == "AHCI":
                        if platform.system() == "Windows":
                            qemu_cmd = qemu_cmd + f" -drive id=disk,file=\"{self.vmSpecs[5]}\",if=none -device ahci,id=ahci -device ide-hd,drive=disk,bus=ahci.0"

                        else:
                            qemu_cmd = qemu_cmd + f" -drive id=disk,file={self.vmSpecs[5]},if=none -device ahci,id=ahci -device ide-hd,drive=disk,bus=ahci.0"

            if self.vmSpecs[2] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -M {self.vmSpecs[2]}"

            if self.vmSpecs[3] != "Let QEMU decide":
                qemu_cmd = qemu_cmd + f" -cpu {self.vmSpecs[3]}"

            if self.vmSpecs[6] != "Let QEMU decide":
                if self.vmSpecs[6] == "std" or self.vmSpecs[6] == "qxl" or self.vmSpecs[6] == "cirrus" or self.vmSpecs[6] == "cg3" or self.vmSpecs[6] == "tcx":
                    qemu_cmd = qemu_cmd + f" -vga {self.vmSpecs[6]}"

                else:
                    qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[6]}"

                """ if self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    if self.vmSpecs[6] == "std":
                        qemu_cmd = qemu_cmd + f" -device VGA -display gtk"
                    
                    else:
                        qemu_cmd = qemu_cmd + f" -device {self.vmSpecs[6]} -display gtk"

                else:
                    qemu_cmd = qemu_cmd + f" -vga {self.vmSpecs[6]}" """

            if self.vmSpecs[7] != "none":
                if self.vmSpecs[1] == "i386" or self.vmSpecs[1] == "x86_64" or self.vmSpecs[1] == "ppc" or self.vmSpecs[1] == "ppc64" or self.vmSpecs[1] == "sparc" or self.vmSpecs[1] == "sparc64":
                    qemu_cmd = qemu_cmd + f" -net nic,model={self.vmSpecs[7]} -net user"

                elif self.vmSpecs[1] == "mips64el" or self.vmSpecs[1] == "mipsel":
                    qemu_cmd = qemu_cmd + f" -nic user,model={self.vmSpecs[7]}"

                elif self.vmSpecs[1] == "aarch64" or self.vmSpecs[1] == "arm":
                    # Due to the circumstances here, for the VM, a random MAC address is
                    # generated at runtime. Due to that, the MAC changes every time you
                    # start your virtual machine.

                    mac_possible_chars = "0123456789abcdef"

                    mac_gen = []
                    i = 0

                    while i < 6:
                        firstLetter = mac_possible_chars[randint(0, 15)]
                        secondLetter = mac_possible_chars[randint(0, 15)]
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
                    if self.vmSpecs[24] == "Let QEMU decide":
                        qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file}\""

                    elif self.vmSpecs[24] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=ide,media=cdrom"

                    elif self.vmSpecs[24] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=scsi,media=cdrom"

                    elif self.vmSpecs[24] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file}\",if=virtio,media=cdrom"

                else:
                    if self.vmSpecs[24] == "Let QEMU decide":
                        qemu_cmd = qemu_cmd + f" -cdrom {cdrom_file}"

                    elif self.vmSpecs[24] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file},if=ide,media=cdrom"

                    elif self.vmSpecs[24] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file},if=scsi,media=cdrom"

                    elif self.vmSpecs[24] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file},if=virtio,media=cdrom"

            if cdrom_file2 != "":
                if platform.system() == "Windows":
                    if self.vmSpecs[25] == "Let QEMU decide":
                        qemu_cmd = qemu_cmd + f" -cdrom \"{cdrom_file2}\""

                    elif self.vmSpecs[25] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file2}\",if=ide,media=cdrom"

                    elif self.vmSpecs[25] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file2}\",if=scsi,media=cdrom"

                    elif self.vmSpecs[25] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file=\"{cdrom_file2}\",if=virtio,media=cdrom"

                else:
                    if self.vmSpecs[25] == "Let QEMU decide":
                        qemu_cmd = qemu_cmd + f" -cdrom {cdrom_file2}"

                    elif self.vmSpecs[25] == "IDE":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=ide,media=cdrom"

                    elif self.vmSpecs[25] == "SCSI":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=scsi,media=cdrom"

                    elif self.vmSpecs[25] == "Virtio":
                        qemu_cmd = qemu_cmd + f" -drive file={cdrom_file2},if=virtio,media=cdrom"

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

            if self.vmSpecs[23] == "TCG":
                qemu_cmd = qemu_cmd + " -accel tcg"

            elif self.vmSpecs[23] == "HAXM":
                qemu_cmd = qemu_cmd + " -accel hax"

            elif self.vmSpecs[23] == "WHPX":
                qemu_cmd = qemu_cmd + " -accel whpx"

            elif self.vmSpecs[23] == "KVM":
                qemu_cmd = qemu_cmd + " -enable-kvm"

            if self.lineEdit_3.text() != "":
                if self.vmSpecs[1] == "x86_64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0"

                elif self.vmSpecs[1] == "aarch64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis-device,tpmdev=tpm0"

                elif self.vmSpecs[1] == "ppc64":
                    qemu_cmd = qemu_cmd + f" -chardev socket,id=chrtpm,path={self.lineEdit_3.text()}/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-spapr,tpmdev=tpm0"

            subprocess.Popen(qemu_cmd)

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
        
        except:
            print("Qemu couldn't be executed. Trying subprocess.run")

            try:
                qemu_cmd_split = qemu_cmd.split(" ")
                # Potentially insert fix for datetime issue here

                i = 0

                while i < len(qemu_cmd_split):
                    if qemu_cmd_split[i] == "-rtc":
                        qemu_time = qemu_cmd_split[i] + " " + qemu_cmd_split[i + 1]
                        qemu_cmd_split.insert(i, qemu_time)
                        del qemu_cmd_split[i + 1]
                        del qemu_cmd_split[i + 1]
                        break

                    i += 1

                subprocess.run(shlex.split(qemu_cmd))
            
            except:
                print("Qemu couldn't be executed. Trying subprocess.call.")

                try:
                    if platform.system() == "Windows":
                        subprocess.call(qemu_cmd)

                    else:
                        subprocess.call(shlex.split(qemu_cmd))

                except:
                    print("Qemu couldn't be executed. Please check if the settings of your VM and/or the QEMU paths are correct.")
        
        self.close()