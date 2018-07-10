
# coding: utf-8

import gzip
import json
from collections import Counter, OrderedDict

file = gzip.open('logfile', 'rb')

def apache_split(line):
    split_line = line.split()
    return split_line

def getSplitTime(split_line):
    return split_line[3].decode("utf-8")[13:15]
    
def getSplitEndPoint(split_line):
    return split_line[6].decode("utf-8")

count = 0
list = []
for line in file:
    split_line = apache_split(line)
    time = getSplitTime(split_line)
    if time == "07":
        list.append(getSplitEndPoint(split_line))

countedList = Counter(list)

orderedList = OrderedDict(countedList.most_common(20))

print(orderedList)

print(json.dumps(orderedList, indent=2))

