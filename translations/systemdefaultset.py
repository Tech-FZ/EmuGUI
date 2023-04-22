def sysDefSet(finalStr, comboBox, comboBoxIndex):
    with open("translations/systemdefault.txt", "r+") as sysDefFile:
        sysDefContent = sysDefFile.read()
    
    if sysDefContent.__contains__(comboBox.itemText(comboBoxIndex)):
        comboBox.setItemText(comboBoxIndex, finalStr)