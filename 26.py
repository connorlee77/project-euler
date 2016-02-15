from decimal import *
import re


def findPattern(x):
	for i in range(2,len(x)):
		


ans = 0
for x in range(1, 1000):
	num = 1 / Decimal(x)
	a = findPattern(str(num[2:]))

print ans