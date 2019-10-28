from PySide2.QtCore import Qt
from PySide2.QtWidgets import QListWidget

from modules.Widgets.browserViewDelegate import BrowserViewDelegate
from modules.Widgets.pictureItem import PictureItem


class BrowserView(QListWidget):

    def __init__(self, folderBrowser):
        super(BrowserView, self).__init__()

        self.setViewMode(QListWidget.IconMode)
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)
        self.setFlow(QListWidget.LeftToRight)
        self.setWrapping(False)
        self.setSpacing(10)
        self.setItemDelegate(BrowserViewDelegate())
        self.setFixedHeight(170)

        self.folderBrowser = folderBrowser
        self.currentPicture = None
        self.folderBrowser.browser.itemClicked.connect(self.refresh)

    def getSelectPicture(self):

        currentItem = self.currentItem()

        if currentItem:
            curPicItem = currentItem.data(Qt.UserRole)
            return curPicItem

    def refresh(self):
        self.clear()

        for pictureObj in self.folderBrowser.browser.getPictureObjects():
            PictureItem(pictureObj, self)
