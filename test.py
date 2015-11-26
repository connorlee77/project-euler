from numpy import prod
from math import sqrt

def isDivisible():
	divisors = [11, 13, 14, 16, 17, 18, 19]
	x = 1	
	while x > 0:
		i = 20
		i *= x
		divide = True
		for div in divisors:
			if i % div != 0:
				divide = False

		if divide == True:
			print i
			return

		x += 1

	return


def problem8():
	nums = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	gettwelve = nums[0:13]
	thirteenth = int(nums[0])
	memProd =  prod(map(int, gettwelve))
	maxProd = memProd

	for i in nums[13:]:
		thirteenth = int(gettwelve[0])
		gettwelve = gettwelve[1:] + i

		if thirteenth == 0:
			memProd = prod(map(int, gettwelve))
		else:
			memProd /= thirteenth
			memProd *= int(i)

		if memProd > maxProd:
			maxProd = memProd  

	return maxProd



def problem9():

	def funcA(b):
		return (500000 - (1000 * b)) / (1000 - b)
	
	b = 1
	while b < 1000:
		a = funcA(b)

		if (a + b) < 1000 and a > 0:
			a = int(a)
			c = 1000 - a - b
			
			if a**2 + b**2 == c**2:
				return a*b*c

		b += 1

	return 0

def problem10(n):
	mem = range(2, n + 1)
	currSum = 2

	currPrime = 2
	currPrimeIndex = 0
	hasPrime = True
	while hasPrime:
		i = 2
		while currPrime * i <= n:
			mem[currPrime * i - 2] = 0
			i += 1

		hasPrime = False
		
		for k in range(currPrimeIndex + 1, len(mem)):
			if mem[k] != 0:
				currPrime = mem[k]
				currSum += currPrime
				currPrimeIndex = k
				hasPrime = True
				break
	return currSum



def problem31():
	coins = [1, 5, 10, 50, 100]
	def countWays(n):
		if n == 0:
			return 1 
		else:
			ways = 0
			for p in coins:
				if n - p >= 0:
					ways += countWays(n - p)
			return ways
	
	ways = countWays(100)
	return ways

print problem31()












