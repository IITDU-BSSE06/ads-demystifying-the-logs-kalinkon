#!/usr/bin/python
import operator
import sys

dictionaryLibrary = dict()


for line in sys.stdin:
    filePath = line.strip()

    if not filePath in dictionaryLibrary:
      dictionaryLibrary[filePath] = 1
    else: 
      dictionaryLibrary[filePath] +=1

result =dictionaryLibrary[max(dictionaryLibrary.iteritems(), key=operator.itemgetter(1))[0]]
print result
