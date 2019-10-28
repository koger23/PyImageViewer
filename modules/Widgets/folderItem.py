from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QListWidgetItem


class FolderItem(QListWidgetItem):

    def __init__(self, path, parent):
        super(FolderItem, self).__init__(parent)

        self.path = path

        folderName = self.path.split("/")[-1]

        self.setText(folderName)

        self.setToolTip(self.path)

        self.setIcon(QIcon("images/icon_folder.png"))
