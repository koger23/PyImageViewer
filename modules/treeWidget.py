from PySide2.QtWidgets import QFileSystemModel, QTreeView, QVBoxLayout, QWidget
from PySide2.QtCore import QDir



class TreeView(QWidget):

    def __init__(self, path=None):

        super(TreeView, self).__init__()

        model = QFileSystemModel()

        print(path)

        if path:
            self.selectedPath = path
            model.setRootPath(self.selectedPath)
        else:
            self.selectedPath = QDir.currentPath()
            model.setRootPath(self.selectedPath)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        tree = QTreeView()
        tree.setModel(model)
        tree.setRootIndex(model.index(self.selectedPath))
        mainLayout.addWidget(tree)


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = TreeView()
    window.show()
    app.exec_()