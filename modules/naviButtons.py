from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


class NaviButtons(QWidget):

    def __init__(self):
        super(NaviButtons, self).__init__()

        mainLayout = QHBoxLayout(self)

        self.btnLeft = QPushButton("<")
        mainLayout.addWidget(self.btnLeft)
        self.btnLeft.setMaximumWidth(30)

        self.btnRight = QPushButton(">")
        mainLayout.addWidget(self.btnRight)
        self.btnRight.setMaximumWidth(30)



