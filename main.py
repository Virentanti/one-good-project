import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from pdsf import *
from db import authenticate

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.frameless(self)
        UIFunctions.window_state(self)


        def move_window(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titlebar_frame.mouseMoveEvent = move_window
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.menu_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 170, True))

        self.ui.home_btn.clicked.connect(lambda: self.ui.stacked_widgets.setCurrentWidget(self.ui.home))
        self.ui.admin_panel_btn.clicked.connect(lambda: self.ui.stacked_widgets.setCurrentWidget(self.ui.admin_panel_login))
        
        items=["Voltage","Capacitance","DriftVelocity"]
        self.ui.chapter_combobox.addItems(items)

        inputlis=[['i','R'],['P','i'],['P','R'],['q','C'],['P','E','q'],['q','r']]
        print(inputlis)
        inputlis=[str(i) for i in inputlis]
        self.ui.input_value_combobpx.addItems(inputlis)
        self.ui.chapter_combobox.currentIndexChanged.connect(lambda: UIFunctions.inputval(self, self.ui.chapter_combobox.currentText()))

        chapters=["current","electrostatics","electromagnetic","aphy", "allquestion"]
        self.ui.generate_chater_comboBox.addItems(chapters)
        
        self.ui.calculate_btn.clicked.connect(lambda: UIFunctions.calculate(self, self.ui.chapter_combobox.currentText(),self.ui.input_value_combobpx.currentText(),self.ui.values_line_edit.text()))
        # PAGE 2
        self.ui.generate_btn.clicked.connect(lambda: self.ui.stacked_widgets.setCurrentWidget(self.ui.generate))

        self.ui.browse_btn.clicked.connect(lambda: UIFunctions.browse(self))

        self.ui.generate_generate_btn.clicked.connect(lambda:pdf_gen(self.ui.generate_chater_comboBox.currentText(), UIFunctions.retur(self)))

        self.ui.question_btn.clicked.connect(lambda: UIFunctions.add_ques(self))
        self.ui.answer_btn.clicked.connect(lambda: UIFunctions.add_ans(self))

        self.ui.login_btn.clicked.connect(lambda: UIFunctions.login(self,self.ui.username_lineedit.text(),self.ui.password_lineedit.text()))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
