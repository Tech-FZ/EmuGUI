import services.pathfinder as pf

def sysDefSet(finalStr, comboBox, comboBoxIndex):
    exec_folder = pf.retrieveExecFolder()
    with open(f"{exec_folder}translations/systemdefault.txt", "r+", encoding="utf8") as sysDefFile:
        sysDefContent = sysDefFile.read()
    
    if sysDefContent.__contains__(comboBox.itemText(comboBoxIndex)):
        comboBox.setItemText(comboBoxIndex, finalStr)