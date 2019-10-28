import os

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton

from main import imageFolderPath
from utils import config


class NaviButtons(QWidget):

    def __init__(self):
        super(NaviButtons, self).__init__()
        self.setFixedHeight(50)

        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.config = config.loadConfig()

        self.btnLeft = QPushButton()
        self.btnLeft.setToolTip("Previous image")
        mainLayout.addWidget(self.btnLeft)
        pixmapLeft = QPixmap(os.path.join(imageFolderPath, self.config["icons"][0]))
        self.btnLeft.setIcon(pixmapLeft)

        self.btnRight = QPushButton()
        self.btnRight.setToolTip("Next image")
        mainLayout.addWidget(self.btnRight)
        pixmapRight = QPixmap(os.path.join(imageFolderPath, self.config["icons"][1]))
        self.btnRight.setIcon(pixmapRight)

        self.btnZoomIn = QPushButton()
        self.btnZoomIn.setToolTip("Zoom in")
        mainLayout.addWidget(self.btnZoomIn)
        pixmapPlus = QPixmap(os.path.join(imageFolderPath, self.config["icons"][8]))
        self.btnZoomIn.setIcon(pixmapPlus)

        self.btnZoomSetBack = QPushButton()
        self.setToolTip("Fit view")
        mainLayout.addWidget(self.btnZoomSetBack)
        pixmapPlus = QPixmap(os.path.join(imageFolderPath, self.config["icons"][2]))
        self.btnZoomSetBack.setIcon(pixmapPlus)

        self.btnZoomOut = QPushButton()
        self.btnZoomOut.setToolTip("Zoom out")
        mainLayout.addWidget(self.btnZoomOut)
        pixmapMinus = QPixmap(os.path.join(imageFolderPath, self.config["icons"][6]))
        self.btnZoomOut.setIcon(pixmapMinus)

        self.btnRotateCw = QPushButton()
        self.btnRotateCw.setToolTip("Rotate clockwise")
        mainLayout.addWidget(self.btnRotateCw)
        pixmapCw = QPixmap(os.path.join(imageFolderPath, self.config["icons"][10]))
        self.btnRotateCw.setIcon(pixmapCw)

        self.btnRotateCCw = QPushButton()
        self.btnRotateCCw.setToolTip("Rotate counterclockwise")
        mainLayout.addWidget(self.btnRotateCCw)
        pixmapCCw = QPixmap(os.path.join(imageFolderPath, self.config["icons"][9]))
        self.btnRotateCCw.setIcon(pixmapCCw)

        self.btnFlipHorizontal = QPushButton()
        self.btnFlipHorizontal.setToolTip("Mirror horizontally")
        mainLayout.addWidget(self.btnFlipHorizontal)
        pixmapFlipHorizontal = QPixmap(os.path.join(imageFolderPath, self.config["icons"][5]))
        self.btnFlipHorizontal.setIcon(pixmapFlipHorizontal)

        self.btnFlipVertical = QPushButton()
        self.btnFlipHorizontal.setToolTip("Mirror vertically")
        mainLayout.addWidget(self.btnFlipVertical)
        pixmapFlipVertical = QPixmap(os.path.join(imageFolderPath, self.config["icons"][11]))
        self.btnFlipVertical.setIcon(pixmapFlipVertical)

        self.btnDeletePicture = QPushButton()
        self.btnDeletePicture.setToolTip("Delete image")
        mainLayout.addWidget(self.btnDeletePicture)
        pixmapDeletePic = QPixmap(os.path.join(imageFolderPath, self.config["icons"][3]))
        self.btnDeletePicture.setIcon(pixmapDeletePic)
