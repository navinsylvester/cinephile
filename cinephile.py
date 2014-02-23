#!/usr/bin/env python
from __future__ import absolute_import

import re
import httplib
import urllib2, urllib
import os
import sys
import json
import yaml
import argparse

def get_movie_info(movie_filename, order_list, rating, votes, genre=None):
    api_uri="www.omdbapi.com"

    params = urllib.urlencode({'t':movie_filename})
    connection = httplib.HTTPConnection(api_uri)

    connection.request("GET", "/?"+params)
    response = connection.getresponse()

    response_json = response.read()
    indent = 12

    parsed_json = json.loads(response_json)

    if parsed_json['Response'] == 'False':
        return

    if "imdbRating" in parsed_json and parsed_json['imdbRating'] != "N/A":
        if genre is None or genre.capitalize() in parsed_json['Genre']:
            if float(parsed_json['imdbRating']) >= rating and parsed_json['imdbVotes'] > votes:
                for order in order_list:
                    spaces = ''
                    for i in range(indent - len(order)):
                        spaces += ' '
                    print order + spaces +': ' + parsed_json[order]
                print '\n'

    connection.close()

def normalize_filename(movie_filename, purge_words_list, remove_year, convert_roman):
    purge_words_list = "(?i)({0})(.*)$".format(purge_words_list)
    purge_digit = "(\d{4})(.*)$"
    purge_spl_chars = "(\[|\()(.*)$"
    purge_dot_underscore = "(\.|_)"
    purge_hypen_aps = "(\-|')"

    re_str = re.sub(purge_spl_chars, "", movie_filename, )

    re_str = re.sub(purge_words_list, "", re_str, re.I)

    if remove_year is True:
        re_str = re.sub(purge_digit, "", re_str, )

    re_str = re.sub(purge_dot_underscore, " ", re_str, )

    re_str = re.sub(purge_hypen_aps, "", re_str, )

    if convert_roman is True:
        re_comp = re.compile(r'\b(?=[MDCLXVI]+\b)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b')
        re_str = re_comp.sub(roman_to_int_repl, re_str)

    return re_str.rstrip().lstrip()

def roman_to_int_repl(match):
    return str(roman_to_int(match.group(0)))

def roman_to_int(n):
    numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    )

    n = unicode(n).upper()
    i = result = 0

    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)

    return result

def convert_roman(roman_str):
    string = roman_str.upper()
    total = 0

    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            total += val[string[0]]
            string = string[1:]
        else:
            total += val[string[1]] - val[string[0]]
            string = string[2:]

    print total

def scan_dir(movie_dir, rating, genre):
    if not os.path.exists(movie_dir):
        print "Scan directory doesn't exist"
        return

    config_file = None
    config_paths = [
        'cinephile.yaml',
        os.path.expanduser('~/.cinephile.yaml'),
        os.path.join(os.path.dirname(__file__), 'cinephile.yaml')
    ]

    for path in config_paths:
        if os.path.exists(path):
            config_file = path
            break

    if not config_file:
        print 'No cinephile.yaml found.'
        return

    #Read yaml file to get config
    with open(config_file) as stream:
        config = yaml.load(stream)

    file_ext_list = config['file_ext'].replace(",", "|")
    purge_words_list = config['purge_words'].replace(",", "|")

    #Scan movie dir recursively
    for root, dirnames, filenames in os.walk(movie_dir, ):
        #Remove the directories mentioned in the ignore list
        if len(config['ignore_dir']):
            for ignore in config['ignore_dir']:
                if ignore in dirnames:
                    dirnames.remove(val)

        for filename in filenames:
            if len(file_ext_list) > 1:
                file_ext_expr = "(?P<name>.*)\.({0})".format(file_ext_list)

                movie_filename = re.match(file_ext_expr, filename, re.I)

                if movie_filename:
                    #Normalize filename
                    movie_filename = normalize_filename(movie_filename.group("name"), purge_words_list, config['remove_year'], config['convert_roman'])

                    #Get movie details
                    get_movie_info(movie_filename, config['order_list'], rating, config['votes'], genre)
            else:
                print "Add file extensions to scan in cinephile.yaml"
                return

def _parse_args():
    parser = argparse.ArgumentParser(description='Fetch movie information from imdb')

    parser.add_argument('-s', '--source_dir', help='source directory of movies', required=True)
    parser.add_argument('-r', '--rating', help='Fetch movies with imdb rating greater than or equal to provided value', type=float, required=True)
    parser.add_argument('-g', '--genre', help='Filter by movie genre')

    parse = parser.parse_args()

    return parse

def main():
    parsed_args = _parse_args()
    movie_dir = parsed_args.source_dir
    rating = parsed_args.rating
    genre = parsed_args.genre

    scan_dir(movie_dir, rating, genre)

if __name__ == '__main__':
    main()