
def sumDivisors(n):
	
	i, s = 1, 0
	while i < n:
		if n % i == 0:
			s += i
		i += 1
	return s 

def getAbundant():
	from sets import Set
	s = Set()
	for i in range(1, 28124):
		if i < sumDivisors(i):
			s.add(i)
	print 'done'
	return s

def isPossible(n, abundant):
	for i in abundant:
		if n - i in abundant:
			return True
	return False

def sumPositive(abundant):
	s = 0
	for i in range(28124):
		if isPossible(i, abundant) == False:
			s += i 
	return s

print sumPositive(getAbundant())

