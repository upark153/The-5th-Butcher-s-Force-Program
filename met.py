from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import sqlite3
from datetime import datetime
from PyQt5.QtPrintSupport import QPrinter

ui, _ = loadUiType('pos.ui')

class MainApp(QMainWindow, ui):

    items = ["ITEMS"]
    price = [0]
    images = ["IMAGES"]

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.LOGINBUTTON.clicked.connect(self.login)
        self.CANCLE.clicked.connect(lambda: self.close())
        self.LOGOUT.clicked.connect(self.logout)
        self.FOODBUTTON_1.clicked.connect(lambda:self.addproduct(1))
        self.FOODBUTTON_2.clicked.connect(lambda:self.addproduct(2))
        self.FOODBUTTON_3.clicked.connect(lambda:self.addproduct(3))
        self.FOODBUTTON_4.clicked.connect(lambda:self.addproduct(4))
        self.FOODBUTTON_5.clicked.connect(lambda:self.addproduct(5))
        self.FOODBUTTON_6.clicked.connect(lambda:self.addproduct(6))
        self.FOODBUTTON_7.clicked.connect(lambda:self.addproduct(7))
        self.FOODBUTTON_8.clicked.connect(lambda:self.addproduct(8))
        self.FOODBUTTON_9.clicked.connect(lambda:self.addproduct(9))
        self.FOODBUTTON_10.clicked.connect(lambda:self.addproduct(10))
        self.PRINT.clicked.connect(self.print_widget)
        self.NOPRINT.clicked.connect(self.noprint_widget)
        self.SETTING.clicked.connect(self.show_setting)
        self.ITEMLIST.currentIndexChanged.connect(self.fill_details_on_combobox_selected)
        self.CHANGEBUTTON.clicked.connect(self.update_product)
        self.CONFIGUREBACK.clicked.connect(self.configurepage_to_productpage)
    # 로그인 화면 코드 작성

    def login(self):
        ui = self.USERID.text()
        pw = self.PASSWORD.text()
        if (ui == "admin" and pw == "admin"):
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("성공적으로 로그인이 되었습니다. 환영합니다.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.USERID.setText("")
            self.PASSWORD.setText("")
            self.getbill_number()
            self.tabWidget.setCurrentIndex(1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("아이디와 비밀번호가 일치하지 않습니다.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def logout(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("로그아웃되었습니다.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.tabWidget.setCurrentIndex(0)

    # 영수증 번호 체크
    def getbill_number(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT MAX(billno) FROM billitems")
        result = cursor.fetchall()
        if result:
            try:
                for data in result:
                    billno = int(data[0]) + 1
            except:
                billno = 1
        else:
            billno = 1
        self.BILLNO.setText(str(billno))
        self.DATE.setText(str(datetime.today()))
        self.configurepage()

    # 데이터베이스로부터 상품 조회

    def configurepage(self):
        self.items = ["ITEMS"]
        self.price = [0]
        self.images = ["IMAGES"]
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.items.append(str(prod[0]))
                self.images.append(str(prod[1]))
                self.price.append(str(prod[2]))
        con.close()
        print(self.items)
        print(self.images)
        print(self.price)

        # 포스기 첫번째 아이템 수정사항 반영
        self.FOODNAME_1.setText(self.items[1])
        self.FOODPRICE_1.setText(self.price[1]+"원")
        filename = "./" + self.images[1]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_1.setPixmap(pixmap)
        # 포스기 두번째 아이템 수정사항 반영
        self.FOODNAME_2.setText(self.items[2])
        self.FOODPRICE_2.setText(self.price[2]+"원")
        filename = "./" + self.images[2]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_2.setPixmap(pixmap)
        # 포스기 세번째 아이템 수정사항 반영
        self.FOODNAME_3.setText(self.items[3])
        self.FOODPRICE_3.setText(self.price[3]+"원")
        filename = "./" + self.images[3]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_3.setPixmap(pixmap)
        # 포스기 네번째 아이템 수정사항 반영
        self.FOODNAME_4.setText(self.items[4])
        self.FOODPRICE_4.setText(self.price[4]+"원")
        filename = "./" + self.images[4]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_4.setPixmap(pixmap)
        # 포스기 다섯번째 아이템 수정사항 반영
        self.FOODNAME_5.setText(self.items[5])
        self.FOODPRICE_5.setText(self.price[5]+"원")
        filename = "./" + self.images[5]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_5.setPixmap(pixmap)
        # 포스기 여섯번째 아이템 수정사항 반영
        self.FOODNAME_6.setText(self.items[6])
        self.FOODPRICE_6.setText(self.price[6]+"원")
        filename = "./" + self.images[6]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_6.setPixmap(pixmap)
        # 포스기 일곱번째 아이템 수정사항 반영
        self.FOODNAME_7.setText(self.items[7])
        self.FOODPRICE_7.setText(self.price[7]+"원")
        filename = "./" + self.images[7]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_7.setPixmap(pixmap)
        # 포스기 여덟번째 아이템 수정사항 반영
        self.FOODNAME_8.setText(self.items[8])
        self.FOODPRICE_8.setText(self.price[8]+"원")
        filename = "./" + self.images[8]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_8.setPixmap(pixmap)
        # 포스기 아홉번째 아이템 수정사항 반영
        self.FOODNAME_9.setText(self.items[9])
        self.FOODPRICE_9.setText(self.price[9]+"원")
        filename = "./" + self.images[9]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_9.setPixmap(pixmap)
        # 포스기 열번째 아이템 수정사항 반영
        self.FOODNAME_10.setText(self.items[10])
        self.FOODPRICE_10.setText(self.price[10]+"원")
        filename = "./" + self.images[10]
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.FOODIMAGE_10.setPixmap(pixmap)





    def addproduct(self, id):
        print("상품이 추가 되었습니다.", id)
        billno = int(self.BILLNO.text())
        itemname = str(self.items[id])
        unitprice = self.price[id]
        quantity = "1"
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM billitems WHERE itemname = '"+ itemname +"' and billno = "+ str(billno) +"")
        result = cursor.fetchall()
        if result:
            print("이미 구매한 상품입니다.")
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("추가로 100g 더 구매합니다.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            con.execute("UPDATE billitems SET quantity = quantity + 1, totalprice = totalprice + "+str(unitprice) +" WHERE itemname = '"+ itemname  +"' and billno = "+ str(billno) +"" )
            con.commit()
        else:
            print("구매합니다.")
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("100g 구매합니다.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            con.execute("INSERT INTO billitems (billno, itemname, unitprice, quantity, totalprice) values("+str(billno)+",'"+itemname+"', "+str(unitprice)+", "+quantity+", "+str(unitprice)+")")
            con.commit()
        self.filltable()
    # 테이블에 추가한 항목 보여주기
    def filltable(self):
        total = 0
        self.billitems.setRowCount(0)
        self.billitems.clear()
        self.billitems.setColumnWidth(0, 180) # 항목
        self.billitems.setColumnWidth(1, 80) # 가격
        self.billitems.setColumnWidth(2, 60) # 수량
        self.billitems.setColumnWidth(3, 120) # 합계
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT itemname, unitprice, quantity, totalprice FROM billitems WHERE billno = "+ self.BILLNO.text()+ " ")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.billitems.setColumnCount(c)
        for row_number, row_data in enumerate(result):
            self.billitems.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.billitems.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.billitems.verticalHeader().setVisible(False)
        self.billitems.horizontalHeader().setVisible(False)
        cursor = con.execute("SELECT * FROM billitems WHERE billno = "+str(self.BILLNO.text()) +"")
        result = cursor.fetchall()
        if result:
            for prod in result:
                total = total + int(prod[4])
        self.TOTAL.setText("%.f" % (total))
        self.TAX.setText("%.f" % (total * .05))
        self.GRANDTOTAL.setText("%.f" % (total + (total * .05)))

    # 영수증 인쇄하고 다음 넘어가기
    def print_widget(self):
        if(self.GRANDTOTAL.text() !="0"):
            printer = QPrinter()
            painter = QPainter()
            painter.begin(printer)
            screen = self.PRINTAREA.grab()
            painter.drawPixmap(10, 10, screen)
            painter.end()
            self.getbill_number()
            self.filltable()
    # 인쇄하지 않고 넘어가기
    def noprint_widget(self):
        if(self.GRANDTOTAL.text()!="0"):
            self.getbill_number()
            self.filltable()

    # 세팅 화면
    def show_setting(self):
        self.tabWidget.setCurrentIndex(2)
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMLIST.addItem(str(prod[0]))

    # 세팅 화면에서 항목이 선택되었을 때 보여주는 값
    def fill_details_on_combobox_selected(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products WHERE itemname = '"+self.ITEMLIST.currentText() +"'")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMNAME.setText(str(prod[0]))
                self.ITEMPRICE.setText(str(prod[2]))
                self.ITEMPICTURE.setText(str(prod[1]))
                self.SETTINGSNAME.setText(str(prod[0]))
                self.SETTINGSPRICE.setText(str(prod[2])+'원')
                filename = "./" + str(prod[1])
                image = QImage(filename)
                pixmap = QPixmap.fromImage(image)
                self.SETTINGSIMAGE.setPixmap(pixmap)

    # 항목 수정하기
    def update_product(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("UPDATE products SET itemname = '"+ self.ITEMNAME.text() +"', imagename = '"+ self.ITEMPICTURE.text() +"', unitprice = "+ self.ITEMPRICE.text() +" WHERE itemname = '"+ self.ITEMLIST.currentText()+"'")
        con.commit()
        con.close()
        self.SETTINGSNAME.setText(self.ITEMNAME.text())
        self.SETTINGSPRICE.setText("금액 : " + self.ITEMPRICE.text())
        filename = "./" + self.ITEMPICTURE.text()
        image = QImage(filename)
        pixmap = QPixmap.fromImage(image)
        self.SETTINGSIMAGE.setPixmap(pixmap)
        self.configurepage()
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("수정사항이 반영되었습니다.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    # 포스기 화면으로 이동하기
    def configurepage_to_productpage(self):
        self.tabWidget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()