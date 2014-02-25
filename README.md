cinephile
=========

Python CLI tool to scan movie directory recursively, normalize the filename and retrieve useful information from imdb.

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

    cinephile movie -s movie_dir -r imdb_rating [-g genre]

To download subtititles

    cinephile subtitle -f movie_file -l language

Example
=======

    cinephile movie -s /media/disk/movies -r 7
    cinephile movie -s /media/disk/movies -r 7 -g action
    cinephile subtitle -f ~/Movies/The\ Croods\ \(2013\)/The.Croods.2013.720p.BluRay.x264.YIFY.mp4 -l en

Output Sample
=============

    sreejitk@gerty ~ $ cinephile movie -s ~/Movies -r 8
    Title       : Grave of the Fireflies
    imdbRating  : 8.5
    Genre       : Animation, Drama, War
    Released    : 16 Apr 1988
    Actors      : Tsutomu Tatsumi, Ayano Shiraishi, Yoshiko Shinohara, Akemi Yamaguchi
    Director    : Isao Takahata
    Runtime     : 89 min
    Rated       : Unrated
    Plot        : A tragic film covering a young boy and his little sister's struggle to
    survive in Japan during World War II.
    File path   : /Users/sreejitk/Movies/Grave of the Fireflies (1988) 720p BRRiP x264 \
    AAC-AMEET6233 (T.M.R.G)/Grave of the Fireflies (1988) 720p BRRiP x264 AAC-AMEET6233 (T.M.R.G).mp4


    Title       : Memento
    imdbRating  : 8.6
    Genre       : Mystery, Thriller
    Released    : 11 Oct 2000
    Actors      : Guy Pearce, Carrie-Anne Moss, Joe Pantoliano, Mark Boone Junior
    Director    : Christopher Nolan
    Runtime     : 113 min
    Rated       : R
    Plot        : A man, suffering from short-term memory loss, uses notes and tattoos to
    hunt for the man he thinks killed his wife.
    File path   : /Users/sreejitk/Movies/Memento (2000)/Memento.2000.720p.BluRay.x264.YIFY.mp4