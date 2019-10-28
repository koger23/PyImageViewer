from PySide2.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from modules.Widgets import imageViewer, imageBrowser, naviButtons


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
        self.naviButtons.btnZoomSetBack.clicked.connect(self.zoom_back_to_original)
        self.naviButtons.btnZoomOut.clicked.connect(self.zoom_out)
        self.naviButtons.btnRotateCw.clicked.connect(self.rotate_CW)
        self.naviButtons.btnRotateCCw.clicked.connect(self.rotate_CCW)
        self.naviButtons.btnFlipHorizontal.clicked.connect(self.flip_Horizontal)
        self.naviButtons.btnFlipVertical.clicked.connect(self.flip_Vertical)
        self.naviButtons.btnDeletePicture.clicked.connect(self.delete_Picture)

    def delete_Picture(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:

            msgBox = QMessageBox()
            msgBox.setText(u'The picture will be deleted from your computer.\n\nAre you sure?')
            msgBox.setWindowTitle('File deletion')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            response = msgBox.exec_()

            if response == QMessageBox.Yes:
                obj.deletePicture()
                self.imgBrowser.imgBrowser.takeItem(self.imgBrowser.imgBrowser.currentRow())
            elif QMessageBox.Cancel:
                return
            else:
                return

    def zoom_in(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            self.imgViewer.zoomIn()

    def zoom_out(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            self.imgViewer.zoomOut()

    def zoom_back_to_original(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            self.imgViewer.fitInView()

    def rotate_CW(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            obj.rotateCW()
            self.imgBrowser.repaint()
            self.imgViewer.setPhoto(obj)

    def rotate_CCW(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            obj.rotateCCW()
            self.imgBrowser.repaint()
            self.imgViewer.setPhoto(obj)

    def flip_Horizontal(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            obj.horizontalFlip()
            self.imgBrowser.repaint()
            self.imgViewer.setPhoto(obj)

    def flip_Vertical(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            obj.verticalFlip()
            self.imgBrowser.repaint()
            self.imgViewer.setPhoto(obj)

    def getSelectedObject(self):

        obj = self.imgBrowser.imgBrowser.getSelectPicture()

        if obj:
            self.imgViewer.setPhoto(obj)