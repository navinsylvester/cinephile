cinephile
=========

Python CLI tool to scan movie directory recursively, normalize the filename and retrieve useful information from imdb.

Features
========

* Filename normalization
* Yaml config for customization
* Filter based on imdb rating
* Filter based on imdb rating along with genre
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

    cinephile subtitle -f ~/Movies/Anchorman.The.Legend.Of.Ron.Burgundy.2004.720p.BrRip.x264.BOKUTOX.YIFY.mp4 -l en

Example
=======

    cinephile movie -s /media/disk/movies -r 7
    cinephile movie -s /media/disk/movies -r 7 -g action
    cinephile subtitle -f ~/Movies/Dexter.mp4 -l en

Output Sample
=============

    sreejitk@gerty ~ $ cinephile movie -s ~/Movies -r 8
    Title       : Dexter
    imdbRating  : 9.1
    Genre       : Crime, Drama, Mystery
    Released    : 01 Oct 2006
    Actors      : Michael C. Hall, Jennifer Carpenter, David Zayas, James Remar
    Director    : N/A
    Runtime     : 60 min
    Rated       : TV-MA
    Plot        : A Miami police forensics expert moonlights as a serial killer of criminalswho he believes have escaped justice.
    File path   : /Users/sreejitk/Movies/dexter.mp4


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
