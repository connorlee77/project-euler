from sets import Set 

dict1 = Set([])

for a in range(2, 101):
	for b in range(2, 101):
		num = a**b
		dict1.add(num)
print len(dict1)