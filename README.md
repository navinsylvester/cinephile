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
