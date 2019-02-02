from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QScrollArea, QSizePolicy
from PySide2.QtGui import QPixmap, QImage, QPalette, QInputEvent
from PySide2.QtCore import Qt, QSize


class ImageViewer(QWidget):

    def __init__(self, folderBrowser, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setMinimumSize(700, 300)

        self.picObjects = None

        self.picObjects = folderBrowser.browser.getPictureObjects()

        mainlayout = QHBoxLayout(self)

        self.lblPicture = QLabel("No image...")
        self.lblPicture.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.lblPicture.setBackgroundRole(QPalette.Dark)
        # self.lblPicture.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.lblPicture.setScaledContents(False)
        mainlayout.addWidget(self.lblPicture)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.lblPicture)
        mainlayout.addWidget(self.scrollArea)



    def setPicture(self, path=None):

        if path:

            print(path)
            # pixmap = QPixmap(path)
            #
            # Resizing picture
            # if pixmap.width() > self.rect().width():
            #     pixmap = pixmap.scaled(QSize(self.rect().width(), pixmap.height()), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
            #
            # if pixmap.height() > self.rect().height():
            #     pixmap = pixmap.scaled(QSize(pixmap.width(), self.rect().height()), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
            # self.lblPicture.setPixmap(pixmap)

            self.image = QImage(path)
            self.lblPicture.setPixmap(QPixmap.fromImage(self.image))


        else:
            self.lblPicture.setText("Select a picture...")

        self.repaint()



if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec_()