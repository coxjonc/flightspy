Flightspy
========
A better python wrapper for Google's cheap flights API. Provides cli tools for getting pricing information about flights. 

Installation
============
I haven't uploaded this to PyPi yet. In the meantime, clone the repo and run `python setup.py install`.

Usage
=====
After installing the program, just run the following command in your bash shell:

`$ flightspy get -d 2016-08-10 -t LAX -o CLT`

Currently the program just prints the price of the flight to STDOUT, which isn't terribly useful, but I'm working on adding options to output a more complete set of data about flight options to a csv file or database.

TODO
====
* Output data about possible flights to a .csv file.

