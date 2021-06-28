import os

from PySide2.QtWidgets import QListWidget

from modules.Widgets.folderItem import FolderItem
from modules import panelProvider
from objects import picture
from os import path
from utils import pictureSearch


class FolderBrowserListWidget(QListWidget):

    def __init__(self, config):
        super(FolderBrowserListWidget, self).__init__()

        self.currentFolder = None
        self.config = config
        self.pictureObjects = []

        self.itemClicked.connect(self.setCurrentFolder)

    def setCurrentFolder(self, arg=None):
        self.pictureObjects.clear()

        imgBrowser = panelProvider.PanelProvider.rightPanel.imgBrowser

        if type(arg) is FolderItem:
            self.currentFolder = arg.path
            pictureFileList = pictureSearch.searchPictures(self.currentFolder, self.config["extensions"])

            for picPath in pictureFileList:
                pictureObj = picture.Picture(picPath)
                self.pictureObjects.append(pictureObj)

        elif type(arg) is str:
            if path.isdir(arg):
                self.currentFolder = arg
                pictureFileList = pictureSearch.searchPictures(self.currentFolder, self.config["extensions"])

            if path.isfile(arg):
                self.currentFolder = os.path.dirname(os.path.abspath(arg))

                pictureFileList = pictureSearch.searchPictures(self.currentFolder, self.config["extensions"])

            index = 0
            for i in range(len(pictureFileList)):
                picPath = pictureFileList[i]
                pictureObj = picture.Picture(picPath)
                self.pictureObjects.append(pictureObj)

                if picPath == arg:
                    index = i

            imgBrowser.imageBrowserListView.refresh()
            imgBrowser.setImageByIndex(index)

    def getPictureObjects(self):
        return self.pictureObjects

    def getSelectedItem(self):
        return self.currentItem()

    def refreshView(self):
        self.clear()

        for path in self.config["folders"]:
            item = FolderItem(path, self)

