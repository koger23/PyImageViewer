from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton

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
        pixmapLeft = QPixmap('images/icon_arrow_left.png')
        self.btnLeft.setIcon(pixmapLeft)

        self.btnRight = QPushButton()
        self.btnRight.setToolTip("Next image")
        mainLayout.addWidget(self.btnRight)
        pixmapRight = QPixmap('images/icon_arrow_right.png')
        self.btnRight.setIcon(pixmapRight)

        self.btnZoomIn = QPushButton()
        self.btnZoomIn.setToolTip("Zoom in")
        mainLayout.addWidget(self.btnZoomIn)
        pixmapPlus = QPixmap('images/icon_plus.png')
        self.btnZoomIn.setIcon(pixmapPlus)

        self.btnZoomSetBack = QPushButton()
        self.setToolTip("Fit view")
        mainLayout.addWidget(self.btnZoomSetBack)
        pixmapPlus = QPixmap('images/icon_back_to_original.png')
        self.btnZoomSetBack.setIcon(pixmapPlus)

        self.btnZoomOut = QPushButton()
        self.btnZoomOut.setToolTip("Zoom out")
        mainLayout.addWidget(self.btnZoomOut)
        pixmapMinus = QPixmap('images/icon_minus.png')
        self.btnZoomOut.setIcon(pixmapMinus)

        self.btnRotateCw = QPushButton()
        self.btnRotateCw.setToolTip("Rotate clockwise")
        mainLayout.addWidget(self.btnRotateCw)
        pixmapCw = QPixmap('images/icon_rotate_cw.png')
        self.btnRotateCw.setIcon(pixmapCw)

        self.btnRotateCCw = QPushButton()
        self.btnRotateCCw.setToolTip("Rotate counterclockwise")
        mainLayout.addWidget(self.btnRotateCCw)
        pixmapCCw = QPixmap('images/icon_rotate_ccw.png')
        self.btnRotateCCw.setIcon(pixmapCCw)

        self.btnFlipHorizontal = QPushButton()
        self.btnFlipHorizontal.setToolTip("Mirror horizontally")
        mainLayout.addWidget(self.btnFlipHorizontal)
        pixmapFlipHorizontal = QPixmap('images/icon_horizontal_flip.png')
        self.btnFlipHorizontal.setIcon(pixmapFlipHorizontal)

        self.btnFlipVertical = QPushButton()
        self.btnFlipHorizontal.setToolTip("Mirror vertically")
        mainLayout.addWidget(self.btnFlipVertical)
        pixmapFlipVertical = QPixmap('images/icon_vertical_flip.png')
        self.btnFlipVertical.setIcon(pixmapFlipVertical)

        self.btnDeletePicture = QPushButton()
        self.btnDeletePicture.setToolTip("Delete image")
        mainLayout.addWidget(self.btnDeletePicture)
        pixmapDeletePic = QPixmap('images/icon_delete.png')
        self.btnDeletePicture.setIcon(pixmapDeletePic)
