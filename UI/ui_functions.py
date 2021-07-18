## ==> GUI FILE
from main import *

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
