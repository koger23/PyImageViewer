from PySide2.QtWidgets import QWidget, QVBoxLayout

from modules.Widgets import folderBrowserWidget


class LeftPanel(QWidget):

    def __init__(self):
        super(LeftPanel, self).__init__()
        self.setFixedWidth(250)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.folderBrowser = folderBrowserWidget.FolderBrowser()
        mainLayout.addWidget(self.folderBrowser)
        self.folderBrowser.browser.setCurrentRow(0)

        try:
            self.folderBrowser.browser.currentItem().path
        except AttributeError:
            pass

    def selectedItemChanged(self):

        self.treeView.changePath(self.folderBrowser.browser.getSelectedItem().path)
