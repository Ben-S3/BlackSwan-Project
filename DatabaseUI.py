# Author: Bradley Franklin & Hope Church
# Date Created: 5/12/2021
# Date updated: 5/12/2021
# Description: UI for database

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QCalendarWidget, QComboBox, QListWidget, QListWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5
import inserter
import selecter
import database_objects
import Filter

global posts
posts = []

class App(QMainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.title = 'Database Search'
        self.left = 500
        self.top = 250
        self.width = 250
        self.height =200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Event Lookup
        self.eventNums = {"--Choose Event--": -1}
        self.eventLookup = QComboBox(self)
        self.eventLookup.addItem("--Choose Event--")
        self.eventLookup.move(80, 90)
        self.eventLookup.resize(150, 30)
        self.checkEvent = QPushButton('Check', self)
        self.checkEvent.move(20, 90)
        self.checkEvent.resize(50, 30)

        self.checkEvent.clicked.connect(self.check_events)

        # Keywords
        self.keyLabel = QLabel("Keywords: (comma seperated)", self)
        self.keyLabel.move(20, 5)
        self.keyLabel.resize(300, 30)
        self.Keywords = QLineEdit("Keywords", self)
        self.Keywords.move(20, 30)
        self.Keywords.resize(210, 30)

        # Create a button in the window
        self.run = QPushButton('Run Search', self)
        self.run.resize(120, 25)
        self.run.move(60, 150)

        self.run.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        global posts
        event = database_objects.event(None, None, None, None, None, None, None)
        for x in self.events:
            if x.name == self.eventLookup.currentText():
                event = x
                break;
        posts = selecter.find_post_by_event(event)
        self.dialog = PostDisplay(self)
        self.dialog.show()


    @pyqtSlot()
    def check_events(self):
        self.events = inserter.event_exists_name(self.Keywords.text())
        self.eventLookup.clear()
        self.eventLookup.addItem("--Choose Event--")
        for x in self.events:
            self.eventLookup.addItem(x.name)
            self.eventNums[x.name] = x.id_

class PostDisplay(QMainWindow):

    def __init__(self, parent=None):
        super(PostDisplay, self).__init__(parent)
        self.title = 'Post Display'
        self.left = 500
        self.top = 250
        self.width = 450
        self.height = 400
        self.initUI()

    def initUI(self):
        global posts
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Keywords = QLineEdit("Refining Keywords", self)
        self.Keywords.move(0, 0)
        self.Keywords.resize(350, 30)

        self.run = QPushButton('Refine Posts', self)
        self.run.resize(100, 30)
        self.run.move(350, 0)

        self.run.clicked.connect(self.on_click)

        self.listWidget = QListWidget(self)
        for x in posts:
            hasmedia = False
            medias = selecter.find_media_by_post(x)
            if len(medias) > 0:
                hasmedia = True
            user=selecter.find_user_by_post(x)[0]
            QListWidgetItem("User: " + str(user.username) + "\t Title: " + str(x.title), self.listWidget)
            QListWidgetItem("Description: " + str(x.description), self.listWidget)
            QListWidgetItem("Link: " + str(x.url), self.listWidget)
            QListWidgetItem("Has media: " + str(hasmedia), self.listWidget)
            QListWidgetItem("________________________________________________________________________________________",
                            self.listWidget)
        if posts is None:
            QListWidgetItem("No posts match the query.", self.listWidget)
        self.listWidget.resize(450, 350)
        self.listWidget.move(0, 50)

    @pyqtSlot()
    def on_click(self):
        global posts
        posts = Filter.filterMedia(posts, self.Keywords.text())
        self.listWidget.clear()
        for x in posts:
            hasmedia = False
            medias = selecter.find_media_by_post(x)
            if len(medias) > 0:
                hasmedia = True
            user=selecter.find_user_by_post(x)[0]
            QListWidgetItem("User: " + str(user.username) + "\t Title: " + str(x.title), self.listWidget)
            QListWidgetItem("Description: " + str(x.description), self.listWidget)
            QListWidgetItem("Link: " + str(x.url), self.listWidget)
            QListWidgetItem("Has media: " + str(hasmedia), self.listWidget)
            QListWidgetItem("________________________________________________________________________________________",
                            self.listWidget)
        if posts is None:
            QListWidgetItem("No posts match the query.", self.listWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    main.show()
    sys.exit(app.exec_())
