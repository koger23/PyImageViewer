from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem, QFrame
from PySide2.QtGui import QPixmap, QBrush, QPen, QColor, QImage
from PySide2.QtCore import Qt, QPoint, QRectF, Signal


class ImageViewer(QGraphicsView):

    photoClicked = Signal(QPoint)

    def __init__(self, imageBrowser, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setMinimumSize(700, 300)

        self._zoom = 0
        self._empty = True

        self._scene = QGraphicsScene(self)
        self._photo = QGraphicsPixmapItem()

        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QBrush(QColor(33, 33, 33)))
        self.setFrameShape(QFrame.NoFrame)

        self.picObject = None

        self.imageBrowser = imageBrowser


    def setPhoto(self, imgObj=None):
        self._zoom = 0

        pixmap = QPixmap(QPixmap.fromImage(imgObj.image))

        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
            self._scene.addPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())
        self.fitInView()

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            self.setDragMode(QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(QPoint(event.pos()))
        super(ImageViewer, self).mousePressEvent(event)

    # OLD FUNCTION FROM HERE
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

    def zoomToOriginal(self, imageObj):

        imageObj.scale = 1.0
        self.setPicture(imageObj)

    def zoomOut(self, imageObj):

        imageObj.scale = imageObj.scale*0.9
        self.setPicture(imageObj)

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