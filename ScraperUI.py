# Author: Benjamin Stark & Bradley Franling
# Date Created: 4/12/2021
# Date updated: 4/18/2021
# Description: UI for scraper

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QCalendarWidget
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5
import Scraper

class Calendar(QMainWindow):

    def __init__(self, parent = None):

        super(Calendar, self).__init__(parent)

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

        # setting geometry to the calender
        calender.setGeometry(0, 0, 400, 250)


    @pyqtSlot()
    def on_click(self):
        print(calender.selectedDate().toString("yyyy-MM-dd"))
        self.close()
        return calender.selectedDate().toString("yyyy-MM-dd")

class App(QMainWindow):

    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.title = 'Scraper'
        self.left = 500
        self.top = 250
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.text = QLabel("Event Name:", self)
        self.text.move(20, 10)
        self.Eventname = QLineEdit("Event Name", self)
        self.Eventname.move(20, 40)
        self.Eventname.resize(280, 30)

        self.LL = QLabel("Latitude, Longitude, radius:", self)
        self.LL.move(20, 120)
        self.LL.resize(200, 30)
        self.LatValidate = QDoubleValidator(-90.0, 90.0, 8, self)
        self.getLatitude = QLineEdit("Latitude", self)
        self.getLatitude.setValidator(self.LatValidate)
        self.getLatitude.move(20, 150)
        self.getLatitude.resize(60, 30)

        self.LonValidate = QDoubleValidator(-180.0, 180.0, 8, self)
        self.getLongitude = QLineEdit("Longitude", self)
        self.getLongitude.setValidator(self.LonValidate)
        self.getLongitude.move(110, 150)
        self.getLongitude.resize(60, 30)

        self.RadValidate = QIntValidator(0, 1000, self)
        self.getRadius = QLineEdit("Radius", self)
        self.getRadius.setValidator(self.RadValidate)
        self.getRadius.move(200, 150)
        self.getRadius.resize(60, 30)

        self.key = QLabel("Keywords: (comma seperated)", self)
        self.key.move(20, 200)
        self.key.resize(300, 30)
        self.Keywords = QLineEdit("Keywords", self)
        self.Keywords.move(20, 230)
        self.Keywords.resize(300, 30)

        # Create a button in the window
        self.button = QPushButton('Run Scrape', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.on_click)

        self.Cbutton = QPushButton('Start Date', self)
        self.Cbutton.move(20, 280)

        self.sdate = QLabel("example", self)
        self.sdate.move(150, 280)
        self.sdate.resize(300, 30)

        # connect button to function on_click
        self.Cbutton.clicked.connect(self.on_calendar_click)

    @pyqtSlot()
    def on_click(self):
        Scraper.Scrape()

    @pyqtSlot()
    def on_calendar_click(self):
        self.dialog = Calendar(self)
        self.dialog.show()

        self.sdate.setText("test")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    main.show()
    sys.exit(app.exec_())
