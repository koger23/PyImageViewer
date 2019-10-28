from PySide2.QtWidgets import QWidget, QVBoxLayout

from modules.Widgets.imageBrowserView import ImageBrowserView


class ImageBrowserWidget(QWidget):

    def __init__(self, folderBrowser):
        super(ImageBrowserWidget, self).__init__()
        self.setFixedHeight(170)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.browserView = ImageBrowserView(folderBrowser)
        self.browserView.setObjectName("ImageBrowser")
        mainLayout.addWidget(self.browserView)

    def nextItem(self):

        self.browserView.setCurrentRow(self.browserView.currentIndex().row() + 1)

        if self.browserView.currentIndex().row() == -1:
            self.browserView.setCurrentRow(0)

    def prevItem(self):

        self.browserView.setCurrentRow(self.browserView.currentIndex().row() - 1)

        if self.browserView.currentIndex().row() == -1:
            self.browserView.setCurrentRow(0)
