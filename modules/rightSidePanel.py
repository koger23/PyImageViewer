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

        self.imgViewer = imageViewer.ImageViewer(folderBrowser)
        mainLayout.addWidget(self.imgViewer)

        self.imgBrowser = imageBrowser.ImageBrowser(folderBrowser)
        mainLayout.addWidget(self.imgBrowser)
        self.imgBrowser.imgBrowser.itemSelectionChanged.connect(self.getSelectedObject)


    def getSelectedObject(self):

        path = self.imgBrowser.imgBrowser.getSelectePicture().path

        if path:
            self.imgViewer.setPicture(path)


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = RightPanel()
    window.show()
    app.exec_()