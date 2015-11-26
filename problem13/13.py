#!/usr/bin/python
import sys

def sumLine(line):
	s = 0
	for x in line:
		s += int(x)
	return str(s)

s = ''
r = '0'
for line in sys.stdin:
	line = line.strip().split()[1:]
	line.append(r)
	sig = sumLine(line)
	s = sig[-1] + s
	r = sig[0:-1]

s = r + s
print s[0:10]





