from PySide2.QtWidgets import QWidget, QVBoxLayout
from modules import imageViewer, naviButtons, imageBrowser

class RightPanel(QWidget):

    def __init__(self, folderBrowser):
        super(RightPanel, self).__init__()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.folderBrowser = folderBrowser

        self.naviButtons = naviButtons.NaviButtons()
        mainLayout.addWidget(self.naviButtons)

        self.imgBrowser = imageBrowser.ImageBrowser(folderBrowser)
        self.imgViewer = imageViewer.ImageViewer(self.imgBrowser)
        mainLayout.addWidget(self.imgViewer)

        mainLayout.addWidget(self.imgBrowser)
        self.imgBrowser.imgBrowser.itemSelectionChanged.connect(self.getSelectedObject)

        self.naviButtons.btnLeft.clicked.connect(self.imgBrowser.prevItem)
        self.naviButtons.btnRight.clicked.connect(self.imgBrowser.nextItem)
        self.naviButtons.btnZoomIn.clicked.connect(self.zoom_in)
        self.naviButtons.btnZoomOut.clicked.connect(self.zoom_out)
        self.naviButtons.btnRotateCw.clicked.connect(self.rotate_CW)
        self.naviButtons.btnRotateCCw.clicked.connect(self.rotate_CCW)
        self.naviButtons.btnFlipHorizontal.clicked.connect(self.flip_Horizontal)
        self.naviButtons.btnFlipVertical.clicked.connect(self.flip_Vertical)


    def zoom_in(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            self.imgViewer.zoomIn(obj)

    def zoom_out(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            self.imgViewer.zoomOut(obj)

    def rotate_CW(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            obj.rotateCW()
            self.imgBrowser.repaint()
            self.imgViewer.refreshView()

    def rotate_CCW(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            obj.rotateCCW()
            self.imgBrowser.repaint()
            self.imgViewer.refreshView()

    def flip_Horizontal(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            obj.horizontalFlip()
            self.imgBrowser.repaint()
            self.imgViewer.refreshView()

    def flip_Vertical(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            obj.verticalFlip()
            self.imgBrowser.repaint()
            self.imgViewer.refreshView()


    def getSelectedObject(self):

        obj = self.imgBrowser.imgBrowser.getSelectePicture()

        if obj:
            self.imgViewer.setPicture(obj)


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = RightPanel()
    window.show()
    app.exec_()