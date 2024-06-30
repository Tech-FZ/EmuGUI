from uiScripts.ui_ErrDialog import Ui_Dialog
from PySide6.QtWidgets import *
from PySide6 import QtGui
import platform

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific

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
import sqlite3
import services.pathfinder as pf

class ErrDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        self.exec_folder = pf.retrieveExecFolder()
        self.setWindowTitle("EmuGUI - Error")
        
        try:
            self.setWindowIcon(QtGui.QIcon(f"{self.exec_folder}EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()
        self.vmSpecs = self.readTempVmFile()
        self.langDetect()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.pushBtnClicked)

    def pushBtnClicked(self):
        if self.vmSpecs[0].startswith("C"):
            exit()

        else:
            self.close()

    def readTempVmFile(self):
        # Searching temporary files
        if platform.system() == "Windows":
            tempVmDef = platformSpecific.windowsSpecific.windowsErrorFile()
        
        else:
            tempVmDef = platformSpecific.unixSpecific.unixErrorFile()

        vmSpecs = []

        with open(tempVmDef, "r+") as tempVmDefFile:
            vmSpecsRaw = tempVmDefFile.readlines()

        for vmSpec in vmSpecsRaw:
            vmSpecNew = vmSpec.replace("\n", "")
            vmSpecs.append(vmSpecNew)

        return vmSpecs

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

                elif result[0][1] == "it":
                    langmode = "it"

                elif result[0][1] == "pl":
                    langmode = "pl"

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
                translations.de.translateErrDialogDE(self, self.vmSpecs[0])

            elif languageToUse.startswith("uk"):
                translations.uk.translateErrDialogUK(self, self.vmSpecs[0])

            elif languageToUse.startswith("fr"):
                translations.fr.translateErrDialogFR(self, self.vmSpecs[0])

            elif languageToUse.startswith("es"):
                translations.es.translateErrDialogES(self, self.vmSpecs[0])

            elif languageToUse.startswith("ro"):
                translations.ro.translateErrDialogRO(self, self.vmSpecs[0])

            elif languageToUse.startswith("ru"):
                translations.ru.translateErrDialogRU(self, self.vmSpecs[0])

            elif languageToUse.startswith("be"):
                translations.be.translateErrDialogBE(self, self.vmSpecs[0])

            elif languageToUse.startswith("cz"):
                translations.cz.translateErrDialogCZ(self, self.vmSpecs[0])

            elif languageToUse.startswith("pt"):
                translations.pt.translateErrDialogPT(self, self.vmSpecs[0])

            elif languageToUse.startswith("pl"):
                translations.pl.translateErrDialogPL(self, self.vmSpecs[0])

            elif languageToUse.startswith("it"):
                translations.it.translateErrDialogIT(self, self.vmSpecs[0])

            else:
                translations.en.translateErrDialogEN(self, self.vmSpecs[0])
        
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
                        translations.de.translateErrDialogDE(self, self.vmSpecs[0])

                    elif languageToUse.startswith("uk"):
                        translations.uk.translateErrDialogUK(self, self.vmSpecs[0])

                    elif languageToUse.startswith("fr"):
                        translations.fr.translateErrDialogFR(self, self.vmSpecs[0])

                    elif languageToUse.startswith("es"):
                        translations.es.translateErrDialogES(self, self.vmSpecs[0])

                    elif languageToUse.startswith("ro"):
                        translations.ro.translateErrDialogRO(self, self.vmSpecs[0])

                    elif languageToUse.startswith("ru"):
                        translations.ru.translateErrDialogRU(self, self.vmSpecs[0])

                    elif languageToUse.startswith("be"):
                        translations.be.translateErrDialogBE(self, self.vmSpecs[0])

                    elif languageToUse.startswith("cz"):
                        translations.cz.translateErrDialogCZ(self, self.vmSpecs[0])

                    elif languageToUse.startswith("pt"):
                        translations.pt.translateErrDialogPT(self, self.vmSpecs[0])

                    elif languageToUse.startswith("pl"):
                        translations.pl.translateErrDialogPL(self, self.vmSpecs[0])

                    elif languageToUse.startswith("it"):
                        translations.it.translateErrDialogIT(self, self.vmSpecs[0])

                    else:
                        translations.en.translateErrDialogEN(self, self.vmSpecs[0])
            
            except:
                print("Translation can't be figured out. Using English language.")
                translations.en.translateErrDialogEN(self, self.vmSpecs[1])