cinephile
=========

Python CLI tool to scan movie directory recursively, normalize the filename and retrieve useful information from imdb.

Features
========

  1)Filename normalization

  2)Yaml config for customization

  3)Filter based on imdb rating alone or along with genre

  4)Ignore duplicate movie names

Installation
============

Please read INSTALL

Configuration
=============

After installation the config file .cinephile.yaml can be found under user's home directory.

Usage
=====

cinephile -s movie_dir -r imdb_rating [-g genre]

Example
=======

cinephile -s /media/disk/movies -r 7

cinephile -s /media/disk/movies -r 7 -g action

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
Plot        : Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.<br/>
File path   : /Users/navinsylvester/Movies/mainstream/english/comedy/Paul (2011)/Paul (2011).avi<br/>

Title       : Groundhog Day<br/>
imdbRating  : 8.1<br/>
Genre       : Comedy, Drama, Fantasy<br/>
Released    : 12 Feb 1993<br/>
Actors      : Bill Murray, Andie MacDowell, Chris Elliott, Stephen Tobolowsky<br/>
Director    : Harold Ramis<br/>
Runtime     : 101 min<br/>
Rated       : PG<br/>
Plot        : A weatherman finds himself living the same day over and over again.<br/>
File path   : /Users/navinsylvester/Movies/mainstream/english/rc/Groundhog Day/Groundhog Day Special Edition 1993 [Eng].avi<br/>