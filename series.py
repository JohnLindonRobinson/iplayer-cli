import json
import re
import sys

import getList


class series:
    def __init__(self, name=None, episode=-1, url=None, pregen=False):
        if pregen:
            return
        if name is None:
            name = input("Enter the name of the series: ")
        self.name = name
        self.episode = episode
        if url==None:
            self.url = self.getUrlFromInput()
        else:
            self.url = url
        self.episodes = getList.main(self.url)
    
    def updateEpisodes(self):
        self.episodes = getList.main(self.url)
    
    def getUrlFromInput(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == '-h':
                print("Usage: python3 series.py <series name>")
                sys.exit(0)
            if isValidURL(sys.argv[1]):
                return sys.argv[1]
        while True:
            url = input("Enter the url of the series: ")
            if isValidURL(url):
                return url
    
    #Getters and Setters
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getEpisode(self):
        return self.episode

    def setEpisode(self, episode):
        self.episode = episode
    
    def returnCurrentEpisodeLink(self):
        return self.episodes[self.episode]

    def incrimentEpisode(self):
        self.episode += 1

    def getEpisodes(self):
        return self.episodes
    
    #Saving and Loading series object
    def save(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
            data.append(self.__dict__)
        with open('data.json', 'w') as f:
            json.dump(data, f)
    
    def load(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
            for item in data:
                if item['name'] == self.name:
                    self.__dict__ = item
                    return True
        return False


def isValidURL(url):
    #Using regex check if the url is valid
    if re.match(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', url) and getList.stringContains(url, 'iplayer'):
        return True
    return False
