''' iplayerScraper List Gatherer
    @author Johnny Lindon Robinson (john@johnlindon.com)
    @version 0.1.0

    https://github.com/JohnLindonRobinson/iplayerScraper

    This module is used for gathering links from HTML data from bbc iplayer website

    @dependencies:
    Python 3.5 or Higher
    BeautifulSoup 4
'''

__author__ = "Johnny Lindon Robinson (john@johnlindon.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022-2022 Johnny Lindon Robinson"
# Use of this source code is governed by the GPLv2 license.
__license__ = "GPLv2.0"


import sys

import bs4
import requests


def string_contains(string, substring):
    '''Check if a string contains another string.
    @param string: The string to check.
    @param substring: The substring to check for.
    @return: True if the string contains the substring, False otherwise.'''
    return substring in string

def return_final_line_from_string(string):
    '''Return the final line of a string.
    @param string: The string to get the final line from.
    @return: The final line of the string.'''
    return string.split('\n')[-1]

def get_episodes_from_series(url):
    '''Get all episodes from a series given a url.
    @param url: The url of the series.
    @return: A list of all episodes in the series.'''
    request_data = requests.get(url)
    soup = bs4.BeautifulSoup(request_data.text, 'html.parser')
    links = soup.find_all('a')
    episodes = []

    for link in links:
        if (string_contains(link.get('href'), 'episode') and
        not string_contains(link.get('href'), 'episodes')):
            episode_link = "https://bbc.co.uk"+link.get('href')
            if episode_link in episodes:
                continue
            if len(episodes)>0:
                if(episode_link.split('/')[-1].split('?')[0]==
                    episodes[0].split('/')[-1].split('?')[0]):
                    continue
            episodes.append(return_final_line_from_string(episode_link))
    return episodes

def get_list(url):
    '''main function of the program
    @param url: The input url of the series'''
    # Get the HTML from the URL1
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find all the links in the HTML document
    links = soup.find_all('a')

    episodes = []
    episodes.extend(get_episodes_from_series(url))
    # print out all episodes on the page
    for link in links:
        if len(episodes)<0:
            print("Invalid Series")
            sys.exit(1)
        if link.get('href').split('/')[-1].split('?')[0]==episodes[0].split('/')[-1].split('?')[0]:
            episodes.extend(get_episodes_from_series("https://bbc.co.uk"+link.get('href'))[1])
    return episodes

if __name__ == '__main__':
    episode_list = get_list(sys.argv[1])
    for e in episode_list:
        print(e)
