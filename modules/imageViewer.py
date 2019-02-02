from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


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

        # Resizing picture
        if pixmap.width() > self.rect().width():
            pixmap = pixmap.scaledToWidth(self.rect().width(), Qt.SmoothTransformation)

        if pixmap.height() > self.rect().height():
            pixmap = pixmap.scaledToWidth(self.rect().height(), Qt.SmoothTransformation)

        print("Setting pixmap... ", pixmap.width(),"x", pixmap.height())

        self.lblPicture.setPixmap(pixmap)

        self.repaint()


    def resetPicture(self, path=None):

        print("reset")
        pixmap = QPixmap(path)

        # Resizing picture
        if pixmap.width() > self.rect().width():
            pixmap = pixmap.scaledToWidth(self.rect().width(), Qt.SmoothTransformation)

        if pixmap.height() > self.rect().height():
            pixmap = pixmap.scaledToWidth(self.rect().height(), Qt.SmoothTransformation)

        print("Setting pixmap... ", pixmap.width(),"x", pixmap.height())
        self.lblPicName.setText(path)
        self.lblPicture.setPixmap(pixmap)


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec_()