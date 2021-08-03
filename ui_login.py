# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBmpQyu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        font = QFont()
        font.setFamily(u"Uni Sans Demo Heavy CAPS")
        font.setPointSize(14)
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(30, 25, 300, 30))
        self.title_label.setMinimumSize(QSize(300, 30))
        self.title_label.setMaximumSize(QSize(16777215, 300))
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.title_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily(u"Uni Sans Demo Heavy CAPS")
        font.setPointSize(10)
        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(30, 80, 300, 30))
        self.username.setMinimumSize(QSize(300, 30))
        self.username.setMaximumSize(QSize(300, 30))
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLineEdit{border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)}\n"
"QLineEdit:hover{border-color: rgb(255, 255, 255);}")
        self.username.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 130, 300, 30))
        self.password.setMinimumSize(QSize(300, 30))
        self.password.setMaximumSize(QSize(300, 30))
        self.password.setFont(font)
        self.password.setStyleSheet(u"QLineEdit{border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)}\n"
"QLineEdit:hover{border-color: rgb(255, 255, 255);}")
        self.password.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily(u"Uni Sans Demo Heavy CAPS")
        font.setPointSize(10)
        self.Auth_label = QLabel(self.frame)
        self.Auth_label.setObjectName(u"Auth_label")
        self.Auth_label.setGeometry(QRect(30, 220, 300, 30))
        self.Auth_label.setMinimumSize(QSize(300, 30))
        self.Auth_label.setMaximumSize(QSize(16777215, 300))
        self.Auth_label.setFont(font)
        self.Auth_label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")
        self.Auth_label.setAlignment(Qt.AlignCenter)


        self.enter_btn = QPushButton(self.frame)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setGeometry(QRect(80, 180, 200, 30))
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

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Auth_label.setText("")
        self.title_label.setText("Database login")
        self.enter_btn.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi

