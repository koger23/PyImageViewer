import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QListWidgetItem

from main import imageFolderPath
from utils import config


class FolderItem(QListWidgetItem):

    def __init__(self, path, parent):
        super(FolderItem, self).__init__(parent)

        self.path = path
        self.folderName = self.path.split("/")[-1]
        self.setText(self.folderName)
        self.setToolTip(self.path)
        self.config = config.loadConfig()
        self.setIcon(QIcon(os.path.join(imageFolderPath, self.config["icons"][4])))
