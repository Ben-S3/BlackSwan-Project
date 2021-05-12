# Author: Bradley Franklin
# Date Created: 5/11/2021
# Date updated: 5/12/2021
# Description:  Simple display of posts from a specified event sent to this display
#               Currently does not directly work with the filter.

import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QCalendarWidget, QComboBox, QListWidget, QListWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot
import PyQt5
import inserter
import selecter
from database_objects import event, post


class App(QMainWindow, event):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.title = 'Post Display'
        self.left = 500
        self.top = 250
        self.width = 450
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        posts = selecter.find_post_by_event(event)
        #posts = [post(123, "title", "date", "time", "description", "like_num", "comment_num", "dislike_num", "is_comment"
        #        , "parentid", "url", "issensitive", "language", "sharecount", "123", "idLocation"), post(124,
        #        "title", "date", "time", "description", "like_num", "comment_num", "dislike_num", "is_comment"
        #        , "parentid", "url", "issensitive", "language", "sharecount", "124", "idLocation")]

        listWidget = QListWidget(self)
        for x in posts:
            QListWidgetItem("User: " + x.idUser + "\t Title: " + x.title, listWidget)
            QListWidgetItem("Description: " + x.description, listWidget)
            QListWidgetItem("Link: " + x.url, listWidget)
            QListWidgetItem("________________________________________________________________________________________", listWidget)
        listWidget.resize(450, 400)

        window_layout = QVBoxLayout(self)
        window_layout.addWidget(listWidget)
        self.setLayout(window_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv, selecter.find_events_by_name("MinnesotaRiot"))
    main = App()
    main.show()
    sys.exit(app.exec_())
