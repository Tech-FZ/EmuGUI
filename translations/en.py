def translateMainEN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "Main")
    window.tabWidget.setTabText(1, "Settings")

    # Main tab
    window.pushButton_8.setText("New virtual machine")
    window.pushButton_9.setText("Start virtual machine")
    window.pushButton_10.setText("Edit selected virtual machine")
    window.pushButton_11.setText("Delete selected virtual machine")

    # Settings tabs
    window.tabWidget_2.setTabText(0, "General")
    window.tabWidget_2.setTabText(3, "About")

    # General tab
    window.label_15.setText("Language")
    window.pushButton_15.setText("Apply")

    # QEMU tab
    window.label.setText("qemu-img Path")
    window.label_2.setText("qemu-system-i386 Path")
    window.label_3.setText("qemu-system-x86_64 Path")
    window.label_4.setText("qemu-system-ppc Path")
    window.label_5.setText("qemu-system-mips64el Path")
    window.label_9.setText("qemu-system-aarch64 Path")
    window.label_11.setText("qemu-system-arm Path")

    window.pushButton.setText("Browse")
    window.pushButton_2.setText("Browse")
    window.pushButton_3.setText("Browse")
    window.pushButton_4.setText("Browse")
    window.pushButton_5.setText("Browse")
    window.pushButton_7.setText("Browse")
    window.pushButton_12.setText("Browse")
    window.pushButton_6.setText("Apply")

    # Update tab
    window.label_12.setText("Update mirror")
    window.label_13.setText("Update notify frequency")
    window.label_14.setText("Update channel")

    window.pushButton_13.setText("Check for updates")
    window.pushButton_14.setText("Apply")

    # About tab
    window.label_7.setText("Built on Python and PyQt technology, licensed under GNU General Public License 3.0")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
        )
