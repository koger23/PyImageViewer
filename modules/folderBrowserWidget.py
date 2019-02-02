from PySide2.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QListWidgetItem
from PySide2.QtGui import QIcon
from objects import picture
from utils import pictureSearch, config


class FolderBrowser(QWidget):

    def __init__(self):
        super(FolderBrowser, self).__init__()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.config = config.loadConfig()

        buttonLayout = QHBoxLayout()
        mainLayout.addLayout(buttonLayout)

        addFolder_btnn = QPushButton("Add Folder")
        buttonLayout.addWidget(addFolder_btnn)
        addFolder_btnn.clicked.connect(self.addFolder)

        removeFolder_bttn = QPushButton("Remove Folder")
        buttonLayout.addWidget(removeFolder_bttn)
        removeFolder_bttn.clicked.connect(self.removeFolder)

        self.browser = BrowserView(self.config)
        self.browser.setObjectName("FolderBrowser")
        mainLayout.addWidget(self.browser)

        self.browser.refreshView(self.config)


    def addFolder(self):

        folder = QFileDialog.getExistingDirectory(self, "Select folder")

        if len(folder):

            if not folder in self.config["folders"]:
                self.config["folders"].append(folder)

            config.saveConfig(self.config)
            self.browser.refreshView(self.config)

        self.browser.refreshView(self.config)

    def removeFolder(self):

        if not self.browser.currentItem():
            return

        folderPath = self.browser.currentItem().path

        self.config["folders"].remove(folderPath)

        config.saveConfig(self.config)

        self.browser.refreshView(self.config)


class BrowserView(QListWidget):

    def __init__(self, config):
        super(BrowserView, self).__init__()

        self.currentFolder = None

        self.config = config

        self.pictureObjects = []

        self.itemClicked.connect(self.setCurrentFolder)

    def setCurrentFolder(self):

        self.pictureObjects = []
        self.currentFolder = self.currentItem().path

        pictureFileList = pictureSearch.searchPictures(self.currentFolder, self.config["extensions"])

        for picPath in pictureFileList:

            pictureObj = picture.Picture(picPath)

            self.pictureObjects.append(pictureObj)

    def getPictureObjects(self):

        return self.pictureObjects

    def getSelectedItem(self):

        return self.currentItem()

    def refreshView(self, config):

        self.clear()

        for path in config["folders"]:
            item = FolderItem(path, self)


class FolderItem(QListWidgetItem):

    def __init__(self, path, parent):
        super(FolderItem, self).__init__(parent)

        folderName = ""

        self.path = path

        folderName = self.path.split("/")[-1]

        self.setText(folderName)
        self.setToolTip(self.path)



if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = FolderBrowser()
    window.show()
    app.exec_()