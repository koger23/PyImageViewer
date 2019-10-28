import os

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QImage, QTransform


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
        self.image = self.image.mirrored(vertically=True, horizontally=False)
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        self.image.save(self.path)

    def horizontalFlip(self):
        self.image = self.image.mirrored(horizontally=True, vertically=False)
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
        self.image.save(self.path)

    def zoomIn(self):
        self.scale = self.scale * 0.9

    def zoomOut(self):
        self.scale = self.scale * 1.1

    def rotateCW(self):
        transform = QTransform()
        transform.translate(self.image.width() / 2, self.image.height() / 2)
        transform.rotate(90)

        self.image = self.image.transformed(transform)
        self.image.save(self.path)
        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)

    def rotateCCW(self):
        transform = QTransform()
        transform.translate(self.image.width() / 2, self.image.height() / 2)
        transform.rotate(-90)

        self.image = self.image.transformed(transform)
        self.image.save(self.path)

        self.thumbnail = self.image.scaled(QSize(110, 110), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)

    def saveImage(self):
        self.image.save(self.path)
