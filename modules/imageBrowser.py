from PySide2.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QListWidgetItem, QStyledItemDelegate, QListView
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt


class ImageBrowser(QWidget):

    def __init__(self, folderBrowser):
        super(ImageBrowser, self).__init__()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.imgBrowser = BrowserView(folderBrowser)
        mainLayout.addWidget(self.imgBrowser)

class BrowserView(QListWidget):

    def __init__(self, folderBrowser):
        super(BrowserView, self).__init__()

        self.setViewMode(QListWidget.IconMode)
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)
        self.setFlow(QListWidget.LeftToRight)
        self.setWrapping(False)
        self.setSpacing(10)
        self.setItemDelegate(MyDelegate())
        self.setFixedHeight(170)

        self.folderBrowser = folderBrowser
        self.currentMovie = None
        self.folderBrowser.browser.itemClicked.connect(self.refresh)



    def refresh(self):
        self.clear() # Itt csak egy self kell, mert már benne vagyunk a ListWidget-ben

        for pictureObj in self.folderBrowser.browser.getPictureObjects():
            pictureItem = PictureItem(pictureObj, self)

class PictureItem(QListWidgetItem):

    def __init__(self, pictureObj, parent):
        super(PictureItem, self).__init__(parent)

        self.pictureObj = pictureObj

        self.setSizeHint(QSize(120, 120))

        self.setData(Qt.UserRole, pictureObj)

class MyDelegate(QStyledItemDelegate):

    def __init__(self):
        super(MyDelegate, self).__init__()

    def paint(self, painter, option, index):

        rect = option.rect

        pictureObj = index.data(Qt.UserRole)

        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, pictureObj.name)

        painter.drawRect(rect)

if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageBrowser()
    window.show()
    app.exec_()