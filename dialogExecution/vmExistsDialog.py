from uiScripts.ui_VmExists import Ui_Dialog
from PySide6.QtWidgets import *

class VmAlreadyExistsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("EmuGUI - VM already exists")
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)