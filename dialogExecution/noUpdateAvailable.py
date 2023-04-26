from PySide6.QtWidgets import *
from PySide6 import QtGui
from uiScripts.ui_NoUpdate import Ui_Dialog
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific
    
import sqlite3
import translations.de
import translations.uk
import translations.en
import locale

class NoUpdateAvailable(QDialog, Ui_Dialog):
    def __init__(self, arg):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("EmuGUI Update")
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

                if result[0][1] == "en":
                    langmode = "en"

                elif result[0][1] == "de":
                    langmode = "de"

                elif result[0][1] == "uk":
                    langmode = "uk"

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
                translations.de.translateNoUpdateAvailableDE(self)

            elif languageToUse.startswith("uk"):
                translations.uk.translateNoUpdateAvailableUK(self)

            else:
                translations.en.translateNoUpdateAvailableEN(self)
        
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
                        translations.de.translateNoUpdateAvailableDE(self)

                    elif languageToUse.startswith("uk"):
                        translations.uk.translateNoUpdateAvailableUK(self)

                    else:
                        translations.en.translateNoUpdateAvailableEN(self)
            
            except:
                print("Translation can't be figured out. Using English language.")
                translations.en.translateNoUpdateAvailableEN(self)