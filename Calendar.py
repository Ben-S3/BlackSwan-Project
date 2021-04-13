# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        value = 3

        # setting title
        self.setWindowTitle("Calendar")

        # setting geometry
        self.setGeometry(50, 50, 400, 280)

        button = QPushButton('Select', self)
        button.setToolTip('Confirm the selected date then close the calendar')
        button.move(300, 250)
        button.clicked.connect(self.on_click)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating a QCalendarWidget object
        global calender
        calender = QCalendarWidget(self)

        # creating label
        label = QLabel(self)

        # setting geometry to the label
        label.setGeometry(65, 235, 250, 60)

        # making label multi line
        label.setWordWrap(True)

        # getting the selected date
        value = calender.selectedDate()

        # setting text to the label
        label.setText("Selected Date: " + value.toString())

        # setting geometry to the calender
        calender.setGeometry(0, 0, 400, 250)


    @pyqtSlot()
    def on_click(self):
        print(calender.selectedDate().toString("yyyy-MM-dd"))
        self.exit


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
