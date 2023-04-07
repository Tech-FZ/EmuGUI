from uiScripts.ui_SettingsRestart import Ui_Dialog
from PySide6.QtWidgets import *
from PySide6 import QtGui

class SettingsRequireEmuGUIReboot(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        try:
            super().__init__(parent)

        except:
            super().__init__()
            
        self.setupUi(self)
        self.setWindowTitle("EmuGUI Settings")
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)