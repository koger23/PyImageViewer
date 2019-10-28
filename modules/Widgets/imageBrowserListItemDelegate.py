from PySide2.QtCore import Qt, QRect
from PySide2.QtGui import QPen, QColor, QBrush, QPixmap
from PySide2.QtWidgets import QStyledItemDelegate, QStyle


class ImageBrowserListItemDelegate(QStyledItemDelegate):

    def __init__(self):
        super(ImageBrowserListItemDelegate, self).__init__()

        self.whitePen = QPen(QColor("#ffffff"))
        self.bgColor = QBrush(QColor(255, 255, 255, 0))
        self.selectedColor = QBrush(QColor(126, 144, 255, 70))

    def paint(self, painter, option, index):
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.bgColor)

        rect = option.rect
        painter.drawRect(rect)

        pictureObj = index.data(Qt.UserRole)

        pixmap = QPixmap.fromImage(pictureObj.thumbnail)

        pixmapRect = QRect(rect.x() + ((rect.width() - pixmap.width()) / 2),
                           rect.y() + ((rect.height() - pixmap.height()) / 2), pixmap.width(), pixmap.height())
        painter.drawPixmap(pixmapRect, pixmap)

        if option.state & QStyle.State_Selected:
            painter.setBrush(self.selectedColor)
            selectionRect = QRect(rect.x(), rect.y(), rect.height(), rect.width())
            painter.drawRect(selectionRect)
        else:
            painter.setBrush(self.bgColor)
