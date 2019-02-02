from PySide2.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QListWidgetItem, QStyledItemDelegate, QListView, QStyle
from PySide2.QtGui import QIcon, QPixmap, QBrush, QColor, QPen
from PySide2.QtCore import QSize, Qt, QRect


class ImageBrowser(QWidget):

    def __init__(self, folderBrowser):
        super(ImageBrowser, self).__init__()
        self.setMaximumHeight(200)

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
        self.currentPicture = None
        self.folderBrowser.browser.itemClicked.connect(self.refresh)

    def getSelectePicture(self):

        currentItem = self.currentItem()

        if currentItem:
            curPicItem = currentItem.data(Qt.UserRole)
            return curPicItem

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

        self.whitePen = QPen(QColor("#ffffff"))
        self.bgColor = QBrush(QColor(255, 255, 255, 60))
        self.selectedColor = QBrush(QColor(30, 30, 30, 60))

    def paint(self, painter, option, index):

        rect = option.rect
        painter.drawRect(rect)

        painter.setPen(self.whitePen)

        pictureObj = index.data(Qt.UserRole)

        # Picture drawing
        pixmap = QPixmap(pictureObj.path)
        pixmap = pixmap.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
                
        pixmapRect = QRect(rect.x() + 5, rect.y() + 5, pixmap.width(), pixmap.height())
        painter.drawPixmap(pixmapRect, pixmap)

        if option.state & QStyle.State_Selected:
            painter.setBrush(self.selectedColor)
        else:
            painter.setBrush(self.bgColor)

        selectionRect = QRect(rect.x(), rect.y(), rect.height(), rect.width())
        painter.drawRect(selectionRect)



if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageBrowser()
    window.show()
    app.exec_()