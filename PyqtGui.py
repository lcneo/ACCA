import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,600)
        self.center()
        QToolTip.setFont(QFont("sansSerif",10))
        #self.setToolTip('This is a <b>Qwidget</b> widget')
        #self.pbtn()
        self.pbtn()
        self.pqbtn()
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.show()

    def pbtn(self):
        btn = QPushButton("按钮", self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(20, 40)

    def pqbtn(self):
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(20,62)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '警告',
                                     "是否要退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class QMW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("hello neo")
        self.setGeometry(300,300,300,200)

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)


        exitAction = QAction(QIcon("exit24.png"), 'Exit',self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        self.setWindowTitle("Statusbar")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QMW()
    sys.exit(app.exec_())
