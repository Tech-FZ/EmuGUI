import sqlite3
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import QTimer
import platform
import platformSpecific.windowsSpecific
import platformSpecific.unixSpecific
from uiScripts.ui_Main import Ui_MainWindow
from dialogExecution.newVirtualMachine import NewVirtualMachineDialog
from uiScripts.ui_SettingsPending1 import Ui_Dialog
from dialogExecution.startVirtualMachine import StartVirtualMachineDialog
from dialogExecution.editVirtualMachine import EditVirtualMachineDialog

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateVmList)
        self.label_8.setText("EmuGUI v0.3")
        self.setWindowTitle("EmuGUI")

        if platform.system() == "Windows":
            self.connection = platformSpecific.windowsSpecific.setupWindowsBackend()
        
        else:
            self.connection = platformSpecific.unixSpecific.setupUnixBackend()
        
        self.prepareDatabase(self.connection)
        self.updateVmList()

    def connectSignalsSlots(self):
        self.pushButton_8.clicked.connect(self.createNewVM)
        self.pushButton.clicked.connect(self.set_qemu_img_path)
        self.pushButton_2.clicked.connect(self.set_qemu_i386_path)
        self.pushButton_3.clicked.connect(self.set_qemu_x86_64_path)
        self.pushButton_4.clicked.connect(self.set_qemu_ppc_path)
        self.pushButton_5.clicked.connect(self.set_qemu_mips64el_path)
        self.pushButton_6.clicked.connect(self.applyChangesQemu)
        self.pushButton_9.clicked.connect(self.startVM)
        self.pushButton_11.clicked.connect(self.deleteVM)
        self.pushButton_10.clicked.connect(self.editVM)
        self.pushButton_7.clicked.connect(self.set_qemu_aarch64_path)

    def prepareDatabase(self, connection):
        create_settings_table = """
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT
        );
        """

        create_vm_table = """
        CREATE TABLE IF NOT EXISTS virtualmachines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            architecture TEXT NOT NULL,
            machine TEXT NOT NULL,
            cpu TEXT NOT NULL,
            ram INTEGER NOT NULL,
            hda TEXT,
            vga TEXT NOT NULL,
            net TEXT,
            usbtablet INTEGER NOT NULL,
            win2k INTEGER NOT NULL,
            dirbios TEXT,
            additionalargs TEXT,
            sound TEXT NOT NULL,
            linuxkernel TEXT NOT NULL,
            linuxinitrid TEXT NOT NULL,
            linuxcmd TEXT NOT NULL,
            mousetype TEXT NOT NULL,
            cores INT DEFAULT 1 NOT NULL,
            filebios TEXT DEFAULT "" NOT NULL
        );
        """

        select02ColumnsVM = """
        SELECT sound, linuxkernel, linuxinitrid, linuxcmd FROM virtualmachines;
        """

        select03ColumnsVM = """
        SELECT mousetype FROM virtualmachines;
        """

        select03ColumnsVM2 = """
        SELECT cores, filebios FROM virtualmachines;
        """

        insertSoundColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN sound TEXT DEFAULT "none" NOT NULL;
        """

        insertLinuxKernelColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxkernel TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxInitridColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxinitrid TEXT DEFAULT "" NOT NULL;
        """

        insertLinuxCmdColVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN linuxcmd TEXT DEFAULT "" NOT NULL;
        """

        insertMouseTypeVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN mousetype TEXT DEFAULT "PS/2 Mouse" NOT NULL;
        """

        insertCpuCoresVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN cores TEXT DEFAULT 1 NOT NULL;
        """

        insertBiosFileVM = """
        ALTER TABLE virtualmachines
        ADD COLUMN filebios TEXT DEFAULT "" NOT NULL;
        """

        insert_qemu_img = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-img"
        );
        """

        insert_qemu_i386 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-i386"
        );
        """

        insert_qemu_x86_64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-x86_64"
        );
        """

        insert_qemu_ppc = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-ppc"
        );
        """

        insert_qemu_mips64el = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-mips64el"
        );
        """

        insert_qemu_aarch64 = """
        INSERT INTO settings (
            name
        ) VALUES (
            "qemu-system-aarch64"
        );
        """

        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        select_qemu_img = """
        SELECT name, value FROM settings
        WHERE name = "qemu-img";
        """

        select_qemu_i386 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-i386";
        """

        select_qemu_x86_64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-x86_64";
        """

        select_qemu_ppc = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-ppc";
        """

        select_qemu_mips64el = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-mips64el";
        """

        select_qemu_aarch64 = """
        SELECT name, value FROM settings
        WHERE name = "qemu-system-aarch64";
        """

        cursor = connection.cursor()

        try:
            cursor.execute(create_settings_table)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(create_vm_table)
            connection.commit()
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_img)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_5.setText(result[0][1])
                print("The query was executed successfully. The qemu-img slot already is in the database.")

            except:
                cursor.execute(insert_qemu_img)
                connection.commit()
                print("The query was executed successfully. The qemu-img slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_i386)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_4.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-i386 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_i386)
                connection.commit()
                print("The query was executed successfully. The qemu-system-i386 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_x86_64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_3.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-x86_64 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_x86_64)
                connection.commit()
                print("The query was executed successfully. The qemu-system-x86_64 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_ppc)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_2.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-ppc slot already is in the database.")

            except:
                cursor.execute(insert_qemu_ppc)
                connection.commit()
                print("The query was executed successfully. The qemu-system-ppc slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_mips64el)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-mips64el slot already is in the database.")

            except:
                cursor.execute(insert_qemu_mips64el)
                connection.commit()
                print("The query was executed successfully. The qemu-system-mips64el slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select_qemu_aarch64)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                self.lineEdit_6.setText(result[0][1])
                print("The query was executed successfully. The qemu-system-aarch64 slot already is in the database.")

            except:
                cursor.execute(insert_qemu_aarch64)
                connection.commit()
                print("The query was executed successfully. The qemu-system-aarch64 slot has been created.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select02ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The v0.2 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertSoundColVM)
                connection.commit()

                cursor.execute(insertLinuxKernelColVM)
                connection.commit()

                cursor.execute(insertLinuxInitridColVM)
                connection.commit()

                cursor.execute(insertLinuxCmdColVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select03ColumnsVM)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The first v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertMouseTypeVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(select03ColumnsVM2)
            connection.commit()
            result = cursor.fetchall()

            try:
                qemu_img_slot = str(result[0])
                print("The query was executed successfully. The second v0.3 feature columns already are in the VM table.")

            except:
                pass
        
        except sqlite3.Error as e:
            try:
                cursor.execute(insertCpuCoresVM)
                connection.commit()

                cursor.execute(insertBiosFileVM)
                connection.commit()
                print("The queries were executed successfully. The missing features have been added to the database.")
            
            except sqlite3.Error as e:
                print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            print(cursor.fetchall())
            print("The query was executed successfully.")
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def createNewVM(self):
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result = cursor.fetchall()

            print(result)

            if result[0][1] == None or result[1][1] == None or result[2][1] == None or result[3][1] == None or result[4][1] == None or result[5][1] == None:
                dialog2 = SettingsPending1Dialog(self)
                dialog2.exec()

            else:
                dialog = NewVirtualMachineDialog(self)
                dialog.exec()
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def startVM(self):
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result = cursor.fetchall()

            print(result)

            if result[0][1] == None or result[1][1] == None or result[2][1] == None or result[3][1] == None or result[4][1] == None or result[5][1] == None:
                dialog2 = SettingsPending1Dialog(self)
                dialog2.exec()

            else:
                selectedVM = self.listView.currentIndex().data()
                print(selectedVM)

                get_vm_to_start = f"""
                SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
                linuxinitrid, linuxcmd, mousetype, cores, filebios FROM virtualmachines
                WHERE name = '{selectedVM}'
                """

                try:
                    cursor.execute(get_vm_to_start)
                    connection.commit()
                    result = cursor.fetchall()

                    print(result)

                    architecture_of_vm = result[0][0]
                    machine_of_vm = result[0][1]
                    cpu_of_vm = result[0][2]
                    ram_of_vm = result[0][3]
                    hda_of_vm = result[0][4]
                    vga_of_vm = result[0][5]
                    net_of_vm = result[0][6]
                    usbtablet_wanted = result[0][7]
                    os_is_win2k = result[0][8]
                    dir_bios = result[0][9]
                    additional_arguments = result[0][10]
                    sound_card = result[0][11]
                    linux_kernel = result[0][12]
                    linux_initrid = result[0][13]
                    linux_cmd = result[0][14]
                    mouse_type = result[0][15]
                    cpu_cores = result[0][16]
                    file_bios = result[0][17]

                except sqlite3.Error as e:
                    print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
                else:
                    tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
                with open(tempVmDef, "w+") as tempVmDefFile:
                    tempVmDefFile.write(selectedVM + "\n")
                    tempVmDefFile.write(architecture_of_vm + "\n")
                    tempVmDefFile.write(machine_of_vm + "\n")
                    tempVmDefFile.write(cpu_of_vm + "\n")
                    tempVmDefFile.write(str(ram_of_vm) + "\n")
                    tempVmDefFile.write(hda_of_vm + "\n")
                    tempVmDefFile.write(vga_of_vm + "\n")
                    tempVmDefFile.write(net_of_vm + "\n")
                    tempVmDefFile.write(str(usbtablet_wanted) + "\n")
                    tempVmDefFile.write(str(os_is_win2k) + "\n")
                    tempVmDefFile.write(dir_bios + "\n")
                    tempVmDefFile.write(additional_arguments + "\n")
                    tempVmDefFile.write(sound_card + "\n")
                    tempVmDefFile.write(linux_kernel + "\n")
                    tempVmDefFile.write(linux_initrid + "\n")
                    tempVmDefFile.write(linux_cmd + "\n")
                    tempVmDefFile.write(mouse_type + "\n")
                    tempVmDefFile.write(str(cpu_cores) + "\n")
                    tempVmDefFile.write(str(file_bios) + "\n")

                dialog = StartVirtualMachineDialog(self)
                dialog.exec()
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def editVM(self):
        debug_db_settings = """
        SELECT name, value FROM settings;
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(debug_db_settings)
            connection.commit()
            result = cursor.fetchall()

            print(result)

            if result[0][1] == None or result[1][1] == None or result[2][1] == None or result[3][1] == None or result[4][1] == None or result[5][1] == None:
                dialog2 = SettingsPending1Dialog(self)
                dialog2.exec()

            else:
                selectedVM = self.listView.currentIndex().data()
                print(selectedVM)

                get_vm_to_start = f"""
                SELECT architecture, machine, cpu, ram, hda, vga, net, usbtablet, win2k, dirbios, additionalargs, sound, linuxkernel,
                linuxinitrid, linuxcmd, mousetype, cores, filebios FROM virtualmachines
                WHERE name = '{selectedVM}'
                """

                try:
                    cursor.execute(get_vm_to_start)
                    connection.commit()
                    result = cursor.fetchall()

                    print(result)

                    architecture_of_vm = result[0][0]
                    machine_of_vm = result[0][1]
                    cpu_of_vm = result[0][2]
                    ram_of_vm = result[0][3]
                    hda_of_vm = result[0][4]
                    vga_of_vm = result[0][5]
                    net_of_vm = result[0][6]
                    usbtablet_wanted = result[0][7]
                    os_is_win2k = result[0][8]
                    dir_bios = result[0][9]
                    additional_arguments = result[0][10]
                    sound_card = result[0][11]
                    linux_kernel = result[0][12]
                    linux_initrid = result[0][13]
                    linux_cmd = result[0][14]
                    mouse_type = result[0][15]
                    cpu_cores = result[0][16]
                    file_bios = result[0][17]

                except sqlite3.Error as e:
                    print(f"The SQLite module encountered an error: {e}.")

                if platform.system() == "Windows":
                    tempVmDef = platformSpecific.windowsSpecific.windowsTempVmStarterFile()
        
                else:
                    tempVmDef = platformSpecific.unixSpecific.unixTempVmStarterFile()
                
                with open(tempVmDef, "w+") as tempVmDefFile:
                    tempVmDefFile.write(selectedVM + "\n")
                    tempVmDefFile.write(architecture_of_vm + "\n")
                    tempVmDefFile.write(machine_of_vm + "\n")
                    tempVmDefFile.write(cpu_of_vm + "\n")
                    tempVmDefFile.write(str(ram_of_vm) + "\n")
                    tempVmDefFile.write(hda_of_vm + "\n")
                    tempVmDefFile.write(vga_of_vm + "\n")
                    tempVmDefFile.write(net_of_vm + "\n")
                    tempVmDefFile.write(str(usbtablet_wanted) + "\n")
                    tempVmDefFile.write(str(os_is_win2k) + "\n")
                    tempVmDefFile.write(dir_bios + "\n")
                    tempVmDefFile.write(additional_arguments + "\n")
                    tempVmDefFile.write(sound_card + "\n")
                    tempVmDefFile.write(linux_kernel + "\n")
                    tempVmDefFile.write(linux_initrid + "\n")
                    tempVmDefFile.write(linux_cmd + "\n")
                    tempVmDefFile.write(mouse_type + "\n")
                    tempVmDefFile.write(str(cpu_cores) + "\n")
                    tempVmDefFile.write(file_bios + "\n")

                dialog = EditVirtualMachineDialog(self)
                dialog.exec()
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def set_qemu_img_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-img executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_5.setText(filename)

    def set_qemu_i386_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-i386 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_4.setText(filename)

    def set_qemu_x86_64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-x86_64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_3.setText(filename)

    def set_qemu_ppc_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-ppc executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_2.setText(filename)

    def set_qemu_mips64el_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-mips64el executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit.setText(filename)

    def set_qemu_aarch64_path(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Select qemu-system-aarch64 executable', dir='.', filter='Windows executables (*.exe);;All files (*.*)')

        if filename:
            self.lineEdit_6.setText(filename)

    def applyChangesQemu(self):
        pathQemuImg = self.lineEdit_5.text()
        pathQemuI386 = self.lineEdit_4.text()
        pathQemuX86_64 = self.lineEdit_3.text()
        pathQemuPpc = self.lineEdit_2.text()
        pathQemuMips64El = self.lineEdit.text()
        pathQemuAarch64 = self.lineEdit_6.text()

        qemu_img_update = f"""
        UPDATE settings
        SET value = '{pathQemuImg}'
        WHERE name = 'qemu-img';
        """

        qemu_i386_update = f"""
        UPDATE settings
        SET value = '{pathQemuI386}'
        WHERE name = 'qemu-system-i386';
        """

        qemu_x86_64_update = f"""
        UPDATE settings
        SET value = '{pathQemuX86_64}'
        WHERE name = 'qemu-system-x86_64';
        """

        qemu_ppc_update = f"""
        UPDATE settings
        SET value = '{pathQemuPpc}'
        WHERE name = 'qemu-system-ppc';
        """

        qemu_mips64el_update = f"""
        UPDATE settings
        SET value = '{pathQemuMips64El}'
        WHERE name = 'qemu-system-mips64el';
        """

        qemu_aarch64_update = f"""
        UPDATE settings
        SET value = '{pathQemuAarch64}'
        WHERE name = 'qemu-system-aarch64';
        """

        connection = self.connection
        cursor = connection.cursor()

        try:
            cursor.execute(qemu_img_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_i386_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_x86_64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_ppc_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_mips64el_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        try:
            cursor.execute(qemu_aarch64_update)
            connection.commit()
            print("The query was executed successfully.")

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

    def updateVmList(self):
        try:
            self.timer.stop()

        except:
            pass

        connection = self.connection
        cursor = connection.cursor()

        sel_vm_names = """
        SELECT name FROM virtualmachines;
        """

        try:
            cursor.execute(sel_vm_names)
            connection.commit()
            result = cursor.fetchall()
            i = 0
            entries = []
            model = QtGui.QStandardItemModel()
            self.listView.setModel(model)

            while i < len(result):
                try:
                    entries.append(str(result[i][0]))
                    print("The query was executed successfully.")

                except:
                    pass

                i += 1

            for entry in entries:
                item = QtGui.QStandardItem(entry)
                model.appendRow(item)
        
        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

        self.timer.start(10000)

    def deleteVM(self):
        connection = self.connection
        cursor = connection.cursor()
        selectedVM = self.listView.currentIndex().data()
        print(selectedVM)

        get_vm_to_start = f"""
        DELETE FROM virtualmachines
        WHERE name = '{selectedVM}'
        """

        try:
            cursor.execute(get_vm_to_start)
            connection.commit()
            print("The query was executed successfully.")
            self.updateVmList()

        except sqlite3.Error as e:
            print(f"The SQLite module encountered an error: {e}.")

class SettingsPending1Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("EmuGUI - Settings pending")
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())