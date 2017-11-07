#!/usr/bin/python


import sys
import urlparse

for line in sys.stdin:
    file = line.strip().split(" ")


    if len(file)> 1:
        url = file[6]
        filePath = urlparse.urlparse(url).path

        print str(filePath)
