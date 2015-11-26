def calcNameScore(name):
	totalSum = 0
	for x in name:
		totalSum += ord(x) - ord('A') + 1
	return totalSum

import sys

totalSum = 0
lineCount = 1
for line in sys.stdin:
	line = line.strip()
	totalSum += lineCount * calcNameScore(line)
	lineCount += 1

print totalSum
