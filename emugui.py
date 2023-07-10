# Importing required modules
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific

import sqlite3
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import QTimer, QSize
from uiScripts.ui_Main import Ui_MainWindow
from dialogExecution.newVirtualMachine import NewVirtualMachineDialog
from dialogExecution.startVirtualMachine import StartVirtualMachineDialog
from dialogExecution.editVMNew import EditVMNewDialog
from dialogExecution.usbTabletDepreciation import UsbTabletDepreciated
from dialogExecution.win81NearEOS import Win812012R2NearEOS
from dialogExecution.vmTooNew import VmIsMadeWithTooYoungEmuGUI
from dialogExecution.settingsRequireRestart import SettingsRequireEmuGUIReboot
from dialogExecution.win2kDepreciation import Win2KDepreciated
from dialogExecution.qemuImgError import QemuImgMissing
from dialogExecution.qemuSysError import QemuSysMissing
from dialogExecution.icelakeClientDepreciation import IcelakeClientCPUDepreciation
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
import glob
import webbrowser
import datetime
import dateutil.easter

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # This function initializes and runs EmuGUI
        try:
            super().__init__(parent)

        except:
            super().__init__()
        
        self.setupUi(self)
        self.connectSignalsSlots()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateVmList)
        self.label_8.setText("EmuGUI v1.1.3.5411\nCodename 'Sara Angeline'")
        self.setWindowTitle("EmuGUI v1.1.3.5411")
        self.languageInUse = "system"

        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass

        self.versionCode = 5411

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()

        self.defaultTheme = self.style().objectName()
        self.osThemes = QStyleFactory.keys()
        print(self.osThemes)

        for osTheme in self.osThemes:
            self.comboBox_5.addItem(osTheme)
            print(osTheme)

        self.userThemeFileList = glob.glob("themes/*.qss")
        self.userThemeList = []
        
        for userThemeFile in self.userThemeFileList:
            userTheme = userThemeFile.replace(".qss", "")
            
            if platform.system() == "Windows":
                userTheme = userTheme.replace("themes\\", "")
            
            else:
                userTheme = userTheme.replace("themes/", "")
            
            self.comboBox_5.addItem(userTheme)
            self.userThemeList.append(userTheme)
        
        self.prepareDatabase(self.connection)
        self.updateVmList()

        if platform.system() == "Windows":
            winvers = sys.getwindowsversion()
            if winvers.major <= 6 and winvers.minor <= 3:
                dialog = Win812012R2NearEOS(self)
                dialog.exec()
                
                self.label_8.setText(
                    f"EmuGUI v1.1.3.5411\nCodename 'Sara Angeline'\nYour OS is no longer supported by EmuGUI. You should upgrade at least to Windows 10. You're currently running Windows {platform.release()}")
    
    def resizeEvent(self, event: QtGui.QResizeEvent):
        super().resizeEvent(event)

        self.gridLayoutWidget.resize(event.size())
        self.tabWidget.resize(event.size())
        self.gridLayoutWidget_4.resize(QSize(event.size().width() - 9, event.size().height() - 66))
        self.tabWidget_2.resize(QSize(event.size().width() - 9, event.size().height() - 56))
        self.gridLayoutWidget_2.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        self.gridLayoutWidget_3.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        self.gridLayoutWidget_6.resize(QSize(event.size().width() - 19, event.size().height() - 86))
        
        self.centralwidget.resize(event.size())
    

    def connectSignalsSlots(self):
        # These buttons are connected to their incorporate functions
        self.pushButton_8.clicked.connect(self.createNewVM)
        self.pushButton.clicked.connect(self.set_qemu_img_path)
        self.pushButton_2.clicked.connect(self.set_qemu_i386_path)
        self.pushButton_3.clicked.connect(self.set_qemu_x86_64_path)
        self.pushButton_4.clicked.connect(self.set_qemu_ppc_path)
        self.pushButton_5.clicked.connect(self.set_qemu_mips64el_path)
        self.pushButton_17.clicked.connect(self.set_qemu_mipsel_path)
        self.pushButton_19.clicked.connect(self.set_qemu_mips64_path)
        self.pushButton_18.clicked.connect(self.set_qemu_mips_path)
        self.pushButton_16.clicked.connect(self.set_qemu_ppc64_path)
        self.pushButton_6.clicked.connect(self.applyChangesQemu)
        self.pushButton_9.clicked.connect(self.startVM)
        self.pushButton_11.clicked.connect(self.deleteVM)
        self.pushButton_10.clicked.connect(self.editVM)
        self.pushButton_7.clicked.connect(self.set_qemu_aarch64_path)
        self.pushButton_12.clicked.connect(self.set_qemu_arm_path)
        self.pushButton_15.clicked.connect(self.applyGeneric)
        self.pushButton_13.clicked.connect(self.set_qemu_sparc_path)
        self.pushButton_14.clicked.connect(self.set_qemu_sparc64_path)
        self.pushButton_20.clicked.connect(self.toGithub)
        self.pushButton_21.clicked.connect(self.toDiscord)

        easter_this_year = dateutil.easter.easter(datetime.date.today().year)
        good_friday_delta = datetime.timedelta(days=-2)
        good_saturday_delta = datetime.timedelta(days=-1)
        easter_monday_delta = datetime.timedelta(days=1)

        print(easter_this_year)

        if datetime.date.today() == easter_this_year or datetime.date.today() == easter_this_year + good_friday_delta:
            self.label_6.setPixmap(QtGui.QPixmap("banners/RobertRabbit.png"))

        elif datetime.date.today() == easter_this_year + easter_monday_delta or datetime.date.today() == easter_this_year + good_saturday_delta:
            self.label_6.setPixmap(QtGui.QPixmap("banners/RobertRabbit.png"))

        else:
            self.label_6.setPixmap(QtGui.QPixmap("banners/SaraAngeline.png"))

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

        elif languageToUse.startswith("fr"):
            translations.fr.translateMainFR(self)

            if langmode != "system":
                self.languageInUse = "fr"

        elif languageToUse.startswith("es"):
            translations.es.translateMainES(self)

            if langmode != "system":
                self.languageInUse = "es"

        elif languageToUse.startswith("ro"):
            translations.ro.translateMainRO(self)

            if langmode != "system":
                self.languageInUse = "ro"

        elif languageToUse.startswith("be"):
            translations.be.translateMainBE(self)

            if langmode != "system":
                self.languageInUse = "be"

        elif languageToUse.startswith("cz"):
            translations.cz.translateMainCZ(self)

            if langmode != "system":
                self.languageInUse = "cz"

        elif languageToUse.startswith("ru"):
            translations.ru.translateMainRU(self)

            if langmode != "system":
                self.languageInUse = "ru"

        elif languageToUse.startswith("pt"):
            translations.pt.translateMainPT(self)

            if langmode != "system":
                self.languageInUse = "pt"

        elif languageToUse.startswith("it"):
            translations.it.translateMainIT(self)

            if langmode != "system":
                self.languageInUse = "it"

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
            usbcontroller TEXT DEFAULT "pci-ohci" NOT NULL,
            kbdtype TEXT DEFAULT "en-us" NOT NULL,
            acceltype TEXT DEFAULT "None" NOT NULL
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

        # The v0.9 feature set
        select09ColumnsVM = """
        SELECT kbdtype FROM virtualmachines;
        """

        # The v1.1 feature set
        select11ColumnsVM = """
        SELECT acceltype FROM virtualmachines;
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

        insertKbdLayoutVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN kbdtype TEXT DEFAULT "en-us" NOT NULL;
        """

        insertAccelTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN acceltype TEXT DEFAULT "None" NOT NULL;
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

        insert_qemu_mips64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-mips64"
        );
        """

        insert_qemu_mips = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-mips"
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

        insert_qemu_sparc = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-sparc"
        );
        """

        insert_qemu_sparc64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-sparc64"
        );
        """

        # Language codes:
        # default: same language as system (English if not present)
        # en: English
        # de: German
        # uk: Ukranian
        # fr: French
        # es: Spanish
        # ro: Romanian
        # be: Belarusian
        # cz: Czech
        # ru: Russian
        # pt: Portuguese
        # it: Italian
        insert_language = """
        INSERT INTO settings (
            name, value
        ) VALUES (
            "lang", "default"
        );
        """

        # Theme support
        insert_theme = """
        INSERT INTO settings (
            name, value
        ) VALUES (
            "theme", "default"
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

        select_qemu_mips64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-mips64";
        """

        select_qemu_mips = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-mips";
        """

        select_qemu_aarch64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-aarch64";
        """

        select_qemu_arm = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-arm";
        """

        select_qemu_sparc = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-sparc";
        """

        select_qemu_sparc64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-sparc64";
        """

        select_language = """
        SELECT name, value FROM settings
        WHERE name = "lang";
        """

        select_theme = """
        SELECT name, value FROM settings
        WHERE name = "theme";
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
            cursor.execute(select_qemu_mips64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_11.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-mips64el slot already is in the database.")

            except:
                cursor.execute(insert_qemu_mips64)
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
            cursor.execute(select_qemu_mips)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_10.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-mips64el slot already is in the database.")

            except:
                cursor.execute(insert_qemu_mips)
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
            cursor.execute(select_qemu_sparc)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_12.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-arm slot already is in the database.")

            except:
                cursor.execute(insert_qemu_sparc)
                connection.commit()
                print("The query was executed successfully. The qemu-system-arm slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_sparc64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_13.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-arm slot already is in the database.")

            except:
                cursor.execute(insert_qemu_sparc64)
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

                elif result[0][1] == "fr":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Français":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "fr"

                elif result[0][1] == "es":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Español":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "es"

                elif result[0][1] == "pt":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Português":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "pt"

                elif result[0][1] == "it":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Italiano":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "it"

                elif result[0][1] == "ro":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Românã":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "ro"

                elif result[0][1] == "cz":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Čeština":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "cz"

                elif result[0][1] == "ru":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Русский":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "ru"

                elif result[0][1] == "uk":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Українська":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "uk"

                elif result[0][1] == "be":
                    while i < self.comboBox_4.count():
                        if self.comboBox_4.itemText(i) == "Беларуская":
                            self.comboBox_4.setCurrentIndex(i)
                            break

                        i += 1

                    langmode = "be"

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
            cursor.execute(select_theme)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The theme slot already is in the database.")
                print(result[0][1])

                if result[0][1] != "default":
                    for osTheme in self.osThemes:
                        if result[0][1].__contains__(osTheme):
                            try:
                                print(osTheme)
                                app.setStyle(osTheme)

                                i = 0
                                while i < self.comboBox_5.count():
                                    if self.comboBox_5.itemText(i) == osTheme:
                                        self.comboBox_5.setCurrentIndex(i)
                                        break

                                    i += 1
                            except:
                                print("Style couldn't be applied.")
                    
                    for userTheme in self.userThemeList:
                        if result[0][1].__contains__(userTheme):
                            try:
                                print(userTheme)
                                userThemeFile = "themes/" + userTheme + ".qss"

                                with open(userThemeFile, "r") as themeFile:
                                    style = themeFile.read()
                                    app.setStyleSheet(style)

                                i = 0
                                while i < self.comboBox_5.count():
                                    if self.comboBox_5.itemText(i) == userTheme:
                                        self.comboBox_5.setCurrentIndex(i)
                                        break

                                    i += 1
                            except:
                                print("Style couldn't be applied.")
                
                else:
                    with open("translations/systemdefault.txt", "r+") as sysDefFile:
                        sysDefContent = sysDefFile.read()

                    i = 0
                    while i < self.comboBox_5.count():
                        if sysDefContent.__contains__(self.comboBox_5.itemText(i)):
                            self.comboBox_5.setCurrentIndex(i)
                            break

                        i += 1

            except:
                cursor.execute(insert_theme)
                connection.commit()
                print("The query was executed successfully. The theme slot has been created.")
        
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
            cursor.execute(select09ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v1.0 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertKbdLayoutVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select11ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v1.1 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertAccelTypeVM)
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
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller, kbdtype, acceltype
            FROM virtualmachines WHERE name = '{selectedVM}'
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
                kbd_layout = result[0][21]
                accel_type = result[0][22]

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
                tempVmDefFile.write(kbd_layout + "\n")
                tempVmDefFile.write(accel_type + "\n")

            if usbtablet_wanted == 1:
                dialog3 = UsbTabletDepreciated(self)
                dialog3.exec()

            if os_is_win2k == 1:
                dialog3 = Win2KDepreciated(self)
                dialog3.exec()

            if cpu_of_vm == "Icelake-Client":
                dialog3 = IcelakeClientCPUDepreciation(self)
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

                elif architecture_of_vm == "ppc64" or architecture_of_vm == "mipsel" or architecture_of_vm == "mips":
                    if result_settings[i][0] == f"qemu-system-{architecture_of_vm}":
                        if result_settings[i][1] == "":
                            dialog = QemuSysMissing(self)
                            dialog.exec()
                            break

                        else:
                            dialog = StartVirtualMachineDialog(self)
                            dialog.exec()
                            break

                elif architecture_of_vm == "mips64" or architecture_of_vm == "sparc" or architecture_of_vm == "sparc64":
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
            linuxinitrid, linuxcmd, mousetype, cores, filebios, keyboardtype, usbsupport, usbcontroller, kbdtype, acceltype
            FROM virtualmachines WHERE name = '{selectedVM}'
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
                kbd_layout = result[0][21]
                accel_type = result[0][22]

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
                tempVmDefFile.write(kbd_layout + "\n")
                tempVmDefFile.write(accel_type + "\n")

            i = 0

            while i < len(result_settings):
                if result_settings[i][0] == "qemu-img":
                    if result_settings[i][1] == "":
                        dialog = QemuImgMissing(self)
                        dialog.exec()

                    else:
                        dialog = EditVMNewDialog(self)
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

    def set_qemu_mips64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_11.setText(filename)

    def set_qemu_mips_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_10.setText(filename)

    def set_qemu_aarch64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-aarch64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def set_qemu_arm_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-arm executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_7.setText(filename)

    def set_qemu_sparc_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-sparc executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_12.setText(filename)

    def set_qemu_sparc64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-sparc64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_13.setText(filename)

    def applyChangesQemu(self):
        pathQemuImg = self.lineEdit_5.text()
        pathQemuI386 = self.lineEdit_4.text()
        pathQemuX86_64 = self.lineEdit_3.text()
        pathQemuPpc = self.lineEdit_2.text()
        pathQemuPpc64 = self.lineEdit_8.text()
        pathQemuMips64El = self.lineEdit.text()
        pathQemuMipsEl = self.lineEdit_9.text()
        pathQemuMips64 = self.lineEdit_11.text()
        pathQemuMips = self.lineEdit_10.text()
        pathQemuAarch64 = self.lineEdit_6.text()
        pathQemuArm = self.lineEdit_7.text()
        pathQemuSparc = self.lineEdit_12.text()
        pathQemuSparc64 = self.lineEdit_13.text()

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

        qemu_mips64_update = f"""
        UPDATE settings
        SET value = '{pathQemuMips64}'
        WHERE name = 'qemu-system-mips64';
        """

        qemu_mips_update = f"""
        UPDATE settings
        SET value = '{pathQemuMips}'
        WHERE name = 'qemu-system-mips';
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

        qemu_sparc_update = f"""
        UPDATE settings
        SET value = '{pathQemuSparc}'
        WHERE name = 'qemu-system-sparc';
        """

        qemu_sparc64_update = f"""
        UPDATE settings
        SET value = '{pathQemuSparc64}'
        WHERE name = 'qemu-system-sparc64';
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
            cursor.execute(qemu_mips64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_mips_update)
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

        try:
            cursor.execute(qemu_sparc_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_sparc64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def applyGeneric(self):
        with open("translations/systemdefault.txt", "r+", encoding="utf8") as sysDefFile:
            sysDefContent = sysDefFile.read()

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

        language_fr = f"""
        UPDATE settings
        SET value = 'fr'
        WHERE name = 'lang';
        """

        language_es = f"""
        UPDATE settings
        SET value = 'es'
        WHERE name = 'lang';
        """

        language_ro = f"""
        UPDATE settings
        SET value = 'ro'
        WHERE name = 'lang';
        """

        language_ru = f"""
        UPDATE settings
        SET value = 'ru'
        WHERE name = 'lang';
        """

        language_be = f"""
        UPDATE settings
        SET value = 'be'
        WHERE name = 'lang';
        """

        language_cz = f"""
        UPDATE settings
        SET value = 'cz'
        WHERE name = 'lang';
        """

        language_pt = f"""
        UPDATE settings
        SET value = 'pt'
        WHERE name = 'lang';
        """

        language_it = f"""
        UPDATE settings
        SET value = 'it'
        WHERE name = 'lang';
        """

        theme_default = f"""
        UPDATE settings
        SET value = 'default'
        WHERE name = 'theme';
        """

        theme_custom = f"""
        UPDATE settings
        SET value = '{self.comboBox_5.currentText()}'
        WHERE name = 'theme';
        """

        connection = self.connection
        cursor = connection.cursor()

        if sysDefContent.__contains__(self.comboBox_4.currentText()): #self.comboBox_4.currentText() == "System default" or self.comboBox_4.currentText() == "Systemstandard":
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

        elif self.comboBox_4.currentText() == "Français":
            langmode = "fr"

            try:
                cursor.execute(language_fr)
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

        elif self.comboBox_4.currentText() == "Español":
            langmode = "es"

            try:
                cursor.execute(language_es)
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

        elif self.comboBox_4.currentText() == "Português":
            langmode = "pt"

            try:
                cursor.execute(language_pt)
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

        elif self.comboBox_4.currentText() == "Italiano":
            langmode = "it"

            try:
                cursor.execute(language_pt)
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

        elif self.comboBox_4.currentText() == "Românã":
            langmode = "ro"

            try:
                cursor.execute(language_ro)
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

        elif self.comboBox_4.currentText() == "Беларуская":
            langmode = "be"

            try:
                cursor.execute(language_be)
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

        elif self.comboBox_4.currentText() == "Русский":
            langmode = "ru"

            try:
                cursor.execute(language_ru)
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

        elif self.comboBox_4.currentText() == "Čeština":
            langmode = "cz"

            try:
                cursor.execute(language_cz)
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

        if sysDefContent.__contains__(self.comboBox_5.currentText()): #self.comboBox_5.currentText() == "System default" or self.comboBox_5.currentText() == "Systemstandard":
            try:
                cursor.execute(theme_default)
                connection.commit()
                
                app.setStyle(self.defaultTheme)

                print("The query was executed successfully.")

                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
                dialog.exec()
        
        else:
            try:
                cursor.execute(theme_custom)
                connection.commit()
                
                for osTheme in self.osThemes:
                    if self.comboBox_5.currentText() == osTheme:
                        app.setStyle(self.comboBox_5.currentText())

                        dialog = SettingsRequireEmuGUIReboot(self)
                        dialog.exec()

                for userTheme in self.userThemeList:
                    if self.comboBox_5.currentText() == userTheme:
                        print(userTheme)
                        userThemeFile = "themes/" + userTheme + ".qss"

                        with open(userThemeFile, "r") as themeFile:
                            style = themeFile.read()
                            app.setStyleSheet(style)

                print("The query was executed successfully.")

            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

            except:
                dialog = SettingsRequireEmuGUIReboot(self)
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

    def toGithub(self):
        webbrowser.open_new_tab("https://www.github.com/Tech-FZ/EmuGUI")
    
    def toDiscord(self):
        webbrowser.open_new_tab("https://discord.gg/rTGpYCwF89")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())