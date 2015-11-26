x = 2
count = 0
powers = []
for x in range(10):
	powers.append(x ** 5)

while x < 355000:
	if x % 100000 == 0:
		print x
	t = str(x)
	s = 0
	for l in t:
		s += powers[int(l)]
	if s == x:
		count += s
	x += 1

print count