cinephile
=========

Python CLI tool to scan movie directory recursively, normalize the filename and retrieve useful information from imdb. Cinephile can also be used to fetch subtitle file for a particular movie in preferred language. See instructions below on how to use the tool.

Features
========

* Filename normalization
* Yaml config for customization
* Filter based on imdb rating alone or along with genre
* Ignore duplicate movie names
* Download subtitles for a movie file in preferred language

Installation
============

Please read INSTALL

Configuration
=============

After installation the config file .cinephile.yaml can be found under user's home directory.

Usage
=====

To get IMDB info

|  ``cinephile movie -s movie_dir -r imdb_rating [-g genre]``

To download subtitles

|  ``cinephile subtitle -f movie_file -l language``

Example
=======

|  ``cinephile movie -s /media/disk/movies -r 7``
|  ``cinephile movie -s /media/disk/movies -r 7 -g action``
|  ``cinephile subtitle -f ~/Movies/The\ Croods\ \(2013\)/The.Croods.2013.720p.BluRay.x264.YIFY.mp4 -l en``
