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
    window.tabWidget_2.setTabText(3, "Über")

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

    window.pushButton.setText("Durchsuchen")
    window.pushButton_2.setText("Durchsuchen")
    window.pushButton_3.setText("Durchsuchen")
    window.pushButton_4.setText("Durchsuchen")
    window.pushButton_5.setText("Durchsuchen")
    window.pushButton_7.setText("Durchsuchen")
    window.pushButton_12.setText("Durchsuchen")
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
