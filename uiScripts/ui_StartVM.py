# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartVM.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 300)
        Dialog.setMinimumSize(QSize(410, 300))
        Dialog.setMaximumSize(QSize(410, 300))
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 397, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 8, 2, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 2)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 7, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 1, 2)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 7, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 8, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 3)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)

        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.dateTimeEdit)
        QWidget.setTabOrder(self.dateTimeEdit, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Boot from", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"cdrom 1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"TPM path (Linux only)", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"a", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"d", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))

        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Date & Time", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-ddThh:mm:ss", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"fda", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Set to system", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Start VM", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Create the TPM from the terminal!", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"cdrom 2", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Browse", None))
    # retranslateUi

