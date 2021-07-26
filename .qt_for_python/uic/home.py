# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
        MainWindow.resize(714, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.central_frame = QFrame(self.centralwidget)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"background-color:rgb(0, 0, 0)")
        self.central_frame.setFrameShape(QFrame.NoFrame)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.central_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, 0, -1)
        self.sidebar_frame = QFrame(self.central_frame)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        self.sidebar_frame.setMaximumSize(QSize(50, 16777215))
        self.sidebar_frame.setFrameShape(QFrame.NoFrame)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 11, 10, 20)
        self.menu_btn = QPushButton(self.sidebar_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QSize(30, 30))
        self.menu_btn.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/menu.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/menu(hover).png);}")

        self.verticalLayout_2.addWidget(self.menu_btn)

        self.home_btn = QPushButton(self.sidebar_frame)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(30, 30))
        self.home_btn.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/home.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/home(hover).png);}")

        self.verticalLayout_2.addWidget(self.home_btn)

        self.verticalSpacer_sidebar = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_sidebar)

        self.generate_btn = QPushButton(self.sidebar_frame)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setMinimumSize(QSize(30, 30))
        self.generate_btn.setStyleSheet(u"QPushButton{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/generate.png);}\n"
"QPushButton:hover{border-image:url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/generate(hover).png);}")

        self.verticalLayout_2.addWidget(self.generate_btn)


        self.horizontalLayout_2.addWidget(self.sidebar_frame)

        self.main_frame = QFrame(self.central_frame)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.main_frame)
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

        self.content_vertical_spacing_frame = QFrame(self.main_frame)
        self.content_vertical_spacing_frame.setObjectName(u"content_vertical_spacing_frame")
        self.content_vertical_spacing_frame.setFrameShape(QFrame.StyledPanel)
        self.content_vertical_spacing_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content_vertical_spacing_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.content_frame = QFrame(self.content_vertical_spacing_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 0))
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chapter_combobox = QComboBox(self.content_frame)
        self.chapter_combobox.setObjectName(u"chapter_combobox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chapter_combobox.sizePolicy().hasHeightForWidth())
        self.chapter_combobox.setSizePolicy(sizePolicy1)
        self.chapter_combobox.setMinimumSize(QSize(250, 30))
        self.chapter_combobox.setMaximumSize(QSize(300, 45))
        font1 = QFont()
        font1.setFamily(u"Uni Sans Demo")
        font1.setPointSize(10)
        self.chapter_combobox.setFont(font1)
        self.chapter_combobox.setStyleSheet(u"QComboBox { background-color:rgba(33, 0, 114,80); border-style: solid;  border: 2px solid rgb(33, 0, 114); ; border-radius: 10px;  padding: 1px 10px 1px 90px; color:rgba(255, 255, 255,90) } QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; color: white; border-left-width: 0px; border-left-color: darkgray;  border-left-style: solid;  border-top-right-radius: 3px;  border-bottom-right-radius: 3px; padding-left: 10px;  } QComboBox::down-arrow { image: url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/down_arrow.png); width: 10px; height: 10px; }")
        self.chapter_combobox.setEditable(True)

        self.verticalLayout_3.addWidget(self.chapter_combobox)

        self.input_value_combobpx = QComboBox(self.content_frame)
        self.input_value_combobpx.setObjectName(u"input_value_combobpx")
        sizePolicy1.setHeightForWidth(self.input_value_combobpx.sizePolicy().hasHeightForWidth())
        self.input_value_combobpx.setSizePolicy(sizePolicy1)
        self.input_value_combobpx.setMinimumSize(QSize(250, 30))
        self.input_value_combobpx.setMaximumSize(QSize(300, 45))
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(10)
        self.input_value_combobpx.setFont(font2)
        self.input_value_combobpx.setStyleSheet(u"QComboBox { background-color:rgba(33, 0, 114,80); border-style: solid;  border: 2px solid rgb(33, 0, 114); ; border-radius: 10px;  padding: 1px 0px 1px 80px; color:rgba(255, 255, 255,90) } QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; color: white; border-left-width: 0px; border-left-color: darkgray;  border-left-style: solid;  border-top-right-radius: 3px;  border-bottom-right-radius: 3px; padding-left: 10px;  } QComboBox::down-arrow { image: url(C:/Users/Rashmi/Desktop/Development/one-good-project/images/down_arrow.png); width: 10px; height: 10px; }")
        self.input_value_combobpx.setEditable(True)

        self.verticalLayout_3.addWidget(self.input_value_combobpx)

        self.values_line_edit = QLineEdit(self.content_frame)
        self.values_line_edit.setObjectName(u"values_line_edit")
        sizePolicy1.setHeightForWidth(self.values_line_edit.sizePolicy().hasHeightForWidth())
        self.values_line_edit.setSizePolicy(sizePolicy1)
        self.values_line_edit.setMinimumSize(QSize(250, 30))
        self.values_line_edit.setMaximumSize(QSize(300, 45))
        font3 = QFont()
        font3.setFamily(u"Uni Sans Demo Heavy CAPS")
        font3.setPointSize(10)
        self.values_line_edit.setFont(font3)
        self.values_line_edit.setStyleSheet(u"QLineEdit{border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)}")
        self.values_line_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.values_line_edit)

        self.calculate_btn = QPushButton(self.content_frame)
        self.calculate_btn.setObjectName(u"calculate_btn")
        sizePolicy1.setHeightForWidth(self.calculate_btn.sizePolicy().hasHeightForWidth())
        self.calculate_btn.setSizePolicy(sizePolicy1)
        self.calculate_btn.setMinimumSize(QSize(250, 30))
        self.calculate_btn.setMaximumSize(QSize(300, 45))
        self.calculate_btn.setFont(font3)
        self.calculate_btn.setStyleSheet(u"QPushButton{border: 2px solid rgb(255, 255, 255); border-radius: 10px; color:rgb(255, 255, 255);}\n"
"QPushButton:hover{border: 2px solid rgb(33, 0, 114); border-radius: 10px; color:rgb(255, 255, 255);}")

        self.verticalLayout_3.addWidget(self.calculate_btn)

        self.answer_label = QLabel(self.content_frame)
        self.answer_label.setObjectName(u"answer_label")
        self.answer_label.setMinimumSize(QSize(250, 30))
        self.answer_label.setMaximumSize(QSize(300, 45))
        font4 = QFont()
        font4.setFamily(u"Uni Sans Demo Heavy CAPS")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.answer_label.setFont(font4)
        self.answer_label.setStyleSheet(u"border-radius:10px; border: 2px solid rgb(33, 0, 114);color:rgba(255, 255, 255,90);background-color:rgba(33, 0, 114,80)")
        self.answer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.answer_label)


        self.horizontalLayout_5.addWidget(self.content_frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.content_vertical_spacing_frame)


        self.horizontalLayout_2.addWidget(self.main_frame)


        self.horizontalLayout.addWidget(self.central_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText("")
        self.home_btn.setText("")
        self.generate_btn.setText("")
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Physics Numerical Solver", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.chapter_combobox.setCurrentText(QCoreApplication.translate("MainWindow", u"select chapter", None))
        self.input_value_combobpx.setCurrentText(QCoreApplication.translate("MainWindow", u"select input value", None))
        self.input_value_combobpx.setPlaceholderText("")
        self.values_line_edit.setText("")
        self.values_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENTER VALUES", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"calculate", None))
        self.answer_label.setText(QCoreApplication.translate("MainWindow", u"ANSWER", None))
    # retranslateUi

