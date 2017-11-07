#!/usr/bin/python
import sys

dictionaryLibrary = dict()


for line in sys.stdin:
    filePath = line.strip()

    if filePath in dictionaryLibrary:
	dictionaryLibrary[filePath] +=1
    else:
	dictionaryLibrary[filePath] = 1


print len(dictionaryLibrary)
 
