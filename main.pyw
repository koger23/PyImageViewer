#!python3
import os
import sys

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

from modules import panelProvider

mainPath = sys.argv[0].split("main.pyw")[0]
imageFolderPath = os.path.join(mainPath, "images")


def main():
    app = QApplication(sys.argv)
    window = PyImageViewer(sys.argv)
    window.show()
    app.exec_()


class PyImageViewer(QMainWindow):

    def __init__(self, args=None):
        super(PyImageViewer, self).__init__()
        print("Args: ", args)

        self.openedPicture = ""
        if len(args) > 1:
            self.openedPicture = sys.argv[1]

        self.setWindowTitle("PyImageViewer")
        self.setMinimumSize(1200, 800)
        self.setWindowIcon(QPixmap(os.path.join(imageFolderPath, 'icon_picture.jpg')))

        self.panelProvider = panelProvider.PanelProvider(self)

        self.centralWidget = QWidget()
        mainLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)
        mainLayout.addWidget(panelProvider.PanelProvider.leftPanel)
        mainLayout.addWidget(panelProvider.PanelProvider.rightPanel)

        self.applyStyle()

    def resizeEvent(self, event):
        if panelProvider.PanelProvider.rightPanel.imgViewer.hasPhoto():
            panelProvider.PanelProvider.rightPanel.imgViewer.fitInView()

    def applyStyle(self):
        with open(os.path.join(imageFolderPath, "style.qss"), "r") as styleFile:
            style = styleFile.read()

        self.setStyleSheet(style)


if __name__ == '__main__':
    main()
