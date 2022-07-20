from uiScripts.ui_USBTabletCheckboxDepreciated import Ui_Dialog
from PySide6.QtWidgets import *
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific

class UsbTabletDepreciated(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.vmSpecs = self.readTempVmFile()
        self.setWindowTitle(f"EmuGUI - {self.vmSpecs[0]} uses a depreciated feature")
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)

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