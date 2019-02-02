from PySide2.QtWidgets import QWidget, QVBoxLayout
from modules import browserWidget, treeWidget

class LeftPanel(QWidget):

    def __init__(self):
        super(LeftPanel, self).__init__()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.folderBrowser = browserWidget.FolderBrowser()
        mainLayout.addWidget(self.folderBrowser)
        self.folderBrowser.browser.setCurrentRow(0) # select first folder in list by default at start
        self.folderBrowser.browser.itemSelectionChanged.connect(self.selectedItemChanged)

        try:
            path = self.folderBrowser.browser.currentItem().path
        except AttributeError:
            path = ""
            pass
        self.treeView = treeWidget.TreeView(path)
        mainLayout.addWidget(self.treeView)

    def selectedItemChanged(self):

        self.treeView.changePath(self.folderBrowser.browser.getSelectedItem().path)

if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = LeftPanel()
    window.show()
    app.exec_()