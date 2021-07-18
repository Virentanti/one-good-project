## ==> GUI FILE
from main import *

GLOBAL_STATE=0

class UIFunctions(MainWindow):
    

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.sidebar_frame.width()
            maxExtend = maxWidth
            standard = 50

            # SET MAX WIDTH
            if width == 50:
                widthExtended = maxExtend
                self.ui.menu_label.setText("Menu")
                self.ui.home_label.setText("Home")
                self.ui.generate_label.setText("Generate")
            else:
                widthExtended = standard
                self.ui.menu_label.setText("")
                self.ui.home_label.setText("")
                self.ui.generate_label.setText("")

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.sidebar_frame, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation.start()
    def maximize_restore(self):
        global GLOBAL_STATE
        glo=GLOBAL_STATE
        if glo==0:
            self.showMaximized()
            GLOBAL_STATE=1

            #self.ui.central_frame.setContentsMargins(0,0,0,0)
            self.ui.restore_btn.setToolTip("Restore")
        else:
            GLOBAL_STATE=0
            self.showNormal()

            self.resize(self.width()+1, self.height()+1)
            self.ui.restore_btn.setToolTip("Maximize")

    def frameless(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.restore_btn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_btn.clicked.connect(lambda: self.close())


    def browse(self):
        fname=QFileDialog.getExistingDirectory(self, 'Select Directory')
        print(fname)
        #self.fname.setText(fname[0])

