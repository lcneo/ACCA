from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

#主窗体类
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Cwidget = CentralWidget() #添加中心widget
        self.initUI()
    #运行Mainwin主函数
    def initUI(self):
        self.resize(1340,750)#窗体大小和位置
        #self.move(50,50)
        self.Center()

        self.setWindowIcon(QIcon(r"C:\icons\Launchpad.icns"))

        self.CreateBar()#添加菜单栏

        self.CreateTools()#添加工具栏

        self.setCentralWidget(self.Cwidget)


        self.setWindowTitle("Demo")
        self.show()

    #添加菜单栏
    def CreateBar(self):

        #创建菜单栏
        menubar = self.menuBar()

        #创建文件菜单
        fileMenu = menubar.addMenu('文件')

        #退出
        exitAction = QAction(QIcon(r"C:\icons\Button-Turn-Off-01.png"),'退出程序',self)
        exitAction.triggered.connect(self.close)
        exitAction.setShortcut("Ctrl+q")

        #读取文件
        OpenFileAction = QAction(QIcon(r"C:\icons\Document-New-01.png"),'打开文件',self)
        OpenFileAction.setShortcut('Ctrl+o')
        OpenFileAction.triggered.connect(self.Cwidget.OpenFile)

        #添加菜单项
        fileMenu.addAction(OpenFileAction)
        fileMenu.addAction(exitAction)

        # 设置菜单
        setMenu = menubar.addMenu('设置')

        fontAction = QAction(QIcon(r"C:\icons\Gear-01.png"),'字体',self)
        fontAction.setShortcut('Ctrl+f')
        fontAction.triggered.connect(QFontDialog.getFont)

        setMenu.addAction(fontAction)

        #帮助菜单
        helpMenu = menubar.addMenu('帮助')

        helpAction = QAction("帮助",self)
        helpAction.setShortcut('Ctrl+h')

        helpMenu.addAction(helpAction)

        self.statusBar()

    #添加工具栏
    def CreateTools(self):
        #读取文件功能
        OpenFileAction = QAction(QIcon(r"C:\icons\Document-New-01.png"),'打开文件',self)
        OpenFileAction.triggered.connect(self.Cwidget.OpenFile)

        #退出功能
        exitAcion = QAction(QIcon(r"C:\icons\Button-Turn-Off-01.png"),'退出',self)
        exitAcion.triggered.connect(self.close)

        #建立工具栏
        self.toolbar = self.addToolBar('工具')

        #将工具添加到工具栏中去
        self.toolbar.addAction(OpenFileAction)
        self.toolbar.addAction(exitAcion)

    #方法重写，在推出程序时询问是否退出
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "是否退出?", QMessageBox.Yes  | QMessageBox.No,QMessageBox.No,)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #将窗体移动到屏幕中央的函数
    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


#窗体中心widget
class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.topleft, self.topright, self.bottom = QFrame(self), QFrame(self), QFrame(self)
        self.QQ = QWidget()
        self.QQ.textEdit = QTextEdit()
        self.initUI()
    def initUI(self):

        self.CreateLayout()#布局框架
        self.CreateFontButton()
    #添加布局框架
    def CreateLayout(self):
        #设置布局
        hbox = QHBoxLayout(self)

        #建立左上模块
        self.topleft = QFrame(self)
        self.topleft.setFrameShape(QFrame.StyledPanel)
        self. topleft.resize(800,800)
        #topleft.createWindowContainer(textEdit)
        #button = QPushButton('hello',topleft)

        #建立右上模块
        self.topright = QFrame(self)
        self.topright.setFrameShape(QFrame.StyledPanel)

        #建立下方模块
        self.bottom = QFrame(self)
        self.bottom.setFrameShape(QFrame.StyledPanel)

        #将上方左右模块进行水平组合
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.topleft)
        splitter1.addWidget(self.topright)
        splitter1.resize(100,100)

        #将成组的上方模块和下方模块进行垂直组合
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.bottom)

        #将建立好的框架设置为布局
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        hbbox = QHBoxLayout()
        hbbox.addWidget(self.QQ.textEdit)
        self.topleft.setLayout(hbbox)


    #test
    def CreateFontButton(self):

        vbox = QVBoxLayout()
        btn = QPushButton(QIcon(r"C:\icons\Gear-01.png"),'字体设置', self.topright)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.clicked.connect(self.SetFont)
        btn.move(20,20)

        self.topright.lbl = QLabel('Knowledge only matters',self.topright)
        vbox.addWidget(btn)
        vbox.addWidget(self.topright.lbl)

        self.topright.setLayout(vbox)


    #设置字体
    def SetFont(self):
        font, ok =QFontDialog.getFont()
        if ok:
            self.topright.lbl.setFont(font)
            self.QQ.textEdit.setFont(font)

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


    #读取文件
    def OpenFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','/home')
        if fname[0]:
            f = open(fname[0],'r')
            print(fname)
            with f:
                data = f.read()
                self.QQ.textEdit.setText(data)
                self.topright.lbl.setText(os.path.basename(fname[0]))
#运行main函数
if __name__ == "__main__":

    app = QApplication(sys.argv)
    aa =MainWin()
    sys.exit(app.exec_())
