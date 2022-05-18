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
# Use of this source code is goverened by the GPLv2 license.
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
    episodes = soup.find_all('a')
    series_list = []
    # print out all episodes
    for episode in episodes:
        if (string_contains(episode.get('href'), 'episode') and
        not string_contains(episode.get('href'), 'episodes')):
            series_list.append("https://bbc.co.uk"+episode.get('href'))
    return series_list

def get_list(url):
    '''main function of the program
    @param url: The input url of the series'''
    # Get the HTML from the URL1
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find all the links in the HTML document
    links = soup.find_all('a')

    # Print the links
    episodes = []

    for link in links:
        if (string_contains(link.get('href'), 'episode') and
        not string_contains(link.get('href'), 'episodes')):
            episode_link = "https://bbc.co.uk"+link.get('href')
            if episode_link in episodes:
                continue
            episodes.append(return_final_line_from_string(episode_link))
    # print out all episodes on the page
    for link in links:
        print(link)
        if string_contains(link.get('href'), 'episodes'):
            print(link.get('class'))
            item = get_episodes_from_series(
                'https://bbc.co.uk'+link.get('href'))
            for given_episode in item:
                if given_episode!=episodes[0]:
                    episodes.append(return_final_line_from_string(given_episode))
    return episodes

if __name__ == '__main__':
    episode_list = get_list(sys.argv[1])
    for e in episode_list:
        print(e)
