from PySide2.QtWidgets import QListWidget

from modules.Widgets.folderItem import FolderItem
from objects import picture
from utils import pictureSearch


class FolderBrowserView(QListWidget):

    def __init__(self, config):
        super(FolderBrowserView, self).__init__()

        self.currentFolder = None
        self.config = config
        self.pictureObjects = []

        self.itemClicked.connect(self.setCurrentFolder)

    def setCurrentFolder(self):
        self.pictureObjects.clear()
        self.currentFolder = self.currentItem().path

        pictureFileList = pictureSearch.searchPictures(self.currentFolder, self.config["extensions"])

        for picPath in pictureFileList:
            pictureObj = picture.Picture(picPath)
            self.pictureObjects.append(pictureObj)

    def getPictureObjects(self):
        return self.pictureObjects

    def getSelectedItem(self):
        return self.currentItem()

    def refreshView(self):
        self.clear()

        for path in self.config["folders"]:
            item = FolderItem(path, self)
