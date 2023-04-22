from uiScripts.ui_Win81SupportNearsEnd import Ui_Dialog
from PySide6.QtWidgets import *
from PySide6 import QtGui

class Win812012R2NearEOS(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("EmuGUI - OS Support")
        
        try:
            self.setWindowIcon(QtGui.QIcon("EmuGUI.png"))

        except:
            pass
        
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)