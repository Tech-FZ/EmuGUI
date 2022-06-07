import os
import sqlite3

def setupUnixBackend():
    userName = os.getlogin()
    connection = None

    try:
        if userName == "root":
            connection = sqlite3.connect(f"/{userName}/Documents/EmuGUI/virtual_machines.sqlite")

        else:
            connection = sqlite3.connect(f"/home/{userName}/Documents/EmuGUI/virtual_machines.sqlite")

        print("Connection established.")
    
    except sqlite3.Error as e:
        print(f"The SQLite module encountered an error: {e}. Trying to create the file.")

        try:
            if userName == "root":
                os.mkdir(f"/{userName}/Documents/EmuGUI")
                file = open(f"/{userName}/Documents/EmuGUI/virtual_machines.sqlite", "w+")
                file.close()

            else:
                os.mkdir(f"/home/{userName}/Documents/EmuGUI")
                file = open(f"/home/{userName}/Documents/EmuGUI/virtual_machines.sqlite", "w+")
                file.close()
        
        except:
            print("EmuGUI wasn't able to create the file.")

        try:
            if userName == "root":
                connection = sqlite3.connect(f"/{userName}/Documents/EmuGUI/virtual_machines.sqlite")

            else:
                connection = sqlite3.connect(f"/home/{userName}/Documents/EmuGUI/virtual_machines.sqlite")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")
    
    return connection

def unixTempVmStarterFile():
    userName = os.getlogin()

    if userName == "root":
        fileName = f"/{userName}/Documents/EmuGUI/vmstart.txt"

    else:
        fileName = f"/home/{userName}/Documents/EmuGUI/vmstart.txt"

    return fileName