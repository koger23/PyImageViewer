import os, fnmatch

def searchPictures(path, extensions):

    extensionList = extensions

    pictureList = []

    for file in os.listdir(path):

        for ext in extensionList:

            if fnmatch.fnmatch(file, ext):
                pictureList.append(os.path.join(path, file))

    return pictureList
