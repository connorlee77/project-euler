#!/usr/bin/python

import sys

it = 0
for line in sys.stdin:
    line = line.strip()
    newCol = it
    for newRow in range(len(line[:])):
        print("{0}.{1}.{2}".format(newRow, newCol, line[newRow]))
    it += 1