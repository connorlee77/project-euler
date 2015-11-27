prod = 1
for x in range(1,101):
	prod *= x
prod = str(prod)

s = 0
for c in prod:
	s += int(c)

print s