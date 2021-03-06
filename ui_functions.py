## ==> GUI FILE
from Solverr import Capacitance
from main import *
import mysql.connector as msql
from Solverr import *

GLOBAL_STATE=0

class UIFunctions(MainWindow):
    
    #TOOGLE MENU
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.sidebar_frame.width()
            maxExtend = maxWidth
            standard = 50

            # SET MAX WIDTH
            if width == 50:     #if width is 50 then change it to maxWidth
                widthExtended = maxExtend
                #Making labels visible
                self.ui.menu_label.setText("Menu")
                self.ui.home_label.setText("Home")
                self.ui.generate_label.setText("Generate")
            else:       #if width is maxwidth then change it to 50
                widthExtended = standard
                #making labels invisible
                self.ui.menu_label.setText("")
                self.ui.home_label.setText("")
                self.ui.generate_label.setText("")

            # ANIMATION GIVING EASING CURVE TO WIDTH CHANGE
            self.animation = QPropertyAnimation(self.ui.sidebar_frame, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation.start()
    
    #connecting windows state buttons to their functions
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

    def window_state(self):
        self.ui.restore_btn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_btn.clicked.connect(lambda: self.close())


    def browse(self):
        self.fname=QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.ui.browse_label.setText(self.fname)
        return self.fname
        #self.fname.setText(fname[0])
    
    def retur(self):
        return self.fname

    def inputval(self,index):
        self.inptlis={"Voltage":[['i','R'],['P','i'],['P','R'],['q','C'],['P','E','q'],['q','r']],"Capacitance":[['q','V'],['U','V'],['A','d'],['q','U'],['n','V'],['r1r2'],['r1r2','l']],"DriftVelocity":[['i','A','q','n'],['l','t'],['E','t'],['j','n']]}
        self.ui.input_value_combobpx.clear()
        self.newlis=[str(i) for i in self.inptlis[index]]
        print(self.newlis)
        self.ui.input_value_combobpx.addItems(self.newlis)

    def calculate(self,index,inp,input_value):
        print(index,inp,input_value)
        if index=="Voltage":
            print(inp,input_value)
            print(Voltage(inp,input_value))
            self.ui.answer_label.setText(Voltage(inp,input_value))
        elif index=="Capacitance":
            self.ui.answer_label.setText(Capacitance(inp,input_value))
        elif index=="DriftVelocity":
            self.ui.answer_label.setText(DriftVelocity(inp,input_value))