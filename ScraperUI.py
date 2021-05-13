# Author: Benjamin Stark & Bradley Franklin
# Date Created: 4/12/2021
# Date updated: 5/6/2021
# Description: UI for scraper

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QCalendarWidget, QComboBox
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5
import inserter
import Scraper
import PremiumScraper

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

        # Event name
        self.eventLabel = QLabel("Event Name:", self)
        self.eventLabel.move(20, 10)
        self.Eventname = QLineEdit("Event Name", self)
        self.Eventname.move(20, 40)
        self.Eventname.resize(200, 30)

        # Event Lookup
        self.eventNums = {"--New Event--": -1}
        self.eventLookup = QComboBox(self)
        self.eventLookup.addItem("--New Event--")
        self.eventLookup.move(270, 40)
        self.eventLookup.resize(200, 30)
        self.checkEvent = QPushButton('Check', self)
        self.checkEvent.move(220, 40)
        self.checkEvent.resize(50, 30)

        self.checkEvent.clicked.connect(self.check_events)

        # Latitude Longitude and Radius
        self.LatLonLabel = QLabel("Latitude, Longitude, radius:", self)
        self.LatLonLabel.move(20, 80)
        self.LatLonLabel.resize(200, 30)
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

        # Keywords
        self.keyLabel = QLabel("Keywords: (comma seperated)", self)
        self.keyLabel.move(20, 160)
        self.keyLabel.resize(300, 30)
        self.Keywords = QLineEdit("Keywords", self)
        self.Keywords.move(20, 190)
        self.Keywords.resize(300, 30)

        # Start Date
        self.calenderButtonStart = QPushButton('Start Date', self)
        self.calenderButtonStart.move(20, 240)

        self.setStartDate = QPushButton("set", self)
        self.setStartDate.move(140, 240)
        self.setStartDate.resize(30, 30)

        self.calenderButtonStart.clicked.connect(self.on_calendar_click)
        self.setStartDate.clicked.connect(self.set_date_start)

        # End Date
        self.calenderButtonEnd = QPushButton('End Date', self)
        self.calenderButtonEnd.move(200, 240)

        self.setEndDate = QPushButton("set", self)
        self.setEndDate.move(320, 240)
        self.setEndDate.resize(30, 30)

        self.calenderButtonEnd.clicked.connect(self.on_calendar_click)
        self.setEndDate.clicked.connect(self.set_date_end)

        # Start time
        self.startTimeLabel = QLabel("Start Time:", self)
        self.startTimeLabel.move(20, 270)
        self.startTimeLabel.resize(300, 30)

        self.startTime = QComboBox(self)
        self.startTime.addItem("00:00")
        self.startTime.addItem("01:00")
        self.startTime.addItem("02:00")
        self.startTime.addItem("03:00")
        self.startTime.addItem("04:00")
        self.startTime.addItem("05:00")
        self.startTime.addItem("06:00")
        self.startTime.addItem("07:00")
        self.startTime.addItem("08:00")
        self.startTime.addItem("09:00")
        self.startTime.addItem("10:00")
        self.startTime.addItem("11:00")
        self.startTime.addItem("12:00")
        self.startTime.addItem("13:00")
        self.startTime.addItem("14:00")
        self.startTime.addItem("15:00")
        self.startTime.addItem("16:00")
        self.startTime.addItem("17:00")
        self.startTime.addItem("18:00")
        self.startTime.addItem("19:00")
        self.startTime.addItem("20:00")
        self.startTime.addItem("21:00")
        self.startTime.addItem("22:00")
        self.startTime.addItem("23:00")
        self.startTime.move(20, 300)
        self.startTime.resize(60, 30)

        # End time
        self.endTimeLabel = QLabel("End Time:", self)
        self.endTimeLabel.move(160, 270)
        self.endTimeLabel.resize(300, 30)

        self.endTime = QComboBox(self)
        self.endTime.addItem("00:00")
        self.endTime.addItem("01:00")
        self.endTime.addItem("02:00")
        self.endTime.addItem("03:00")
        self.endTime.addItem("04:00")
        self.endTime.addItem("05:00")
        self.endTime.addItem("06:00")
        self.endTime.addItem("07:00")
        self.endTime.addItem("08:00")
        self.endTime.addItem("09:00")
        self.endTime.addItem("10:00")
        self.endTime.addItem("11:00")
        self.endTime.addItem("12:00")
        self.endTime.addItem("13:00")
        self.endTime.addItem("14:00")
        self.endTime.addItem("15:00")
        self.endTime.addItem("16:00")
        self.endTime.addItem("17:00")
        self.endTime.addItem("18:00")
        self.endTime.addItem("19:00")
        self.endTime.addItem("20:00")
        self.endTime.addItem("21:00")
        self.endTime.addItem("22:00")
        self.endTime.addItem("23:00")
        self.endTime.move(160, 300)
        self.endTime.resize(60, 30)

        # Create a button in the window
        self.run = QPushButton('Run Standard Scrape', self)
        self.run.resize(120, 25)
        self.run.move(20, 350)

        self.run.clicked.connect(self.on_click_standard)

        # Create a button in the window
        self.runP = QPushButton('Run Premium Scrape', self)
        self.runP.resize(120, 25)
        self.runP.move(160, 350)

        self.runP.clicked.connect(self.on_click_premium)

    @pyqtSlot()
    def on_click_standard(self):
        Scraper.Scrape(self.Eventname.text(), self.Keywords.text(), self.getLatitude.text(), self.getLongitude.text(),
                       self.getRadius.text(), self.calenderButtonStart.text(), self.startTime.currentText(),
                       self.calenderButtonEnd.text(), self.endTime.currentText(),
                       self.eventNums[self.eventLookup.currentText()])

    @pyqtSlot()
    def on_click_premium(self):
        PremiumScraper.Scrape(self.Eventname.text(), self.Keywords.text(), self.getLatitude.text(), self.getLongitude.text(),
                        self.getRadius.text(), self.calenderButtonStart.text(), self.startTime.currentText(),
                        self.calenderButtonEnd.text(), self.endTime.currentText(),
                        self.eventNums[self.eventLookup.currentText()])

    @pyqtSlot()
    def on_calendar_click(self):
        self.dialog = Calendar(self)
        self.dialog.show()

    @pyqtSlot()
    def set_date_start(self):
        self.calenderButtonStart.setText(date)

    @pyqtSlot()
    def set_date_end(self):
        self.calenderButtonEnd.setText(date)

    @pyqtSlot()
    def check_events(self):
        events = inserter.event_exists_name(self.Eventname.text())
        self.eventLookup.clear()
        self.eventLookup.addItem("--New Event--")
        for x in events:
            self.eventLookup.addItem(x.name)
            self.eventNums[x.name] = x.id_


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    main.show()
    sys.exit(app.exec_())
