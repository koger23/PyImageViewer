import os


class Picture(object):

    def __init__(self, path):
        super(Picture, self).__init__()

        self.path = path
        self.name = self.path.split("/")[-1]
        self.extension = os.path.splitext(self.path)[1]
