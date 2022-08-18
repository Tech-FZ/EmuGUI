def translateMainDE(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Hauptmenü")
    window.tabWidget.setTabText(1, "Einstellungen")

    # Main tab
    window.pushButton_8.setText("Neue virtuelle Maschine")
    window.pushButton_9.setText("Virtuelle Maschine starten")
    window.pushButton_10.setText("Ausgewählte virtuelle Maschine bearbeiten")
    window.pushButton_11.setText("Ausgewählte virtuelle Maschine löschen")

    # Settings tabs
    window.tabWidget_2.setTabText(0, "Allgemein")
    window.tabWidget_2.setTabText(3, "Über EmuGUI")

    # General tab
    window.label_15.setText("Sprache")
    window.pushButton_15.setText("Übernehmen")

    # QEMU tab
    window.label.setText("qemu-img-Pfad")
    window.label_2.setText("qemu-system-i386-Pfad")
    window.label_3.setText("qemu-system-x86_64-Pfad")
    window.label_4.setText("qemu-system-ppc-Pfad")
    window.label_5.setText("qemu-system-mips64el-Pfad")
    window.label_9.setText("qemu-system-aarch64-Pfad")
    window.label_11.setText("qemu-system-arm-Pfad")
    window.label_16.setText("qemu-system-ppc64-Pfad")
    window.label_17.setText("qemu-system-mipsel-Pfad")

    window.pushButton.setText("Durchsuchen")
    window.pushButton_2.setText("Durchsuchen")
    window.pushButton_3.setText("Durchsuchen")
    window.pushButton_4.setText("Durchsuchen")
    window.pushButton_5.setText("Durchsuchen")
    window.pushButton_7.setText("Durchsuchen")
    window.pushButton_12.setText("Durchsuchen")
    window.pushButton_16.setText("Durchsuchen")
    window.pushButton_17.setText("Durchsuchen")
    window.pushButton_6.setText("Übernehmen")

    # Update tab
    window.label_12.setText("Update-Spiegel")
    window.label_13.setText("Häufigkeit der Update-Benachrichtigungen")
    window.label_14.setText("Update-Kanal")

    window.pushButton_13.setText("Nach Updates suchen")
    window.pushButton_14.setText("Übernehmen")

    # About tab
    window.label_7.setText("Basierend auf Python- und PyQt-Technologien, lizenziert unter GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNUNG: Das Programm kommt, sofern das Gesetz es zulässt, OHNE JEGLICHE GARANTIE. Bitte sehen Sie für Details die GNU GPL-Lizenz ein.
        """
        )

def translateNewVmDE(window):
    # First page
    window.label.setText("Name")
    window.label_3.setText("Architektur")
    window.comboBox.setPlaceholderText("Bitte wählen Sie eine Architektur")

    window.pushButton_3.setText("Weiter >")
    window.pushButton_2.setText("Abbrechen")

    # Second page (i386/x64 machines)
    window.label_4.setText("Maschine")
    window.label_5.setText("CPU")
    window.label_6.setText("RAM in MB")

    window.comboBox_2.setPlaceholderText("Bitte wählen Sie eine Maschine")
    window.comboBox_3.setPlaceholderText("Bitte wählen Sie einen Prozessor")

    window.pushButton_5.setText("< Zurück")
    window.pushButton_4.setText("Weiter >")
    window.pushButton_6.setText("Abbrechen")

    # Second page (PowerPC machines)
    window.label_9.setText("Maschine")
    window.label_8.setText("CPU")
    window.label_7.setText("RAM in MB")

    window.comboBox_4.setPlaceholderText("Bitte wählen Sie eine Maschine")
    window.comboBox_5.setPlaceholderText("Bitte wählen Sie einen Prozessor")

    window.pushButton_7.setText("< Zurück")
    window.pushButton_8.setText("Weiter >")
    window.pushButton_9.setText("Abbrechen")

    # Second page (MIPSel machines)
    window.label_12.setText("Maschine")
    window.label_11.setText("CPU")
    window.label_10.setText("RAM in MB")

    window.comboBox_6.setPlaceholderText("Bitte wählen Sie eine Maschine")
    window.comboBox_7.setPlaceholderText("Bitte wählen Sie einen Prozessor")

    window.pushButton_10.setText("< Zurück")
    window.pushButton_11.setText("Weiter >")
    window.pushButton_12.setText("Abbrechen")

    # Second page (ARM machines)
    window.label_31.setText("Maschine")
    window.label_30.setText("CPU")
    window.label_29.setText("RAM in MB")

    window.comboBox_14.setPlaceholderText("Bitte wählen Sie eine Maschine")
    window.comboBox_15.setPlaceholderText("Bitte wählen Sie einen Prozessor")

    window.pushButton_33.setText("< Zurück")
    window.pushButton_34.setText("Weiter >")
    window.pushButton_35.setText("Abbrechen")

    # Third page
    window.label_13.setText("VHD-Ort")
    window.label_14.setText("VHD-Dateiformat")
    window.label_15.setText("Maximale Größe")

    window.comboBox_8.setPlaceholderText("(Bitte wählen Sie ein Dateiformat)")

    window.pushButton_13.setText("Durchsuchen")
    window.pushButton_16.setText("< Zurück")
    window.pushButton_14.setText("Weiter >")
    window.pushButton_15.setText("Abbrechen")

    # Fourth page
    window.label_16.setText("VGA")
    window.label_17.setText("Netzwerk")
    window.label_28.setText("Maus")

    window.comboBox_10.setPlaceholderText("(Bitte wählen Sie einen Grafikadapter)")
    window.comboBox_11.setPlaceholderText("(Bitte wählen Sie einen Netzwerkadapter)")

    window.pushButton_18.setText("< Zurück")
    window.pushButton_17.setText("Weiter >")
    window.pushButton_19.setText("Abbrechen")

    # Fifth page
    window.label_19.setText("Ort der externen\nBIOS-Datei (Lassen\nSie dies leer, um das\nStandard-BIOS zu\nnutzen.)")
    window.label_32.setText("Externe BIOS-Datei")

    window.pushButton_36.setText("Durchsuchen")
    window.pushButton_25.setText("< Zurück")
    window.pushButton_24.setText("Weiter >")
    window.pushButton_23.setText("Abbrechen")

    # Sixth page
    window.label_23.setText("Soundkarte")
    window.label_33.setText("CPU-Kerne")
    window.label_34.setText("Tastatur")

    window.pushButton_28.setText("< Zurück")
    window.pushButton_27.setText("Weiter >")
    window.pushButton_26.setText("Abbrechen")

    # Seventh page
    window.label_24.setText("Linux-Kernel")
    window.label_25.setText("Linux-initrd-Image")
    window.label_26.setText("Linux-CMD-Argumente")

    window.pushButton.setText("Durchsuchen")
    window.pushButton_32.setText("Durchsuchen")
    window.pushButton_31.setText("< Zurück")
    window.pushButton_30.setText("Weiter >")
    window.pushButton_29.setText("Abbrechen")

    # Eighth page
    window.label_2.setText("Zusätzliche Argumente (sofern nötig)")

    window.checkBox_2.setText("Ich will Windows 2000 installieren\n(überholt)")
    window.checkBox_3.setText("USB-Support hinzufügen")

    window.pushButton_22.setText("< Zurück")
    window.pushButton_20.setText("Abschließen")
    window.pushButton_21.setText("Abbrechen")

def translateStartVmDE(window):
    window.label_4.setText("Datum & Zeit")
    window.label_3.setText("Booten von")
    
    window.label_5.setText("""
    Notiz: Sollte die VM innerhalb fünf Minuten nicht starten, sollten Sie die Einstellungen von VM und QEMU überprüfen.
    """)

    window.pushButton.setText("Durchsuchen")
    window.pushButton_2.setText("Durchsuchen")
    window.pushButton_5.setText("Auf Systemzeit setzen")
    window.pushButton_3.setText("VM starten")
    window.pushButton_4.setText("Abbrechen")

def translateVmExistsDE(window):
    window.label.setText("Tut mir leid, jedoch trägt bereits eine andere VM diesen Namen.")
    window.label_2.setText("Bitte löschen Sie die entsprechende VM oder geben Sie dieser einen neuen Namen.")

    window.pushButton.setText("OK")

def translateVhdExistsDE(window):
    window.label.setText("Es tut mir leid, aber die Platte, die Sie erstellen wollen, existiert bereits.")
    window.label_2.setText("Wollen Sie dieses behalten oder überschreiben?")

    window.pushButton.setText("Überschreiben")
    window.pushButton_2.setText("Behalten")

def translateUpdateAvailableDE(window):
    window.label.setText(
        "Es ist ein Update verfügbar! Möchten Sie für den Download weitergeleitet werden?\nHinweis: Wollen Sie Pre-Release-Updates haben, werden Sie unabhängig vom bevorzugten Update-Spiegel zum Pre-Release-Repository auf Codeberg weitergeleitet."
        )

    window.pushButton.setText("Ja")
    window.pushButton_2.setText("Nein")

def translateNoUpdateAvailableDE(window):
    window.label.setText("Sie nutzen bereits die neueste Version von EmuGUI.")
    window.label_2.setText("...oder es stimmt etwas mit Ihrer Internetverbindung nicht.")

    window.pushButton.setText("OK")

def translateSettingsPendingDE(window):
    window.label.setText("Sie haben die QEMU-Pfade noch nicht eingestellt.")
    window.label_2.setText("Bitte gehen Sie in die Einstellungen, um dies zu beheben und versuchen Sie es danach nochmal.")

    window.pushButton.setText("OK")

def translateVmTooNewDE(window):
    window.label.setText("Diese VM wurde mit einer zu neuen Version von EmuGUI erstellt. Bitte verwenden Sie eine neuere Version!")

    window.pushButton.setText("OK")