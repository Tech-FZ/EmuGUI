import random
import platform
import datetime
import errors.logID

if platform.system() == "Windows":
    import platformSpecific.windowsSpecific

else:
    import platformSpecific.unixSpecific

class LogMan:
    def __init__(self):
        self.logFile = ""

    def generateLogID(self):
        possible_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        logID = ""
    
        for k in range(0, 32):
            logID = logID + possible_chars[random.randint(0, len(possible_chars) - 1)]
        
        errors.logID.logID = logID

    def setLogFile(self):
        if platform.system() == "Windows":
            logFile = platformSpecific.windowsSpecific.windowsLogFile(errors.logID.logID)

        else:
            logFile = platformSpecific.unixSpecific.unixLogFile(errors.logID.logID)

        return logFile

    def writeToLogFile(self, text):
        with open(self.logFile, "a+") as logger:
            logger.write(
                datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + " " + text + "\n")