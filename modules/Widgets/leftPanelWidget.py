from PySide2.QtWidgets import QWidget, QVBoxLayout

from modules import panelProvider
from modules.Widgets import folderBrowserWidget
# from modules.Widgets.treeWidget import TreeView


class LeftPanelWidget(QWidget):

    def __init__(self):
        super(LeftPanelWidget, self).__init__()
        self.setFixedWidth(250)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.folderBrowser = folderBrowserWidget.FolderBrowserWidget()
        mainLayout.addWidget(self.folderBrowser)
        self.folderBrowser.folderBrowserView.setCurrentRow(0)
        # self.treeView = TreeView()
        # mainLayout.addWidget(self.treeView)

        # try:
        #     self.folderBrowser.folderBrowserView.currentItem().path
        # except AttributeError:
        #     pass

    def selectedItemChanged(self):
        self.treeView.changePath(self.folderBrowser.folderBrowserView.getSelectedItem().path)
