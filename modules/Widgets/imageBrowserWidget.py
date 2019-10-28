from PySide2.QtWidgets import QWidget, QVBoxLayout

from modules.Widgets.imageBrowserListWidget import ImageBrowserListWidget


class ImageBrowserWidget(QWidget):

    def __init__(self):
        super(ImageBrowserWidget, self).__init__()
        self.setFixedHeight(170)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.imageBrowserListView = ImageBrowserListWidget()
        self.imageBrowserListView.setObjectName("ImageBrowser")
        mainLayout.addWidget(self.imageBrowserListView)

    def nextImage(self):
        self.imageBrowserListView.setCurrentRow(self.imageBrowserListView.currentIndex().row() + 1)

        if self.imageBrowserListView.currentIndex().row() == -1:
            self.imageBrowserListView.setCurrentRow(0)

    def previousImage(self):
        self.imageBrowserListView.setCurrentRow(self.imageBrowserListView.currentIndex().row() - 1)
        self.imageBrowserListView.currentIndex()

        if self.imageBrowserListView.currentIndex().row() == -1:
            self.imageBrowserListView.setCurrentRow(0)

    def setImageByIndex(self, index=0):
        self.imageBrowserListView.setCurrentRow(index)
