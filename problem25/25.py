
prevNum = 1
num = 1
it = 2
while len(str(num)) != 1000:
	temp = num
	num = num + prevNum
	prevNum = temp
	it += 1
print it