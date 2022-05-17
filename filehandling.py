import json

import getList


def checkIsValidFile(fileName):
    try:
        file = open(fileName, 'r')
        file.close()
        return True
    except:
        return False

def addToJsonFile(fileName, data):
    with open(fileName, 'r') as f:
        data = json.load(f)
        data.append(data)
    with open(fileName, 'w') as f:
        json.dump(data, f)


def getDataForJsonFile(seriesName, episodeNumber):
    data = {}
    data['seriesName'] = seriesName
    data['episodeNumber'] = episodeNumber
    return data

def saveNewData(seriesName, episodeNumber):
    data = getDataForJsonFile(seriesName, episodeNumber)
    addToJsonFile('data.json', data)

def checkIfSeriesExists(filename, seriesName):
    if checkIsValidFile(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            #check if the json is empty
            if len(data) == 0:
                return False
            for item in data:
                if item['name'] == seriesName:
                    return True
    return False

def returnSeriesData(filename, seriesName):
    if checkIsValidFile(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                if item['seriesName'] == seriesName:
                    return item
    return None

def generateEmptyJsonFile(filename):
    with open(filename, 'w') as f:
        json.dump([], f)
