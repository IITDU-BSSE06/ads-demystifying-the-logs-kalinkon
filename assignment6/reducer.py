#!/usr/bin/python
import sys


counter2009=0
counter2010=0
counter2011=0


for line in sys.stdin:
    timeAndDate = line.strip()
    
    if timeAndDate.find("2009"):
	counter2009 = counter2009+1 
    if timeAndDate.find("2010"):
	counter2010 = counter2010+1
    if timeAndDate.find("2011"):
	counter2011 = counter2011 +1			
    

print counter2009
print counter2010
print counter2011
