import os
from PySide2.QtGui import QImage, QTransform
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QMessageBox


class Picture(object):

    def __init__(self, path):
        super(Picture, self).__init__()

        self.path = path
        self.name = self.path.split("/")[-1]
        self.extension = os.path.splitext(self.path)[1]
        self.scale = 1.0
        self.image = QImage(self.path)
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        self.resolution = "Resolution: " + str(self.image.width()) + "x" + str(self.image.height()) + "px"

    def deletePicture(self):
        os.remove(self.path)

    def verticalFlip(self):
        img = QImage(self.path)
        img = img.mirrored(vertically=True, horizontally=False)
        self.image = img
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        img.save(self.path)

    def horizontalFlip(self):
        img = QImage(self.path)
        img = img.mirrored(horizontally=True, vertically=False)
        self.image = img
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        img.save(self.path)

    def zoomIn(self):
        self.scale = self.scale*0.9

    def zoomOut(self):
        self.scale = self.scale*1.1

    def rotateCW(self):

        img = QImage(self.path)

        transform = QTransform()
        transform.translate(img.width() / 2, img.height() / 2)
        transform.rotate(90)

        img = img.transformed(transform)
        img.save(self.path)
        self.image = img
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)


    def rotateCCW(self):

        img = QImage(self.path)

        transform = QTransform()
        transform.translate(self.image.width() / 2, self.image.height() / 2)
        transform.rotate(-90)

        img = img.transformed(transform)
        img.save(self.path)

        self.image = img
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)

    def saveImage(self):

        self.image.save(self.path)