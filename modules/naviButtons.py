from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


class NaviButtons(QWidget):

    def __init__(self):
        super(NaviButtons, self).__init__()
        self.setFixedHeight(50)

        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.btnLeft = QPushButton("<")
        mainLayout.addWidget(self.btnLeft)

        self.btnRight = QPushButton(">")
        mainLayout.addWidget(self.btnRight)

        self.btnZoomIn = QPushButton("+")
        mainLayout.addWidget(self.btnZoomIn)

        self.btnZoomOut = QPushButton(">")
        mainLayout.addWidget(self.btnZoomOut)



