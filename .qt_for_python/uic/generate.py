# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_frame = QFrame(self.frame)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        self.sidebar_frame.setMaximumSize(QSize(50, 16777215))
        self.sidebar_frame.setFrameShape(QFrame.NoFrame)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 11, 10, 20)
        self.menu_btn_2 = QPushButton(self.sidebar_frame)
        self.menu_btn_2.setObjectName(u"menu_btn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn_2.sizePolicy().hasHeightForWidth())
        self.menu_btn_2.setSizePolicy(sizePolicy)
        self.menu_btn_2.setMinimumSize(QSize(30, 30))
        self.menu_btn_2.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/menu.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/menu(hover).png);}")

        self.verticalLayout_3.addWidget(self.menu_btn_2)

        self.home_btn_2 = QPushButton(self.sidebar_frame)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setMinimumSize(QSize(30, 30))
        self.home_btn_2.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/home.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/home(hover).png);}")

        self.verticalLayout_3.addWidget(self.home_btn_2)

        self.verticalSpacer_sidebar_2 = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_sidebar_2)

        self.generate_btn_2 = QPushButton(self.sidebar_frame)
        self.generate_btn_2.setObjectName(u"generate_btn_2")
        self.generate_btn_2.setMinimumSize(QSize(30, 30))
        self.generate_btn_2.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/generate.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/generate(hover).png);}")

        self.verticalLayout_3.addWidget(self.generate_btn_2)


        self.horizontalLayout_2.addWidget(self.sidebar_frame)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.frame_2)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMaximumSize(QSize(16777215, 60))
        self.titlebar.setFrameShape(QFrame.NoFrame)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.title_label = QLabel(self.titlebar)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamily(u"Uni Sans Demo Heavy CAPS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.window_state_frame = QFrame(self.titlebar)
        self.window_state_frame.setObjectName(u"window_state_frame")
        self.window_state_frame.setMaximumSize(QSize(80, 16777215))
        self.window_state_frame.setFrameShape(QFrame.NoFrame)
        self.window_state_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.window_state_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 5, 15)
        self.minimize_btn = QPushButton(self.window_state_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        self.minimize_btn.setStyleSheet(u"QPushButton{background-color: rgb(84, 84, 84);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(0, 202, 78);}")

        self.horizontalLayout_4.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.window_state_frame)
        self.restore_btn.setObjectName(u"restore_btn")
        sizePolicy.setHeightForWidth(self.restore_btn.sizePolicy().hasHeightForWidth())
        self.restore_btn.setSizePolicy(sizePolicy)
        self.restore_btn.setMinimumSize(QSize(20, 20))
        self.restore_btn.setMaximumSize(QSize(20, 20))
        self.restore_btn.setStyleSheet(u"QPushButton{background-color: rgb(84, 84, 84);border-radius:10px;}\n"
"QPushButton:hover{background-color:rgb(255, 189, 68);}")

        self.horizontalLayout_4.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.window_state_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(20, 20))
        self.close_btn.setStyleSheet(u"QPushButton{background-color: rgb(84, 84, 84);border-radius:10px;}\n"
"QPushButton:hover{background-color:rgb(255, 96, 92);}")

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.window_state_frame)


        self.verticalLayout.addWidget(self.titlebar)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 29))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{border: 2px solid rgb(255, 255, 255); border-radius: 10px; color:rgb(255, 255, 255);}\n"
"QPushButton:hover{border: 2px solid rgb(33, 0, 114); border-radius: 10px; color:rgb(255, 255, 255);}")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 29))
        self.comboBox.setStyleSheet(u"QComboBox { background-color:rgba(33, 0, 114,80); border-style: solid;  border: 2px solid rgb(33, 0, 114); ; border-radius: 10px;  padding: 1px 1px 1px 35px; color:rgba(255, 255, 255,90) } QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; color: white; border-left-width: 0px; border-left-color: darkgray;  border-left-style: solid;  border-top-right-radius: 3px;  border-bottom-right-radius: 3px; padding-left: 10px;  } QComboBox::down-arrow { image: url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/down_arrow.png); width: 10px; height: 10px; }")
        self.comboBox.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 29))
        self.pushButton_2.setStyleSheet(u"QPushButton{border: 2px solid rgb(255, 255, 255); border-radius: 10px; color:rgb(255, 255, 255);}\n"
"QPushButton:hover{border: 2px solid rgb(33, 0, 114); border-radius: 10px; color:rgb(255, 255, 255);}")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn_2.setText("")
        self.home_btn_2.setText("")
        self.generate_btn_2.setText("")
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Physics Numerical Solver", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Browse Path", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Chapter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

