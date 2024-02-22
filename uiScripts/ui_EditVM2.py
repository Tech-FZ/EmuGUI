# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditVM2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(813, 474)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(813, 474))
        Dialog.setMaximumSize(QSize(813, 474))
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 811, 421))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 791, 371))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.le_name = QLineEdit(self.gridLayoutWidget)
        self.le_name.setObjectName(u"le_name")

        self.gridLayout.addWidget(self.le_name, 0, 1, 1, 1)

        self.lbl_name = QLabel(self.gridLayoutWidget)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)

        self.lbl_arch = QLabel(self.gridLayoutWidget)
        self.lbl_arch.setObjectName(u"lbl_arch")

        self.gridLayout.addWidget(self.lbl_arch, 1, 0, 1, 1)

        self.cb_arch = QComboBox(self.gridLayoutWidget)
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.addItem("")
        self.cb_arch.setObjectName(u"cb_arch")

        self.gridLayout.addWidget(self.cb_arch, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 801, 391))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayoutWidget_8 = QWidget(self.page_2)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_cpu = QLabel(self.gridLayoutWidget_8)
        self.lbl_cpu.setObjectName(u"lbl_cpu")

        self.gridLayout_8.addWidget(self.lbl_cpu, 0, 0, 1, 1)

        self.lbl_ram = QLabel(self.gridLayoutWidget_8)
        self.lbl_ram.setObjectName(u"lbl_ram")

        self.gridLayout_8.addWidget(self.lbl_ram, 1, 0, 1, 1)

        self.lbl_machine = QLabel(self.gridLayoutWidget_8)
        self.lbl_machine.setObjectName(u"lbl_machine")

        self.gridLayout_8.addWidget(self.lbl_machine, 2, 0, 1, 1)

        self.cb_cpu = QComboBox(self.gridLayoutWidget_8)
        self.cb_cpu.addItem("")
        self.cb_cpu.setObjectName(u"cb_cpu")

        self.gridLayout_8.addWidget(self.cb_cpu, 0, 1, 1, 1)

        self.sb_ram = QSpinBox(self.gridLayoutWidget_8)
        self.sb_ram.setObjectName(u"sb_ram")
        self.sb_ram.setMaximum(32768)

        self.gridLayout_8.addWidget(self.sb_ram, 1, 1, 1, 1)

        self.cb_machine = QComboBox(self.gridLayoutWidget_8)
        self.cb_machine.addItem("")
        self.cb_machine.setObjectName(u"cb_machine")

        self.gridLayout_8.addWidget(self.cb_machine, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_vhdp = QLabel(self.gridLayoutWidget_2)
        self.lbl_vhdp.setObjectName(u"lbl_vhdp")

        self.gridLayout_2.addWidget(self.lbl_vhdp, 1, 0, 1, 1)

        self.lbl_maxsize = QLabel(self.gridLayoutWidget_2)
        self.lbl_maxsize.setObjectName(u"lbl_maxsize")

        self.gridLayout_2.addWidget(self.lbl_maxsize, 3, 0, 1, 1)

        self.lbl_cdc2 = QLabel(self.gridLayoutWidget_2)
        self.lbl_cdc2.setObjectName(u"lbl_cdc2")

        self.gridLayout_2.addWidget(self.lbl_cdc2, 5, 0, 1, 1)

        self.cb_cdc2 = QComboBox(self.gridLayoutWidget_2)
        self.cb_cdc2.addItem("")
        self.cb_cdc2.addItem("")
        self.cb_cdc2.addItem("")
        self.cb_cdc2.addItem("")
        self.cb_cdc2.setObjectName(u"cb_cdc2")

        self.gridLayout_2.addWidget(self.cb_cdc2, 5, 1, 1, 2)

        self.cb_vhdu = QComboBox(self.gridLayoutWidget_2)
        self.cb_vhdu.addItem("")
        self.cb_vhdu.addItem("")
        self.cb_vhdu.addItem("")
        self.cb_vhdu.setObjectName(u"cb_vhdu")

        self.gridLayout_2.addWidget(self.cb_vhdu, 0, 1, 1, 2)

        self.lbl_cdc1 = QLabel(self.gridLayoutWidget_2)
        self.lbl_cdc1.setObjectName(u"lbl_cdc1")

        self.gridLayout_2.addWidget(self.lbl_cdc1, 4, 0, 1, 1)

        self.btn_vhdp = QPushButton(self.gridLayoutWidget_2)
        self.btn_vhdp.setObjectName(u"btn_vhdp")

        self.gridLayout_2.addWidget(self.btn_vhdp, 1, 2, 1, 1)

        self.cb_cdc1 = QComboBox(self.gridLayoutWidget_2)
        self.cb_cdc1.addItem("")
        self.cb_cdc1.addItem("")
        self.cb_cdc1.addItem("")
        self.cb_cdc1.addItem("")
        self.cb_cdc1.setObjectName(u"cb_cdc1")

        self.gridLayout_2.addWidget(self.cb_cdc1, 4, 1, 1, 2)

        self.lbl_vhdu = QLabel(self.gridLayoutWidget_2)
        self.lbl_vhdu.setObjectName(u"lbl_vhdu")

        self.gridLayout_2.addWidget(self.lbl_vhdu, 0, 0, 1, 1)

        self.le_vhdp = QLineEdit(self.gridLayoutWidget_2)
        self.le_vhdp.setObjectName(u"le_vhdp")

        self.gridLayout_2.addWidget(self.le_vhdp, 1, 1, 1, 1)

        self.lbl_vhdf = QLabel(self.gridLayoutWidget_2)
        self.lbl_vhdf.setObjectName(u"lbl_vhdf")

        self.gridLayout_2.addWidget(self.lbl_vhdf, 2, 0, 1, 1)

        self.cb_maxsize = QComboBox(self.gridLayoutWidget_2)
        self.cb_maxsize.addItem("")
        self.cb_maxsize.addItem("")
        self.cb_maxsize.addItem("")
        self.cb_maxsize.setObjectName(u"cb_maxsize")

        self.gridLayout_2.addWidget(self.cb_maxsize, 3, 2, 1, 1)

        self.sb_maxsize = QSpinBox(self.gridLayoutWidget_2)
        self.sb_maxsize.setObjectName(u"sb_maxsize")
        self.sb_maxsize.setMaximum(214748368)

        self.gridLayout_2.addWidget(self.sb_maxsize, 3, 1, 1, 1)

        self.cb_vhdf = QComboBox(self.gridLayoutWidget_2)
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.addItem("")
        self.cb_vhdf.setObjectName(u"cb_vhdf")

        self.gridLayout_2.addWidget(self.cb_vhdf, 2, 1, 1, 2)

        self.lbl_hddc = QLabel(self.gridLayoutWidget_2)
        self.lbl_hddc.setObjectName(u"lbl_hddc")

        self.gridLayout_2.addWidget(self.lbl_hddc, 6, 0, 1, 1)

        self.cb_hddc = QComboBox(self.gridLayoutWidget_2)
        self.cb_hddc.addItem("")
        self.cb_hddc.addItem("")
        self.cb_hddc.addItem("")
        self.cb_hddc.addItem("")
        self.cb_hddc.setObjectName(u"cb_hddc")

        self.gridLayout_2.addWidget(self.cb_hddc, 6, 1, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_3 = QWidget(self.tab_5)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 3, 0, 1, 1)

        self.cb_kbdtype = QComboBox(self.gridLayoutWidget_3)
        self.cb_kbdtype.addItem("")
        self.cb_kbdtype.addItem("")
        self.cb_kbdtype.setObjectName(u"cb_kbdtype")

        self.gridLayout_3.addWidget(self.cb_kbdtype, 1, 1, 1, 1)

        self.cb_mouse = QComboBox(self.gridLayoutWidget_3)
        self.cb_mouse.addItem("")
        self.cb_mouse.addItem("")
        self.cb_mouse.addItem("")
        self.cb_mouse.setObjectName(u"cb_mouse")

        self.gridLayout_3.addWidget(self.cb_mouse, 0, 1, 1, 1)

        self.lbl_mouse = QLabel(self.gridLayoutWidget_3)
        self.lbl_mouse.setObjectName(u"lbl_mouse")

        self.gridLayout_3.addWidget(self.lbl_mouse, 0, 0, 1, 1)

        self.lbl_kbdtype = QLabel(self.gridLayoutWidget_3)
        self.lbl_kbdtype.setObjectName(u"lbl_kbdtype")

        self.gridLayout_3.addWidget(self.lbl_kbdtype, 1, 0, 1, 1)

        self.lbl_kbdlayout = QLabel(self.gridLayoutWidget_3)
        self.lbl_kbdlayout.setObjectName(u"lbl_kbdlayout")

        self.gridLayout_3.addWidget(self.lbl_kbdlayout, 2, 0, 1, 1)

        self.cb_kbdlayout = QComboBox(self.gridLayoutWidget_3)
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.addItem("")
        self.cb_kbdlayout.setObjectName(u"cb_kbdlayout")

        self.gridLayout_3.addWidget(self.cb_kbdlayout, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_5 = QWidget(self.tab_6)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.le_biosf = QLineEdit(self.gridLayoutWidget_5)
        self.le_biosf.setObjectName(u"le_biosf")

        self.gridLayout_5.addWidget(self.le_biosf, 1, 1, 1, 1)

        self.lbl_biosloc = QLabel(self.gridLayoutWidget_5)
        self.lbl_biosloc.setObjectName(u"lbl_biosloc")
        self.lbl_biosloc.setWordWrap(True)

        self.gridLayout_5.addWidget(self.lbl_biosloc, 0, 0, 1, 1)

        self.lbl_biosf = QLabel(self.gridLayoutWidget_5)
        self.lbl_biosf.setObjectName(u"lbl_biosf")
        self.lbl_biosf.setWordWrap(True)

        self.gridLayout_5.addWidget(self.lbl_biosf, 1, 0, 1, 1)

        self.btn_biosf = QPushButton(self.gridLayoutWidget_5)
        self.btn_biosf.setObjectName(u"btn_biosf")

        self.gridLayout_5.addWidget(self.btn_biosf, 1, 2, 1, 1)

        self.le_biosloc = QLineEdit(self.gridLayoutWidget_5)
        self.le_biosloc.setObjectName(u"le_biosloc")

        self.gridLayout_5.addWidget(self.le_biosloc, 0, 1, 1, 2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayoutWidget_6 = QWidget(self.tab_7)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.le_initrd = QLineEdit(self.gridLayoutWidget_6)
        self.le_initrd.setObjectName(u"le_initrd")

        self.gridLayout_6.addWidget(self.le_initrd, 1, 1, 1, 1)

        self.btn_kernel = QPushButton(self.gridLayoutWidget_6)
        self.btn_kernel.setObjectName(u"btn_kernel")

        self.gridLayout_6.addWidget(self.btn_kernel, 0, 2, 1, 1)

        self.le_kernel = QLineEdit(self.gridLayoutWidget_6)
        self.le_kernel.setObjectName(u"le_kernel")

        self.gridLayout_6.addWidget(self.le_kernel, 0, 1, 1, 1)

        self.lbl_initrd = QLabel(self.gridLayoutWidget_6)
        self.lbl_initrd.setObjectName(u"lbl_initrd")

        self.gridLayout_6.addWidget(self.lbl_initrd, 1, 0, 1, 1)

        self.btn_initrd = QPushButton(self.gridLayoutWidget_6)
        self.btn_initrd.setObjectName(u"btn_initrd")

        self.gridLayout_6.addWidget(self.btn_initrd, 1, 2, 1, 1)

        self.lbl_kernel = QLabel(self.gridLayoutWidget_6)
        self.lbl_kernel.setObjectName(u"lbl_kernel")

        self.gridLayout_6.addWidget(self.lbl_kernel, 0, 0, 1, 1)

        self.lbl_cmd = QLabel(self.gridLayoutWidget_6)
        self.lbl_cmd.setObjectName(u"lbl_cmd")

        self.gridLayout_6.addWidget(self.lbl_cmd, 2, 0, 1, 1)

        self.le_cmd = QLineEdit(self.gridLayoutWidget_6)
        self.le_cmd.setObjectName(u"le_cmd")

        self.gridLayout_6.addWidget(self.le_cmd, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 781, 371))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_vga = QLabel(self.gridLayoutWidget_4)
        self.lbl_vga.setObjectName(u"lbl_vga")

        self.gridLayout_4.addWidget(self.lbl_vga, 0, 0, 1, 1)

        self.cb_net = QComboBox(self.gridLayoutWidget_4)
        self.cb_net.addItem("")
        self.cb_net.setObjectName(u"cb_net")

        self.gridLayout_4.addWidget(self.cb_net, 1, 1, 1, 1)

        self.le_addargs = QLineEdit(self.gridLayoutWidget_4)
        self.le_addargs.setObjectName(u"le_addargs")

        self.gridLayout_4.addWidget(self.le_addargs, 4, 1, 1, 1)

        self.lbl_sound = QLabel(self.gridLayoutWidget_4)
        self.lbl_sound.setObjectName(u"lbl_sound")

        self.gridLayout_4.addWidget(self.lbl_sound, 2, 0, 1, 1)

        self.chb_usb = QCheckBox(self.gridLayoutWidget_4)
        self.chb_usb.setObjectName(u"chb_usb")

        self.gridLayout_4.addWidget(self.chb_usb, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_4.addWidget(self.checkBox_3, 5, 0, 1, 1)

        self.lbl_addargs = QLabel(self.gridLayoutWidget_4)
        self.lbl_addargs.setObjectName(u"lbl_addargs")

        self.gridLayout_4.addWidget(self.lbl_addargs, 4, 0, 1, 1)

        self.cb_vga = QComboBox(self.gridLayoutWidget_4)
        self.cb_vga.addItem("")
        self.cb_vga.setObjectName(u"cb_vga")

        self.gridLayout_4.addWidget(self.cb_vga, 0, 1, 1, 1)

        self.cb_usb = QComboBox(self.gridLayoutWidget_4)
        self.cb_usb.setObjectName(u"cb_usb")

        self.gridLayout_4.addWidget(self.cb_usb, 3, 1, 1, 1)

        self.lbl_net = QLabel(self.gridLayoutWidget_4)
        self.lbl_net.setObjectName(u"lbl_net")

        self.gridLayout_4.addWidget(self.lbl_net, 1, 0, 1, 1)

        self.cb_sound = QComboBox(self.gridLayoutWidget_4)
        self.cb_sound.addItem("")
        self.cb_sound.setObjectName(u"cb_sound")

        self.gridLayout_4.addWidget(self.cb_sound, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_cpuc = QLabel(self.gridLayoutWidget_4)
        self.lbl_cpuc.setObjectName(u"lbl_cpuc")

        self.horizontalLayout.addWidget(self.lbl_cpuc)

        self.sb_cpuc = QSpinBox(self.gridLayoutWidget_4)
        self.sb_cpuc.setObjectName(u"sb_cpuc")
        self.sb_cpuc.setMinimum(1)
        self.sb_cpuc.setMaximum(8)

        self.horizontalLayout.addWidget(self.sb_cpuc)


        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 1, 1, 1)

        self.lbl_accel = QLabel(self.gridLayoutWidget_4)
        self.lbl_accel.setObjectName(u"lbl_accel")

        self.gridLayout_4.addWidget(self.lbl_accel, 6, 0, 1, 1)

        self.cb_accel = QComboBox(self.gridLayoutWidget_4)
        self.cb_accel.addItem("")
        self.cb_accel.addItem("")
        self.cb_accel.addItem("")
        self.cb_accel.addItem("")
        self.cb_accel.addItem("")
        self.cb_accel.addItem("")
        self.cb_accel.setObjectName(u"cb_accel")

        self.gridLayout_4.addWidget(self.cb_accel, 6, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(720, 430, 75, 24))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(630, 430, 75, 24))
        QWidget.setTabOrder(self.tabWidget, self.le_name)
        QWidget.setTabOrder(self.le_name, self.cb_arch)
        QWidget.setTabOrder(self.cb_arch, self.cb_cpu)
        QWidget.setTabOrder(self.cb_cpu, self.sb_ram)
        QWidget.setTabOrder(self.sb_ram, self.cb_machine)
        QWidget.setTabOrder(self.cb_machine, self.cb_vhdu)
        QWidget.setTabOrder(self.cb_vhdu, self.le_vhdp)
        QWidget.setTabOrder(self.le_vhdp, self.btn_vhdp)
        QWidget.setTabOrder(self.btn_vhdp, self.cb_vhdf)
        QWidget.setTabOrder(self.cb_vhdf, self.sb_maxsize)
        QWidget.setTabOrder(self.sb_maxsize, self.cb_maxsize)
        QWidget.setTabOrder(self.cb_maxsize, self.cb_cdc1)
        QWidget.setTabOrder(self.cb_cdc1, self.cb_cdc2)
        QWidget.setTabOrder(self.cb_cdc2, self.cb_mouse)
        QWidget.setTabOrder(self.cb_mouse, self.cb_kbdtype)
        QWidget.setTabOrder(self.cb_kbdtype, self.cb_kbdlayout)
        QWidget.setTabOrder(self.cb_kbdlayout, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.le_biosloc)
        QWidget.setTabOrder(self.le_biosloc, self.le_biosf)
        QWidget.setTabOrder(self.le_biosf, self.btn_biosf)
        QWidget.setTabOrder(self.btn_biosf, self.le_kernel)
        QWidget.setTabOrder(self.le_kernel, self.btn_kernel)
        QWidget.setTabOrder(self.btn_kernel, self.le_initrd)
        QWidget.setTabOrder(self.le_initrd, self.btn_initrd)
        QWidget.setTabOrder(self.btn_initrd, self.le_cmd)
        QWidget.setTabOrder(self.le_cmd, self.cb_vga)
        QWidget.setTabOrder(self.cb_vga, self.cb_net)
        QWidget.setTabOrder(self.cb_net, self.cb_sound)
        QWidget.setTabOrder(self.cb_sound, self.chb_usb)
        QWidget.setTabOrder(self.chb_usb, self.cb_usb)
        QWidget.setTabOrder(self.cb_usb, self.le_addargs)
        QWidget.setTabOrder(self.le_addargs, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.sb_cpuc)
        QWidget.setTabOrder(self.sb_cpuc, self.cb_accel)
        QWidget.setTabOrder(self.cb_accel, self.btn_ok)
        QWidget.setTabOrder(self.btn_ok, self.btn_cancel)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"EmuGUI - Edit VM", None))
        self.lbl_name.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.lbl_arch.setText(QCoreApplication.translate("Dialog", u"Architecture", None))
        self.cb_arch.setItemText(0, QCoreApplication.translate("Dialog", u"i386", None))
        self.cb_arch.setItemText(1, QCoreApplication.translate("Dialog", u"x86_64", None))
        self.cb_arch.setItemText(2, QCoreApplication.translate("Dialog", u"mips", None))
        self.cb_arch.setItemText(3, QCoreApplication.translate("Dialog", u"mips64", None))
        self.cb_arch.setItemText(4, QCoreApplication.translate("Dialog", u"mipsel", None))
        self.cb_arch.setItemText(5, QCoreApplication.translate("Dialog", u"mips64el", None))
        self.cb_arch.setItemText(6, QCoreApplication.translate("Dialog", u"ppc", None))
        self.cb_arch.setItemText(7, QCoreApplication.translate("Dialog", u"ppc64", None))
        self.cb_arch.setItemText(8, QCoreApplication.translate("Dialog", u"arm", None))
        self.cb_arch.setItemText(9, QCoreApplication.translate("Dialog", u"aarch64", None))
        self.cb_arch.setItemText(10, QCoreApplication.translate("Dialog", u"sparc", None))
        self.cb_arch.setItemText(11, QCoreApplication.translate("Dialog", u"sparc64", None))
        self.cb_arch.setItemText(12, QCoreApplication.translate("Dialog", u"alpha", None))
        self.cb_arch.setItemText(13, QCoreApplication.translate("Dialog", u"riscv32", None))
        self.cb_arch.setItemText(14, QCoreApplication.translate("Dialog", u"riscv64", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"General", None))
        self.lbl_cpu.setText(QCoreApplication.translate("Dialog", u"CPU", None))
        self.lbl_ram.setText(QCoreApplication.translate("Dialog", u"RAM in MB", None))
        self.lbl_machine.setText(QCoreApplication.translate("Dialog", u"Machine", None))
        self.cb_cpu.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))

        self.cb_machine.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Machine", None))
        self.lbl_vhdp.setText(QCoreApplication.translate("Dialog", u"VHD path", None))
        self.lbl_maxsize.setText(QCoreApplication.translate("Dialog", u"Maximum size", None))
        self.lbl_cdc2.setText(QCoreApplication.translate("Dialog", u"CD controller 2", None))
        self.cb_cdc2.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))
        self.cb_cdc2.setItemText(1, QCoreApplication.translate("Dialog", u"IDE", None))
        self.cb_cdc2.setItemText(2, QCoreApplication.translate("Dialog", u"SCSI", None))
        self.cb_cdc2.setItemText(3, QCoreApplication.translate("Dialog", u"Virtio", None))

        self.cb_vhdu.setItemText(0, QCoreApplication.translate("Dialog", u"Add an existing virtual hard drive", None))
        self.cb_vhdu.setItemText(1, QCoreApplication.translate("Dialog", u"Create a new virtual hard drive", None))
        self.cb_vhdu.setItemText(2, QCoreApplication.translate("Dialog", u"Don't add a virtual hard drive", None))

        self.lbl_cdc1.setText(QCoreApplication.translate("Dialog", u"CD controller 1", None))
        self.btn_vhdp.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.cb_cdc1.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))
        self.cb_cdc1.setItemText(1, QCoreApplication.translate("Dialog", u"IDE", None))
        self.cb_cdc1.setItemText(2, QCoreApplication.translate("Dialog", u"SCSI", None))
        self.cb_cdc1.setItemText(3, QCoreApplication.translate("Dialog", u"Virtio", None))

        self.lbl_vhdu.setText(QCoreApplication.translate("Dialog", u"VHD usage", None))
        self.lbl_vhdf.setText(QCoreApplication.translate("Dialog", u"VHD file format", None))
        self.cb_maxsize.setItemText(0, QCoreApplication.translate("Dialog", u"KB", None))
        self.cb_maxsize.setItemText(1, QCoreApplication.translate("Dialog", u"MB", None))
        self.cb_maxsize.setItemText(2, QCoreApplication.translate("Dialog", u"GB", None))

        self.cb_vhdf.setItemText(0, QCoreApplication.translate("Dialog", u"qcow2", None))
        self.cb_vhdf.setItemText(1, QCoreApplication.translate("Dialog", u"qcow", None))
        self.cb_vhdf.setItemText(2, QCoreApplication.translate("Dialog", u"vdi", None))
        self.cb_vhdf.setItemText(3, QCoreApplication.translate("Dialog", u"raw", None))
        self.cb_vhdf.setItemText(4, QCoreApplication.translate("Dialog", u"vhdx", None))
        self.cb_vhdf.setItemText(5, QCoreApplication.translate("Dialog", u"vpc", None))
        self.cb_vhdf.setItemText(6, QCoreApplication.translate("Dialog", u"vmdk", None))
        self.cb_vhdf.setItemText(7, QCoreApplication.translate("Dialog", u"parallels", None))
        self.cb_vhdf.setItemText(8, QCoreApplication.translate("Dialog", u"file", None))

        self.lbl_hddc.setText(QCoreApplication.translate("Dialog", u"HDD controller", None))
        self.cb_hddc.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))
        self.cb_hddc.setItemText(1, QCoreApplication.translate("Dialog", u"IDE", None))
        self.cb_hddc.setItemText(2, QCoreApplication.translate("Dialog", u"VirtIO SCSI", None))
        self.cb_hddc.setItemText(3, QCoreApplication.translate("Dialog", u"AHCI", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Virtual hard disks", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"USB Tablet Device (depreciated)", None))
        self.cb_kbdtype.setItemText(0, QCoreApplication.translate("Dialog", u"PS/2 Keyboard", None))
        self.cb_kbdtype.setItemText(1, QCoreApplication.translate("Dialog", u"USB Keyboard", None))

        self.cb_mouse.setItemText(0, QCoreApplication.translate("Dialog", u"PS/2 Mouse", None))
        self.cb_mouse.setItemText(1, QCoreApplication.translate("Dialog", u"USB Mouse", None))
        self.cb_mouse.setItemText(2, QCoreApplication.translate("Dialog", u"USB Tablet Device", None))

        self.lbl_mouse.setText(QCoreApplication.translate("Dialog", u"Mouse type", None))
        self.lbl_kbdtype.setText(QCoreApplication.translate("Dialog", u"Keyboard type", None))
        self.lbl_kbdlayout.setText(QCoreApplication.translate("Dialog", u"Keyboard layout", None))
        self.cb_kbdlayout.setItemText(0, QCoreApplication.translate("Dialog", u"en-us", None))
        self.cb_kbdlayout.setItemText(1, QCoreApplication.translate("Dialog", u"en-gb", None))
        self.cb_kbdlayout.setItemText(2, QCoreApplication.translate("Dialog", u"de", None))
        self.cb_kbdlayout.setItemText(3, QCoreApplication.translate("Dialog", u"fr", None))
        self.cb_kbdlayout.setItemText(4, QCoreApplication.translate("Dialog", u"ru", None))
        self.cb_kbdlayout.setItemText(5, QCoreApplication.translate("Dialog", u"pl", None))
        self.cb_kbdlayout.setItemText(6, QCoreApplication.translate("Dialog", u"pt", None))
        self.cb_kbdlayout.setItemText(7, QCoreApplication.translate("Dialog", u"it", None))
        self.cb_kbdlayout.setItemText(8, QCoreApplication.translate("Dialog", u"ja", None))
        self.cb_kbdlayout.setItemText(9, QCoreApplication.translate("Dialog", u"es", None))
        self.cb_kbdlayout.setItemText(10, QCoreApplication.translate("Dialog", u"is", None))
        self.cb_kbdlayout.setItemText(11, QCoreApplication.translate("Dialog", u"fi", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"Peripherals", None))
        self.lbl_biosloc.setText(QCoreApplication.translate("Dialog", u"Location of external BIOS file (Leave empty to use the default BIOS)", None))
        self.lbl_biosf.setText(QCoreApplication.translate("Dialog", u"External BIOS file", None))
        self.btn_biosf.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"BIOS", None))
        self.btn_kernel.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.lbl_initrd.setText(QCoreApplication.translate("Dialog", u"Linux initrd image", None))
        self.btn_initrd.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.lbl_kernel.setText(QCoreApplication.translate("Dialog", u"Linux kernel", None))
        self.lbl_cmd.setText(QCoreApplication.translate("Dialog", u"Linux cmd arguments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Dialog", u"Linux", None))
        self.lbl_vga.setText(QCoreApplication.translate("Dialog", u"VGA", None))
        self.cb_net.setItemText(0, QCoreApplication.translate("Dialog", u"none", None))

        self.lbl_sound.setText(QCoreApplication.translate("Dialog", u"Sound card", None))
        self.chb_usb.setText(QCoreApplication.translate("Dialog", u"Add USB support", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"I want to install Windows 2000 (depreciated)", None))
        self.lbl_addargs.setText(QCoreApplication.translate("Dialog", u"Additional arguments (if necessary)", None))
        self.cb_vga.setItemText(0, QCoreApplication.translate("Dialog", u"Let QEMU decide", None))

        self.lbl_net.setText(QCoreApplication.translate("Dialog", u"Network adapter", None))
        self.cb_sound.setItemText(0, QCoreApplication.translate("Dialog", u"none", None))

        self.lbl_cpuc.setText(QCoreApplication.translate("Dialog", u"CPU cores", None))
        self.lbl_accel.setText(QCoreApplication.translate("Dialog", u"Acceleration", None))
        self.cb_accel.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.cb_accel.setItemText(1, QCoreApplication.translate("Dialog", u"TCG", None))
        self.cb_accel.setItemText(2, QCoreApplication.translate("Dialog", u"HAXM (depreciated)", None))
        self.cb_accel.setItemText(3, QCoreApplication.translate("Dialog", u"WHPX", None))
        self.cb_accel.setItemText(4, QCoreApplication.translate("Dialog", u"WHPX (kernel-irqchip off)", None))
        self.cb_accel.setItemText(5, QCoreApplication.translate("Dialog", u"KVM", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Additional components", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

