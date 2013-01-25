#!/usr/bin/python

import sys 
import datetime 

def unix2dt(offset):
    """
    Converts unix time stamps to python date time
    """
    return datetime.datetime.fromtimestamp(float(offset))

from urlparse import urlparse
for eachLine in sys.stdin:
    eachLine = eachLine.strip() 
    url = urlparse(eachLine.split()[6]).hostname
    if type(url) != type(None):
        url = ".".join(url.split(".")[::-1])
        if len(url.split(".")[0]) == 2 and len(url.split(".")[1]) == 2:
            url = ".".join(url.split(".")[:3])
        else:
            url = ".".join(url.split(".")[:2])
        print "\t".join([str(unix2dt(float(eachLine.split()[0])).date()),eachLine.split()[2],url])
