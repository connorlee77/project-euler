def isMatch(n):
	import re
	pattern = re.compile("1.2.3.4.5.6.7.8.9")
	return pattern.match(str(n))

def findSquare():
	from math import sqrt
	s = int(sqrt(19293949596979899)) + 1
	while s > 0:
		s -= 2
		if isMatch(s ** 2) is not None:
			return str(s) + '0'

print findSquare()

