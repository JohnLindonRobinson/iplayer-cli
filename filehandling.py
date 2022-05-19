''' iplayer-cli File Handling
    @author Johnny Lindon Robinson (john@johnlindon.com)
    @version 0.1.0

    https://github.com/JohnLindonRobinson/iplayer-cli

    This module is used for handling file management for the series objects

    @dependencies:
    Python 3.5 or Higher
'''

__author__ = "Johnny Lindon Robinson (john@johnlindon.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022-2022 Johnny Lindon Robinson"
# Use of this source code is governed by the GPLv2 license.
__license__ = "GPLv2.0"

import json


def check_is_valid_file(file_name):
    '''Check if a file exists and is not empty.
    @param fileName: The file to check.
    @return: True if the file exists and is not empty, False otherwise.'''
    try:
        file = open(file_name, 'r', encoding='utf-8')
        length = len(file.read())
        file.close()
        return length!=0
    except FileNotFoundError:
        return False

def add_to_json_file(file_name, data):
    '''Add data to a json file.
    @param fileName: The file to add the data to.
    @param data: The data to add to the file.'''
    with open(file_name, 'r', encoding='utf-8') as file_temp:
        data = json.load(file_temp)
        data.append(data)
    with open(file_name, 'w', encoding='utf-8') as file_temp:
        json.dump(data, file_temp)


def check_if_series_exists(file_name, series_name):
    '''Check if a series exists in a json file.
    @param fileName: The file to check.
    @param seriesName: The series to check for.
    @return: True if the series exists, False otherwise.'''
    if check_is_valid_file(file_name):
        with open(file_name, 'r', encoding='utf-8') as file_temp:
            data = json.load(file_temp)
            #check if the json is empty
            if len(data) == 0:
                return False
            for item in data:
                if item['name'] == series_name:
                    return True
    return False

def generate_empty_json(file_name):
    '''Generate an empty json file.
    @param fileName: The file to generate.'''
    with open(file_name, 'w', encoding='utf-8') as file_temp:
        json.dump([], file_temp)
