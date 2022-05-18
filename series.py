''' iplayerScraper Series Object
    @author Johnny Lindon Robinson (
    @version 0.1.0

    https://github.com/JohnLindonRobinson/iplayerScraper

    This module is used for handling the series objects

    @dependecies:
    Python 3.5 or Higher
'''

__author__ = "Johnny Lindon Robinson (john@johnlindon.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022-2022 Johnny Lindon Robinson"
# Use of this source code is goverened by the GPLv2 license.
__license__ = "GPLv2.0"

import json
import re
import sys

from get_list import get_list, string_contains


class Series:
    '''Series Object containing neccessary data for a series
    Can be saved to a json file
    '''

    def __init__(self, name=None, episode=-1, url=None, pregen=False):
        '''Initialize a series object
        @param name: The name of the series.
        @param episode: The current episode of the series.
        @param url: The url of the series.
        @param pregen: Whether the series object is pregenerated or not.'''
        if pregen:
            return
        if name is None:
            name = input("Enter the name of the series: ")
        self.name = name
        self.episode = episode
        if url is None:
            self.url = self.get_url_from_input()
        else:
            self.url = url
        self.episodes = get_list(self.url)


    def update_episodes(self):
        '''Update the episodes of the series object'''
        self.episodes = get_list(self.url)


    def get_url_from_input(self):
        '''Get the url of the series from input'''
        if len(sys.argv) > 1:
            if sys.argv[1] == '-h':
                print("Usage: python3 series.py <series name>")
                sys.exit(0)
            if is_valid_url(sys.argv[1]):
                return sys.argv[1]
        while True:
            url = input("Enter the url of the series: ")
            if is_valid_url(url):
                return url


    def get_name(self):
        '''Get the name of the series
        @return: The name of the series'''
        return self.name


    def set_name(self, name):
        '''Set the name of the series
        @param name: The name of the series'''
        self.name = name


    def get_episode(self):
        '''Get the current episode of the series
        @return: The current episode of the series'''
        return self.episode

    def set_episode(self, episode):
        '''Set the current episode of the series
        @param episode: The current episode of the series'''
        self.episode = episode


    def return_current_episode_link(self):
        '''Return the link to the current episode of the series
        @return: The link to the current episode of the series'''
        return self.episodes[self.episode]

    def incriment_episode(self):
        '''Incriment the current episode of the series
        @return: If the series is completed'''
        self.episode += 1
        return self.episode < len(self.episodes)

    def get_episodes(self):
        '''Get the episodes of the series
        @return: The episodes of the series'''
        return self.episodes


    #Saving and Loading series object
    def save(self):
        '''Save the series object to a json file'''
        with open('data.json', 'r', encoding='utf-8') as file_temp:
            data = json.load(file_temp)
            data.append(self.__dict__)
        with open('data.json', 'w', encoding='utf-8') as file_temp:
            json.dump(data, file_temp)


    def load(self):
        '''Load the series object from a json file
        @return: The series object'''
        with open('data.json', 'r', encoding='utf-8') as file_temp:
            data = json.load(file_temp)
            for item in data:
                if item['name'] == self.name:
                    self.__dict__ = item
                    return True
        return False


def is_valid_url(url):
    '''Use regex to check if url is valid
    @param url: The url to be checked
    @return: True if the url is valid, False otherwise'''
    if re.match(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
                , url) and string_contains(url, 'iplayer'):
        return True
    return False
