import sys
import mysql.connector
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
#     QCalendarWidget, QComboBox
# from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
# from PyQt5.QtCore import pyqtSlot
# import PyQt5


usserinput = input("Enter the Event name ?")
print(usserinput)
# import Scraper
cnx = mysql.connector.connect(host="localhost", port=8889, user="root", password="root", database="Blackswan")
cursor = cnx.cursor()
query = "SELECT idUser,username,website FROM Blackswan.Blackswan_table WHERE idUser = 4;"



cursor.execute(query)
for i in cursor:
    print(i)
cursor = cnx.cursor()

class Example(QMainWindow):

    def __init__(self):
         super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Search Events')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
     main()
