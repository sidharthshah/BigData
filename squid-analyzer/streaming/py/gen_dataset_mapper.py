#!/usr/bin/python

import sys 

for eachLine in sys.stdin:
    eachLine = eachLine.strip() 
    print "\t".join([eachLine.split()[0],eachLine.split()[2],eachLine.split()[6]])
