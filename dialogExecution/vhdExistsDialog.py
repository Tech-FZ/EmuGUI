from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_VhdExists import Ui_Dialog
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
import sqlite3
import translations.de
import translations.uk
import translations.en
import locale

class VhdAlreadyExists(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("EmuGUI - This virtual hard disk exists")
        self.langDetect()
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.overwriteDisk)
        self.pushButton_2.clicked.connect(self.keepDisk)

    def keepDisk(self):
        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
        
        with open(tempVmDef, "w+") as tempVmDefFile:
            tempVmDefFile.write("keep")

        self.close()

    def overwriteDisk(self):
        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()

        with open(tempVmDef, "w+") as tempVmDefFile:
            tempVmDefFile.write("overwrite")

        self.close()

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
            translations.de.translateVhdExistsDE(self)

        elif languageToUse.startswith("uk"):
            translations.uk.translateVhdExistsUK(self)

        else:
            translations.en.translateVhdExistsEN(self)