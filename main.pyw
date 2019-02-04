#!python3
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PySide2.QtGui import QPixmap
from modules import rightSidePanel, leftSidePanel
import sys


class PyImageViewer(QMainWindow):

    def __init__(self):

        super(PyImageViewer, self).__init__()
        self.setWindowTitle("PyImageViewer")
        self.setMinimumSize(1200, 800)
        self.setWindowIcon(QPixmap('images/icon_picture.jpg'))


        self.centralWidget = QWidget()
        mainLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        panelLeft = leftSidePanel.LeftPanel()
        mainLayout.addWidget(panelLeft)

        panelRight = rightSidePanel.RightPanel(panelLeft.folderBrowser)
        mainLayout.addWidget(panelRight)

        self.applyStyle()

    def applyStyle(self):

        with open("images/style.qss", "r") as styleFile:
            style = styleFile.read()

        self.setStyleSheet(style)


app = QApplication(sys.argv)
window = PyImageViewer()
window.show()
app.exec_()