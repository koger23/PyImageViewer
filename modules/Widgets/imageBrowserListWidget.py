from PySide2.QtCore import Qt
from PySide2.QtWidgets import QListWidget

from modules import panelProvider
from modules.Widgets.imageBrowserListItemDelegate import ImageBrowserListItemDelegate
from modules.Widgets.pictureItem import PictureItem


class ImageBrowserListWidget(QListWidget):

    def __init__(self):
        super(ImageBrowserListWidget, self).__init__()

        self.setViewMode(QListWidget.IconMode)
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)
        self.setFlow(QListWidget.LeftToRight)
        self.setWrapping(False)
        self.setSpacing(10)
        self.setItemDelegate(ImageBrowserListItemDelegate())
        self.setFixedHeight(170)
        self.currentPicture = None

        self.folderBrowserView = panelProvider.PanelProvider.leftPanel.folderBrowser.folderBrowserView
        self.folderBrowserView.itemClicked.connect(self.refresh)

    def getSelectPicture(self):
        currentItem = self.currentItem()

        if currentItem:
            curPicItem = currentItem.data(Qt.UserRole)
            return curPicItem

    def refresh(self):
        self.clear()

        for pictureObj in self.folderBrowserView.getPictureObjects():
            PictureItem(pictureObj, self)