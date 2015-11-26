
def getCollatz(n):
	count = 0

	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		count += 1
	return count + 1

maxS = 0
maxX = 0
for x in range(1, 1000000):
	n = getCollatz(x)
	if n > maxS:
		maxS = n
		maxX = x

print maxX