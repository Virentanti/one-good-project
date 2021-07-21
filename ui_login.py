# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerZjOmmU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 323)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(300, 30))
        self.password.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setFamily(u"Uni Sans Demo Heavy CAPS")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet(u"QLineEdit{border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)}\n"
"QLineEdit:hover{border-color: rgb(255, 255, 255);}")
        self.password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.password)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 30))
        self.lineEdit_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)}\n"
"QLineEdit:hover{border-color: rgb(255, 255, 255);}")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enter_btn = QPushButton(self.frame)
        self.enter_btn.setObjectName(u"enter_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_btn.sizePolicy().hasHeightForWidth())
        self.enter_btn.setSizePolicy(sizePolicy)
        self.enter_btn.setMinimumSize(QSize(200, 30))
        self.enter_btn.setMaximumSize(QSize(200, 30))
        self.enter_btn.setFont(font)
        self.enter_btn.setStyleSheet(u"QPushButton{border: 2px solid rgb(255, 255, 255); border-radius: 10px; color:rgb(255, 255, 255);}\n"
"QPushButton:hover{border: 2px solid rgb(33, 0, 114); border-radius: 10px; color:rgb(255, 255, 255);}")

        self.horizontalLayout_2.addWidget(self.enter_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 30))
        self.label.setMaximumSize(QSize(16777215, 300))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.enter_btn.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label.setText("")
    # retranslateUi

