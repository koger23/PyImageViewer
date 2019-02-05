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
        self._scene.addItem(self._photo)
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

        self.picObject = imgObj

        self._zoom = 0

        pixmap = QPixmap(QPixmap.fromImage(imgObj.image))

        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
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
        self.setPhoto(self.picObject)

        self.fitInView()
        self.imageBrowser.imgBrowser.refresh()

    def _rotateCCW(self):

        self.picObject.rotateCCW()
        self.setPhoto(self.imageBrowser.imgBrowser.getSelectePicture().image)
        self.imageBrowser.imgBrowser.refresh()

    def zoomIn(self, imageObj):

        self.scale(1.2, 1.2)

    def zoomToOriginal(self, imageObj):

        self.fitInView()

    def zoomOut(self, imageObj):

        self.scale(0.9, 0.9)

if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec_()