from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
import sys
import tt
import threading
import time

class Example(QWidget):
    # 创建一个QHBox的布局

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #设置当前窗体的布局为QHBox布局
        conLayout = QHBoxLayout()

        # 将表格类添加到QHBox布局中去
        conLayout.addWidget(self.CreatTable())
        #conLayout.addWidget(self.CreatTable())
        self.setGeometry(200,200,800,600)
        self.setWindowTitle("Quit button")
        self.setLayout(conLayout)
        self.show()


    def CreatTable(self):

        data, head, index = tt.readcav(r"C:\Users\neo\Desktop\end.csv")

        #row 为行数， col 为列数
        row = len(data)
        col = len(data.columns)

        #创建一个表格类
        table = QTableWidget()

        #设置表格的长和宽
        table.setRowCount(row)
        table.setColumnCount(col)

        # 每一列的标题
        table.setHorizontalHeaderLabels(head)
        # 每一行的标题
        table.setVerticalHeaderLabels(index)


        #将DataFrame中的元素打印到表格中去，i为行，j为列
        for i in range(row):
            for j in range(col):
                table.setItem(i,j, QTableWidgetItem(str(data.ix[i][j])))
        return table
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())