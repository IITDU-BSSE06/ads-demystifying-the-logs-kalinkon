#!/usr/bin/python


import sys

for line in sys.stdin:
    if len(line.strip()) > 0:
        Path = "/assets/js/the-associates.js"
        if line.find(Path) != -1:
            print "{0}".format(line)
