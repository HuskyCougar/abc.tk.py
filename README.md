# abc.tk.py
Tool to replace command some basic command line functions. This version in Python.

## What is this?
I spend a lot of time extracting pieces of data from log files. Often the next step is to compare extracted values with some other values. 

It used to be that I would leave a couple of files open at all times. I would paste info into them as needed and do things like `sort tmp1.txt tmp2.txt | uniq -c | sort -nr | grep " 2 " | cut -c 9-128` to figure out which values were in both files. I wrote this script initially to do basic set comparisons and provide a GUI interface for some other basic text extraction and manipulation functions. 

I originally wrote this in Perl back in probably 2011-2012ish and I am steadily translating the functionality over to Python. I only recently needed to learn Python so this has been a good opportunity to play with the language.

Contructive criticism is welcome. I have only been writing Python for about a year so I am still a noob. I learned other languages in school but never used them. I've written code in 6+ languages but the only language I would consider myself proficient in is Perl so any wonky looking code is probably based on some Perl syntax or idioms.

## What this is not:

This is not a lot of things or a tool to do anything specific. It is a random collection of functions that I or someone I have known has needed at some point.

This is not a CyberChef replacement. I wrote mine before CyberChef's initial commit. CyberChef is amazing and I use it often and will probably get some ideas from there but not everything makes sense to put in ABC unless it does.
