from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QScrollArea, QSizePolicy
from PySide2.QtGui import QPixmap, QPalette
from PySide2.QtCore import Qt


class ImageViewer(QWidget):

    def __init__(self, imageBrowser, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setMinimumSize(700, 300)

        self.picObject = None

        self.imageBrowser = imageBrowser

        mainlayout = QHBoxLayout(self)

        self.lblPicture = QLabel("No image...")
        self.lblPicture.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.lblPicture.setBackgroundRole(QPalette.Dark)
        self.lblPicture.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lblPicture.setScaledContents(False)
        mainlayout.addWidget(self.lblPicture)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.lblPicture)
        mainlayout.addWidget(self.scrollArea)

    def _rotateCW(self):

        self.picObject.rotateCW()
        self.setPicture(self.picObject)
        self.imageBrowser.imgBrowser.refresh()

    def _rotateCCW(self):

        self.picObject.rotateCCW()
        self.setPicture(self.picObject)
        self.imageBrowser.imgBrowser.refresh()

    def zoomIn(self, imageObj):

        imageObj.scale = imageObj.scale*1.1
        self.setPicture(imageObj)
        self.repaint()


    def zoomOut(self, imageObj):

        imageObj.scale = imageObj.scale*0.9
        self.setPicture(imageObj)
        self.repaint()


    def setPicture(self, imageObj=None):

        if imageObj.path:

            self.picObject = imageObj

            if imageObj.image.height() > self.scrollArea.height():
                imageObj.image = imageObj.image.scaledToHeight(self.scrollArea.height() * imageObj.scale - 2, Qt.SmoothTransformation)

            if imageObj.image.width() > self.scrollArea.width():
                imageObj.image = imageObj.image.scaledToWidth(self.scrollArea.width() * imageObj.scale - 2, Qt.SmoothTransformation)

            if imageObj.scale != 1.0:

                if imageObj.image.width() == self.scrollArea.width():
                    imageObj.image = imageObj.image.scaledToWidth(self.scrollArea.width() * imageObj.scale - 2, Qt.SmoothTransformation)
                else:
                    imageObj.image = imageObj.image.scaledToWidth(self.scrollArea.height() * imageObj.scale - 2, Qt.SmoothTransformation)

            self.lblPicture.setPixmap(QPixmap.fromImage(imageObj.image))


        else:
            self.lblPicture.setText("Select a picture...")


    def refreshView(self):

        if self.picObject.image.height() > self.scrollArea.height():
            self.picObject.image = self.picObject.image.scaledToHeight(self.scrollArea.height() * self.picObject.scale - 2,
                                                           Qt.SmoothTransformation)

        if self.picObject.image.width() > self.scrollArea.width():
            self.picObject.image = self.picObject.image.scaledToWidth(self.scrollArea.width() * self.picObject.scale - 2,
                                                          Qt.SmoothTransformation)

        if self.picObject.scale != 1.0:

            if self.picObject.image.width() == self.scrollArea.width():
                self.picObject.image = self.picObject.image.scaledToWidth(self.scrollArea.width() * self.picObject.scale - 2,
                                                              Qt.SmoothTransformation)
            else:
                self.picObject.image = self.picObject.image.scaledToWidth(self.scrollArea.height() * self.picObject.scale - 2,
                                                              Qt.SmoothTransformation)

        self.lblPicture.setPixmap(QPixmap.fromImage(self.picObject.image))

        self.repaint()

if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec_()