import json
import os

configFile = "config.json"


def loadConfig():
    if not os.path.exists(configFile):
        return {"folders": [], "extensions": ["*.png", "*.jpg", "*.bmp", "*.svg", "*.tiff", "*.gif"],
                "icons": ["icon_rotate_cw", "icon_rotate_ccw"]}

    with open(configFile, "r") as dataFile:
        data = json.load(dataFile)
        return data


def saveConfig(data):
    with open(configFile, "w") as dataFile:
        json.dump(data, dataFile)


def getIcon(icon):
    config = loadConfig()

    return config[icon]
