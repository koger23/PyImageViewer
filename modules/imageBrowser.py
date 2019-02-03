from PySide2.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QListWidgetItem, QStyledItemDelegate, QListView, QStyle
from PySide2.QtGui import QIcon, QPixmap, QBrush, QColor, QPen
from PySide2.QtCore import QSize, Qt, QRect


class ImageBrowser(QWidget):

    def __init__(self, folderBrowser):
        super(ImageBrowser, self).__init__()
        self.setFixedHeight(170)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.imgBrowser = BrowserView(folderBrowser)
        self.imgBrowser.setObjectName("ImageBrowser")
        mainLayout.addWidget(self.imgBrowser)

    def nextItem(self):

        self.imgBrowser.setCurrentRow(self.imgBrowser.currentIndex().row()+1)

        if self.imgBrowser.currentIndex().row() == -1:
            self.imgBrowser.setCurrentRow(0)

    def prevItem(self):

        self.imgBrowser.setCurrentRow(self.imgBrowser.currentIndex().row()-1)

        if self.imgBrowser.currentIndex().row() == -1:
            self.imgBrowser.setCurrentRow(0)

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

        self.setToolTip(str(pictureObj.name) + "\n" + pictureObj.resolution)

class MyDelegate(QStyledItemDelegate):

    def __init__(self):
        super(MyDelegate, self).__init__()

        self.whitePen = QPen(QColor("#ffffff"))
        self.bgColor = QBrush(QColor(255, 255, 255, 0))
        self.selectedColor = QBrush(QColor( 126, 144, 255, 70))

    def paint(self, painter, option, index):

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.bgColor)

        rect = option.rect
        painter.drawRect(rect)

        pictureObj = index.data(Qt.UserRole)

        # Picture drawing
        pixmap = QPixmap.fromImage(pictureObj.thumbnail)
                
        pixmapRect = QRect(rect.x() + ((rect.width()-pixmap.width())/2), rect.y() + ((rect.height()-pixmap.height())/2), pixmap.width(), pixmap.height())
        painter.drawPixmap(pixmapRect, pixmap)

        if option.state & QStyle.State_Selected:
            painter.setBrush(self.selectedColor)
            selectionRect = QRect(rect.x(), rect.y(), rect.height(), rect.width())
            painter.drawRect(selectionRect)
        else:
            painter.setBrush(self.bgColor)





if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageBrowser()
    window.show()
    app.exec_()