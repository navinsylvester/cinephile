cinephile
=========

Python CLI tool to scan movie directory recursively, normalize the filename and retrieve useful information from imdb.

Features
========

  1)File name normalization

  2)Yaml config for customization

  3)Filter based on imdb rating

  4)Filter based on imdb rating along with genre

Installation
============

Please read INSTALL

Usage
=====

python cinephile.py -s movie_dir -r imdb_rating [-g action]

Example
=======

python cinephile.py -s /media/disk/movies -r 7

python cinephile.py -s /media/disk/movies -r 7 -g action

Output Sample
=============

Title       : Paul
imdbRating  : 7.1
Genre       : Adventure, Comedy, Sci-Fi
Released    : 18 Mar 2011
Actors      : Mia Stallard, Simon Pegg, Nick Frost, Jeremy Owen
Director    : Greg Mottola
Runtime     : 104 min
Rated       : R
Plot        : Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.

Title       : Groundhog Day
imdbRating  : 8.1
Genre       : Comedy, Drama, Fantasy
Released    : 12 Feb 1993
Actors      : Bill Murray, Andie MacDowell, Chris Elliott, Stephen Tobolowsky
Director    : Harold Ramis
Runtime     : 101 min
Rated       : PG
Plot        : A weatherman finds himself living the same day over and over again.
