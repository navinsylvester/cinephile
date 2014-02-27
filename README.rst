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

Output Sample
=============

::
semk@gerty ~ $ cinephile movie -s ~/Movies -r 8
Title       : Grave of the Fireflies 
imdbRating  : 8.5
Genre       : Animation, Drama, War
Released    : 16 Apr 1988
Actors      : Tsutomu Tatsumi, Ayano Shiraishi, Yoshiko Shinohara, Akemi Yamaguchi
Director    : Isao Takahata
Runtime     : 89 min
Rated       : Unrated
Plot        : A tragic film covering a young boy and his little sister's struggle to survive in Japan during World War II.
File path   : /Users/sreejitk/Movies/Grave of the Fireflies (1988) 720p BRRiP x264 AAC-AMEET6233 (T.M.R.G)/Grave of the Fireflies (1988) 720p BRRiP x264 AAC-AMEET6233 (T.M.R.G).mp4
