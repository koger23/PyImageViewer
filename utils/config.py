import json
import os
from pathlib import Path

mainPath = mainPath = Path(__file__).parents[0]
configFile = "config.json"


def loadConfig():
    if not os.path.exists(os.path.join(mainPath, configFile)):
        return {"folders": [], "extensions": ["*.png", "*.jpg", "*.bmp", "*.svg", "*.tiff", "*.gif"],
                "icons": ["icon_arrow_left.png",
                          "icon_arrow_right.png",
                          "icon_back_to_original.png",
                          "icon_delete.png",
                          "icon_folder.png",
                          "icon_horizontal_flip.png",
                          "icon_minus.png",
                          "icon_picture.jpg",
                          "icon_plus.png",
                          "icon_rotate_ccw.png",
                          "icon_rotate_cw.png",
                          "icon_vertical_flip.png"]}

    with open(os.path.join(mainPath, configFile), "r") as dataFile:
        data = json.load(dataFile)
        return data


def saveConfig(data):
    with open(os.path.join(mainPath, configFile), "w") as dataFile:
        json.dump(data, dataFile)


def getIcon(icon):
    config = loadConfig()
    return config[icon]
