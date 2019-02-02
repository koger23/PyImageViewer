import json, os

configFile = "config.json"

def loadConfig():

    if not os.path.exists(configFile):
        return {"folders":[], "extensions":["*.png", "*.jpg", "*.bmp", "*.svg", "*.tiff", "*.gif"]}

    with open(configFile, "r") as dataFile:
        datas = json.load(dataFile)
        return datas

def saveConfig(data):

    with open(configFile, "w") as dataFile:
        json.dump(data, dataFile)