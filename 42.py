def isTriangle(n):
	from math import sqrt
	
	s = sqrt(float(1)/4 + 2*n) - (float(1) / 2)
	if s.is_integer():
		return True
	return False

def sumWord(word):
	s = 0
	for c in word:
		s += ord(c) - ord('A') + 1
	return s

def countTriangle():
	import sys

	count = 0
	for line in sys.stdin:
		line = line.strip().split(',')

		for word in line:
			if isTriangle(sumWord(word.strip('"'))) is True:
				count += 1
			
	return count


print countTriangle()

