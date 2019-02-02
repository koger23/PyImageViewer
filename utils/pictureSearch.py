import os, fnmatch

def searchPictures(path):

    extensionList = ["*.png", "*.jpg", "*.bmp", "*.svg", "*.tiff", "*.gif"]

    pictureList = []

    for file in os.listdir(path):

        for ext in extensionList:

            if fnmatch.fnmatch(file, ext):
                pictureList.append(file)

    return pictureList
