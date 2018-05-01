# Simone's Gravity Calculator

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a pyqt5 app with the following attributes:
# - use an App/Window class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function or custom method
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed. 
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 2 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 200, 300)

        # Widgets
        self.title = QLabel("Gravity Calculator")
        self.grid.addWidget(self.title, 1, 1, 1, 1)

        self.labelA = QLabel("Mass of First Object:")
        self.grid.addWidget(self.labelA, 2, 1, 1, 1)

        self.labelB = QLabel("Mass of Second Object:")
        self.grid.addWidget(self.labelB, 3, 1, 1, 1)

        self.labelC = QLabel("Center to Center Distance Between the Objects:")
        self.grid.addWidget(self.labelC, 4, 1, 1, 1)

        self.labelD = QLabel()
        self.grid.addWidget(self.labelD, 6, 1, 1, 1)

        self.sideA = QLineEdit()
        self.grid.addWidget(self.sideA, 2, 2, 1, 1)

        self.sideB = QLineEdit()
        self.grid.addWidget(self.sideB, 3, 2, 1, 1)

        self.sideC = QLineEdit()
        self.grid.addWidget(self.sideC, 4, 2, 1, 1)

        self.calc = QPushButton("Calculate")
        self.grid.addWidget(self.calc, 5, 1, 1, 1)

        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 5, 2, 1, 1)

        # Signals and slots
        self.calc.clicked.connect(self.find_hyp)

        # Set Style
        self.set_style()

        # made background color light pink
        # made text boxes white
        # made labels red
        # made font comic sans
        # made font size larger
        # changed width of boxes 

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "pyqt gravity calc.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())


    def find_hyp(self):
        self.labelD.setText(" ")
        try:
            m1 = float(self.sideA.text())
            m2 = float(self.sideB.text())
            r = float(self.sideC.text())
            G = 6.67e-11
            F = G * (m1 * m2) / (r ** 2)
            self.answer.setText(str(F))

        except:
            self.labelD.setText("Try again! The values you chose as inputs were invalid.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())
