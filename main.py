import os
import sys
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from datetime import date
from datetime import datetime
from interface import Ui_MainWindow

class MainApp(QMainWindow , Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_btn()
        self.load_save()
        self.interface_ui()

    def interface_ui(self):
        self.setWindowTitle("To Do")
        self.setFixedSize(366,379)


    def handel_btn(self):
        self.pushButton.clicked.connect(self.add_item)
        self.pushButton_2.clicked.connect(self.del_item)
        self.pushButton_3.clicked.connect(self.clear_item)
        self.pushButton_4.clicked.connect(self.save_todo)

    def load_save(self):
        try:
            with open("save.txt","r") as f:
                for item in f:
                    self.listWidget.addItem(item.strip())
        except:
            pass
        

    def add_item(self):
        item = self.lineEdit.text()
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if len(item) != 0:
            self.listWidget.addItem(item+" "*16+current_time+" | "+str(today))
            self.lineEdit.setText("")
        else:
            pass

    def del_item(self):
        select = self.listWidget.currentRow()
        self.listWidget.takeItem(select)

    def clear_item(self):
        self.listWidget.clear()

    def save_todo(self):
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        
        with open("save.txt","w") as f:
            for item in items:
                a = item.text()
                f.write(a+"\n")


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.add_item()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
