from PySide6.QtWidgets import *
from uiScripts.ui_NoUpdate import Ui_Dialog

class NoUpdateAvailable(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)