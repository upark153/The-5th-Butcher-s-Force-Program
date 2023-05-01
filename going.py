import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
import csv
from PyQt5.QtCore import QDate, Qt
import MySQLdb

form_widget = uic.loadUiType('population.ui')[0]

class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search_pushButton.clicked.connect(self.search)
        self.modifybutton.clicked.connect(self.Add_New_Crime)
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety'
                               )
        a = conn.cursor()
        a.execute("SELECT * from 'safety'.'경찰서'")
        police = a.fetchall()
        police_list1 = list(police)
        self.police_info = []
        for i in police_list1:
            self.police_info.append(list(i))

    def search(self):
        word = self.search_lineEdit.text()
        for i in range(len(self.police_info)):
            if word in self.police_info[i][4]:
                Row = 0
                self.tableWidget.setRowCount(len(self.police_info))
                for s in self.police_info:
                    self.tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
                    self.tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
                    self.tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
                    self.tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
                    self.tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
                    Row += 1

    #해당 경찰서 혹은 파출소의 새로운 범죄 항목 추가
    def Add_New_Crime(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                   port=3306,
                                   user='root',
                                   password='0000',
                                   db='criminal'
                                   )

        self.cur = self.db.cursor()


        # police_office_title = self.lineEdit.text()
        crime_occurrence_year = self.lineEdit1.text()
        crime_category = self.lineEdit2.text()
        crime_number = self.lineEdit3.text()




    def Edit_Number_Criminal(self):
        pass

    def Delete_Category_Criminal(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainWindow = Search()
    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()