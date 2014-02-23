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

Title       : Paul<br/>
imdbRating  : 7.1<br/>
Genre       : Adventure, Comedy, Sci-Fi<br/>
Released    : 18 Mar 2011<br/>
Actors      : Mia Stallard, Simon Pegg, Nick Frost, Jeremy Owen<br/>
Director    : Greg Mottola<br/>
Runtime     : 104 min<br/>
Rated       : R<br/>
Plot        : Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.

Title       : Groundhog Day<br/>
imdbRating  : 8.1<br/>
Genre       : Comedy, Drama, Fantasy<br/>
Released    : 12 Feb 1993<br/>
Actors      : Bill Murray, Andie MacDowell, Chris Elliott, Stephen Tobolowsky<br/>
Director    : Harold Ramis<br/>
Runtime     : 101 min<br/>
Rated       : PG<br/>
Plot        : A weatherman finds himself living the same day over and over again.<br/>
