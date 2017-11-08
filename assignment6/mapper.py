#!/usr/bin/python


import sys


for line in sys.stdin:
    file = line.strip().split(" ")
	
    if len(file)> 1:
        
        timeAndDate = file[3]
	  
    print str(timeAndDate)

	
