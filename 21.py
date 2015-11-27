
def sumDivisors(n):
	
	i, s = 1, 0
	while i < n:
		if n % i == 0:
			s += i
		i += 1
	return s 

def sumAmicables():
	from sets import Set
	s = Set()
	for i in range(1, 10000):
		
		a = i 
		b = sumDivisors(a)

		if sumDivisors(b) == a and a != b and b < 10000:
			s.add(a)
			s.add(b)

	return sum(s)

print sumAmicables()
