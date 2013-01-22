#!/usr/bin/python

import sys 
from urlparse import urlparse
for eachLine in sys.stdin:
    eachLine = eachLine.strip() 
    url = urlparse(eachLine.split()[6]).hostname
    if type(url) != type(None):
        url = ".".join(url.split(".")[::-1])
        print "\t".join([eachLine.split()[0],eachLine.split()[2],url])
