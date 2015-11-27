def getData():
	import sys
	arr = []
	for line in sys.stdin:
		line = line.strip().split()

		newLine = []
		for word in line:
			if word[0] == '0':
				newLine.append(word[1])
			else:
				newLine.append(word)

		arr.append(newLine)
	return arr

def horizontalHelper(nums):
	from numpy import prod

	getThird = nums[0:4]
	fourth = int(nums[0])
	memProd =  prod(map(int, getThird))
	maxProd = memProd

	for i in nums[4:]:
		fourth = int(getThird[0])
		getThird = getThird[1:]
		getThird.append(i)
		if fourth == 0:
			memProd = prod(map(int, getThird))
		else:
			memProd /= fourth
			memProd *= int(i)

		if memProd > maxProd:
			maxProd = memProd  
	return maxProd	


def horizontal(mat):
	maxProd = 0

	for line in mat:
		maxProd = max(horizontalHelper(line), maxProd)
	return maxProd


def vertical(mat):
	import numpy as np

	grid = np.transpose(np.array(mat))
	maxProd = 0

	for line in grid:
		maxProd = max(horizontalHelper(line.tolist()), maxProd)
	return maxProd

def diagonal(mat):

	maxProd = 0
	i = 0
	while i < len(mat) - 3:
		diag = []
		row = i
		col = 0
		while row < len(mat):
			diag.append(mat[row][col])
			row += 1
			col += 1
		i += 1
		maxProd = max(maxProd, horizontalHelper(diag))	


	i = 0
	while i < len(mat[0]) - 3:
		diag = []
		col = i
		row = 0
		while col < len(mat[0]):
			diag.append(mat[row][col])
			row += 1
			col += 1
		i += 1
		maxProd = max(maxProd, horizontalHelper(diag))

	i = 3
	while i < len(mat):
		diag = []
		row = i
		col = 0
		while row >= 0:
			diag.append(mat[row][col])
			row -= 1
			col += 1
		i += 1
		maxProd = max(maxProd, horizontalHelper(diag))	

	i = 0
	while i < len(mat) - 3:
		diag = []
		row = i
		col = len(mat[0]) - 1
		while row < len(mat):
			diag.append(mat[row][col])
			row += 1
			col -= 1
		i += 1
		maxProd = max(maxProd, horizontalHelper(diag))	
	return maxProd





mat = getData()
hori = horizontal(mat)
vert = vertical(mat)
diag = diagonal(mat)

print max(hori, vert, diag) 










