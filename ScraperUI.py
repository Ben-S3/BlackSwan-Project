# Author: Benjamin Stark
# Date Created: 4/12/2021
# Date updated: 4/12/2021
# Description: UI for scraper

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Scraper'
        self.left = 1000
        self.top = 500
        self.width = 1000
        self.height = 800
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

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.Eventname.text()
        QMessageBox.question(self, "Placeholder" + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
