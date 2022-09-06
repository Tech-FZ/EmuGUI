# Importing required modules
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import sqlite3
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import QTimer
from uiScripts.ui_Main import Ui_MainWindow
from dialogExecution.newVirtualMachine import NewVirtualMachineDialog
from uiScripts.ui_SettingsPending1 import Ui_Dialog
from dialogExecution.startVirtualMachine import StartVirtualMachineDialog
from dialogExecution.editVirtualMachine import EditVirtualMachineDialog
from dialogExecution.noUpdateAvailable import NoUpdateAvailable
from dialogExecution.updateAvailable import UpdateAvailable
from dialogExecution.usbTabletDepreciation import UsbTabletDepreciated
from dialogExecution.win81NearEOS import Win812012R2NearEOS
from dialogExecution.vmTooNew import VmIsMadeWithTooYoungEmuGUI
from dialogExecution.settingsRequireRestart import SettingsRequireEmuGUIReboot
from dialogExecution.win2kDepreciation import Win2KDepreciated
from dialogExecution.qemuImgError import QemuImgMissing
from dialogExecution.qemuSysError import QemuSysMissing
import translations.de
import translations.uk
import translations.en
import requests
import locale

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # This function initializes and runs EmuGUI
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateVmList)
        self.label_8.setText("EmuGUI v0.7.3.5109")
        self.setWindowTitle("EmuGUI")
        self.languageInUse = "system"

        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass

        self.versionCode = 5109

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()
        
        self.prepareDatabase(self.connection)
        self.updateVmList()

        if platform.system() == "Windows":
            winvers = sys.getwindowsversion()

            if winvers.major <= 6 and winvers.minor <= 3:
                dialog = Win812012R2NearEOS(self)
                dialog.exec()

    def connectSignalsSlots(self):
        # These buttons are connected to their incorporate functions
        self.pushButton_8.clicked.connect(self.createNewVM)
        self.pushButton.clicked.connect(self.set_qemu_img_path)
        self.pushButton_2.clicked.connect(self.set_qemu_i386_path)
        self.pushButton_3.clicked.connect(self.set_qemu_x86_64_path)
        self.pushButton_4.clicked.connect(self.set_qemu_ppc_path)
        self.pushButton_5.clicked.connect(self.set_qemu_mips64el_path)
        self.pushButton_17.clicked.connect(self.set_qemu_mipsel_path)
        self.pushButton_16.clicked.connect(self.set_qemu_ppc64_path)
        self.pushButton_6.clicked.connect(self.applyChangesQemu)
        self.pushButton_9.clicked.connect(self.startVM)
        self.pushButton_11.clicked.connect(self.deleteVM)
        self.pushButton_10.clicked.connect(self.editVM)
        self.pushButton_7.clicked.connect(self.set_qemu_aarch64_path)
        self.pushButton_12.clicked.connect(self.set_qemu_arm_path)
        self.pushButton_14.clicked.connect(self.applyChangesUpdate)
        self.pushButton_13.clicked.connect(self.checkForUpdatesManually)
        self.pushButton_15.clicked.connect(self.applyGeneric)
        self.label_6.setPixmap(QtGui.QPixmap("Text colourized.png"))

    def setLanguage(self, langmode):
        if langmode == "system" or langmode == None:
            languageToUse = locale.getlocale()[0]
            self.languageInUse = "system"

        else:
            languageToUse = langmode

        if languageToUse.startswith("de"):
            translations.de.translateMainDE(self)

            if langmode != "system":
                self.languageInUse = "de"

        elif languageToUse.startswith("uk"):
            translations.uk.translateMainUK(self)

            if langmode != "system":
                self.languageInUse = "uk"

        else:
            translations.en.translateMainEN(self)

            if langmode != "system":
                self.languageInUse = "en"

    def prepareDatabase(self, connection):
        # Some SQL statements to initialize EmuGUI
        create_settings_table = """
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT
        );
        """

        create_vm_table = """
        CREATE TABLE IF NOT EXISTS virtualmachines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            architecture TEXT NOT NULL,
            machine TEXT NOT NULL,
            cpu TEXT NOT NULL,
            ram INTEGER NOT NULL,
            hda TEXT,
            vga TEXT NOT NULL,
            net TEXT,
            usbtablet INTEGER NOT NULL,
            win2k INTEGER NOT NULL,
            dirbios TEXT,
            additionalargs TEXT,
            sound TEXT NOT NULL,
            linuxkernel TEXT NOT NULL,
            linuxinitrid TEXT NOT NULL,
            linuxcmd TEXT NOT NULL,
            mousetype TEXT NOT NULL,
            cores INT DEFAULT 1 NOT NULL,
            filebios TEXT DEFAULT "" NOT NULL,
            keyboardtype TEXT NOT NULL,
            usbsupport INT DEFAULT 0 NOT NULL,
            usbcontroller TEXT DEFAULT "pci-ohci" NOT NULL
        );
        """

        create_update_table = """
        CREATE TABLE IF NOT EXISTS updater (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        );
        """

        # The v0.2 feature set
        select02ColumnsVM = """
        SELECT sound, linuxkernel, linuxinitrid, linuxcmd FROM virtualmachines;
        """

        # The v0.3 feature set
        select03ColumnsVM = """
        SELECT mousetype FROM virtualmachines;
        """

        select03ColumnsVM2 = """
        SELECT cores, filebios FROM virtualmachines;
        """

        # The v0.4 feature set
        select04ColumnsVM = """
        SELECT keyboardtype, usbsupport FROM virtualmachines;
        """

        # The v0.5 feature set
        select05ColumnsVM = """
        SELECT usbcontroller FROM virtualmachines;
        """

        insertSoundColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN sound TEXT DEFAULT "none" NOT NULL;
        """

        insertLinuxKernelColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxkernel TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxInitridColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxinitrid TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxCmdColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxcmd TEXT DEFAULT "" NOT NULL;
        """

        insertMouseTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN mousetype TEXT DEFAULT "PS/2 Mouse" NOT NULL;
        """

        insertCpuCoresVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN cores TEXT DEFAULT 1 NOT NULL;
        """

        insertBiosFileVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN filebios TEXT DEFAULT "" NOT NULL;
        """

        insertKeyboardTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN keyboardtype TEXT DEFAULT "PS/2 Keyboard" NOT NULL;
        """

        insertUsbSupportVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN usbsupport INT DEFAULT 0 NOT NULL;
        """

        insertUsbControllerVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN usbcontroller TEXT DEFAULT "pci-ohci" NOT NULL;
        """

        insert_qemu_img = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-img"
        );
        """

        insert_qemu_i386 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-i386"
        );
        """

        insert_qemu_x86_64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-x86_64"
        );
        """

        insert_qemu_ppc = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-ppc"
        );
        """

        insert_qemu_ppc64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-ppc64"
        );
        """

        insert_qemu_mips64el = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-mips64el"
        );
        """

        insert_qemu_mipsel = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-mipsel"
        );
        """

        insert_qemu_aarch64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-aarch64"
        );
        """

        insert_qemu_arm = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-arm"
        );
        """

        # Language codes:
        # default: same language as system (English if not present)
        # en: English
        # de: German
        # uk: Ukranian
        insert_language = """
        INSERT INTO settings (
            name, value
        ) VALUES (
            "lang", "default"
        );
        """

        # The mirrors are GitHub and Codeberg
        insert_update_mirror = """
        INSERT INTO updater (
            name, value
        ) VALUES (
            "updatemirror", "GitHub"
        );
        """

        # For the frequency, it's as follows:
        # boot = Everytime I run this program
        # never = Never
        insert_update_freq = """
        INSERT INTO updater (
            name, value
        ) VALUES (
            "updatefreq", "boot"
        );
        """

        # stable and pre-release are available
        insert_update_channel = """
        INSERT INTO updater (
            name, value
        ) VALUES (
            "updatechannel", "stable"
        );
        """

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        select_qemu_img = """
        SELECT name, value FROM settings
        WHERE name = "qemu-img";
        """

        select_qemu_i386 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-i386";
        """

        select_qemu_x86_64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-x86_64";
        """

        select_qemu_ppc = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-ppc";
        """

        select_qemu_ppc64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-ppc64";
        """

        select_qemu_mips64el = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-mips64el";
        """

        select_qemu_mipsel = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-mipsel";
        """

        select_qemu_aarch64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-aarch64";
        """

        select_qemu_arm = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-arm";
        """

        select_language = """
        SELECT name, value FROM settings
        WHERE name = "lang";
        """

        select_update_mirror = """
        SELECT name, value FROM updater
        WHERE name = "updatemirror";
        """

        select_update_freq = """
        SELECT name, value FROM updater
        WHERE name = "updatefreq";
        """

        select_update_channel = """
        SELECT name, value FROM updater
        WHERE name = "updatechannel";
        """

        cursor = connection.cursor()

        # If they don't exist yet, the settings and VM tables are created.

        try:
            cursor.execute(create_settings_table)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(create_vm_table)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(create_update_table)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        # Then, the tables will be checked for completeness.

        try:
            cursor.execute(select_qemu_img)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_5.setText(result[0][1])
                print("The query was executed successfully. The qemu-img slot already is in the database.")

            except:
                cursor.execute(insert_qemu_img)
                connection.commit()
                print("The query was executed successfully. The qemu-img slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_i386)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_4.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-i386 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_i386)
                connection.commit()
                print("The query was executed successfully. The qemu-system-i386 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_x86_64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_3.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-x86_64 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_x86_64)
                connection.commit()
                print("The query was executed successfully. The qemu-system-x86_64 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_ppc)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_2.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-ppc slot already is in the database.")

            except:
                cursor.execute(insert_qemu_ppc)
                connection.commit()
                print("The query was executed successfully. The qemu-system-ppc slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_ppc64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_8.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-ppc slot already is in the database.")

            except:
                cursor.execute(insert_qemu_ppc64)
                connection.commit()
                print("The query was executed successfully. The qemu-system-ppc slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_mips64el)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-mips64el slot already is in the database.")

            except:
                cursor.execute(insert_qemu_mips64el)
                connection.commit()
                print("The query was executed successfully. The qemu-system-mips64el slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_mipsel)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_9.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-mips64el slot already is in the database.")

            except:
                cursor.execute(insert_qemu_mipsel)
                connection.commit()
                print("The query was executed successfully. The qemu-system-mips64el slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_aarch64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_6.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-aarch64 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_aarch64)
                connection.commit()
                print("The query was executed successfully. The qemu-system-aarch64 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_arm)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_7.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-arm slot already is in the database.")

            except:
                cursor.execute(insert_qemu_arm)
                connection.commit()
                print("The query was executed successfully. The qemu-system-arm slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

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

                i = 0
                
                if result[0][1] == "default":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "System default":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1                    

                elif result[0][1] == "en":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "English":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "en"

                elif result[0][1] == "de":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Deutsch":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "de"

                elif result[0][1] == "uk":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Українська":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "uk"

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                self.setLanguage(langmode)

                print("The query was executed successfully. The language slot already is in the database.")

            except:
                cursor.execute(insert_language)
                connection.commit()
                langmode = "system"

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")
                    
                self.setLanguage(langmode)
                print("The query was executed successfully. The language slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_update_mirror)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                
                i = 0

                while i < self.comboBox.count():
                    if self.comboBox.itemText(i) == result[0][1]:
                        self.comboBox.setCurrentIndex(i)
                        break

                    i += 1

                print("The query was executed successfully. The update mirror slot already is in the database.")

            except:
                cursor.execute(insert_update_mirror)
                connection.commit()
                print("The query was executed successfully. The update mirror slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_update_freq)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print(result)
                
                if result[0][1] == "boot":
                    self.comboBox_2.setCurrentIndex(0)
                    self.checkForUpdates(False)

                elif result[0][1] == "never":
                    self.comboBox_2.setCurrentIndex(1)

                print("The query was executed successfully. The update mirror slot already is in the database.")

            except:
                cursor.execute(insert_update_freq)
                connection.commit()
                print("The query was executed successfully. The update mirror slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_update_channel)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                
                i = 0

                while i < self.comboBox_3.count():
                    if self.comboBox_3.itemText(i) == result[0][1]:
                        self.comboBox_3.setCurrentIndex(i)
                        break

                    i += 1

                print("The query was executed successfully. The update mirror slot already is in the database.")

            except:
                cursor.execute(insert_update_channel)
                connection.commit()
                print("The query was executed successfully. The update mirror slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select02ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.2 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertSoundColVM)
                connection.commit()

                cursor.execute(insertLinuxKernelColVM)
                connection.commit()

                cursor.execute(insertLinuxInitridColVM)
                connection.commit()

                cursor.execute(insertLinuxCmdColVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select03ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The first v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertMouseTypeVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select03ColumnsVM2)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The second v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertCpuCoresVM)
                connection.commit()

                cursor.execute(insertBiosFileVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select04ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.4 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertKeyboardTypeVM)
                connection.commit()

                cursor.execute(insertUsbSupportVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select05ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.5 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertUsbControllerVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            print(cursor.fetchall())
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def createNewVM(self):
        # This is the code that launches the dialog for creating a VM.
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result = cursor.fetchall()

            print(result)

            i = 0

            while i < len(result):
                if result[i][0] == "qemu-img":
                    if result[i][1] == "":
                        dialog = QemuImgMissing(self)
                        dialog.exec()

                    else:
                        dialog = NewVirtualMachineDialog(self)
                        dialog.exec()
                
                    break

                i += 1
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def startVM(self):
        # This is the code that lets you power your virtual machines in the first place.

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result_settings = cursor.fetchall()

            print(result_settings)

            selectedVM = self.listView.currentIndex().data()
            print(selectedVM)

            get_vm_to_start = f"""
            SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller FROM virtualmachines
            WHERE name = '{selectedVM}'
            """

            try:
                cursor.execute(get_vm_to_start)
                connection.commit()
                result = cursor.fetchall()

                print(result)

                architecture_of_vm = result[0][0]
                machine_of_vm = result[0][1]
                cpu_of_vm = result[0][2]
                ram_of_vm = result[0][3]
                hda_of_vm = result[0][4]
                vga_of_vm = result[0][5]
                net_of_vm = result[0][6]
                usbtablet_wanted = result[0][7]
                os_is_win2k = result[0][8]
                dir_bios = result[0][9]
                additional_arguments = result[0][10]
                sound_card = result[0][11]
                linux_kernel = result[0][12]
                linux_initrid = result[0][13]
                linux_cmd = result[0][14]
                mouse_type = result[0][15]
                cpu_cores = result[0][16]
                file_bios = result[0][17]
                kbd_type = result[0][18]
                usb_support = result[0][19]
                usb_controller = result[0][20]

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
            with open(tempVmDef, "w+") as tempVmDefFile:
                tempVmDefFile.write(selectedVM + "\n")
                tempVmDefFile.write(architecture_of_vm + "\n")
                tempVmDefFile.write(machine_of_vm + "\n")
                tempVmDefFile.write(cpu_of_vm + "\n")
                tempVmDefFile.write(str(ram_of_vm) + "\n")
                tempVmDefFile.write(hda_of_vm + "\n")
                tempVmDefFile.write(vga_of_vm + "\n")
                tempVmDefFile.write(net_of_vm + "\n")
                tempVmDefFile.write(str(usbtablet_wanted) + "\n")
                tempVmDefFile.write(str(os_is_win2k) + "\n")
                tempVmDefFile.write(dir_bios + "\n")
                tempVmDefFile.write(additional_arguments + "\n")
                tempVmDefFile.write(sound_card + "\n")
                tempVmDefFile.write(linux_kernel + "\n")
                tempVmDefFile.write(linux_initrid + "\n")
                tempVmDefFile.write(linux_cmd + "\n")
                tempVmDefFile.write(mouse_type + "\n")
                tempVmDefFile.write(str(cpu_cores) + "\n")
                tempVmDefFile.write(str(file_bios) + "\n")
                tempVmDefFile.write(kbd_type + "\n")
                tempVmDefFile.write(str(usb_support) + "\n")
                tempVmDefFile.write(usb_controller + "\n")

            if usbtablet_wanted == 1:
                dialog3 = UsbTabletDepreciated(self)
                dialog3.exec()

            if os_is_win2k == 1:
                dialog3 = Win2KDepreciated(self)
                dialog3.exec()

            if selectedVM == "Tic Tac Py":
                print("Let's respect Tic Tac Py, the first program released to the public by Nicolas Lucien.")
                print("RIP Tic Tac Py")
                print("2021-2022")

            i = 0

            while i < len(result_settings):
                if architecture_of_vm == "i386" or architecture_of_vm == "x86_64" or architecture_of_vm == "mips64el":
                    if result_settings[i][0] == f"qemu-system-{architecture_of_vm}":
                        if result_settings[i][1] != "":
                            dialog = StartVirtualMachineDialog(self)
                            dialog.exec()
                            break

                        else:
                            dialog = QemuSysMissing(self)
                            dialog.exec()
                            break

                elif architecture_of_vm == "ppc" or architecture_of_vm == "aarch64" or architecture_of_vm == "arm":
                    if result_settings[i][0] == f"qemu-system-{architecture_of_vm}":
                        if result_settings[i][1] == "":
                            dialog = QemuSysMissing(self)
                            dialog.exec()
                            break

                        else:
                            dialog = StartVirtualMachineDialog(self)
                            dialog.exec()
                            break

                elif architecture_of_vm == "ppc64" or architecture_of_vm == "mipsel":
                    if result_settings[i][0] == f"qemu-system-{architecture_of_vm}":
                        if result_settings[i][1] == "":
                            dialog = QemuSysMissing(self)
                            dialog.exec()
                            break

                        else:
                            dialog = StartVirtualMachineDialog(self)
                            dialog.exec()
                            break

                else:
                    dialog = VmIsMadeWithTooYoungEmuGUI(self)
                    dialog.exec()
                    break

                i += 1
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def editVM(self):
        # Of course, this code prepares the dialog for editing VMs.

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result_settings = cursor.fetchall()

            print(result_settings)

            selectedVM = self.listView.currentIndex().data()
            print(selectedVM)

            get_vm_to_start = f"""
            SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller FROM virtualmachines
            WHERE name = '{selectedVM}'
            """

            try:
                cursor.execute(get_vm_to_start)
                connection.commit()
                result = cursor.fetchall()

                print(result)

                architecture_of_vm = result[0][0]
                machine_of_vm = result[0][1]
                cpu_of_vm = result[0][2]
                ram_of_vm = result[0][3]
                hda_of_vm = result[0][4]
                vga_of_vm = result[0][5]
                net_of_vm = result[0][6]
                usbtablet_wanted = result[0][7]
                os_is_win2k = result[0][8]
                dir_bios = result[0][9]
                additional_arguments = result[0][10]
                sound_card = result[0][11]
                linux_kernel = result[0][12]
                linux_initrid = result[0][13]
                linux_cmd = result[0][14]
                mouse_type = result[0][15]
                cpu_cores = result[0][16]
                file_bios = result[0][17]
                kbd_type = result[0][18]
                usb_support = result[0][19]
                usb_controller = result[0][20]

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            if platform.system() == "Windows":
                tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
            else:
                tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
            with open(tempVmDef, "w+") as tempVmDefFile:
                tempVmDefFile.write(selectedVM + "\n")
                tempVmDefFile.write(architecture_of_vm + "\n")
                tempVmDefFile.write(machine_of_vm + "\n")
                tempVmDefFile.write(cpu_of_vm + "\n")
                tempVmDefFile.write(str(ram_of_vm) + "\n")
                tempVmDefFile.write(hda_of_vm + "\n")
                tempVmDefFile.write(vga_of_vm + "\n")
                tempVmDefFile.write(net_of_vm + "\n")
                tempVmDefFile.write(str(usbtablet_wanted) + "\n")
                tempVmDefFile.write(str(os_is_win2k) + "\n")
                tempVmDefFile.write(dir_bios + "\n")
                tempVmDefFile.write(additional_arguments + "\n")
                tempVmDefFile.write(sound_card + "\n")
                tempVmDefFile.write(linux_kernel + "\n")
                tempVmDefFile.write(linux_initrid + "\n")
                tempVmDefFile.write(linux_cmd + "\n")
                tempVmDefFile.write(mouse_type + "\n")
                tempVmDefFile.write(str(cpu_cores) + "\n")
                tempVmDefFile.write(file_bios + "\n")
                tempVmDefFile.write(kbd_type + "\n")
                tempVmDefFile.write(str(usb_support) + "\n")
                tempVmDefFile.write(usb_controller + "\n")

            i = 0

            while i < len(result_settings):
                if result_settings[i][0] == "qemu-img":
                    if result_settings[i][1] == "":
                        dialog = QemuImgMissing(self)
                        dialog.exec()

                    else:
                        dialog = EditVirtualMachineDialog(self)
                        dialog.exec()
                
                    break

                i += 1
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    # These functions are for setting the QEMU paths.

    def set_qemu_img_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-img executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def set_qemu_i386_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-i386 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def set_qemu_x86_64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-x86_64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_3.setText(filename)

    def set_qemu_ppc_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-ppc executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_qemu_ppc64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-ppc64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_8.setText(filename)


    def set_qemu_mips64el_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips64el executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit.setText(filename)

    def set_qemu_mipsel_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mipsel executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_9.setText(filename)

    def set_qemu_aarch64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-aarch64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def set_qemu_arm_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-arm executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_7.setText(filename)

    def applyChangesQemu(self):
        pathQemuImg = self.lineEdit_5.text()
        pathQemuI386 = self.lineEdit_4.text()
        pathQemuX86_64 = self.lineEdit_3.text()
        pathQemuPpc = self.lineEdit_2.text()
        pathQemuPpc64 = self.lineEdit_8.text()
        pathQemuMips64El = self.lineEdit.text()
        pathQemuMipsEl = self.lineEdit_9.text()
        pathQemuAarch64 = self.lineEdit_6.text()
        pathQemuArm = self.lineEdit_7.text()

        qemu_img_update = f"""
        UPDATE settings
        SET value = '{pathQemuImg}'
        WHERE name = 'qemu-img';
        """

        qemu_i386_update = f"""
        UPDATE settings
        SET value = '{pathQemuI386}'
        WHERE name = 'qemu-system-i386';
        """

        qemu_x86_64_update = f"""
        UPDATE settings
        SET value = '{pathQemuX86_64}'
        WHERE name = 'qemu-system-x86_64';
        """

        qemu_ppc_update = f"""
        UPDATE settings
        SET value = '{pathQemuPpc}'
        WHERE name = 'qemu-system-ppc';
        """

        qemu_ppc64_update = f"""
        UPDATE settings
        SET value = '{pathQemuPpc64}'
        WHERE name = 'qemu-system-ppc64';
        """

        qemu_mips64el_update = f"""
        UPDATE settings
        SET value = '{pathQemuMips64El}'
        WHERE name = 'qemu-system-mips64el';
        """

        qemu_mipsel_update = f"""
        UPDATE settings
        SET value = '{pathQemuMipsEl}'
        WHERE name = 'qemu-system-mipsel';
        """

        qemu_aarch64_update = f"""
        UPDATE settings
        SET value = '{pathQemuAarch64}'
        WHERE name = 'qemu-system-aarch64';
        """

        qemu_arm_update = f"""
        UPDATE settings
        SET value = '{pathQemuArm}'
        WHERE name = 'qemu-system-arm';
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(qemu_img_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_i386_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_x86_64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_ppc_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_ppc64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_mips64el_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_mipsel_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_aarch64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_arm_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def applyChangesUpdate(self):
        updateMirror = self.comboBox.currentText()

        if self.comboBox_2.currentText() == "Everytime I run this program":
            updateNotifyFreq = "boot"

        elif self.comboBox_2.currentText() == "Jedes Mal, wenn ich dieses Programm ausführe":
            updateNotifyFreq = "boot"

        elif self.comboBox_2.currentText() == "Never" or self.comboBox_2.currentText() == "Nie":
            updateNotifyFreq = "never"

        updateChannel = self.comboBox_3.currentText()

        mirror_update = f"""
        UPDATE updater
        SET value = '{updateMirror}'
        WHERE name = 'updatemirror';
        """

        freq_update = f"""
        UPDATE updater
        SET value = '{updateNotifyFreq}'
        WHERE name = 'updatefreq';
        """

        channel_update = f"""
        UPDATE updater
        SET value = '{updateChannel}'
        WHERE name = 'updatechannel';
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(mirror_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(freq_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(channel_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def applyGeneric(self):
        language_system = f"""
        UPDATE settings
        SET value = 'default'
        WHERE name = 'lang';
        """

        language_en = f"""
        UPDATE settings
        SET value = 'en'
        WHERE name = 'lang';
        """

        language_de = f"""
        UPDATE settings
        SET value = 'de'
        WHERE name = 'lang';
        """

        language_uk = f"""
        UPDATE settings
        SET value = 'uk'
        WHERE name = 'lang';
        """

        connection = self.connection
        cursor = connection.cursor()

        if self.comboBox_4.currentText() == "System default" or self.comboBox_4.currentText() == "Systemstandard":
            langmode = "system"

            try:
                cursor.execute(language_system)
                connection.commit()
                

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "English":
            langmode = "en"

            try:
                cursor.execute(language_en)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Deutsch":
            langmode = "de"

            try:
                cursor.execute(language_de)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

        elif self.comboBox_4.currentText() == "Українська":
            langmode = "uk"

            try:
                cursor.execute(language_uk)
                connection.commit()

                if platform.system() == "Windows":
                    langfile = platformSpecific.windowsSpecific.windowsLanguageFile()
                
                else:
                    langfile = platformSpecific.unixSpecific.unixLanguageFile()

                if langmode == "system":
                    languageToUseLater = locale.getlocale()[0]
                    languageToUseEvenLater = languageToUseLater.split("_")
                    languageToUseHere = languageToUseEvenLater[0]

                else:
                    languageToUseHere = langmode
                
                try:
                    with open(langfile, "w+") as language:
                        language.write(languageToUseHere)

                except:
                    print("EmuGUI failed to create a language file. Expect some issues.")

                self.setLanguage(langmode)
                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

    def checkForUpdatesManually(self):
        manually = True
        self.checkForUpdates(manually)

    def checkForUpdates(self, manually):
        try:
            if platform.system() == "Windows":
                connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
            else:
                connection = platformSpecific.unixSpecific.setupUnixBackend()

            select_update_mirror = """
            SELECT name, value FROM updater
            WHERE name = "updatemirror";
            """

            select_update_channel = """
            SELECT name, value FROM updater
            WHERE name = "updatechannel";
            """

            cursor = connection.cursor()

            try:
                cursor.execute(select_update_mirror)
                connection.commit()
                result = cursor.fetchall()

                try:
                    qemu_img_slot = str(result[0])
                
                    if result[0][1] == "GitHub":
                        url = "https://raw.githubusercontent.com/Tech-FZ/EmuGUI/main/update.txt"
                
                    elif result[0][1] == "Codeberg":
                        url = "https://codeberg.org/lucien-rowan/EmuGUI/raw/branch/main/update.txt"

                    print("The query was executed successfully. The update mirror slot already is in the database.")

                except:
                    print("The query was executed successfully but the mirror couldn't be retrieved. Please check one of the following mirrors:")
                    print("https://github.com/Tech-FZ/EmuGUI or")
                    print("https://codeberg.org/lucien-rowan/EmuGUI")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            
            rq = requests.get(url, allow_redirects=True)
            newVer = open("update.txt", "wb+")
            newVer.write(rq.content)
            newVer.close()
            latest_versions = []

            newVer = open("update.txt", "r+")
            newVerContent = newVer.readlines()

            for line in newVerContent:
                line = line.replace("\n", "")
                latest_version = line.split(" = ")
                latest_versions.append(latest_version)

            print(latest_versions)

            try:
                cursor.execute(select_update_channel)
                connection.commit()
                result = cursor.fetchall()

                try:
                    qemu_img_slot = str(result[0])
                
                    if result[0][1] == "pre-release":
                        channel = "pre_release"
                    
                    else:
                        channel = "stable"

                    print("The query was executed successfully. The update mirror slot already is in the database.")

                except:
                    print("Using stable channel as desired channel couldn't be determined.")
        
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            for latest_version in latest_versions:
                if latest_version[0] == channel:
                    if int(latest_version[1]) > self.versionCode:
                        dialog = UpdateAvailable(self)
                        dialog.exec()

                    elif manually == True:
                        dialog = NoUpdateAvailable(self)
                        dialog.exec()

            self.applyChangesUpdate()
            newVer.close()

        except:
            if manually == True:
                dialog = NoUpdateAvailable(self)
                dialog.exec()

    # Your VM list will be updated every 10 seconds.

    def updateVmList(self):
        try:
            self.timer.stop()

        except:
            pass

        connection = self.connection
        cursor = connection.cursor()

        sel_vm_names = """
        SELECT name FROM virtualmachines;
        """

        try:
            cursor.execute(sel_vm_names)
            connection.commit()
            result = cursor.fetchall()
            i = 0
            entries = []
            model = QtGui.QStandardItemModel()
            self.listView.setModel(model)

            while i < len(result):
                try:
                    entries.append(str(result[i][0]))
                    print("The query was executed successfully.")

                except:
                    pass

                i += 1

            for entry in entries:
                item = QtGui.QStandardItem(entry)
                model.appendRow(item)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        self.timer.start(10000)

    def deleteVM(self):
        # This code wipes your obsolete VM from the list.

        connection = self.connection
        cursor = connection.cursor()
        selectedVM = self.listView.currentIndex().data()
        print(selectedVM)

        get_vm_to_start = f"""
        DELETE FROM virtualmachines
        WHERE name = '{selectedVM}'
        """

        try:
            cursor.execute(get_vm_to_start)
            connection.commit()
            print("The query was executed successfully.")
            self.updateVmList()

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

class SettingsPending1Dialog(QDialog, Ui_Dialog):
    # This comes up if you didn't setup the QEMU paths.

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("EmuGUI - Settings pending")
        self.langDetect()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)

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

                i = 0
                
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
        if langmode == "system":
            languageToUse = locale.getlocale()[0]

        else:
            languageToUse = langmode

        if languageToUse.startswith("de"):
            translations.de.translateSettingsPendingDE(self)

        elif languageToUse.startswith("uk"):
            translations.uk.translateSettingsPendingUK(self)

        else:
            translations.en.translateSettingsPendingEN(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())