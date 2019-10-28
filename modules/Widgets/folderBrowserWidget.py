from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

from modules.Widgets.folderBrowserView import FolderBrowserView
from utils import config


class FolderBrowser(QWidget):

    def __init__(self):
        super(FolderBrowser, self).__init__()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.config = config.loadConfig()

        buttonLayout = QHBoxLayout()
        mainLayout.addLayout(buttonLayout)

        addFolder_btn = QPushButton("Add Folder")
        buttonLayout.addWidget(addFolder_btn)
        addFolder_btn.clicked.connect(self.addFolder)

        removeFolder_btn = QPushButton("Remove Folder")
        buttonLayout.addWidget(removeFolder_btn)
        removeFolder_btn.clicked.connect(self.removeFolder)

        self.browser = FolderBrowserView(self.config)
        self.browser.setObjectName("FolderBrowser")
        mainLayout.addWidget(self.browser)

        self.browser.refreshView(self.config)

    def addFolder(self):

        folder = QFileDialog.getExistingDirectory(self, "Select folder")

        if len(folder):

            if folder not in self.config["folders"]:
                self.config["folders"].append(folder)

            config.saveConfig(self.config)
            self.browser.refreshView(self.config)

        self.browser.refreshView(self.config)

    def removeFolder(self):

        if not self.browser.currentItem():
            return

        folderPath = self.browser.currentItem().path

        self.config["folders"].remove(folderPath)

        config.saveConfig(self.config)

        self.browser.refreshView(self.config)
