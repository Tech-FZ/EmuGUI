# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 801, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayoutWidget_4 = QWidget(self.tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 791, 511))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.gridLayoutWidget_4)
        self.listView.setObjectName(u"listView")

        self.gridLayout_4.addWidget(self.listView, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_22 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout.addWidget(self.pushButton_23)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 791, 521))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_6 = QWidget(self.tab_6)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 0, 781, 491))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_7.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.gridLayoutWidget_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_7.addWidget(self.pushButton_15, 2, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_7.addWidget(self.comboBox_5, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 781, 498))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_2.addWidget(self.pushButton_19, 12, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 7, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 13, 1, 1, 1)

        self.lbl_alpha = QLabel(self.gridLayoutWidget_2)
        self.lbl_alpha.setObjectName(u"lbl_alpha")

        self.gridLayout_2.addWidget(self.lbl_alpha, 15, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 11, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_2.addWidget(self.pushButton_16, 9, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_2.addWidget(self.lineEdit_12, 13, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_2.addWidget(self.lineEdit_13, 14, 2, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 6, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_2.addWidget(self.lineEdit_11, 12, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 9, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 8, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_2.addWidget(self.pushButton_17, 10, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.lbl_riscv32 = QLabel(self.gridLayoutWidget_2)
        self.lbl_riscv32.setObjectName(u"lbl_riscv32")

        self.gridLayout_2.addWidget(self.lbl_riscv32, 16, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 11, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 12, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 10, 1, 1, 1)

        self.btn_alpha = QPushButton(self.gridLayoutWidget_2)
        self.btn_alpha.setObjectName(u"btn_alpha")

        self.gridLayout_2.addWidget(self.btn_alpha, 15, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.btn_riscv32 = QPushButton(self.gridLayoutWidget_2)
        self.btn_riscv32.setObjectName(u"btn_riscv32")

        self.gridLayout_2.addWidget(self.btn_riscv32, 16, 3, 1, 1)

        self.le_riscv32 = QLineEdit(self.gridLayoutWidget_2)
        self.le_riscv32.setObjectName(u"le_riscv32")

        self.gridLayout_2.addWidget(self.le_riscv32, 16, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 14, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 8, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_2.addWidget(self.pushButton_18, 11, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 7, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 6, 3, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_2.addWidget(self.lineEdit_9, 10, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 13, 3, 1, 1)

        self.le_alpha = QLineEdit(self.gridLayoutWidget_2)
        self.le_alpha.setObjectName(u"le_alpha")

        self.gridLayout_2.addWidget(self.le_alpha, 15, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_2.addWidget(self.pushButton_14, 14, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 9, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 17, 3, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 781, 498))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_riscv64 = QPushButton(self.gridLayoutWidget_5)
        self.btn_riscv64.setObjectName(u"btn_riscv64")

        self.gridLayout_6.addWidget(self.btn_riscv64, 2, 3, 1, 1)

        self.lbl_riscv64 = QLabel(self.gridLayoutWidget_5)
        self.lbl_riscv64.setObjectName(u"lbl_riscv64")

        self.gridLayout_6.addWidget(self.lbl_riscv64, 2, 1, 1, 1)

        self.btn_apply_qemu2 = QPushButton(self.gridLayoutWidget_5)
        self.btn_apply_qemu2.setObjectName(u"btn_apply_qemu2")

        self.gridLayout_6.addWidget(self.btn_apply_qemu2, 3, 3, 1, 1)

        self.le_riscv64 = QLineEdit(self.gridLayoutWidget_5)
        self.le_riscv64.setObjectName(u"le_riscv64")

        self.gridLayout_6.addWidget(self.le_riscv64, 2, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_3 = QWidget(self.tab_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 781, 481))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_25 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_5.addWidget(self.pushButton_25, 0, 4, 1, 1)

        self.pushButton_24 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_5.addWidget(self.pushButton_24, 0, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_5.addWidget(self.pushButton_20, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_5.addWidget(self.pushButton_21, 0, 2, 1, 1)

        self.btn_guilded = QPushButton(self.gridLayoutWidget_3)
        self.btn_guilded.setObjectName(u"btn_guilded")

        self.gridLayout_5.addWidget(self.btn_guilded, 0, 5, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 6, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.listView, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.le_alpha)
        QWidget.setTabOrder(self.le_alpha, self.btn_alpha)
        QWidget.setTabOrder(self.btn_alpha, self.le_riscv32)
        QWidget.setTabOrder(self.le_riscv32, self.btn_riscv32)
        QWidget.setTabOrder(self.btn_riscv32, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.btn_riscv64)
        QWidget.setTabOrder(self.btn_riscv64, self.btn_apply_qemu2)
        QWidget.setTabOrder(self.btn_apply_qemu2, self.le_riscv64)
        QWidget.setTabOrder(self.le_riscv64, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_25)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"New Virtual Machine", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Start Selected Virtual Machine", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Edit Selected Virtual Machine", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Virtual Machine", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Export selected virtual machine", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Import virtual machine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"System default", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Deutsch", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Rom\u00e2n\u00e3", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("MainWindow", u"\u010ce\u0161tina", None))
        self.comboBox_4.setItemText(10, QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))
        self.comboBox_4.setItemText(11, QCoreApplication.translate("MainWindow", u"Italiano", None))
        self.comboBox_4.setItemText(12, QCoreApplication.translate("MainWindow", u"Polski", None))

        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"System default", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"General", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"qemu-img Path", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"qemu-system-sparc path", None))
        self.lbl_alpha.setText(QCoreApplication.translate("MainWindow", u"qemu-system-alpha path", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips64el path", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"qemu-system-ppc path", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"qemu-system-arm path", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"qemu-system-x86_64 path", None))
        self.lbl_riscv32.setText(QCoreApplication.translate("MainWindow", u"qemu-system-riscv32 path", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"qemu-system-i386 path", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mips64 path", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"qemu-system-mipsel path", None))
        self.btn_alpha.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btn_riscv32.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"qemu-system-sparc64 path", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"qemu-system-ppc64 path", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"qemu-system-aarch64 path", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"QEMU (1)", None))
        self.btn_riscv64.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lbl_riscv64.setText(QCoreApplication.translate("MainWindow", u"qemu-system-riscv64 path", None))
        self.btn_apply_qemu2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"QEMU (2)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"EmuGUI", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Banner made by Tech-FZ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Built on Python and PyQt technology, licensed under GNU General Public License 3.0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"EmuGUI v0.0.1", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Odysee", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"EmuGUI on social media", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.btn_guilded.setText(QCoreApplication.translate("MainWindow", u"Guilded", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"About EmuGUI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

