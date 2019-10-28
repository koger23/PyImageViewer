from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QListWidgetItem


class PictureItem(QListWidgetItem):

    def __init__(self, pictureObj, parent):
        super(PictureItem, self).__init__(parent)

        self.pictureObj = pictureObj

        self.setSizeHint(QSize(120, 120))

        self.setData(Qt.UserRole, pictureObj)

        self.setToolTip(str(pictureObj.name) + "\n" + pictureObj.resolution)
