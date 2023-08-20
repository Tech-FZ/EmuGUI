import os
import pwd
import sqlite3

def setupUnixBackend():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]
    
    connection = None

    try:
        if userName == "root":
            connection = sqlite3.connect(f"/{userName}/EmuGUI/virtual_machines.sqlite")

        else:
            connection = sqlite3.connect(f"/home/{userName}/EmuGUI/virtual_machines.sqlite")

        print("Connection established.")
    
    except sqlite3.Error as e:
        print(f"The SQLite module encountered an error: {e}. Trying to create the file.")

        try:
            if userName == "root":
                os.mkdir(f"/{userName}/EmuGUI")
                file = open(f"/{userName}/EmuGUI/virtual_machines.sqlite", "w+")
                file.close()

            else:
                os.mkdir(f"/home/{userName}/EmuGUI")
                file = open(f"/home/{userName}/EmuGUI/virtual_machines.sqlite", "w+")
                file.close()
        
        except:
            print("EmuGUI wasn't able to create the file.")

        try:
            if userName == "root":
                connection = sqlite3.connect(f"/{userName}/EmuGUI/virtual_machines.sqlite")

            else:
                connection = sqlite3.connect(f"/home/{userName}/EmuGUI/virtual_machines.sqlite")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
    
    return connection

def unixTempVmStarterFile():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/vmstart.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/vmstart.txt"

    return fileName

def unixLanguageFile():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/lang.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/lang.txt"
        
    return fileName

def unixUpdateFile():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/update.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/update.txt"

    return fileName

def unixExportFile():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/vmdef.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/vmdef.txt"
        
    return fileName

def unixErrorFile():
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/error.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/error.txt"
        
    return fileName

def unixLogFile(logID):
    try:
        userName = os.getlogin()
    
    except:
        userName = pwd.getpwuid(os.getuid())[0]

    if userName == "root":
        fileName = f"/{userName}/EmuGUI/log-{logID}.txt"

    else:
        fileName = f"/home/{userName}/EmuGUI/log-{logID}.txt"
        
    return fileName