from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QSize


class ImageViewer(QWidget):

    def __init__(self, folderBrowser):
        super(ImageViewer, self).__init__()
        self.setMinimumSize(700, 300)

        self.picObjects = None

        self.picObjects = folderBrowser.browser.getPictureObjects()

        mainlayout = QHBoxLayout(self)

        self.lblPicture = QLabel("No image...")
        self.lblPicture.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        mainlayout.addWidget(self.lblPicture)

        if len(self.picObjects):
            self.setPicture(self.picObjects[0].path)


    def setPicture(self, path=None):

        pixmap = QPixmap(path)

        print("self.rect: " , self.rect().width(), "x", self.rect().height())

        # Resizing picture
        if pixmap.width() > self.rect().width():
            # pixmap = pixmap.scaledToWidth(self.rect().width(), Qt.SmoothTransformation)
            pixmap = pixmap.scaled(QSize(self.rect().width(), pixmap.height()), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)

        if pixmap.height() > self.rect().height():
            # pixmap = pixmap.scaledToWidth(self.rect().height(), Qt.SmoothTransformation)
            pixmap = pixmap.scaled(QSize(pixmap.width(), self.rect().height()), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)


        print("Pixmap... ", pixmap.width(),"x", pixmap.height())

        self.lblPicture.setPixmap(pixmap)

        self.repaint()


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec_()