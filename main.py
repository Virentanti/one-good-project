import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow
from ui_login import Ui_login

# IMPORT FUNCTIONS
from ui_functions import *
from pdsf import *

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

        # PAGE 1
        self.ui.home_btn.clicked.connect(lambda: self.ui.stacked_widgets.setCurrentWidget(self.ui.home))
        
        items=['Vd','Resistance','current','Voltage','Ef','u']
        self.ui.chapter_combobox.addItems(items)

        chapters=["current","electrostatics","electromagnetic","atomic physics"]
        self.ui.generate_chater_comboBox.addItems(chapters)
        
        # PAGE 2
        self.ui.generate_btn.clicked.connect(lambda: self.ui.stacked_widgets.setCurrentWidget(self.ui.generate))

        br=lambda : UIFunctions.browse(self)
        self.ui.browse_btn.clicked.connect(br)

        self.ui.generate_generate_btn.clicked.connect(lambda: pdf_gen(self.ui.generate_chater_comboBox.currentText(), br))


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
