from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from utils import config


class NaviButtons(QWidget):

    def __init__(self):
        super(NaviButtons, self).__init__()
        self.setFixedHeight(50)

        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.config = config.loadConfig()

        self.btnLeft = QPushButton()
        mainLayout.addWidget(self.btnLeft)
        pixmapLeft = QPixmap('images/icon_arrow_left.png')
        self.btnLeft.setIcon(pixmapLeft)

        self.btnRight = QPushButton()
        mainLayout.addWidget(self.btnRight)
        pixmapRight = QPixmap('images/icon_arrow_right.png')
        self.btnRight.setIcon(pixmapRight)

        self.btnZoomIn = QPushButton()
        mainLayout.addWidget(self.btnZoomIn)
        pixmapPlus = QPixmap('images/icon_plus.png')
        self.btnZoomIn.setIcon(pixmapPlus)

        self.btnZoomOut = QPushButton()
        mainLayout.addWidget(self.btnZoomOut)
        pixmapMinus = QPixmap('images/icon_minus.png')
        self.btnZoomOut.setIcon(pixmapMinus)

        self.btnRotateCw = QPushButton()
        mainLayout.addWidget(self.btnRotateCw)
        pixmapCw = QPixmap('images/icon_rotate_cw.png')
        self.btnRotateCw.setIcon(pixmapCw)

        self.btnRotateCCw = QPushButton()
        mainLayout.addWidget(self.btnRotateCCw)
        pixmapCCw = QPixmap('images/icon_rotate_ccw.png')
        self.btnRotateCCw.setIcon(pixmapCCw)



