# Simone's Desktop Calculator

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#  Make a desktop calculator app with pyqt  (40pts)
#  Calculator will have the following functions and buttons. 
#     Answer label where your equation and answer will appear.  It will be nicely formatted and update properly with every button push. (10pts)
#     Clear button to zero your answer Label.  (2pts)
#     buttons 0 through 9.   (5pts)
#     *, /, -, and + buttons (5pts)
#     = button to evaluate the current answer label. (5pts)
#     Decimal button to add float capability (2pts)
#     All buttons, columns, and rows will be of same relative size. (3pts)
#     Use a stylesheet to change the color, font and size to approximately match the built in OS calulator app. (5pts)
#     Add one or more additional functional button to your calculator (square, sqrt, pi, memory, trig, or whatever you choose) (3pts)

#  Model your calculator after the built in calc on your operating system.  (minus the +/- and % buttons)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.equation = ""

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 350, 500)

        # Widgets
        self.display = QLabel("")
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.button1= QPushButton("AC")
        self.grid.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton("(-)")
        self.grid.addWidget(self.button2, 1, 1 , 1, 1)

        self.button3 = QPushButton("%")
        self.grid.addWidget(self.button3, 1, 2, 1, 1)

        self.button4 = QPushButton("/")
        self.grid.addWidget(self.button4, 1, 3, 1, 1)

        self.button5 = QPushButton("7")
        self.grid.addWidget(self.button5, 2, 0, 1, 1)

        self.button6 = QPushButton("8")
        self.grid.addWidget(self.button6, 2, 1, 1, 1)

        self.button7 = QPushButton("9")
        self.grid.addWidget(self.button7, 2, 2, 1, 1)

        self.button8 = QPushButton("x")
        self.grid.addWidget(self.button8, 2, 3, 1, 1)

        self.button9 = QPushButton("4")
        self.grid.addWidget(self.button9, 3, 0, 1, 1)

        self.button10 = QPushButton("5")
        self.grid.addWidget(self.button10, 3, 1, 1, 1)

        self.button11 = QPushButton("6")
        self.grid.addWidget(self.button11, 3, 2, 1, 1)

        self.button12 = QPushButton("-")
        self.grid.addWidget(self.button12, 3, 3, 1, 1)

        self.button13 = QPushButton("1")
        self.grid.addWidget(self.button13, 4, 0, 1, 1)

        self.button14 = QPushButton("2")
        self.grid.addWidget(self.button14, 4, 1, 1, 1)

        self.button15 = QPushButton("3")
        self.grid.addWidget(self.button15, 4, 2, 1, 1)

        self.button16 = QPushButton("+")
        self.grid.addWidget(self.button16, 4, 3, 1, 1)

        self.button17 = QPushButton("0")
        self.grid.addWidget(self.button17, 5, 0, 1, 2)

        self.button18 = QPushButton(".")
        self.grid.addWidget(self.button18, 5, 2, 1, 1)

        self.button19 = QPushButton("=")
        self.grid.addWidget(self.button19, 5, 3, 1, 1)

        # Signals and Slots
        self.button1.clicked.connect(self.ac)


        self.button5.clicked.connect(lambda: self.concat("7"))
        self.button6.clicked.connect(lambda: self.concat("8"))
        self.button7.clicked.connect(lambda: self.concat("9"))

        self.button9.clicked.connect(lambda: self.concat("4"))
        self.button10.clicked.connect(lambda: self.concat("5"))
        self.button11.clicked.connect(lambda: self.concat("6"))

        self.button13.clicked.connect(lambda: self.concat("1"))
        self.button14.clicked.connect(lambda: self.concat("2"))
        self.button15.clicked.connect(lambda: self.concat("3"))

        self.button17.clicked.connect(lambda: self.concat("0"))

        self.button1.clicked.connect(lambda: self.concat("0"))

        self.button2.clicked.connect(lambda: self.concat("* (-1)"))
        self.button3.clicked.connect(lambda: self.concat("/ 10"))
        self.button4.clicked.connect(lambda: self.concat("/"))

        self.button8.clicked.connect(lambda: self.concat("*"))

        self.button12.clicked.connect(lambda: self.concat("-"))

        self.button16.clicked.connect(lambda: self.concat("+"))

        self.button18.clicked.connect(lambda: self.concat("."))

        self.button19.clicked.connect(self.equal)

        self.set_style()

        # Draw
        self.show()
    def concat(self, val):
        self.equation += val
        self.display.setText(self.equation)

    def set_style(self):
        style_file = "desktopcalc.css"
        with open(style_file) as f:
            self.setStyleSheet(f.read())

    def ac(self):
        self.equation = ""
        self.display.setText(self.equation)


    def equal(self):
        self.equation = str(eval(self.equation))
        self.display.setText(self.equation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())