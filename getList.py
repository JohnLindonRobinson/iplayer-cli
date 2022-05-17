import sys
from pydoc import tempfilepager

import bs4
import requests


def stringContains(string, substring):
    return substring in string

def returnFinalLineFromString(string):
    return string.split('\n')[-1]

def getEpisodesFromSeries(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    episodes = soup.find_all('a')
    E = []
    # print out all episodes
    for episode in episodes:
        if (stringContains(episode.get('href'), 'episode') and
        not stringContains(episode.get('href'), 'episodes')):
            E.append("https://bbc.co.uk"+episode.get('href'))
    return E

def getList(links, episodes):
    tempEpisode = True
    for link in links:
        if tempEpisode:
            tempEpisode = False
            continue
        if (stringContains(link.get('href'), 'episode') and
        not stringContains(link.get('href'), 'episodes')):
            episodes.append("https://bbc.co.uk"+link.get('href'))
    return episodes

def main(url):
    # Get the HTML from the URL1
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find all the links in the HTML document
    links = soup.find_all('a')

    # Print the links
    episodes = []

    for link in links:
        if (stringContains(link.get('href'), 'episode') and
        not stringContains(link.get('href'), 'episodes')):
            episodeLink = "https://bbc.co.uk"+link.get('href')
            if episodeLink in episodes:
                continue
            episodes.append(returnFinalLineFromString(episodeLink))
    # print out all episodes on the page
    for link in links:
        if(stringContains(link.get('href'), 'episodes')):
            item = getEpisodesFromSeries(
                'https://bbc.co.uk'+link.get('href'))
            for e in item:
                if e!=episodes[0]:
                    episodes.append(returnFinalLineFromString(e))
    return episodes

if __name__ == '__main__':
    list = main(sys.argv[1])
    for e in list:
        print(e)
