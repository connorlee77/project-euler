import sys

for line in sys.stdin:
	line = line.strip().split(',')

	for name in line:
		print name[1:-1]