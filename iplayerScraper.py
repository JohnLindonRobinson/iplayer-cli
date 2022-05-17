import argparse
import sys

from filehandling import (checkIfSeriesExists, checkIsValidFile,
                          generateEmptyJsonFile)
from series import isValidURL, series


def main(inputSeries, inputName=None, inputEpisode=-1):
    if inputEpisode==None:
        inputEpisode = -1
    #check if data.json exists
    if not checkIsValidFile('data.json'):
        generateEmptyJsonFile('data.json')
    #check if series exists
    if not checkIfSeriesExists('data.json', inputName):
        if len(sys.argv) > 1:
            if sys.argv[1] == '-h':
                print("Usage: python3 series.py <series name>")
                sys.exit(0)
            if isValidURL(sys.argv[1]):
                srs = series(url=inputSeries, name=inputName, episode=inputEpisode)
            else:
                srs = series(url=inputSeries, name=inputName, episode=inputEpisode)
        #save new series object
        srs.save()
    else:
        #load series object
        srs = series(pregen=True)
        srs.setName(inputName)
        srs.load()
    #update episodes
    srs.updateEpisodes()
    #incriment episode
    srs.incrimentEpisode()
    srs.save()
    #play next episode
    sys.stdout.write("mpv --fs --pause "+srs.returnCurrentEpisodeLink())
    #print current episode number
    print("\nCurrent episode: "+str(srs.getEpisode()))



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
