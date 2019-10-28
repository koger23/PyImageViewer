from PySide2.QtCore import QDir
from PySide2.QtWidgets import QFileSystemModel, QTreeView, QVBoxLayout, QWidget


class TreeView(QWidget):

    def __init__(self, path=None):

        super(TreeView, self).__init__()

        self.model = QFileSystemModel()

        if path:
            self.selectedPath = path
            self.model.setRootPath(self.selectedPath)
        else:
            self.selectedPath = QDir.currentPath()
            self.model.setRootPath(self.selectedPath)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.selectedPath))
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)
        mainLayout.addWidget(self.tree)

    def changePath(self, path):

        self.selectedPath = path

        self.tree.setModel(None)

        self.model.setRootPath(self.selectedPath)
        self.model.setNameFilters(["*.png", "*.jpg", "*.bmp", "*.svg", "*.tiff", "*.gif"])

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.selectedPath))
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)

        self.repaint()


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = TreeView()
    window.show()
    app.exec_()
