import os

from modules.Widgets.leftPanelWidget import LeftPanelWidget
from modules.Widgets.rightPanelWidget import RightPanelWidget


class PanelProvider:
    leftPanel = None
    rightPanel = None

    @staticmethod
    def getInstance():
        if PanelProvider.leftPanel is None:
            PanelProvider()
        return PanelProvider.leftPanel

    def __init__(self, main):
        if PanelProvider.leftPanel is not None or PanelProvider.rightPanel is not None:
            raise Exception("This class is a singleton!")
        else:
            PanelProvider.leftPanel = LeftPanelWidget()
            PanelProvider.rightPanel = RightPanelWidget()

        if len(main.openedPicture) > 0:
            PanelProvider.leftPanel.setHidden(True)
            PanelProvider.leftPanel.folderBrowser.folderBrowserView.setCurrentFolder(
                main.openedPicture)
        else:
            print(PanelProvider.leftPanel.folderBrowser.folderBrowserView.currentFolder)
            pic = PanelProvider.leftPanel.folderBrowser.folderBrowserView.currentFolder
            # PanelProvider.leftPanel.folderBrowser.folderBrowserView.setCurrentFolder(pic)
            pic = PanelProvider.leftPanel.folderBrowser.folderBrowserView.getPictureObjects()
            print(pic)
            # pic = pic[0]
            # PanelProvider.leftPanel.folderBrowser.folderBrowserView.setCurrentFolder(pic.path)

            try:
                currPath = self.leftPanel.folderBrowser.folderBrowserView.currentItem().path
                PanelProvider.leftPanel.folderBrowser.folderBrowserView.setCurrentFolder(currPath)
                pics = PanelProvider.leftPanel.folderBrowser.folderBrowserView.getPictureObjects()
                # pic = pics[0]
            except AttributeError:
                pass
