def nextTriangle():
	from sets import Set 

	triangles = 0
	pentSet = Set()
	hexSet = Set()
	n = 1
	while True:
		t = n * (n + 1) / 2
		p = n * (3 * n - 1) / 2
		h = n * (2 * n - 1)

		triangles = t

		if (p % 10 == 0 and h % 10 == 0) or (p % 10 == 1 and h % 10 == 1) or (p % 10 == 5 and h % 10 == 5)  or (p % 10 == 6 and h % 10 == 6)  :
			pentSet.add(p)
			hexSet.add(h)

		temp = pentSet & hexSet

		if triangles % 5 == 0 and triangles in temp and n > 285:
			return t
		n += 1

print nextTriangle()


