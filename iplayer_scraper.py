''' iplayerScraper is a python module for scraping iPlayer data.
    @author Johnny Lindon Robinson (john@johnlindon.com)
    @version 0.1.0

    https://github.com/JohnLindonRobinson/iplayerScraper

    This is the main module for the iplayerScraper.

    @dependencies:
    Python 3.5 or Higher
    BeautifulSoup 4
'''

import argparse
import sys

import filehandling
from series import Series, is_valid_url


def main(input_series, input_name=None, input_episode=-1):
    '''Main function for the iplayerScraper.
    @param inputSeries: The series to scrape.
    @param inputName: The name of the series.
    @param inputEpisode: The episode to scrape.
    @return: The series object.'''
    if input_episode is None:
        input_episode = -1
    #check if data.json exists
    if not filehandling.check_is_valid_file('data.json'):
        filehandling.generate_empty_json('data.json')
    #check if series exists
    if not filehandling.check_if_series_exists('data.json', input_name):
        if len(sys.argv) > 1:
            if sys.argv[1] == '-h':
                print("Usage: python3 series.py <series name>")
                sys.exit(0)
            if is_valid_url(sys.argv[1]):
                srs = Series(url=input_series, name=input_name, episode=input_episode)
            else:
                srs = Series(url=input_series, name=input_name, episode=input_episode)
        #save new series object
        srs.save()
    else:
        #load series object
        srs = Series(pregen=True)
        srs.set_name(input_name)
        srs.load()
    #update episodes
    srs.update_episodes()
    #incriment episode
    srs.incriment_episode()
    srs.save()
    #play next episode
    sys.stdout.write("mpv --fs --pause "+srs.return_current_episode_link())
    #print current episode number
    print("\nCurrent episode: "+str(srs.get_episode()))



if __name__ == '__main__':
    argparse.ArgumentParser(description='Play episodes of a series')
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--series', help='Series name', required=False)
    parser.add_argument('-n', '--name', help='Episode name', required=True)
    parser.add_argument('-e', '--episode', help='Episode number', required=False)

    #parse arguments
    args = parser.parse_args()
    if args.series is not None:
        main(args.series, args.name, args.episode)
