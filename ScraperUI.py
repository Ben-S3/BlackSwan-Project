# Author: Benjamin Stark & Bradley Franling
# Date Created: 4/12/2021
# Date updated: 4/26/2021
# Description: UI for scraper

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QCalendarWidget, QComboBox
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5
import Scraper

global date
date = ""

class Calendar(QMainWindow):

    def __init__(self, parent=None):
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
        global calendar
        calendar = QCalendarWidget(self)

        # setting geometry to the calendar
        calendar.setGeometry(0, 0, 400, 250)

    @pyqtSlot()
    def on_click(self):
        print(calendar.selectedDate().toString("yyyy-MM-dd"))
        global date
        date = calendar.selectedDate().toString("yyyy-MM-dd")
        self.close()
        return calendar.selectedDate().toString("yyyy-MM-dd")


class App(QMainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.title = 'Scraper'
        self.left = 500
        self.top = 250
        self.width = 1000
        self.height = 550
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
        self.LL.move(20, 80)
        self.LL.resize(200, 30)
        self.LatValidate = QDoubleValidator(-90.0, 90.0, 8, self)
        self.getLatitude = QLineEdit("Latitude", self)
        self.getLatitude.setValidator(self.LatValidate)
        self.getLatitude.move(20, 110)
        self.getLatitude.resize(60, 30)

        self.LonValidate = QDoubleValidator(-180.0, 180.0, 8, self)
        self.getLongitude = QLineEdit("Longitude", self)
        self.getLongitude.setValidator(self.LonValidate)
        self.getLongitude.move(110, 110)
        self.getLongitude.resize(60, 30)

        self.RadValidate = QIntValidator(0, 1000, self)
        self.getRadius = QLineEdit("Radius", self)
        self.getRadius.setValidator(self.RadValidate)
        self.getRadius.move(200, 110)
        self.getRadius.resize(60, 30)

        self.key = QLabel("Keywords: (comma seperated)", self)
        self.key.move(20, 160)
        self.key.resize(300, 30)
        self.Keywords = QLineEdit("Keywords", self)
        self.Keywords.move(20, 190)
        self.Keywords.resize(300, 30)

        # Create a button in the window
        self.button = QPushButton('Run Scrape', self)
        self.button.move(20, 450)

        self.button.clicked.connect(self.on_click)

        self.Cbutton = QPushButton('Start Date', self)
        self.Cbutton.move(20, 240)

        self.sdate = QPushButton("set", self)
        self.sdate.move(140, 240)
        self.sdate.resize(30, 30)

        # connect button to function on_click
        self.Cbutton.clicked.connect(self.on_calendar_click)
        self.sdate.clicked.connect(self.set_date_start)

        self.Cbuttone = QPushButton('End Date', self)
        self.Cbuttone.move(200, 240)

        self.sdatee = QPushButton("set", self)
        self.sdatee.move(320, 240)
        self.sdatee.resize(30, 30)

        # connect button to function on_click
        self.Cbuttone.clicked.connect(self.on_calendar_click)
        self.sdatee.clicked.connect(self.set_date_end)

        self.stl = QLabel("Start Time:", self)
        self.stl.move(20, 270)
        self.stl.resize(300, 30)

        # Start time
        self.sTime = QComboBox(self)
        self.sTime.addItem("1:00")
        self.sTime.addItem("2:00")
        self.sTime.addItem("3:00")
        self.sTime.addItem("4:00")
        self.sTime.addItem("5:00")
        self.sTime.addItem("6:00")
        self.sTime.addItem("7:00")
        self.sTime.addItem("8:00")
        self.sTime.addItem("9:00")
        self.sTime.addItem("10:00")
        self.sTime.addItem("11:00")
        self.sTime.addItem("12:00")
        self.sTime.move(20, 300)
        self.sTime.resize(60, 30)

        self.sTimea = QComboBox(self)
        self.sTimea.addItem("a.m.")
        self.sTimea.addItem("p.m.")
        self.sTimea.move(90, 300)
        self.sTimea.resize(50, 30)

        self.etl = QLabel("End Time:", self)
        self.etl.move(20, 340)
        self.etl.resize(300, 30)

        # End time
        self.eTime = QComboBox(self)
        self.eTime.addItem("1:00")
        self.eTime.addItem("2:00")
        self.eTime.addItem("3:00")
        self.eTime.addItem("4:00")
        self.eTime.addItem("5:00")
        self.eTime.addItem("6:00")
        self.eTime.addItem("7:00")
        self.eTime.addItem("8:00")
        self.eTime.addItem("9:00")
        self.eTime.addItem("10:00")
        self.eTime.addItem("11:00")
        self.eTime.addItem("12:00")
        self.eTime.move(20, 370)
        self.eTime.resize(60, 30)

        self.eTimea = QComboBox(self)
        self.eTimea.addItem("a.m.")
        self.eTimea.addItem("p.m.")
        self.eTimea.move(90, 370)
        self.eTimea.resize(50, 30)

    @pyqtSlot()
    def on_click(self):
        Scraper.Scrape()

    @pyqtSlot()
    def on_calendar_click(self):
        self.dialog = Calendar(self)
        self.dialog.show()

    @pyqtSlot()
    def set_date_start(self):
        self.Cbutton.setText(date)

    @pyqtSlot()
    def set_date_end(self):
        self.Cbuttone.setText(date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    main.show()
    sys.exit(app.exec_())
