import os
import sqlite3

def setupWindowsBackend():
    userName = os.getlogin()
    connection = None

    try:
        connection = sqlite3.connect(f"C:\\Users\\{userName}\\Documents\\EmuGUI\\virtual_machines.sqlite")
        print("Connection established.")
    
    except sqlite3.Error as e:
        print(f"The SQLite module encountered an error: {e}. Trying to create the file.")

        try:
            os.mkdir(f"C:\\Users\\{userName}\\Documents\\EmuGUI")
            file = open(f"C:\\Users\\{userName}\\Documents\\EmuGUI\\virtual_machines.sqlite", "w+")
            file.close()
        
        except:
            print("EmuGUI wasn't able to create the file.")

        try:
            connection = sqlite3.connect(f"C:\\Users\\{userName}\\Documents\\EmuGUI\\virtual_machines.sqlite")
            print("Connection established.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
    
    return connection

def windowsTempVmStarterFile():
    userName = os.getlogin()
    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\vmstart.txt"
    return fileName

def windowsLanguageFile():
    userName = os.getlogin()
    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\lang.txt"
    return fileName

def windowsUpdateFile():
    userName = os.getlogin()
    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\update.txt"
    return fileName

def windowsExportFile():
    userName = os.getlogin()
    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\vmdef.txt"
    return fileName

def windowsErrorFile():
    userName = os.getlogin()

    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\error.txt"
        
    return fileName

def windowsLogFile(logID):
    userName = os.getlogin()

    fileName = f"C:\\Users\\{userName}\\Documents\\EmuGUI\\log-{logID}.txt"
        
    return fileName