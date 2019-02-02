import os


class Picture(object):

    def __init__(self, path):
        super(Picture, self).__init__()

        self.path = path
        self.name = self.path.split("/")[-1]
        self.extension = os.path.splitext(self.path)[1]
        self.scale = 1.0

    def zoomIn(self):
        self.scale = self.scale*0.9

    def zoomOut(self):
        self.scale = self.scale*1.1
