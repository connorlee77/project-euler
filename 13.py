#!/usr/bin/python
import sys

def sumLine(line):
	s = 0
	for x in line:
		s += int(x)
	print s
	return str(s)

s = ''
r = '0'
for line in sys.stdin:
	line = line.strip().split()[1:]
	print line
	#sig = sumLine(line.append(r))
	#s += sig[-1]
	#r = sig[0:-1]

print s.reverse()[0:10]



