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
import hashlib

def get_config():
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
        return yaml.load(stream)

def get_hash(name):
    """ This hash function receives the name of the file
    and returns the hash code
    """
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


def fetch_subtitles(filename, movie_name, quiet, language='en'):
    """ Fetch subtitles from SubDB. Saves it in the same directory
    as the movie file.
    """
    file_hash = get_hash(filename)

    base_url = 'http://api.thesubdb.com/?{0}'
    user_agent = 'SubDB/1.0 (Cinephile/1.0; https://github.com/navinsylvester/cinephile)'
    params = {
        'action': 'download',
        'language': language or 'en',
        'hash': file_hash
    }

    url = base_url.format(urllib.urlencode(params))
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)

    try:
        if not quiet and movie_name: print 'Trying to fetch subtitle for "' + movie_name + '"...'
        response = urllib2.urlopen(req)
        ext = response.info()['Content-Disposition'].split(".")[1]
        sub_file = os.path.splitext(filename)[0] + "." + ext

        with open(sub_file, "wb") as fout:
            fout.write(response.read())

        print 'Subtitle saved to ' + sub_file
        return True
    except urllib2.URLError as e:
        print 'Error fetching subtitles (Code: %r, Message: %s).' % (e.errno, e.reason)
    except Exception:
        print 'Unknown Error'

    return False

def get_movie_info(movie_filename, order_list, rating, votes, full_path, genre=None):
    api_uri = "www.omdbapi.com"

    params = urllib.urlencode({'t': movie_filename})
    connection = httplib.HTTPConnection(api_uri)

    connection.request("GET", "/?" + params)
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

                    print u''.join((order, spaces, ': ', parsed_json[order])).encode('utf-8')

                print "File path   :", full_path[0]
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

def get_movies_set(movie_dir, skip_dupes):
    if not os.path.exists(movie_dir):
        print "Scan directory doesn't exist"
        return

    config = get_config()

    file_ext_list = config['file_ext'].replace(",", "|")
    purge_words_list = config['purge_words'].replace(",", "|")

    movies = []
    # Skip duplicate movie names
    dupes = set()

    #Scan movie dir recursively
    for root, dirnames, filenames in os.walk(movie_dir, ):
        #Remove the directories mentioned in the ignore list
        if len(config['ignore_dir']):
            for ignore in config['ignore_dir']:
                if ignore in dirnames:
                    dirnames.remove(ignore)

        for filename in filenames:
            # skip 'em pesky dot files
            if filename[0] == '.': continue

            full_path = []

            if len(file_ext_list) > 1:
                file_ext_expr = "(?P<name>.*)\.({0})".format(file_ext_list)

                movie_filename = re.match(file_ext_expr, filename, re.I)

                if movie_filename:
                    #Normalize filename
                    movie_filename = normalize_filename(movie_filename.group("name"), purge_words_list, config['remove_year'], config['convert_roman'])

                    full_path.append(os.path.join(root, filename))

                    #Get movie details
                    if movie_filename not in dupes:
                        movies.append({'movie_filename': movie_filename, 'full_path': full_path})
                        dupes.add(movie_filename)
            else:
                print "Add file extensions to scan in cinephile.yaml"
                return

    return movies

def run_movie_commands(args):
    movie_dir = args.source_dir
    rating = args.rating
    genre = args.genre
    movies = get_movies_set(movie_dir, True)
    config = get_config()

    for movie in movies:
        get_movie_info(movie['movie_filename'], config['order_list'], rating, config['votes'], movie['full_path'], genre)


def run_subtitle_commands(args):
    if args.recursive_scan:
        movies = get_movies_set(args.filename, False)
        total_movies = len(movies)
        success_count = 0
        print 'A total of %d movies found.' % (total_movies)
        for movie in movies:
            ret = fetch_subtitles(movie['full_path'][0], movie['movie_filename'], args.stfu, args.language)
            if ret: success_count += 1
        print '=' * 80
        print 'Total movies: %d Got subtitles for: %d Failed for: %d' % (total_movies, success_count, total_movies - success_count)
        print '=' * 80
    else:
        fetch_subtitles(args.filename, None, True, args.language)


def run():
    parser = argparse.ArgumentParser(description='Fetch movie information from imdb')

    sub_parsers = parser.add_subparsers(help='Cinephile commands')
    movie_parser = sub_parsers.add_parser('movie', help='Movie commands')
    movie_parser.add_argument('-s', '--source_dir', help='Source directory of movies', required=True)
    movie_parser.add_argument('-r', '--rating', help='Fetch movies with imdb rating greater than or equal to provided value', type=float, required=True)
    movie_parser.add_argument('-g', '--genre', help='Filter by movie genre')
    movie_parser.set_defaults(func=run_movie_commands)

    sub_parser = sub_parsers.add_parser('subtitle', help='Subtitles commands')
    sub_parser.add_argument('-f', '--fetch', dest='filename', help='Name of file or directory to fetch subtitles for', required=True)
    sub_parser.add_argument('-l', '--lang', dest='language', help='Choose Language (en,es,fr,it,nl,pl,pt,ro,sv,tr)')
    sub_parser.add_argument('-R', '--recursive', dest='recursive_scan', help='Scan source directory recursively for movies to fetch subtitles for', action='store_true')
    sub_parser.add_argument('-q', '--quiet', dest='stfu', help='Don\'t print what the program is up to while fetching subtitles', action='store_true')
    sub_parser.set_defaults(func=run_subtitle_commands)

    args = parser.parse_args()
    args.func(args)


def main():
    try:
        run()
    except KeyboardInterrupt:
        print 'Exiting ...'


if __name__ == '__main__':
    main()
