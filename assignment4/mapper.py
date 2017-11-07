#!/usr/bin/python


import sys

for line in sys.stdin:
    file = line.strip().split(" ")


    if len(file)> 1:
       
        filePath = file[6]

        print str(filePath)
