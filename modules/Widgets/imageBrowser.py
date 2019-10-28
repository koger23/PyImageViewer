from PySide2.QtWidgets import QWidget, QVBoxLayout

from modules.Widgets.browserView import BrowserView


class ImageBrowser(QWidget):

    def __init__(self, folderBrowser):
        super(ImageBrowser, self).__init__()
        self.setFixedHeight(170)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.imgBrowser = BrowserView(folderBrowser)
        self.imgBrowser.setObjectName("ImageBrowser")
        mainLayout.addWidget(self.imgBrowser)

    def nextItem(self):

        self.imgBrowser.setCurrentRow(self.imgBrowser.currentIndex().row() + 1)

        if self.imgBrowser.currentIndex().row() == -1:
            self.imgBrowser.setCurrentRow(0)

    def prevItem(self):

        self.imgBrowser.setCurrentRow(self.imgBrowser.currentIndex().row() - 1)

        if self.imgBrowser.currentIndex().row() == -1:
            self.imgBrowser.setCurrentRow(0)
